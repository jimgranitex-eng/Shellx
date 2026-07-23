# ai_heart_system_utils.py
import json
import os
from pathlib import Path
from datetime import datetime

# Core paths
TIMELINE_PATH = Path("activity_timeline.json")
BLACKBOX_DIR = Path(".blackbox_runs")
REPORTS_DIR = Path(".reports")
STONES_DIR = Path(".quarantine/stones")
LINKX_PATH = Path("LinkX_AI_Heart.md")

BLACKBOX_DIR.mkdir(exist_ok=True, parents=True)
REPORTS_DIR.mkdir(exist_ok=True, parents=True)
STONES_DIR.mkdir(exist_ok=True, parents=True)

# Search roots for timeline (can be overridden by environment variable AI_HEART_SEARCH_ROOTS)
env_roots = os.environ.get("AI_HEART_SEARCH_ROOTS")
if env_roots:
    SEARCH_ROOTS = [Path(p) for p in env_roots.split(os.pathsep) if p]
else:
    SEARCH_ROOTS = [
        Path("C:/"),
        Path("D:/")
    ]

KEY_FILENAMES = {
    "exe": ["KickerOS.exe"],
    "qml": ["main.qml"],
    "qt": ["Qt6Core.dll", "Qt6Quick.dll"],
    "logs": [".log"],
    "stones": [".md"]
}

# ---------- Timeline helpers ----------

def _find_files_by_name(name_list):
    results = []
    for root in SEARCH_ROOTS:
        for name in name_list:
            for path in root.rglob(name):
                results.append(path)
    return results

def _find_files_by_extension(ext):
    results = []
    for root in SEARCH_ROOTS:
        for path in root.rglob(f"*{ext}"):
            results.append(path)
    return results

def _get_latest(paths):
    if not paths:
        return None
    existing = []
    for p in paths:
        try:
            if p.exists():
                existing.append(p)
        except OSError:
            continue
    if not existing:
        return None
    return max(existing, key=lambda p: p.stat().st_mtime)

def load_timeline():
    if TIMELINE_PATH.exists():
        return json.loads(TIMELINE_PATH.read_text(encoding="utf-8"))
    return {
        "timeline_version": 1,
        "last_run": {},
        "last_edit": {},
        "active_paths": {},
        "observations": {}
    }

def save_timeline(data):
    TIMELINE_PATH.write_text(json.dumps(data, indent=4), encoding="utf-8")

def update_activity_timeline():
    # Allow skipping timeline scanning for faster, targeted runs
    if os.environ.get("AI_HEART_SKIP_TIMELINE") == "1":
        print("[TIMELINE] Skipping activity timeline scan (AI_HEART_SKIP_TIMELINE=1).")
        return

    timeline = load_timeline()

    exe_files = _find_files_by_name(KEY_FILENAMES["exe"])
    qml_files = _find_files_by_name(KEY_FILENAMES["qml"])
    qt_files = _find_files_by_name(KEY_FILENAMES["qt"])
    logs = _find_files_by_extension(".log")
    stones = _find_files_by_extension(".md")

    active_exe = _get_latest(exe_files)
    active_qml = _get_latest(qml_files)
    active_qt = _get_latest(qt_files)
    active_log = _get_latest(logs)
    active_stone = _get_latest(stones)

    timeline["observations"] = {
        "detected_build_dirs": list({str(p.parent) for p in exe_files}),
        "detected_qml_dirs": list({str(p.parent) for p in qml_files}),
        "detected_qt_dirs": list({str(p.parent) for p in qt_files}),
        "detected_exe_files": [str(p) for p in exe_files],
        "detected_logs": [str(p) for p in logs],
        "detected_stones": [str(p) for p in stones]
    }

    timeline["active_paths"] = {
        "project_root": "",
        "active_build_root": str(active_exe.parent) if active_exe else "",
        "active_qml_root": str(active_qml.parent) if active_qml else "",
        "active_qt_root": str(active_qt.parent) if active_qt else "",
        "active_logs_root": str(active_log.parent) if active_log else "",
        "active_stones_root": str(active_stone.parent) if active_stone else ""
    }

    save_timeline(timeline)
    print("[TIMELINE] Updated activity timeline.")

# ---------- Intelligent global search + Qt module detection ----------

