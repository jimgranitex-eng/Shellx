#!/usr/bin/env python3
"""
ai_heart_launcher.py
Lightweight launcher that hunts for a KickerOS exe, Qt DLLs, QML roots and plugins,
wires env vars (PATH/QML2_IMPORT_PATH/QT_PLUGIN_PATH) and launches the exe with
cwd set to the exe folder. Drop at project root and run `python ai_heart_launcher.py`.
"""
import os
import subprocess
import time
import shutil
from pathlib import Path
from typing import List, Optional

PROJECT_ROOT = Path(__file__).resolve().parent

# Optional: point to a local Qt install so we can copy missing QML modules
# when packaging or running from a dist folder. Adjust if you have a different
# Qt installation path on your machine.
import os as _os

# Allow overriding the Qt install via environment for automated rewires/tests.
# Do not force a global Qt path by default; prefer deployed runtime beside exe.
_qt_root_env = _os.environ.get("AI_HEART_QT_ROOT", "").strip()
QT_ROOT = Path(_qt_root_env) if _qt_root_env else None
QT_QML_ROOT = (QT_ROOT / "qml") if QT_ROOT else None
QT_PLUGIN_ROOT = (QT_ROOT / "plugins") if QT_ROOT else None


def find_files(root: Path, names: List[str]) -> List[Path]:
    hits: List[Path] = []
    lower_names = [n.lower() for n in names]
    for r, d, f in os.walk(root):
        rpath = Path(r)
        for name in f:
            if name.lower() in lower_names:
                hits.append(rpath / name)
    return hits

def find_dirs_named(root: Path, names: List[str]) -> List[Path]:
    hits: List[Path] = []
    lower_names = [n.lower() for n in names]
    for r, d, f in os.walk(root):
        rpath = Path(r)
        for name in d:
            if name.lower() in lower_names:
                hits.append(rpath / name)
    return hits

def pick_latest(paths: List[Path]) -> Optional[Path]:
    paths = [p for p in paths if p.exists()]
    if not paths:
        return None
    return max(paths, key=lambda p: p.stat().st_mtime)

def discover_runtime():
    exe_candidates = find_files(PROJECT_ROOT, ["KickerOS.exe", "kicker_os.exe"])

    # Prefer known runtime folders before falling back to newest binary.
    preferred_markers = [
        str(PROJECT_ROOT / "build_adaptive").lower(),
        str(PROJECT_ROOT / "build_adaptive_build").lower(),
        str(PROJECT_ROOT / "build_msvc").lower(),
        str(PROJECT_ROOT / "build").lower(),
    ]

    exe = None
    for marker in preferred_markers:
        for cand in exe_candidates:
            if marker in str(cand).lower() and cand.exists():
                exe = cand
                break
        if exe:
            break

    if not exe:
        exe = pick_latest(exe_candidates)

    qt_core_candidates = find_files(PROJECT_ROOT, ["Qt6Core.dll", "Qt5Core.dll"])
    qt_bin_dir = None
    if exe:
        for local_core in (exe.parent / "Qt6Core.dll", exe.parent / "Qt5Core.dll"):
            if local_core.exists():
                qt_bin_dir = local_core.parent
                break
    if not qt_bin_dir:
        qt_bin_hit = pick_latest(qt_core_candidates)
        if qt_bin_hit:
            qt_bin_dir = qt_bin_hit.parent

    ignored_markers = ["shellx_bundle", "shellx_operation_bundle", "recovery_stones", "_archive", ".quarantine"]

    qml_dirs = [
        p for p in find_dirs_named(PROJECT_ROOT, ["qml"])
        if not any(marker in str(p).lower() for marker in ignored_markers)
    ]
    preferred_qml_roots = []
    if exe:
        preferred_qml_roots.extend([exe.parent / "qml", exe.parent.parent / "qml"])
    preferred_qml_roots.append(PROJECT_ROOT / "qml")
    qml_root = next((p for p in preferred_qml_roots if p.exists()), None)
    if not qml_root:
        qml_root = pick_latest(qml_dirs)

    preferred_plugin_roots = []
    if exe:
        preferred_plugin_roots.extend([exe.parent / "platforms", exe.parent / "plugins"])
    preferred_plugin_roots.extend([
        PROJECT_ROOT / "build_adaptive" / "platforms",
        PROJECT_ROOT / "build_adaptive_build" / "platforms",
    ])
    plugin_root = next((p for p in preferred_plugin_roots if p.exists()), None)
    if not plugin_root:
        plugin_dirs = [
            p for p in find_dirs_named(PROJECT_ROOT, ["plugins", "platforms"])
            if not any(marker in str(p).lower() for marker in ignored_markers)
        ]
        plugin_root = pick_latest(plugin_dirs)

    return {
        "exe": exe,
        "qt_bin_dir": qt_bin_dir,
        "qml_root": qml_root,
        "plugin_root": plugin_root,
    }


