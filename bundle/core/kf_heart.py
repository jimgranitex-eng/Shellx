#!/usr/bin/env python3
"""
kf_heart.py
AI Heart v1 — discovers project layout and launches canonical EXE with working directory set.
"""
import os
import json
import time
import subprocess
from pathlib import Path
from typing import Dict, List, Optional

# --- CONFIG: adjust only if needed ---
PROJECT_ROOT = Path(__file__).resolve().parent  # assume this file lives in the real root
HEART_STATE_DIR = PROJECT_ROOT / "_ai_heart_state"
HEART_STATE_DIR.mkdir(exist_ok=True)

HEART_LOG = HEART_STATE_DIR / "heart_log.json"
RUNTIME_MAP = HEART_STATE_DIR / "runtime_map.json"


def _find_candidates(patterns: List[str]) -> List[Path]:
    matches: List[Path] = []
    for root, dirs, files in os.walk(PROJECT_ROOT):
        root_path = Path(root)
        for name in files:
            for pat in patterns:
                if name.lower() == pat.lower():
                    matches.append(root_path / name)
    return matches


def discover_project_layout() -> Dict:
    """
    Scan the whole tree and find:
    - all KickerOS executables
    - all main QML entrypoints
    - all folders that look like build/dist variants
    """
    exe_candidates = _find_candidates(["kickeros.exe", "kicker_os.exe", "KickerOS"])
    qml_candidates = _find_candidates(["main.qml", "Main.qml"])

    build_like_dirs = []
    for child in PROJECT_ROOT.iterdir():
        if child.is_dir() and any(
            tag in child.name.lower() for tag in ["build", "dist", "output", "bin"]
        ):
            build_like_dirs.append(child)

    layout = {
        "project_root": str(PROJECT_ROOT),
        "exe_candidates": [str(p) for p in exe_candidates],
        "qml_candidates": [str(p) for p in qml_candidates],
        "build_like_dirs": [str(p) for p in build_like_dirs],
        "timestamp": time.time(),
    }
    return layout


def choose_canonical_runtime(layout: Dict) -> Dict:
    """
    Decide which EXE + QML are the 'canonical' runtime for now.
    Strategy (v1, simple):
    - Prefer EXE under a build-like dir (dist/build)
    - If multiple, pick the most recently modified
    - Same idea for main.qml
    """
    exe_paths = [Path(p) for p in layout["exe_candidates"]]
    qml_paths = [Path(p) for p in layout["qml_candidates"]]

    def pick_latest(paths: List[Path]) -> Optional[Path]:
        if not paths:
            return None
        paths = [p for p in paths if p.exists()]
        if not paths:
            return None
        return max(paths, key=lambda p: p.stat().st_mtime)

    # Prefer exe inside build-like dirs
    build_dirs = [Path(p) for p in layout["build_like_dirs"]]
    exe_in_build = []
    for exe in exe_paths:
        if any(str(exe).startswith(str(b)) for b in build_dirs):
            exe_in_build.append(exe)

    canonical_exe = pick_latest(exe_in_build) or pick_latest(exe_paths)

    # Prefer a QML that is colocated with the chosen EXE (share the longest
    # common path prefix). Fall back to the most-recently-modified QML.
    canonical_qml = None
    if canonical_exe and qml_paths:
        def common_prefix_len(a: Path, b: Path) -> int:
            a_parts = a.resolve().parts
            b_parts = b.resolve().parts
            match = 0
            for x, y in zip(a_parts, b_parts):
                if x == y:
                    match += 1
                else:
                    break
            return match

        best = None
        best_score = -1
        exe_path = canonical_exe
        for q in qml_paths:
            if not q.exists():
                continue
            score = common_prefix_len(exe_path, q)
            if score > best_score:
                best_score = score
                best = q
        if best:
            canonical_qml = best
        else:
            canonical_qml = pick_latest(qml_paths)
    else:
        canonical_qml = pick_latest(qml_paths)

    runtime = {
        "canonical_exe": str(canonical_exe) if canonical_exe else None,
        "canonical_qml": str(canonical_qml) if canonical_qml else None,
        "timestamp": time.time(),
    }
    return runtime


def save_state(layout: Dict, runtime: Dict) -> None:
    HEART_LOG.write_text(json.dumps(layout, indent=2), encoding="utf-8")
    RUNTIME_MAP.write_text(json.dumps(runtime, indent=2), encoding="utf-8")


def load_runtime() -> Optional[Dict]:
    if not RUNTIME_MAP.exists():
        return None
    try:
        return json.loads(RUNTIME_MAP.read_text(encoding="utf-8"))
    except Exception:
        return None


def summarize(layout: Dict, runtime: Dict) -> str:
    lines = []
    lines.append("=== AI HEART PROJECT SUMMARY ===")
    lines.append(f"Project root: {layout['project_root']}")
    lines.append("")
    lines.append("EXE candidates:")
    for p in layout["exe_candidates"]:
        lines.append(f"  - {p}")
    lines.append("")
    lines.append("main.qml candidates:")
    for p in layout["qml_candidates"]:
        lines.append(f"  - {p}")
    lines.append("")
    lines.append("Build-like dirs:")
    for p in layout["build_like_dirs"]:
        lines.append(f"  - {p}")
    lines.append("")
    lines.append("Chosen canonical runtime:")
    lines.append(f"  EXE: {runtime.get('canonical_exe')}")
    lines.append(f"  QML: {runtime.get('canonical_qml')}")
    return "\n".join(lines)


def run_preflight() -> Dict:
    """
    This is the AI Heart preflight:
    - scan everything
    - choose canonical runtime
    - save state
    """
    layout = discover_project_layout()
    runtime = choose_canonical_runtime(layout)
    save_state(layout, runtime)
    print(summarize(layout, runtime))
    return runtime


def launch_kickeros(runtime: Dict) -> int:
    exe = runtime.get("canonical_exe")
    if not exe:
        print("[AI HEART] No canonical EXE found. Cannot launch KickerOS.")
        return -1

    exe_path = Path(exe)
    if not exe_path.exists():
        print(f"[AI HEART] Canonical EXE does not exist: {exe}")
        return -1

    print(f"[AI HEART] Launching KickerOS from: {exe}")
    try:
        # Run with working directory set to its parent
        proc = subprocess.Popen(
            [str(exe_path)],
            cwd=str(exe_path.parent),
        )
        proc.wait()
        return proc.returncode
    except Exception as e:
        print(f"[AI HEART] Failed to launch KickerOS: {e}")
        return -1


if __name__ == "__main__":
    runtime = run_preflight()
    code = launch_kickeros(runtime)
    print(f"[AI HEART] KickerOS exited with code: {code}")