QT_MODULE_PATTERNS = {
    "QtWebEngine": [
        "QtWebEngine",
        "QtWebEngineCore",
        "QtWebEngineQuick",
        "QtWebEngineProcess",
        "QtWebEngineWidgets"
    ],
    "QtQuick3D": [
        "QtQuick3D",
        "QtQuick3D.Helpers",
        "QtQuick3D.Materials",
        "QtQuick3D.AssetUtils",
        "QtQuick3D.Effects",
        "QtQuick3D.Particles3D"
    ],
    "QtQuick.Controls": [
        "QtQuick.Controls",
        "QtQuick.Controls.Basic",
        "QtQuick.Controls.Fusion",
        "QtQuick.Controls.Material",
        "QtQuick.Controls.Universal"
    ]
}


def global_search_paths(name_patterns, roots=None, max_results=500):
    if roots is None:
        roots = SEARCH_ROOTS
    if isinstance(name_patterns, str):
        name_patterns = [name_patterns]

    results = []
    for root in roots:
        try:
            for path in root.rglob("*"):
                s = str(path).replace("\\", "/")
                for pat in name_patterns:
                    if pat in s:
                        results.append(path)
                        if len(results) >= max_results:
                            return results
        except (PermissionError, OSError):
            continue
    return results


def classify_presence(expected_root: Path, patterns: list, timeline: dict, kind: str = "qt"):
    expected_root = expected_root.resolve() if expected_root and expected_root.exists() else expected_root
    obs = timeline.get("observations", {})

    present_in_expected = []
    if expected_root and Path(expected_root).exists():
        for pat in patterns:
            try:
                for p in Path(expected_root).rglob(pat):
                    present_in_expected.append(p)
            except (PermissionError, OSError):
                continue

    global_hits = global_search_paths(patterns)

    if kind == "qt":
        past_dirs = [Path(p) for p in obs.get("detected_qt_dirs", [])]
    else:
        past_dirs = [Path(p) for p in obs.get("detected_build_dirs", [])]

    classification = {
        "present_in_expected": [str(p) for p in present_in_expected],
        "global_hits": [str(p) for p in global_hits],
        "past_dirs": [str(p) for p in past_dirs],
        "status": "unknown",
        "note": ""
    }

    if present_in_expected:
        classification["status"] = "ok"
        classification["note"] = "Found in expected root."
        return classification

    if global_hits:
        parents = {str(Path(h).parent) for h in global_hits}
        if len(parents) > 1:
            classification["status"] = "duplicate"
            classification["note"] = f"Found in multiple locations: {sorted(parents)}"
        else:
            classification["status"] = "misplaced"
            classification["note"] = f"Found only under {list(parents)[0]}, not under expected root {expected_root}."
        return classification

    classification["status"] = "missing"
    classification["note"] = "Not found in expected root or anywhere in scanned roots."
    return classification


def deep_detect_qt_modules(qt_root: Path, timeline: dict):
    results = {}
    for logical_name, patterns in QT_MODULE_PATTERNS.items():
        classification = classify_presence(qt_root, patterns, timeline, kind="qt")
        results[logical_name] = classification
    return results


def investigate_exe(timeline: dict):
    active = timeline.get("active_paths", {})
    build_root = Path(active.get("active_build_root") or "")
    return classify_presence(build_root, KEY_FILENAMES["exe"], timeline, kind="exe")


def investigate_qml_root(timeline: dict):
    active = timeline.get("active_paths", {})
    qml_root = Path(active.get("active_qml_root") or "")
    return classify_presence(qml_root, KEY_FILENAMES["qml"], timeline, kind="qml")


def investigate_logs(timeline: dict):
    active = timeline.get("active_paths", {})
    logs_root = Path(active.get("active_logs_root") or "")
    return classify_presence(logs_root, [".log"], timeline, kind="logs")


def investigate_stones(timeline: dict):
    active = timeline.get("active_paths", {})
    stones_root = Path(active.get("active_stones_root") or "")
    return classify_presence(stones_root, [".md"], timeline, kind="stones")


# ---------- Preflight ----------

