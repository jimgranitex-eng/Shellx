# SHELLX OPERATIONS — FULL LAY OF THE LAND AND GUIDE

Date: 2026-04-14
Workspace: D:/KickerOS
Scope: ShellX / AI Heart / KickerOS runtime, diagnostics, commands, wiring, logs, reports, and operator usage.

---

## 1. Executive Summary

ShellX in this repository is not a single executable. It is a layered operating workflow made of:

1. Python orchestration scripts that discover the runtime, wire the Qt environment, run diagnostics, and create reports.
2. A native Qt and QML application that actually launches the KickerOS UI.
3. QML feature panels, orb rendering, voice wiring, probe forwarding, and local browser and AI bridge behavior.
4. Recovery and observability artifacts such as reports, stones, blackbox runs, and the LinkX history file.

The active production-like flow currently centers on the following live path:

- Primary diagnostic entry: ai_heart_doctor.py
- Primary runtime launcher: ai_heart_launcher.py
- Primary executable: build_adaptive/KickerOS.exe
- Primary UI source: qml/main.qml
- Primary orb component: qml/components/SFIOrb.qml
- Report output path: .reports/
- Recovery stone path: .quarantine/stones/

Important note:
The app is not purely running from sealed packaged resources. The launcher and native app are set up so that source QML under the repo qml folder is part of the active runtime path. That means live source edits can immediately affect the running application.

---

## 2. Directory Map — What Lives Where

### Core operational folders

- qml/
  Main live QML source tree. This is where the active UI layout, orb, panels, services, and probe forwarders live.

- build_adaptive/
  The main active runtime build folder. Contains KickerOS.exe, Qt DLLs, plugins, platform binaries, runtime qml modules, screenshots, logs, diagnostics, and deployment artifacts.

- .reports/
  Generated ShellX and doctor reports. This is the historical evidence center for many runs.

- .quarantine/stones/
  Recovery stones and checkpoints. These are human-readable recovery breadcrumbs.

- .blackbox_runs/
  JSON run captures containing exit codes, stdout, and preflight issue lists.

- _ai_heart_state/
  State and daemon-related tracking, including runtime maps and proposed config.

- shellx_bundle/
  Bundle copy of the Python ShellX stack. Useful for packaging or export, but easy to confuse with the live source tree.

- shellx_operation_bundle/
  Another bundle variant. Similar duplication risk as shellx_bundle.

### High-value files

- ai_heart_doctor.py
- ai_heart_launcher.py
- ai_heart_system_utils.py
- ai_heart_daemon.py
- ai_brain.py
- kf_heart.py
- main.cpp
- ThemeManager.cpp
- qml/main.qml
- qml/components/SFIOrb.qml
- qml/components/AIBrainCommandCenter.qml
- LinkX_AI_Heart.md
- activity_timeline.json

---

## 3. Main ShellX Entry Points

### A. Doctor run
File: ai_heart_doctor.py
Purpose:
- Run a preflight check
- Launch the app once
- Record issues non-destructively
- Write blackbox JSON
- Write ShellX report
- Write recovery stone
- Update LinkX

This is the main ShellX operations command when you want diagnosis plus paperwork.

Typical command:
python -u ai_heart_doctor.py

### B. Launcher run
File: ai_heart_launcher.py
Purpose:
- Discover the best runtime candidate
- Wire the environment
- Start the local Grok and search bridge
- Launch KickerOS.exe
- Capture stdout and stderr
- Optionally attempt safe auto-repair relaunch logic

Typical command:
python ai_heart_launcher.py

### C. Preflight only
File: ai_heart_system_utils.py
Function: preflight_check()
Purpose:
- Check active paths
- Check Qt module presence
- Check exe and qml alignment
- Check logs and stones roots
- Report duplicates or missing pieces

Typical command:
python -c "from ai_heart_system_utils import preflight_check; ok, issues = preflight_check(); print('PREFLIGHT_OK=', ok); print('\n'.join(issues) if issues else 'NO_ISSUES')"

