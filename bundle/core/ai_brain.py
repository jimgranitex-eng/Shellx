#!/usr/bin/env python3
"""
ai_brain.py
Single-file AI Brain: scans project layout, builds runtime candidates, runs real attempts,
captures stdout/stderr, writes a black-box JSON under `_ai_brain_state/black_box/`.

Drop into the project root and run `python ai_brain.py`.
"""
import os
import json
import time
import subprocess
from pathlib import Path
from typing import List, Dict, Optional

# ---------- CORE PATHS ----------
PROJECT_ROOT = Path(__file__).resolve().parent
STATE_DIR = PROJECT_ROOT / "_ai_brain_state"
BLACKBOX_DIR = STATE_DIR / "black_box"
MANUALS_FILE = STATE_DIR / "manuals.json"

STATE_DIR.mkdir(exist_ok=True)
BLACKBOX_DIR.mkdir(parents=True, exist_ok=True)

MAX_ATTEMPTS = 5        # how many real runs to try per session
ATTEMPT_TIMEOUT = 60    # seconds per run


# ---------- UTILITIES ----------

def find_files(root: Path, names: List[str]) -> List[Path]:
    hits: List[Path] = []
    lower = [n.lower() for n in names]
    for r, d, f in os.walk(root):
        rpath = Path(r)
        for name in f:
            if name.lower() in lower:
                hits.append(rpath / name)
    return hits


def find_dirs(root: Path, names: List[str]) -> List[Path]:
    hits: List[Path] = []
    lower = [n.lower() for n in names]
    for r, d, f in os.walk(root):
        rpath = Path(r)
        for name in d:
            if name.lower() in lower:
                hits.append(rpath / name)
    return hits


def pick_latest(paths: List[Path]) -> Optional[Path]:
    paths = [p for p in paths if p.exists()]
    if not paths:
        return None
    return max(paths, key=lambda p: p.stat().st_mtime)


def load_manuals() -> List[Dict]:
    if not MANUALS_FILE.exists():
        return []
    try:
        return json.loads(MANUALS_FILE.read_text(encoding="utf-8"))
    except Exception:
        return []


def write_manual(event_type: str, summary: str, details: Dict) -> None:
    manuals = load_manuals()
    manuals.append(
        {
            "timestamp": time.time(),
            "type": event_type,
            "summary": summary,
            "details": details,
        }
    )
    MANUALS_FILE.write_text(json.dumps(manuals, indent=2), encoding="utf-8")


# ---------- LAYOUT SCAN ----------

def scan_layout() -> Dict:
    exe_candidates = find_files(PROJECT_ROOT, ["kickeros.exe", "kicker_os.exe", "KickerOS"])
    qml_dirs = find_dirs(PROJECT_ROOT, ["qml"])
    plugin_dirs = find_dirs(PROJECT_ROOT, ["plugins", "platforms"])
    qt_core = find_files(PROJECT_ROOT, ["Qt6Core.dll", "Qt5Core.dll", "libQt6Core.so", "libQt5Core.so"])

    layout = {
        "project_root": str(PROJECT_ROOT),
        "exe_candidates": [str(p) for p in exe_candidates],
        "qml_dirs": [str(p) for p in qml_dirs],
        "plugin_dirs": [str(p) for p in plugin_dirs],
        "qt_core_candidates": [str(p) for p in qt_core],
        "timestamp": time.time(),
    }

    write_manual(
        "preflight_scan",
        "Scanned project layout",
        {"layout": layout},
    )

    return layout


# ---------- RUNTIME CANDIDATES ----------

def build_runtime_candidates(layout: Dict) -> List[Dict]:
    exe_paths = [Path(p) for p in layout["exe_candidates"]]
    qml_paths = [Path(p) for p in layout["qml_dirs"]]
    plugin_paths = [Path(p) for p in layout["plugin_dirs"]]
    qt_core_paths = [Path(p) for p in layout["qt_core_candidates"]]

    qt_bin_dirs = []
    for core in qt_core_paths:
        if core.exists():
            qt_bin_dirs.append(core.parent)

    candidates: List[Dict] = []

    def add_candidate(exe: Optional[Path],
                      qt_bin: Optional[Path],
                      qml_root: Optional[Path],
                      plugin_root: Optional[Path]):
        if not exe or not exe.exists():
            return
        candidates.append(
            {
                "exe": str(exe),
                "qt_bin_dir": str(qt_bin) if qt_bin else None,
                "qml_root": str(qml_root) if qml_root else None,
                "plugin_root": str(plugin_root) if plugin_root else None,
            }
        )

    latest_exe = pick_latest(exe_paths)
    latest_qml = pick_latest(qml_paths)
    latest_plugin = pick_latest(plugin_paths)
    latest_qt_bin = pick_latest(qt_bin_dirs)

    # main candidate
    add_candidate(latest_exe, latest_qt_bin, latest_qml, latest_plugin)

    # other exes with same env
    for exe in exe_paths:
        if exe == latest_exe:
            continue
        add_candidate(exe, latest_qt_bin, latest_qml, latest_plugin)

    # mix a few combos if multiple envs exist
    for exe in exe_paths:
        for qml in qml_paths:
            for plug in plugin_paths:
                for qt_bin in qt_bin_dirs:
                    add_candidate(exe, qt_bin, qml, plug)

    # dedupe
    seen = set()
    unique: List[Dict] = []
    for c in candidates:
        key = (
            c["exe"],
            c.get("qt_bin_dir"),
            c.get("qml_root"),
            c.get("plugin_root"),
        )
        if key in seen:
            continue
        seen.add(key)
        unique.append(c)

    write_manual(
        "runtime_candidates",
        f"Built {len(unique)} runtime candidates",
        {"candidates": unique},
    )

    return unique