def preflight_check(use_proposed: bool = False, proposed_path: Path = Path("_ai_heart_state/proposed_config.json")):
    timeline = load_timeline()
    if use_proposed:
        proposed = load_proposed_config(proposed_path)
        if proposed:
            # shallow-merge proposed active paths into a copy of timeline for checks
            ap = timeline.get("active_paths", {}).copy()
            ap.update(proposed)
            timeline = timeline.copy()
            timeline["active_paths"] = ap
    issues = []
    notes = []

    active = timeline.get("active_paths", {})
    last_run = timeline.get("last_run", {})
    last_edit = timeline.get("last_edit", {})

    if not active.get("active_build_root"):
        issues.append("No active build root detected.")
    if not active.get("active_qml_root"):
        issues.append("No active QML root detected.")
    if not active.get("active_qt_root"):
        issues.append("No active Qt root detected.")

    for f in last_edit.get("qml_files_edited", []):
        if active.get("active_qml_root") and active["active_qml_root"] not in f:
            issues.append(f"QML edited outside active QML root: {f}")

    if last_run.get("exit_code") not in [0, None]:
        issues.append(f"Last run exited with code {last_run['exit_code']}")

    qt_root = Path(active.get("active_qt_root") or "")
    if qt_root.exists():
        qt_status = deep_detect_qt_modules(qt_root, timeline)
        for logical_name, info in qt_status.items():
            status = info["status"]
            note = info["note"]
            if status == "ok":
                notes.append(f"{logical_name}: OK — {note}")
            elif status == "misplaced":
                issues.append(f"{logical_name}: present but misplaced. {note}")
            elif status == "duplicate":
                issues.append(f"{logical_name}: duplicates detected. {note}")
            elif status == "missing":
                issues.append(f"{logical_name}: missing after global search. {note}")
    else:
        issues.append("Active Qt root does not exist on disk.")

    exe_info = investigate_exe(timeline)
    qml_info = investigate_qml_root(timeline)
    logs_info = investigate_logs(timeline)
    stones_info = investigate_stones(timeline)

    def summarize(kind, info):
        status = info["status"]
        note = info["note"]
        if status == "ok":
            notes.append(f"{kind}: OK — {note}")
        else:
            issues.append(f"{kind}: {status.upper()} — {note}")

    summarize("EXE", exe_info)
    summarize("QML root", qml_info)
    summarize("Logs", logs_info)
    summarize("Stones", stones_info)

    if issues:
        print("[PREFLIGHT] Issues detected:")
        for i in issues:
            print(" -", i)
        if notes:
            print("[PREFLIGHT] Notes:")
            for n in notes:
                print(" -", n)
        return False, issues

    print("[PREFLIGHT] All checks passed.")
    for n in notes:
        print(" -", n)
    return True, []


def load_proposed_config(path: Path = Path("_ai_heart_state/proposed_config.json")) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def save_proposed_config(proposed: dict, path: Path = Path("_ai_heart_state/proposed_config.json")) -> str:
    path.parent.mkdir(exist_ok=True, parents=True)
    path.write_text(json.dumps(proposed, indent=2), encoding="utf-8")
    return str(path)

# ---------- Blackbox / ShellX / Stones / LinkX ----------

def write_blackbox_run(run_id: str, data: dict) -> str:
    ts = datetime.utcnow().strftime("%Y-%m-%dT%H%M%SZ")
    path = BLACKBOX_DIR / f"blackbox_{ts}_{run_id}.json"
    path.write_text(json.dumps(data, indent=4), encoding="utf-8")
    print(f"[BLACKBOX] Wrote {path}")
    return str(path)