### D. Brain scan engine
File: ai_brain.py
Purpose:
- Scan the whole repo
- Build runtime candidates
- Try real launch attempts
- Write black-box evidence under _ai_brain_state/

Typical command:
python ai_brain.py

### E. Daemon supervisor
File: ai_heart_daemon.py
Purpose:
- Watch the tree
- Re-run a cycle after changes
- Optionally auto-repair and relaunch
- Log daemon events

Typical commands:
python ai_heart_daemon.py --once
python ai_heart_daemon.py

### F. KF heart preflight and canonical chooser
File: kf_heart.py
Purpose:
- Scan the project
- Pick canonical exe and qml
- Save runtime map

Typical command:
python kf_heart.py

---

## 4. Detailed Startup Chain

### Step 1 — Doctor begins
The doctor updates the activity timeline and performs a preflight scan.

Doctor call flow:
1. update_activity_timeline()
2. preflight_check()
3. run_launcher_once()
4. write_blackbox_run()
5. build_shellx_doctor_report()
6. write_recovery_stone()
7. update_linkx_with_doctor_run()

### Step 2 — Launcher discovers runtime
The launcher walks the repo and prefers these runtime markers in order:

- build_adaptive
- build_adaptive_build
- build_msvc
- build

It looks for:
- KickerOS.exe
- Qt6Core.dll or Qt5Core.dll
- qml roots
- plugin and platforms folders

### Step 3 — Environment is wired
The launcher builds the process environment using:
- PATH
- QML2_IMPORT_PATH
- QT_QPA_PLATFORM_PLUGIN_PATH
- QT_PLUGIN_PATH

These decide whether Qt can find:
- qwindows.dll
- QtQuick Controls
- QtQuick3D
- QtQuick3D Effects
- any lab or helper modules

### Step 4 — Local bridge is started
The launcher starts tools/grok_http_bridge.py.
This creates a local HTTP server on:

127.0.0.1:8765

Supported endpoints:
- /grok
- /search
- /evaluate

These endpoints feed the QML interface with local text replies, search results, and ranking/evaluation data.

### Step 5 — Native app starts
main.cpp does the native boot work:
- creates QGuiApplication
- writes startup marker
- selects Direct3D11 RHI by default on Windows
- creates QQmlApplicationEngine
- exposes speechEngine
- exposes use3DFace
- adds import and plugin paths
- logs QML warnings
- probes Quick3D availability
- loads qml/main.qml from disk
- writes startup_debug.log entries
- writes screenshots such as snap_DEFAULT.png

### Step 6 — QML root comes online
qml/main.qml becomes the central live state machine.
It controls:
- appState
- orb mode versus content mode versus listening mode
- speech callbacks
- AI Brain panel toggles
- search and Grok bridge calls
- probe forwarder connections

---

## 5. Live UI and Wiring Map

### Root UI file
qml/main.qml

### Key live components

1. SFIOrb
   The visual 3D orb and particles layer.

2. AIBrainCommandCenter
   Operator control panel for toggles and runtime features.

3. ProbeRunner_forward
   Lightweight QML-side forwarder for probe results.

4. DocumentCard
   Receives and displays parsed result data.

### Main signal and state wiring

speechEngine signals are connected into the UI for:
- text recognized
- listening started
- listening stopped
- speaking started
- speaking finished

Main properties that shape runtime behavior:
- enableBrowserBridge
- enableProbeRunner
- enableDiagnostics
- enableVoiceCommands
- enablePerformanceOptimizations
- orbListening
- appState

The orb is bound to the AI Brain switches so the control panel can directly affect visual behavior.

---

## 6. ShellX Commands Guide

## Core operator commands

### Quick diagnosis and report generation
python -u ai_heart_doctor.py

Use when:
- you want a diagnostic pass
- you want blackbox evidence
- you want the report and recovery stone updated

### Direct runtime launch
python ai_heart_launcher.py

