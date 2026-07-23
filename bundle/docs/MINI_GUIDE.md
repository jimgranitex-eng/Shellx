# Mini Guide — Use ShellX Right Away

## Quickest path

### For diagnostics
Run:

```powershell
.\START_SHELLX_PORTABLE.ps1 -Mode doctor
```

### For a fast check only
Run:

```powershell
.\START_SHELLX_PORTABLE.ps1 -Mode preflight
```

### For the local HTTP helper
Run:

```powershell
.\START_SHELLX_PORTABLE.ps1 -Mode bridge
```

## What ShellX does

ShellX is the operator layer around a project. It helps you:

- inspect the workspace
- preflight the runtime
- launch a target app or flow
- capture evidence
- keep reports and recovery notes

## If you are new

Read in this order:

1. this file
2. the full operations guide
3. the doctor script
4. the launcher script

## If you want VS Code integration

Open the folder named vscode-integration and copy the snippets into your extension or tool project.

## Default local port

The helper bridge uses port 8765.

## Good first commands

```powershell
.\START_SHELLX_PORTABLE.ps1 -Mode preflight
.\START_SHELLX_PORTABLE.ps1 -Mode doctor
.\START_SHELLX_PORTABLE.ps1 -Mode launcher
```