# ---------- ENV + REAL RUN ----------

def wire_env(runtime: Dict) -> Dict[str, str]:
    env = os.environ.copy()

    qt_bin = runtime.get("qt_bin_dir")
    qml_root = runtime.get("qml_root")
    plugin_root = runtime.get("plugin_root")

    if qt_bin:
        env["PATH"] = str(qt_bin) + os.pathsep + env.get("PATH", "")

    if qml_root:
        env["QML2_IMPORT_PATH"] = str(qml_root)

    if plugin_root:
        env["QT_PLUGIN_PATH"] = str(plugin_root)

    env.setdefault("QML_XHR_ALLOW_FILE_READ", "1")

    return env


def run_attempt(runtime: Dict, attempt_index: int) -> Dict:
    from pathlib import Path

    exe = runtime.get("exe")
    exe_path = Path(exe) if exe else None

    result: Dict = {
        "attempt_index": attempt_index,
        "runtime": runtime,
        "start_time": time.time(),
        "end_time": None,
        "exit_code": None,
        "stdout": None,
        "stderr": None,
        "error": None,
    }

    if not exe_path or not exe_path.exists():
        result["error"] = f"Exe not found: {exe}"
        result["end_time"] = time.time()
        return result

    env = wire_env(runtime)

    try:
        proc = subprocess.Popen(
            [str(exe_path)],
            cwd=str(exe_path.parent),
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        try:
            out, err = proc.communicate(timeout=ATTEMPT_TIMEOUT)
        except subprocess.TimeoutExpired:
            proc.kill()
            out, err = proc.communicate()
            result["error"] = "TimeoutExpired"
        result["exit_code"] = proc.returncode
        result["stdout"] = out
        result["stderr"] = err
    except Exception as e:
        result["error"] = f"Launch error: {e}"

    result["end_time"] = time.time()
    return result


# ---------- BLACK BOX ----------

def write_black_box(layout: Dict, attempts: List[Dict]) -> Path:
    ts = time.strftime("%Y%m%d_%H%M%S", time.localtime())
    fname = BLACKBOX_DIR / f"black_box_{ts}.json"

    payload = {
        "timestamp": time.time(),
        "project_root": layout["project_root"],
        "layout": layout,
        "attempts": attempts,
    }
    fname.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    write_manual(
        "black_box_written",
        f"Black box created: {fname.name}",
        {"path": str(fname)},
    )

    return fname


# ---------- MAIN SESSION (REAL SIMULATION) ----------

def run_ai_brain_session() -> Path:
    print("[AI BRAIN] Preflight scan...")
    layout = scan_layout()

    print("[AI BRAIN] Building runtime candidates...")
    candidates = build_runtime_candidates(layout)
    if not candidates:
        print("[AI BRAIN] No runtime candidates found.")
        bb = write_black_box(layout, [])
        print("[AI BRAIN] Black box:", bb)
        return bb

    print(f"[AI BRAIN] {len(candidates)} candidates found.")
    attempts: List[Dict] = []

    for i, runtime in enumerate(candidates[:MAX_ATTEMPTS]):
        print(f"[AI BRAIN] Attempt {i+1}/{min(len(candidates), MAX_ATTEMPTS)}")
        print("  exe:", runtime["exe"])
        print("  qt_bin_dir:", runtime.get("qt_bin_dir"))
        print("  qml_root:", runtime.get("qml_root"))
        print("  plugin_root:", runtime.get("plugin_root"))

        attempt_result = run_attempt(runtime, i)
        attempts.append(attempt_result)

        code = attempt_result.get("exit_code")
        err = attempt_result.get("error")

        if code == 0 and not err:
            print("[AI BRAIN] Stable run detected.")
            break
        else:
            print("[AI BRAIN] Crash/error.")
            print("  exit_code:", code, "error:", err)

    bb_path = write_black_box(layout, attempts)
    print("[AI BRAIN] Session complete. Black box:", bb_path)
    return bb_path


# ---------- ENTRY POINT ----------

if __name__ == "__main__":
    run_ai_brain_session()