def build_shellx_doctor_report(run_id: str,
                               exit_code: int,
                               preflight_issues: list,
                               timeline: dict,
                               blackbox_path: str) -> str:
    ts = datetime.utcnow().strftime("%Y-%m-%dT%H%M%SZ")
    report_path = REPORTS_DIR / f"ShellX_Doctor_{ts}_{run_id}.md"

    active = timeline.get("active_paths", {})
    last_run = timeline.get("last_run", {})
    observations = timeline.get("observations", {})

    lines = []
    lines.append("===========================================================")
    lines.append("# SHELLX — AI HEART DOCTOR RUN REPORT")
    lines.append("===========================================================\n")

    # COMPLEX SUMMARY
    lines.append("### COMPLEX SUMMARY")
    lines.append(f"- **Run ID:** `{run_id}`")
    lines.append(f"- **Exit code:** `{exit_code}`")
    if preflight_issues:
        lines.append("- **Preflight:** Issues detected (non-destructive).")
    else:
        lines.append("- **Preflight:** Clean.")
    lines.append(f"- **Blackbox:** `{blackbox_path}`")
    lines.append(f"- **Active build root:** `{active.get('active_build_root', '')}`")
    lines.append(f"- **Active QML root:** `{active.get('active_qml_root', '')}`")
    lines.append(f"- **Active Qt root:** `{active.get('active_qt_root', '')}`")
    lines.append("")

    # DETAILED REPORT
    lines.append("### DETAILED REPORT")
    lines.append("- **Preflight issues:**")
    if preflight_issues:
        for issue in preflight_issues:
            lines.append(f"  - {issue}")
    else:
        lines.append("  - None.")
    lines.append("")
    lines.append("- **Timeline last_run:**")
    lines.append(f"  - timestamp: {last_run.get('timestamp', '')}")
    lines.append(f"  - launcher_path: {last_run.get('launcher_path', '')}")
    lines.append("")
    lines.append("- **Observations:**")
    lines.append(f"  - build dirs: {observations.get('detected_build_dirs', [])}")
    lines.append(f"  - qml dirs: {observations.get('detected_qml_dirs', [])}")
    lines.append(f"  - qt dirs: {observations.get('detected_qt_dirs', [])}")
    lines.append("")

    # FULL REPORT
    lines.append("### FULL REPORT")
    lines.append("- See blackbox JSON for full stdout / metadata:")
    lines.append(f"  - `{blackbox_path}`")
    lines.append("")

    # CHECKLIST
    lines.append("### CHECKLIST")
    lines.append(f"- [x] Timeline updated for run `{run_id}`")
    lines.append("- [x] Preflight executed")
    lines.append(f"- [{'x' if preflight_issues else ' '}] Preflight issues recorded")
    lines.append("- [x] Launcher executed once")
    lines.append("- [x] Blackbox written")
    lines.append("- [ ] Deep Attempt-2 analysis (future)")
    lines.append("- [ ] Battle plan Attempt-3 (future)")
    lines.append("- [ ] LinkX updated")
    lines.append("- [ ] Recovery stone written")
    lines.append("")

    # OVERALL PROJECT GOAL
    lines.append("### OVERALL PROJECT GOAL")
    lines.append("- Build a self-observing, non-destructive, adaptive diagnostic layer for KickerOS that:")
    lines.append("  - tracks what is actually used (timeline),")
    lines.append("  - checks alignment before each run (preflight),")
    lines.append("  - records every run (blackbox),")
    lines.append("  - and produces ShellX-style reports + stones for recovery and history.")
    lines.append("")

    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[SHELLX] Wrote doctor report: {report_path}")
    return str(report_path)

def write_recovery_stone(title: str, description: str) -> str:
    ts = datetime.utcnow().strftime("%Y-%m-%dT%H%M%SZ")
    stone_path = STONES_DIR / f"AI_Heart_Doctor_{ts}.md"
    content = [
        f"# {title}",
        f"Timestamp: {ts}",
        "",
        "## Description",
        description,
        ""
    ]
    stone_path.write_text("\n".join(content), encoding="utf-8")
    print(f"[STONE] Wrote recovery stone: {stone_path}")
    return str(stone_path)

def update_linkx_with_doctor_run(report_path: str, stone_path: str):
    ts = datetime.utcnow().strftime("%Y-%m-%dT%H%M%SZ")
    header = "## AI Heart Doctor Runs\n"
    entry = f"- {ts}: report `{report_path}`, stone `{stone_path}`\n"

    if LINKX_PATH.exists():
        text = LINKX_PATH.read_text(encoding="utf-8")
        if header not in text:
            text += "\n" + header
        text += entry
        LINKX_PATH.write_text(text, encoding="utf-8")
    else:
        LINKX_PATH.write_text(header + entry, encoding="utf-8")

    print(f"[LINKX] Updated LinkX with doctor run: {report_path}, {stone_path}")


# ---------- FIX PLAN GENERATOR (ATTEMPT 3) ----------

