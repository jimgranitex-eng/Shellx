# ai_heart_doctor.py
import subprocess
from datetime import datetime
from pathlib import Path

from ai_heart_doctor_config import LAUNCHER_CMD, PROJECT_ROOT, LOG_PREFIX
from ai_heart_system_utils import (
    load_timeline,
    update_activity_timeline,
    write_blackbox_run,
    deep_detect_qt_modules,
    investigate_exe,
    investigate_qml_root,
    investigate_logs,
    investigate_stones,
    build_fix_plan_from_investigation,
    write_fix_plan_report,
    preflight_check,
    save_timeline,
    save_proposed_config,
    build_shellx_doctor_report,
    write_recovery_stone,
    update_linkx_with_doctor_run,
)

def run_launcher_once(timeout_seconds: int = 45):
    print(f"{LOG_PREFIX} Running launcher once: {LAUNCHER_CMD}")
    proc = subprocess.Popen(
        LAUNCHER_CMD,
        cwd=PROJECT_ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )
    try:
        stdout, _ = proc.communicate(timeout=timeout_seconds)
        code = proc.returncode
    except subprocess.TimeoutExpired:
        proc.kill()
        stdout, _ = proc.communicate()
        code = 124
        stdout += f"\n[{LOG_PREFIX}] Launcher timed out after {timeout_seconds}s and was terminated.\n"

    print(f"{LOG_PREFIX} Launcher exit code: {code}")
    print(stdout)
    return code, stdout

def attempt_1_quick():
    update_activity_timeline()
    ok, issues = preflight_check()
    if not ok:
        print(f"{LOG_PREFIX} Preflight issues detected — doctor will continue non-destructively and record issues.")

    code, out = run_launcher_once()

    timeline = load_timeline()
    timeline["last_run"] = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "exit_code": code,
        "launcher_path": str(PROJECT_ROOT / "ai_heart_launcher.py"),
        "exe_path_used": "",
        "qml_root_used": "",
        "qt_root_used": "",
        "logs_written": [],
        "stones_written": []
    }
    save_timeline(timeline)

    blackbox_path = write_blackbox_run("doctor_run", {
        "exit_code": code,
        "stdout": out,
        "preflight_issues": issues
    })

    report_path = build_shellx_doctor_report(
        run_id="doctor_run",
        exit_code=code,
        preflight_issues=issues,
        timeline=timeline,
        blackbox_path=blackbox_path,
    )

    stone_path = write_recovery_stone(
        title="AI Heart Doctor — ShellX Run",
        description="Doctor run with timeline, preflight, blackbox, and ShellX report."
    )

    update_linkx_with_doctor_run(report_path, stone_path)

    return code, out

def attempt_2_deep_scan():
    print(f"{LOG_PREFIX} Attempt 2: deep scan (non-destructive).")

    update_activity_timeline()
    timeline = load_timeline()
    active = timeline.get("active_paths", {})

    qt_root = Path(active.get("active_qt_root") or "")
    if qt_root.exists():
        qt_status = deep_detect_qt_modules(qt_root, timeline)
    else:
        qt_status = {}

    exe_info = investigate_exe(timeline)
    qml_info = investigate_qml_root(timeline)
    logs_info = investigate_logs(timeline)
    stones_info = investigate_stones(timeline)

    # You can also pass preflight issues here if you want richer context
    generic_issues = []

    investigation_payload = {
        "qt_status": qt_status,
        "exe_info": exe_info,
        "qml_info": qml_info,
        "logs_info": logs_info,
        "stones_info": stones_info,
        "generic_issues": generic_issues,
    }

    write_blackbox_run("attempt2_deep", {
        "timeline": timeline,
        "investigation": investigation_payload,
        "note": "Deep scan performed. No destructive actions taken."
    })

    print(f"{LOG_PREFIX} Attempt 2 deep scan complete.")
    return investigation_payload

def attempt_3_battle_plan(investigation_payload):
    """
    Attempt 3: build a non-destructive battle plan from deep investigation.
    """
    print(f"{LOG_PREFIX} Attempt 3: compiling battle plan from investigation results.")

    qt_status = investigation_payload.get("qt_status", {})
    exe_info = investigation_payload.get("exe_info", {})
    qml_info = investigation_payload.get("qml_info", {})
    logs_info = investigation_payload.get("logs_info", {})
    stones_info = investigation_payload.get("stones_info", {})
    generic_issues = investigation_payload.get("generic_issues", [])

    plan = build_fix_plan_from_investigation(
        qt_status=qt_status,
        exe_info=exe_info,
        qml_info=qml_info,
        logs_info=logs_info,
        stones_info=stones_info,
        generic_issues=generic_issues,
    )

    bb_path = write_blackbox_run("attempt3_plan", plan)
    report_path = write_fix_plan_report(plan, run_id="attempt3_plan")

    print(f"{LOG_PREFIX} Attempt 3 battle plan written: {report_path} (blackbox: {bb_path})")
    print(f"{LOG_PREFIX} No files were modified. Follow the recommended actions manually.")
    return plan


