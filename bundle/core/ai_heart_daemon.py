#!/usr/bin/env python3
"""
ai_heart_daemon.py
Supervisor daemon: watches the project tree, runs preflight, launches KickerOS,
captures output, attempts auto-repair and relaunch, and logs events.

Run once for a single cycle with `--once`, or let it run forever.
"""
import os
import time
import json
import argparse
from pathlib import Path
from typing import Dict

from kf_heart import run_preflight
import ai_heart_launcher as launcher
from ai_heart_autofix import auto_repair

WATCH_ROOT = Path(__file__).resolve().parent
STATE_DIR = WATCH_ROOT / "_ai_heart_state"
STATE_DIR.mkdir(exist_ok=True)
DAEMON_LOG = STATE_DIR / "daemon_log.json"


def snapshot_tree() -> Dict[str, float]:
    mtimes = {}
    for root, dirs, files in os.walk(WATCH_ROOT):
        for f in files:
            p = Path(root) / f
            try:
                mtimes[str(p)] = p.stat().st_mtime
            except Exception:
                pass
    return mtimes


def tree_changed(old: Dict[str, float], new: Dict[str, float]) -> bool:
    for k, v in new.items():
        if k not in old or old[k] != v:
            return True
    return False


def log_event(event: Dict) -> None:
    events = []
    if DAEMON_LOG.exists():
        try:
            events = json.loads(DAEMON_LOG.read_text(encoding="utf-8"))
        except Exception:
            events = []
    events.append(event)
    DAEMON_LOG.write_text(json.dumps(events, indent=2), encoding="utf-8")


def run_cycle() -> None:
    print("[HEART-DAEMON] Running preflight and one launch cycle")
    # 1) preflight (updates kf_heart state files)
    runtime = run_preflight()

    # 2) prefer discover_runtime for launcher-friendly shape
    lrt = launcher.discover_runtime()

    # 3) launch and capture output (no auto-repair inside this call)
    code, output = launcher.launch_capture(lrt, timeout=30)

    # 4) if crash, attempt auto-repair using a canonical qml path (try kf_heart runtime)
    try:
        canonical_qml = runtime.get("canonical_qml") or lrt.get("qml_root")
    except Exception:
        canonical_qml = None

    repaired = False
    if code != 0 and output and canonical_qml:
        repaired = auto_repair(output, canonical_qml)
        if repaired:
            print("[HEART-DAEMON] Auto-repair applied; relaunching once")
            code, output = launcher.launch_capture(lrt, timeout=30)

    # 5) log the event
    event = {
        "timestamp": time.time(),
        "exit_code": code,
        "repaired": repaired,
        "status": "ok" if code == 0 else "crash",
    }
    log_event(event)
    print(f"[HEART-DAEMON] Cycle complete: exit_code={code} repaired={repaired}")


def daemon_loop(interval_seconds: int = 1) -> None:
    last_snapshot = snapshot_tree()

    while True:
        time.sleep(interval_seconds)
        new_snapshot = snapshot_tree()
        if tree_changed(last_snapshot, new_snapshot):
            print("[HEART-DAEMON] Change detected → running cycle")
            run_cycle()
            last_snapshot = new_snapshot


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--once", action="store_true", help="Run one cycle and exit")
    args = parser.parse_args()

    if args.once:
        run_cycle()
    else:
        print("[HEART-DAEMON] Starting continuous daemon. Press Ctrl-C to stop.")
        try:
            daemon_loop()
        except KeyboardInterrupt:
            print("[HEART-DAEMON] Stopped by user.")