def build_fix_plan_from_investigation(
    qt_status: dict,
    exe_info: dict,
    qml_info: dict,
    logs_info: dict,
    stones_info: dict,
    generic_issues: list,
):
    """
    Turn deep investigation results into a structured, non-destructive fix plan.
    """
    plan = {
        "summary": "",
        "qt": {},
        "exe": {},
        "qml": {},
        "logs": {},
        "stones": {},
        "generic_issues": generic_issues or [],
        "recommended_actions": [],
    }

    # ---- QT SECTION ----
    qt_actions = []
    for logical_name, info in (qt_status or {}).items():
        status = info.get("status", "unknown")
        note = info.get("note", "")
        entry = {
            "status": status,
            "note": note,
            "present_in_expected": info.get("present_in_expected", []),
            "global_hits": info.get("global_hits", []),
            "past_dirs": info.get("past_dirs", []),
        }
        plan["qt"][logical_name] = entry

        if status == "misplaced":
            qt_actions.append(
                f"{logical_name}: align Qt module location. {note} "
                "Manual options: install module for the active kit, or update active_qt_root to the kit that actually has it."
            )
        elif status == "duplicate":
            qt_actions.append(
                f"{logical_name}: resolve duplicate Qt modules. {note} "
                "Manual options: choose one Qt kit, remove the others from PATH or adjust launcher to target the chosen kit."
            )
        elif status == "missing":
            qt_actions.append(
                f"{logical_name}: install or restore this Qt module. {note} "
                "Manual options: use Qt Maintenance Tool to add the module for the active kit."
            )

    plan["recommended_actions"].extend(qt_actions)

    # ---- EXE SECTION ----
    exe_status = exe_info.get("status", "unknown")
    exe_note = exe_info.get("note", "")
    plan["exe"] = {
        "status": exe_status,
        "note": exe_note,
        "present_in_expected": exe_info.get("present_in_expected", []),
        "global_hits": exe_info.get("global_hits", []),
        "past_dirs": exe_info.get("past_dirs", []),
    }
    if exe_status == "misplaced":
        plan["recommended_actions"].append(
            "KickerOS.exe: update launcher to point to the build directory where the EXE actually lives, "
            "or rebuild into the active_build_root. " + exe_note
        )
    elif exe_status == "duplicate":
        plan["recommended_actions"].append(
            "KickerOS.exe: choose a single authoritative build directory and update launcher / PATH accordingly. " + exe_note
        )
    elif exe_status == "missing":
        plan["recommended_actions"].append(
            "KickerOS.exe: rebuild the project to produce the executable in the active_build_root. " + exe_note
        )

    # ---- QML SECTION ----
    qml_status = qml_info.get("status", "unknown")
    qml_note = qml_info.get("note", "")
    plan["qml"] = {
        "status": qml_status,
        "note": qml_note,
        "present_in_expected": qml_info.get("present_in_expected", []),
        "global_hits": qml_info.get("global_hits", []),
        "past_dirs": qml_info.get("past_dirs", []),
    }
    if qml_status == "misplaced":
        plan["recommended_actions"].append(
            "QML root: align active_qml_root with the QML tree actually used (where main.qml lives), "
            "or move QML files into the active_qml_root. " + qml_note
        )
    elif qml_status == "duplicate":
        plan["recommended_actions"].append(
            "QML root: choose a single authoritative QML tree (source vs dist) and update import paths / launcher accordingly. " + qml_note
        )
    elif qml_status == "missing":
        plan["recommended_actions"].append(
            "QML root: restore or recreate main.qml in the active_qml_root, or point active_qml_root to the correct tree. " + qml_note
        )

    # ---- LOGS SECTION ----
    logs_status = logs_info.get("status", "unknown")
    logs_note = logs_info.get("note", "")
    plan["logs"] = {
        "status": logs_status,
        "note": logs_note,
        "present_in_expected": logs_info.get("present_in_expected", []),
        "global_hits": logs_info.get("global_hits", []),
        "past_dirs": logs_info.get("past_dirs", []),
    }
    if logs_status in ("missing", "misplaced", "duplicate"):
        plan["recommended_actions"].append(
            "Logs: ensure the launcher writes logs into a dedicated KickerOS logs directory, "
            "or update active_logs_root to where KickerOS logs are actually written. " + logs_note
        )

    # ---- STONES SECTION ----
    stones_status = stones_info.get("status", "unknown")
    stones_note = stones_info.get("note", "")
    plan["stones"] = {
        "status": stones_status,
        "note": stones_note,
        "present_in_expected": stones_info.get("present_in_expected", []),
        "global_hits": stones_info.get("global_hits", []),
        "past_dirs": stones_info.get("past_dirs", []),
    }
    if stones_status in ("missing", "misplaced", "duplicate"):
        plan["recommended_actions"].append(
            "Stones: ensure recovery stones for this project live under the project stones directory "
            "(e.g., .quarantine/stones) and not mixed with other projects. " + stones_note
        )

    # ---- GENERIC ISSUES ----
    for gi in generic_issues or []:
        plan["recommended_actions"].append(f"Generic issue: {gi}")

    # ---- SUMMARY ----
    if plan["recommended_actions"]:
        plan["summary"] = (
            "Environment inconsistencies detected. Manual, non-destructive actions are recommended to align Qt, "
            "EXE, QML, logs, stones, and launcher configuration for KickerOS."
        )
    else:
        plan["summary"] = (
            "No critical environment inconsistencies detected. If KickerOS still fails to boot, inspect runtime logs "
            "and QML errors for logic-level issues."
        )

    return plan