def ensure_qml_modules(dist_qml: Path):
    """
    Non-destructive sync: copy missing QML modules from the Qt install
    into the `dist/qml` tree so the packaged app can find Controls/Quick3D/etc.
    """
    if not QT_QML_ROOT or not QT_QML_ROOT.exists():
        print(f"[AI HEART] Qt QML root not found: {QT_QML_ROOT}")
        return

    dist_qml.mkdir(parents=True, exist_ok=True)

    needed = ["QtQuick", "QtQuick3D", "QtQuick/Window"]

    for rel in needed:
        src = QT_QML_ROOT / rel
        dst = dist_qml / rel
        if not src.exists():
            continue
        if dst.exists():
            continue
        print(f"[AI HEART] Syncing QML module: {rel}")
        try:
            shutil.copytree(src, dst)
        except Exception as e:
            print(f"[AI HEART] Failed to copy {src} -> {dst}: {e}")

    # Ensure Controls module (handle variant names like Controls, Controls.2)
    controls_dst = dist_qml / "QtQuick" / "Controls"
    if not controls_dst.exists():
        qtquick_dir = QT_QML_ROOT / "QtQuick"
        if qtquick_dir.exists():
            # try to find any Controls* folder
            for child in qtquick_dir.iterdir():
                try:
                    if child.is_dir() and child.name.lower().startswith("controls"):
                        print(f"[AI HEART] Syncing QML Controls module: {child.name}")
                        try:
                            shutil.copytree(child, controls_dst)
                            break
                        except Exception as e:
                            print(f"[AI HEART] Failed to copy Controls {child} -> {controls_dst}: {e}")
                except Exception:
                    continue

def wire_env(runtime: dict):
    exe = runtime["exe"]
    qt_bin_dir = runtime["qt_bin_dir"]
    qml_root = runtime["qml_root"]
    plugin_root = runtime["plugin_root"]
    # Prepend discovered Qt bin to PATH so DLL resolution prefers local build Qt
    path_list = []
    if qt_bin_dir:
        path_list.append(str(qt_bin_dir))

    # Also prefer the configured QT_ROOT/bin if present
    if QT_ROOT and (QT_ROOT / "bin").exists():
        path_list.append(str(QT_ROOT / "bin"))

    if path_list:
        os.environ["PATH"] = os.pathsep.join(path_list) + os.pathsep + os.environ.get("PATH", "")

    # QML import paths: discovered qml root first, then local Qt qml
    qml_paths = []
    if qml_root:
        qml_paths.append(str(qml_root))
    if QT_QML_ROOT and QT_QML_ROOT.exists():
        qml_paths.append(str(QT_QML_ROOT))
    if qml_paths:
        # preserve any existing imports
        existing = os.environ.get("QML2_IMPORT_PATH", "")
        combined = os.pathsep.join(qml_paths)
        if existing:
            combined = combined + os.pathsep + existing
        os.environ["QML2_IMPORT_PATH"] = combined

    # Plugin paths: prefer Qt install plugins/platforms
    plugin_paths = []
    if plugin_root:
        # if plugin_root is a 'platforms' folder, use it directly
        try:
            if plugin_root.name.lower() == "platforms":
                plugin_paths.append(str(plugin_root))
            else:
                plugin_paths.append(str(Path(plugin_root) / "platforms"))
        except Exception:
            plugin_paths.append(str(plugin_root))

    if QT_PLUGIN_ROOT and (QT_PLUGIN_ROOT / "platforms").exists():
        plugin_paths.append(str(QT_PLUGIN_ROOT / "platforms"))

    if plugin_paths:
        existing = os.environ.get("QT_QPA_PLATFORM_PLUGIN_PATH", "")
        combined = os.pathsep.join(plugin_paths)
        if existing:
            combined = combined + os.pathsep + existing
        os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = combined

    # Keep old QT_PLUGIN_PATH for other plugin discovery
    if plugin_root:
        os.environ.setdefault("QT_PLUGIN_PATH", str(plugin_root))

    os.environ.setdefault("QML_XHR_ALLOW_FILE_READ", "1")

from ai_heart_autofix import auto_repair
# Optional integration: run doctor preflight-only before launching (avoids recursion)
try:
    from ai_heart_doctor_config import AUTO_RUN_DOCTOR
except Exception:
    # Default to disabled for CLI tests; set AUTO_RUN_DOCTOR in config to opt-in.
    AUTO_RUN_DOCTOR = False


