# ============================================================
# SHELLX — MASTER MODULE FILE
# ============================================================
#
# This file defines every ShellX mode, variant, and behavior.
# Use these commands by typing:
#
#   ShellX-<Mode>: <Your message>
#
# Examples:
#   ShellX-AutoFix: fix the error in server.py
#   ShellX-Deep: analyze and repair everything
#   ShellX-Debug: diagnose this crash
#   ShellX-Lite: quick summary only
#   ShellX-Architect: map the system design
#
# ============================================================

## SHELLX MODULES — COMPLETE MODE REFERENCE

| Mode | Purpose |
|------|---------|
| `ShellX-Core` | Full workflow — runs all standard passes |
| `ShellX-Lite` | Short summaries — minimal output |
| `ShellX-Deep` | Detailed audits — exhaustive analysis |
| `ShellX-Debug` | Diagnostics — finds errors, traces, root causes |
| `ShellX-Fix` | Fix suggestions — proposes patches and rewrites |
| `ShellX-AutoFix` | Fix + re-check — applies fixes and re-verifies |
| `ShellX-Memory` | Task tracking — remembers state across runs |
| `ShellX-AutoArchive` | Save runs — archives current session |
| `ShellX-AutoStone` | Recovery stones — stamps timestamped milestone |
| `ShellX-MultiProject` | Project switching — manages multiple codebases |
| `ShellX-SmartInput` | Input classification — routes the message |
| `ShellX-Quick` | Minimal output — fastest response |
| `ShellX-Silent` | Checklist only — no prose |
| `ShellX-Explain` | Explain reasoning — verbose rationale |
| `ShellX-Architect` | System design — maps components and data flow |
| `ShellX-Refactor` | Code improvement — cleans up and restructures |

---

## SHELLX-PIPELINE — MULTI-STEP AUTOMATION

**Syntax:**
```
ShellX-Pipeline: <Step1> → <Step2> → <Step3> ... --report
```

**Supported Steps:**
`Deep` `Lite` `Debug` `Fix` `AutoFix` `Memory` `Architect`
`Refactor` `Quick` `Silent` `Explain` `Summary` `Checklist`

**Advanced operators:**
- `Repeat(n)` — repeat a step n times
- `UntilClean` — keep looping until no errors remain

---

## SHELLX-PIPELINE-TEMPLATES

| Template | Pipeline |
|----------|---------|
| **FullAudit** | `Deep → AutoFix → Deep → Summary` |
| **BugHunt** | `Debug → AutoFix → Debug → Checklist` |
| **ReleasePrep** | `Architect → Deep → Summary → AutoStone` |
| **QuickFix** | `Debug → Fix → Summary` |
| **Stabilize** | `AutoFix → Deep → AutoFix → Summary` |

---

## AIWORKERS — SPECIALIZED MINI-AGENTS

ShellX-Superman deploys these workers automatically based on the goal.

### 1. Worker-Debug
- **Role:** Extract errors, stack traces, missing imports, broken wiring, runtime failures.
- **Behavior:** Reads logs, identifies root causes, flags missing services.
- **Usage:** `ShellX-Debug: <message> --report`

### 2. Worker-Fix
- **Role:** Suggest patches, rewrites, wiring fixes, missing imports, code corrections.
- **Behavior:** Generates diffs, rewrites broken functions, fixes call chains.
- **Usage:** `ShellX-Fix: <message> --report`

### 3. Worker-Architect
- **Role:** Design system structure, data flow, and component relationships.
- **Behavior:** Maps UI → backend → pipeline → worker → service.
- **Usage:** `ShellX-Architect: <message> --report`

### 4. Worker-UI
- **Role:** Analyze UI files, layout, bindings, and dashboard logic.
- **Behavior:** Checks that UI buttons call real endpoints; detects missing bindings.
- **Usage:** `ShellX-Deep: analyze UI --report`

### 5. Worker-Pipeline
- **Role:** Validate pipeline steps, order, missing stages.
- **Behavior:** Ensures workers and services are registered; detects stub stages.
- **Usage:** `ShellX-Pipeline: Deep → Fix → Deep --report`

### 6. Worker-Integration
- **Role:** Map file → function → call chain → triggers.
- **Behavior:** Finds mismatched imports, missing calls, dead code, namespace issues.
- **Usage:** `ShellX-Deep: map integration --report`

