# ShellX Portable Bundle

This package is a portable ShellX starter set extracted from the live KickerOS workflow.

## What is inside

- Core ShellX doctor and launcher scripts
- Browser and bridge helpers
- VS Code integration snippets
- The full ShellX operations guide
- A quick on-the-spot startup path for new users

## Fast start for a new user

### 1. Unzip the bundle
Unzip this folder anywhere you want to work.

### 2. Open it in VS Code or another coding tool
Any editor is fine, but VS Code gives the best experience for the included integration snippets.

### 3. Install Python packages
On Windows PowerShell:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 4. Run the quick checks

```powershell
.\START_SHELLX_PORTABLE.ps1 -Mode preflight
.\START_SHELLX_PORTABLE.ps1 -Mode doctor
```

### 5. If you want the local bridge

```powershell
.\START_SHELLX_PORTABLE.ps1 -Mode bridge
```

This starts the local helper service on port 8765.

## Modes

- doctor: run the main diagnostic flow
- launcher: run the launcher flow
- preflight: fast alignment check
- daemon-once: supervised single cycle
- brain: repo sweep and candidate scan
- bridge: local HTTP helper

## Important reality

This portable bundle preserves the ShellX workflow, reports, bridges, and startup logic, but some flows still assume a Qt or QML style project unless you adapt the target paths.

If you are integrating into a non-KickerOS project, start with preflight and the VS Code snippets, then retarget the runtime-specific paths as needed.

## Best files to read first

1. docs/MINI_GUIDE.md
2. docs/SHELLX_OPERATIONS_GUIDE_2026-04-14.md
3. core/ai_heart_doctor.py
4. core/ai_heart_launcher.py