Use when:
- you want to test whether the app boots
- you need the launcher to auto-discover the runtime

### One-line preflight check
python -c "from ai_heart_system_utils import preflight_check; ok, issues = preflight_check(); print('PREFLIGHT_OK=', ok); print('\n'.join(issues) if issues else 'NO_ISSUES')"

Use when:
- you want a quick alignment check without the full doctor sequence

### Run daemon once
python ai_heart_daemon.py --once

Use when:
- you want one supervised cycle
- you want to include auto-repair attempt logic without staying resident

### Full daemon loop
python ai_heart_daemon.py

Use when:
- you want continuous monitoring while iterating on the codebase

### Brain-based candidate runtime sweep
python ai_brain.py

Use when:
- multiple builds exist and you want the brain logic to scan runtime candidates

---

## 7. VS Code Tasks Guide

Defined in .vscode/tasks.json.

### CMake Configure
cmake -S . -B build_adaptive -G MinGW Makefiles -DCMAKE_PREFIX_PATH=C:/Qt/6.10.2/mingw_64

Purpose:
- configure the build folder
- lock in the MinGW Qt path

### CMake Build
cmake --build build_adaptive -- -j 4

Purpose:
- build the main runtime
- this is the default build task

### windeployqt
C:/Qt/6.10.2/mingw_64/bin/windeployqt.exe --release build_adaptive/KickerOS.exe

Purpose:
- copy Qt runtime dependencies for deployment

### Run Build Toolbox
py -3 tools/build_toolbox.py

Purpose:
- build utility workflow for the repo

### Pack Probe Venv for build_adaptive
pwsh -NoProfile -ExecutionPolicy Bypass -Command .\scripts\pack_probe_venv.ps1 -ExePath 'D:\KickerOS\build_adaptive\kickeros.exe' -VenvPath 'D:\KickerOS\.venv_probe'

Purpose:
- package the probe virtual environment beside the target runtime

---

## 8. Logs, Reports, Stones, and Evidence

### Report outputs
Folder: .reports/

Contains:
- ShellX doctor run reports
- summary reports
- deep diagnostic writeups
- full reports

Typical file naming pattern:
ShellX_Doctor_TIMESTAMP_doctor_run.md

### Recovery stones
Folder: .quarantine/stones/

Purpose:
- human-readable checkpoints
- restore points in narrative form
- traceable decision history

### Blackbox runs
Folder: .blackbox_runs/

Purpose:
- structured JSON evidence for each run
- stdout and exit code capture

### Activity timeline
File: activity_timeline.json

Purpose:
- detect active roots
- record detected builds, qml roots, qt roots, logs, and stones

### LinkX
File: LinkX_AI_Heart.md

Purpose:
- long-lived history index of what happened and when
- ties reports and stones together over time

---

## 9. Local Services and Bridges

### Grok HTTP bridge
File: tools/grok_http_bridge.py
Port: 8765

Routes:
- /grok -> simple local AI stub response
- /search -> launches headless_browser.py for search-style result extraction
- /evaluate -> returns ranked comparison and summary payloads

### Browser runner
File: browser_runner.py

Purpose:
- run a query
- optionally trigger the headless browser
- return JSON to the QML side

### Headless browser
File: headless_browser.py

Purpose:
- run a Playwright-backed DuckDuckGo search
- produce a normalized result list

Dependency note:
If Playwright is missing, the script returns fallback results instead of crashing the entire UI flow.

---

## 10. Voice and Probe Operations

### Voice path
File: src/SpeechEngine.cpp

Behavior:
- Windows SAPI backend
- listening thread for recognition
- speaking thread for text-to-speech
- emits signals back to QML

### Probe path
Files:
- qml/Probes/ProbeRunner_forward.qml
- examples/probe_runner/
- scripts and wrapper tooling nearby

Behavior:
- watches for JSON probe outputs under logs/documents/
- updates the document card if matching data arrives
- avoids hard failure when the C++ probe type is not actively used in the main app path

---