def start_grok_http_bridge():
    try:
        proc = subprocess.Popen(
            ["python", str(PROJECT_ROOT / "tools" / "grok_http_bridge.py")],
            cwd=str(PROJECT_ROOT),
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        print("[AI HEART] Started Grok HTTP bridge (pid=", proc.pid, ")")
        return proc
    except Exception as e:
        print("[AI HEART] Failed to start Grok HTTP bridge:", e)
        return None


def _find_canonical_qml_path(runtime: dict, exe_path: Path) -> Path:
    # Prefer an explicitly provided canonical QML path
    cand = runtime.get("canonical_qml") or runtime.get("main_qml")
    if cand:
        p = Path(cand)
        if p.exists():
            return p

    # If we have a qml_root, prefer main.qml there
    qroot = runtime.get("qml_root")
    if qroot:
        p = Path(qroot) / "main.qml"
        if p.exists():
            return p

    # Try exe relative locations
    candidates = [exe_path.parent.parent / "qml" / "main.qml", exe_path.parent / ".." / "qml" / "main.qml"]
    for p in candidates:
        try:
            p = p.resolve()
        except Exception:
            pass
        if p.exists():
            return p

    # Fallback to exe parent /qml/main.qml
    return exe_path.parent / ".." / "qml" / "main.qml"


def launch(runtime: dict) -> int:
    exe = runtime["exe"]
    if not exe or not exe.exists():
        print("[AI HEART] No KickerOS exe found.")
        return -1
    wire_env(runtime)

    # Start the local Grok HTTP bridge so QML can call it via XHR
    try:
        bridge = start_grok_http_bridge()
        # give it a moment to bind the port
        time.sleep(0.5)
        if bridge:
            runtime["grok_bridge_proc"] = bridge
    except Exception:
        pass

    # Determine a dist/qml location to populate (prefer real dist if present)
    dist_qml = PROJECT_ROOT / "dist" / "qml"
    if not dist_qml.exists():
        # fall back to discovered qml root or exe-relative qml
        dist_qml = runtime.get("qml_root") or (exe.parent.parent / "qml")

    # Ensure basic QML modules are present in the dist/qml before launching
    try:
        if isinstance(dist_qml, Path):
            ensure_qml_modules(dist_qml)
    except Exception as e:
        print(f"[AI HEART] ensure_qml_modules failed: {e}")

    print("[AI HEART] Launching:", exe)
    print("  Qt bin:", runtime.get("qt_bin_dir"))
    print("  QML root:", runtime.get("qml_root"))
    print("  Plugins:", runtime.get("plugin_root"))
    print("  Dist QML:", dist_qml)

    # Build a safe env copy and explicitly set QML/import/plugin paths
    env = os.environ.copy()
    # --- QML IMPORT PATHS ---
    qml_paths = []

    # 1. dist qml (packaged)
    try:
        if dist_qml and Path(dist_qml).exists():
            qml_paths.append(str(dist_qml))
    except Exception:
        pass

    # 2. build qml (development)
    try:
        if runtime.get("qml_root") and Path(runtime.get("qml_root")).exists():
            qml_paths.append(str(runtime.get("qml_root")))
    except Exception:
        pass

    # 3. Qt install qml (critical for Qt.labs.platform, Controls, etc.)
    try:
        qt_qml_root = QT_QML_ROOT if QT_QML_ROOT and QT_QML_ROOT.exists() else None
        if qt_qml_root:
            qml_paths.append(str(qt_qml_root))
    except Exception:
        pass

    if qml_paths:
        env["QML2_IMPORT_PATH"] = os.pathsep.join(qml_paths)

    # Ensure PATH includes Qt bin so DLLs and platform plugins resolve
    try:
        qt_bin = (QT_ROOT / "bin") if QT_ROOT else None
        if qt_bin and qt_bin.exists():
            env["PATH"] = str(qt_bin) + os.pathsep + env.get("PATH", "")
    except Exception:
        pass

    plugin_root = runtime.get("plugin_root")
    # Preserve any existing QT_QPA_PLATFORM_PLUGIN_PATH and append discovered paths
    existing_qpa = os.environ.get("QT_QPA_PLATFORM_PLUGIN_PATH", "")
    # Choose the first existing platforms path (prefer discovered, then Qt install)
    qpa_path = None

    # Prefer deployed platforms folder next to the executable.
    try:
        exe_platforms = Path(exe).parent / "platforms"
        if exe_platforms.exists():
            qpa_path = str(exe_platforms)
    except Exception:
        pass

    if plugin_root:
        p1 = Path(plugin_root)
        if p1.name.lower() == "platforms" and p1.exists():
            if not qpa_path:
                qpa_path = str(p1)
        else:
            p2 = p1 / "platforms"
            if p2.exists():
                if not qpa_path:
                    qpa_path = str(p2)

    # Fallback to Qt install plugins/platforms
    if not qpa_path and QT_PLUGIN_ROOT and (QT_PLUGIN_ROOT / "platforms").exists():
        qpa_path = str(QT_PLUGIN_ROOT / "platforms")

    if qpa_path:
        env["QT_QPA_PLATFORM_PLUGIN_PATH"] = qpa_path

    # Debug: print important env vars being passed to the child process
    try:
        print("[AI HEART] ENV QML2_IMPORT_PATH:", env.get("QML2_IMPORT_PATH"))
        # Diagnostic: check for Qt.labs.platform availability on disk
        try:
            labs_platform = Path(env.get("QML2_IMPORT_PATH", "").split(os.pathsep)[-1]) / "Qt" / "labs" / "platform"
            print("[AI HEART] Qt.labs.platform exists:", labs_platform.exists(), str(labs_platform))
        except Exception:
            pass
        print("[AI HEART] ENV QT_QPA_PLATFORM_PLUGIN_PATH:", env.get("QT_QPA_PLATFORM_PLUGIN_PATH"))
        # print only first PATH entries for brevity
        path_preview = env.get("PATH", "").split(os.pathsep)[:4]
        print("[AI HEART] ENV PATH (preview):", path_preview)
    except Exception:
        pass

    try:
        # Capture combined stdout/stderr so we can analyze crashes
        proc = subprocess.Popen(
            [str(exe)],
            cwd=str(exe.parent),
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
        try:
            out, _ = proc.communicate(timeout=30)
        except Exception:
            proc.kill()
            out = ""

        code = proc.returncode if proc.returncode is not None else -1

        # Try auto-repair if a crash was detected in output
        try:
            exe_path = Path(exe)
            canonical_qml = _find_canonical_qml_path(runtime, exe_path)
            if code != 0 and out and auto_repair(out, str(canonical_qml)):
                print("[AI HEART] Auto-repair applied. Relaunching...")
                return launch(runtime)
        except Exception as e:
            print(f"[AI HEART] Auto-repair check failed: {e}")

        # Print captured output for inspection
        if out:
            print(out)

        return code
    except Exception as e:
        print("[AI HEART] Launch failed:", e)
        return -1


def launch_capture(runtime: dict, timeout: int = 30) -> tuple:
    """
    Launch the runtime and return a tuple `(exit_code, output_str)`.
    This variant does not attempt auto-repair; it's suitable for supervisors.
    """
    exe = runtime["exe"]
    if not exe or not exe.exists():
        print("[AI HEART] No KickerOS exe found for capture.")
        return -1, ""

    # reuse env wiring
    wire_env(runtime)

    dist_qml = PROJECT_ROOT / "dist" / "qml"
    if not dist_qml.exists():
        dist_qml = runtime.get("qml_root") or (exe.parent.parent / "qml")

    # ensure qml modules copied (best-effort)
    try:
        if isinstance(dist_qml, Path):
            ensure_qml_modules(dist_qml)
    except Exception:
        pass

    env = os.environ.copy()
    if dist_qml:
        env["QML2_IMPORT_PATH"] = str(dist_qml)
    plugin_root = runtime.get("plugin_root")
    if plugin_root:
        if plugin_root.name.lower() == "platforms":
            env["QT_QPA_PLATFORM_PLUGIN_PATH"] = str(plugin_root)
        else:
            env["QT_QPA_PLATFORM_PLUGIN_PATH"] = str(plugin_root / "platforms")

    try:
        proc = subprocess.Popen(
            [str(exe)],
            cwd=str(exe.parent),
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
        try:
            out, _ = proc.communicate(timeout=timeout)
        except Exception:
            proc.kill()
            out = ""
        code = proc.returncode if proc.returncode is not None else -1
        return code, out
    except Exception as e:
        print("[AI HEART] Launch capture failed:", e)
        return -1, ""

if __name__ == "__main__":
    # Optionally run the doctor in preflight-only mode before launching
    if AUTO_RUN_DOCTOR:
        try:
            print("[AI HEART] AUTO_RUN_DOCTOR is enabled — running AI Heart Doctor preflight...")
            subprocess.run(["python", "-u", "ai_heart_doctor.py"], cwd=str(PROJECT_ROOT), check=False)
        except Exception as e:
            print(f"[AI HEART] Failed to run preflight doctor: {e}")

    rt = discover_runtime()
    code = launch(rt)
    print("[AI HEART] Exit code:", code)
    time.sleep(1)