def write_fix_plan_report(plan: dict, run_id: str = "attempt3_plan") -> str:
    """
    Write a ShellX-style Attempt-3 battle plan report (Markdown).
    """
    ts = datetime.utcnow().strftime("%Y-%m-%dT%H%M%SZ")
    report_path = REPORTS_DIR / f"ShellX_Attempt3_{ts}_{run_id}.md"

    lines = []
    lines.append("===========================================================")
    lines.append("AI HEART DOCTOR — ATTEMPT 3 BATTLE PLAN")
    lines.append("===========================================================\n")

    lines.append("### SUMMARY")
    lines.append(plan.get("summary", ""))
    lines.append("")

    # QT
    lines.append("### 1. QT MODULES")
    qt = plan.get("qt", {})
    if not qt:
        lines.append("- No Qt module information available.")
    else:
        for name, info in qt.items():
            lines.append(f"- {name}:")
            lines.append(f"  - Status: {info.get('status', 'unknown')}")
            lines.append(f"  - Note: {info.get('note', '')}")
            if info.get("present_in_expected"):
                lines.append(f"  - Present in expected: {info['present_in_expected']}")
            if info.get("global_hits"):
                lines.append(f"  - Global hits: {info['global_hits']}")
            if info.get("past_dirs"):
                lines.append(f"  - Past dirs: {info['past_dirs']}")
            lines.append("")
    lines.append("")

    # EXE
    lines.append("### 2. EXECUTABLE (KickerOS.exe)")
    exe = plan.get("exe", {})
    lines.append(f"- Status: {exe.get('status', 'unknown')}")
    lines.append(f"- Note: {exe.get('note', '')}")
    if exe.get("present_in_expected"):
        lines.append(f"- Present in expected: {exe['present_in_expected']}")
    if exe.get("global_hits"):
        lines.append(f"- Global hits: {exe['global_hits']}")
    if exe.get("past_dirs"):
        lines.append(f"- Past dirs: {exe['past_dirs']}")
    lines.append("")

    # QML
    lines.append("### 3. QML ROOT / main.qml")
    qml = plan.get("qml", {})
    lines.append(f"- Status: {qml.get('status', 'unknown')}")
    lines.append(f"- Note: {qml.get('note', '')}")
    if qml.get("present_in_expected"):
        lines.append(f"- Present in expected: {qml['present_in_expected']}")
    if qml.get("global_hits"):
        lines.append(f"- Global hits: {qml['global_hits']}")
    if qml.get("past_dirs"):
        lines.append(f"- Past dirs: {qml['past_dirs']}")
    lines.append("")

    # LOGS
    lines.append("### 4. LOGS")
    logs = plan.get("logs", {})
    lines.append(f"- Status: {logs.get('status', 'unknown')}")
    lines.append(f"- Note: {logs.get('note', '')}")
    lines.append("")

    # STONES
    lines.append("### 5. STONES")
    stones = plan.get("stones", {})
    lines.append(f"- Status: {stones.get('status', 'unknown')}")
    lines.append(f"- Note: {stones.get('note', '')}")
    lines.append("")

    # GENERIC ISSUES
    lines.append("### 6. GENERIC ISSUES")
    for gi in plan.get("generic_issues", []):
        lines.append(f"- {gi}")
    if not plan.get("generic_issues"):
        lines.append("- None recorded.")
    lines.append("")

    # RECOMMENDED ACTIONS
    lines.append("### 7. RECOMMENDED ACTIONS (NON-DESTRUCTIVE)")
    for ra in plan.get("recommended_actions", []):
        lines.append(f"- {ra}")
    if not plan.get("recommended_actions"):
        lines.append("- No specific actions recommended.")
    lines.append("")

    lines.append("### 8. GUARANTEES")
    lines.append("- No files were modified by this plan.")
    lines.append("- All actions are manual, non-destructive suggestions.")
    lines.append("")

    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[SHELLX] Wrote Attempt-3 battle plan: {report_path}")
    return str(report_path)