## 11. Known Operational Realities

### Active runtime truth
The active runtime currently points at build_adaptive/KickerOS.exe.

### Source-of-truth UI
The UI currently uses the repo qml source tree as part of the runtime path.

### Build-side wrappers exist
Some build-side QML component files are only wrappers that Loader-redirect back into the repo source tree.
This is especially important for SFIOrb.

### Not every scary log is current
Several diagnostics under build_adaptive are historical and should not be treated as live failures unless their timestamps are fresh.

Examples of often-stale evidence:
- engine_diagnostics_err.txt
- older kickeros_run.log files
- older direct_diagnostics_*.txt files

---

## 12. Major Fragile Spots

### 1. Duplicate bundle trees
Both shellx_bundle and shellx_operation_bundle contain copies of the ShellX Python stack.
Risk:
- fixes in the live source may not exist in the bundles
- searching the repo can make stale copies look like the live code

### 2. Broad preflight scanning
The preflight code can scan very broadly across C:/ and D:/.
Risk:
- duplicate warnings may refer to unrelated machine-wide paths
- this creates noise during diagnosis

### 3. Dist qml precedence
If dist/qml exists and gets placed first in QML2_IMPORT_PATH, it can shadow other working QML modules.
Risk:
- partial or stale packaged modules may override valid live ones

### 4. Runtime source loading
Because the app loads qml/main.qml from disk, source edits are immediately live.
Risk:
- fast iteration is easy
- accidental breakage is also easy

### 5. ThemeManager presence versus context exposure
The codebase clearly contains a C++ ThemeManager, but not all active paths show direct rootContext exposure in the same way older archived copies did.
Risk:
- some components safely fall back if themeManager is missing
- styling can still behave differently depending on path

---

## 13. Operator Workflow Guide

## If you want the fastest healthy cycle
1. Run doctor
2. Read newest file in .reports/
3. Check startup_debug.log and snap_DEFAULT.png under build_adaptive/
4. If needed, inspect LinkX_AI_Heart.md and the newest stone

## If you want to verify the runtime build target
1. Confirm build_adaptive/KickerOS.exe exists
2. Check the .vscode task entries
3. Run the launcher directly
4. Watch for rendererApi entries in startup_debug.log

## If you want a deployment cycle
1. Configure CMake
2. Build build_adaptive
3. Run windeployqt
4. Pack the probe venv if probe features matter for the deployment

## If you want deep evidence
Check these in order:
- activity_timeline.json
- .blackbox_runs/
- .reports/
- .quarantine/stones/
- LinkX_AI_Heart.md
- build_adaptive/startup_debug.log
- build_adaptive/module_versions.txt

---

## 14. Recommended Reading Order for Future Work

If someone new opens this repo and needs to understand ShellX quickly, the best order is:

1. This guide
2. ai_heart_doctor.py
3. ai_heart_launcher.py
4. ai_heart_system_utils.py
5. main.cpp
6. qml/main.qml
7. qml/components/SFIOrb.qml
8. qml/components/AIBrainCommandCenter.qml
9. LinkX_AI_Heart.md
10. the newest doctor report in .reports/

---

## 15. Practical Meaning of ShellX in This Repo

In this repository, ShellX means the operating layer that:
- observes the app
- chooses the runtime
- diagnoses startup and alignment issues
- launches the app safely
- records evidence
- writes reports and stones
- keeps a repair and history trail

It is both a tooling workflow and a recovery discipline, not just a single script.

---

## 16. Final Bottom Line

If you only remember five things, remember these:

1. The main ShellX runtime flow begins with ai_heart_doctor.py and ai_heart_launcher.py.
2. The current live executable is build_adaptive/KickerOS.exe.
3. The current live UI source is qml/main.qml and qml/components/SFIOrb.qml.
4. The local bridge on 127.0.0.1:8765 is part of the query and evaluation flow.
5. Reports, stones, blackbox runs, and LinkX together form the ShellX operational memory of the project.

---

End of guide.