### 7. Worker-Memory
- **Role:** Track tasks, stones, context, and progress across runs.
- **Behavior:** Remembers what was fixed, what is pending, last errors and pipeline state.
- **Usage:** `ShellX-Memory: update state --report`

---

## SHELLX-SUPERMAN — UNIFIED MODE

**Command:**
```
ShellX-Superman: <goal> --report
```

**Purpose:** Combine ALL ShellX capabilities — full automation using all modules, pipelines, and AIWorkers.

**Behavior:**
1. SmartInput classifies the goal.
2. Deploys all relevant AIWorkers.
3. Builds a dynamic pipeline.
4. Runs modules and workers in parallel.
5. Merges results into a master report.
6. Updates stones, LinkX, tasks.

**Output includes:**
- Plan
- Architecture map
- Integration mapping
- Code proposals
- Pipeline trace
- UI notes
- Risks
- Next steps
- Checklist

---

## SHELLX-SUPERMAN WORKER FLOWCHART

```
ShellX-Superman
  ↓
SmartInput
  ↓
AIWorker Deployment Layer
  ↓
[Debug] [Fix] [Architect] [UI] [Pipeline] [Integration] [Memory]
  ↓
ShellX Pipeline Engine
  ↓
ShellX Report Builder
  ↓
Final ShellX Report
```

---

## GENERAL INTEGRATION MAP (ANY PROJECT)

```
UI / Frontend
  ↓
Backend API Endpoint
  ↓
Workflow / Pipeline
  ↓
Worker Manager
  ↓
Workers (render, upload, process, etc.)
  ↓
Service Adapter (YouTube, DB, API, OS, etc.)
  ↓
Return result to UI / Dashboard
```

---

## SHELLX-SUPERMAN AUTO-WIRING SCRIPT

1. Detect UI → Backend wiring
2. Detect Backend → Pipeline wiring
3. Detect Pipeline → Worker wiring
4. Detect Worker → Service wiring
5. Detect Namespace / Import issues
6. Detect Missing Services
7. Build Fix Plan
8. Verify with tests
9. Update stones + LinkX

---

## SHELLX-V3 — MULTI-AGENT SYSTEM

**Agents:** Debug · Fix · Architect · Memory · Refactor

**Behavior:**
- Agents run in parallel.
- Results merge into a unified report.
- Stones, LinkX, tasks updated automatically.

**Trigger:**
```
ShellX-V3: <message>
```

---

## SHELLX-DAEMON — BACKGROUND ENGINE

```
ShellX-Daemon: Start
ShellX-Daemon: Stop
```

**Purpose:** Background ShellX engine that watches files, logs, errors, and tasks; auto-runs modules; auto-updates stones, LinkX, reports.

---

## SHELLX-UI — VISUAL DASHBOARD CONCEPT

**Panels:** Stones · Tasks · Reports · Pipelines · Project structure · Errors/logs

**Capabilities:**
- Click-to-run modules
- Click-to-run pipelines
- View history
- View LinkX map
- Project health overview

---

## QUICK GUIDE

1. Use `ShellX-Superman` for big goals.
2. Add `--report` to force full ShellX output.
3. Use pipelines for multi-step analysis.
4. Let AIWorkers handle specialized tasks.
5. Use the **Fix-Everything** command when stuck:
   ```
   ShellX-Superman: fix all wiring, workers, pipelines, services, and integration issues in this project so the UI, backend, pipelines, workers, and services all function end-to-end --report
   ```
6. Use Integration Map to understand data flow.
7. Use Auto-Wiring Script to repair structure.

---

## VERIFY CHECKLIST (run after every change)

Before committing, verify:

- [ ] No missing imports
- [ ] No missing wiring
- [ ] No missing function calls
- [ ] No missing return values
- [ ] No mismatched variable names
- [ ] No incomplete logic
- [ ] No unconnected components

---

## INTEGRATE TEMPLATE (use when adding new features)

```
INTEGRATE:

New feature: <feature name>

- File:     <path/to/file>
- Function: <function name>
- Line:     <line number>
- Calls:    <what it calls>
- Triggers: <what triggers it>
- Called by: <what calls it>
```

---

*End of SHELLX Master Module File*