MAX_AUTO_REWIRES = 4
DEFAULT_QT_PATH = r"C:\Qt\6.11.0\mingw_64"


def propose_qt_root_candidates(timeline: dict, qt_status: dict, preferred_first: str = None):
    candidates = []
    # prefer explicit preferred_first
    if preferred_first:
        candidates.append(preferred_first)

    # collect from qt_status global_hits and past_dirs
    for info in qt_status.values():
        for d in info.get("past_dirs", []):
            if d and d not in candidates:
                candidates.append(d)
        for h in info.get("global_hits", []):
            p = str(Path(h).parent)
            if p and p not in candidates:
                candidates.append(p)

    # add common C:\Qt subfolders if present
    root = Path("C:/Qt")
    if root.exists():
        for child in root.iterdir():
            if child.is_dir():
                p = str(child)
                if p not in candidates:
                    candidates.append(p)

    return candidates


def try_auto_rewire_qt(investigation_payload: dict, max_attempts: int = MAX_AUTO_REWIRES, preferred_first: str = DEFAULT_QT_PATH):
    timeline = load_timeline()
    qt_status = investigation_payload.get("qt_status", {})

    candidates = propose_qt_root_candidates(timeline, qt_status, preferred_first=preferred_first)
    tried = []
    attempts = 0

    for cand in candidates:
        if attempts >= max_attempts:
            break
        if not cand:
            continue
        cand_path = Path(cand)
        attempts += 1
        tried.append(cand)

        print(f"{LOG_PREFIX} Auto-rewire attempt {attempts}: trying Qt root {cand}")

        proposed = {
            "active_qt_root": str(cand_path)
        }
        save_proposed_config(proposed)

        # Run preflight using proposed config
        ok, issues = preflight_check(use_proposed=True)
        if not ok:
            print(f"{LOG_PREFIX} Proposed preflight failed for {cand}: {issues}")
            continue

        # If preflight ok, try launching with this proposed config
        # Promote proposed into timeline for the launcher run
        tl = load_timeline()
        ap = tl.get("active_paths", {})
        ap["active_qt_root"] = str(cand_path)
        tl["active_paths"] = ap
        save_timeline(tl)

        code, out = run_launcher_once()
        write_blackbox_run("auto_rewire_attempt", {"candidate": cand, "exit_code": code, "stdout": out})

        if code == 0:
            print(f"{LOG_PREFIX} Auto-rewire succeeded with Qt root: {cand}")
            return {"status": "success", "chosen_qt_root": cand, "attempts": attempts, "tried": tried}
        else:
            print(f"{LOG_PREFIX} Launcher still failed with Qt root {cand} (exit {code}).")

    return {"status": "failed", "attempts": attempts, "tried": tried}

def main():
    # Attempt 1: quick preflight + launcher run
    code, _ = attempt_1_quick()
    if code == 0:
        print(f"{LOG_PREFIX} Launcher exited cleanly on Attempt 1.")
        return

    # Attempt 2: deep scan
    investigation_payload = attempt_2_deep_scan()

    # Optionally merge preflight issues into generic_issues
    ok, issues = preflight_check()
    investigation_payload["generic_issues"] = issues

    # Attempt: try auto-rewire for Qt using candidates (up to MAX_AUTO_REWIRES)
    auto = try_auto_rewire_qt(investigation_payload, max_attempts=MAX_AUTO_REWIRES, preferred_first=DEFAULT_QT_PATH)
    if auto.get("status") == "success":
        print(f"{LOG_PREFIX} Auto-rewire succeeded; launcher worked. Promoted Qt root: {auto.get('chosen_qt_root')}")
        return

    # If auto-rewire failed, escalate to Attempt 3 battle plan
    investigation_payload.setdefault("generic_issues", []).append(
        f"Auto-rewire exhausted ({auto.get('attempts')} attempts). User input required to choose Qt root."
    )
    attempt_3_battle_plan(investigation_payload)
    print(f"{LOG_PREFIX} Escalation required. See Attempt-3 battle plan in .reports.")

if __name__ == "__main__":
    main()
