# ShellX Ecosystem — Master Specification

**Version:** 3.2.1  
**Purpose:** Defines the complete ShellX module system, pipeline architecture, AIWorker agents, ShellX-V2/V3 engines, daemon, UI, and future roadmap.

---

## Overview

ShellX is more than a CLI — it's a **cognitive engine ecosystem** with:

- **ShellX-V2** — Next-gen operating system for all modes
- **Modules** — Individual mode commands (Lite, Deep, Debug, Fix, etc.)
- **Pipelines** — Multi-step automation chains
- **AIWorkers** — Specialized mini-agents deployed automatically
- **ShellX-Superman** — Unified mode combining all capabilities
- **ShellX-Daemon** — Background watcher/automation
- **ShellX-UI** — Visual dashboard (conceptual)
- **ShellX-V3** — Multi-agent parallel system (future)

---

## ShellX-V2 (Next Generation Engine)

ShellX-V2 is the unified architecture that powers all ShellX modes.

**Core Principles:**
1. Every ShellX mode is a module
2. Each module has: Input, Execution Logic, Output
3. ShellX-V2 can chain modules together (pipelines)
4. ShellX-V2 maintains state (stones, tasks, context)
5. ShellX-V2 is the "OS" for ShellX

**Core Components:**
- **V2-Core** — Main engine
- **V2-Memory** — Persistent state (tasks, stones, context)
- **V2-Modules** — Plugin system (Lite, Deep, Debug, Fix, etc.)
- **V2-Pipeline** — Multi-step automation
- **V2-Context** — Multi-project awareness
- **V2-Reports** — Unified reporting format

**Triggers:**
```
ShellX-V2: <message>
ShellX-V2-Run: <pipeline>
ShellX-V2-Module: <module> <message>
```

---

## ShellX Modules (Modes)

Each module is invoked as `ShellX-<Mode>: <message>` (designed for VS Coder / agentic use).

| Module | Purpose | Output |
|--------|---------|--------|
| **ShellX-Core** | Full workflow engine | Analyze, Integrate, Verify, reports, checklist |
| **ShellX-Lite** | Fast minimal output | 5–10 line summary, quick checklist |
| **ShellX-Deep** | Ultra-detailed audit | File-by-file breakdown, dependency graph, risk assessment |
| **ShellX-Debug** | Diagnostics mode | Error extraction, stack traces, root-cause analysis |
| **ShellX-Fix** | Fix suggestions | Code edits, file rewrites, missing imports |
| **ShellX-AutoFix** | Fix + re-check twice | Fix → verify → integrate → re-check |
| **ShellX-Memory** | Persistent task tracking | What was done, pending, last stones, errors |
| **ShellX-AutoArchive** | Save every run | Archive input, output, stones, logs, reports |
| **ShellX-AutoStone** | Rich recovery stones | Timestamp, title, description, what changed |
| **ShellX-MultiProject** | Project switching | Load project-specific stones, LinkX, reports |
| **ShellX-SmartInput** | Auto-detect input type | Classify code/logs/tasks/instructions |
| **ShellX-Quick** | Instant output | One paragraph, one checklist, one next step |
| **ShellX-Silent** | Checklist only | No explanations, just checklist |
| **ShellX-Explain** | Explain reasoning | Why errors happen, architecture, decisions |
| **ShellX-Architect** | System design | Component mapping, data flow, API flow, risk analysis |
| **ShellX-Refactor** | Code improvement | Cleaner structure, better patterns, better performance |

---

## ShellX-Pipeline (Multi-Step Automation)

Run multiple modules in sequence automatically.

**Syntax:**
```
ShellX-Pipeline: <Step1> → <Step2> → <Step3> ...
```

**Examples:**
```
ShellX-Pipeline: Deep → AutoFix → Deep → Summary
ShellX-Pipeline: Debug → Fix → Summary
ShellX-Pipeline: Architect → Deep → Checklist
ShellX-Pipeline: Debug → AutoFix → Repeat(2) → Summary
ShellX-Pipeline: Deep → AutoFix → UntilClean → Summary
```

**Supported Steps:**
Deep, Lite, Debug, Fix, AutoFix, Memory, Architect, Refactor, Quick, Silent, Explain, Summary, Checklist

**Advanced modifiers:**
- `Repeat(n)` — repeat previous step n times
- `UntilClean` — repeat until no errors remain

**Execution Rules:**
1. Each step runs as a ShellX module
2. Output of each step feeds into the next
3. Final output is written to the report area
4. Stones and LinkX update after the final step

**The `--report` flag:**
Adding `--report` to any ShellX-Superman or ShellX module command forces the system to skip code patching and produce a full structured report instead (Summary, Detailed, Full, Integration, Checklist).

---

## ShellX-Pipeline-Templates

Prebuilt named pipelines for common tasks.

| Template | Steps |
|----------|-------|
| **FullAudit** | `Deep → AutoFix → Deep → Summary` |
| **BugHunt** | `Debug → AutoFix → Debug → Checklist` |
| **ReleasePrep** | `Architect → Deep → Summary → Checklist → AutoStone` |
| **QuickFix** | `Debug → Fix → Summary` |
| **Stabilize** | `AutoFix → Deep → AutoFix → Summary` |

Usage: `ShellX-Pipeline: FullAudit`

---

## AIWorkers (Specialized Mini-Agents)

Deployed automatically by ShellX-Superman. Each has a single focused job.

| Worker | Role | What It Does |
|--------|------|-------------|
| **Worker-Debug** | Error extraction | Reads logs, stack traces, finds root causes |
| **Worker-Fix** | Patch generator | Code diffs, function rewrites, wiring fixes |
| **Worker-Architect** | System mapper | Component relationships, data flow, structure |
| **Worker-UI** | UI analyzer | Checks bindings, triggers, dashboard logic |
| **Worker-Pipeline** | Flow validator | Ensures pipeline ordering, missing stages |
| **Worker-Integration** | Wiring inspector | Maps file→function→call chain, finds mismatches |
| **Worker-Memory** | State tracker | Remembers what was fixed, pending, errors |
| **Worker-Docs** | Documentation | Generates reports, architecture summaries |
| **Worker-Security** | Vulnerability scan | Scans for secrets, exposed keys |
| **Worker-Terminal** | Output reader | Reads terminal output, detects runtime failures |

### AIWorker Flowchart

```
ShellX-Superman
   ↓
SmartInput Engine
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

### Integration Map (Conceptual)

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

### Auto-Wiring Script (Conceptual)

ShellX-Superman uses this logic to detect and repair wiring issues:

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

## ShellX-Daemon (Background Engine)

Conceptual background mode that watches files and reacts automatically.

| Trigger | Action |
|---------|--------|
| File changes | Run ShellX-Debug |
| Build fails | Run `Debug → AutoFix → Summary` |
| New folder appears | Run ShellX-Architect |
| New errors in logs | Run ShellX-Fix or AutoFix |
| New tasks added | Update ShellX-Memory |

Commands: `ShellX-Daemon: Start`, `ShellX-Daemon: Stop`

---

## ShellX-UI (Visual Dashboard — Conceptual)

A visual interface for ShellX with the following panels:

| Panel | Purpose |
|-------|---------|
| **Stones** | List of recovery stones |
| **Tasks** | Current and pending tasks |
| **Reports** | Summary / Detailed / Full |
| **Pipelines** | Available pipelines and templates |
| **Project** | Structure, files, components |
| **Errors/Logs** | Current issues and logs |

**Capabilities:**
- Click-to-run modules (e.g., run ShellX-Deep on a file)
- Click-to-run pipelines (e.g., FullAudit)
- View history of runs
- View LinkX map
- View project health at a glance

Commands: `ShellX-UI: Open`, `ShellX-UI: Refresh`

---

## ShellX-V3 (Multi-Agent System)

Runs multiple specialized agents in parallel for comprehensive analysis.

**Agents:** Debug, Fix, Architect, Memory, Refactor

**Behavior:**
1. You type: `ShellX-V3: <high-level goal>`
2. Agents run in parallel
3. Results merge into unified report
4. Stones, LinkX, tasks update

**Example:**
```
ShellX-V3: stabilize the project
  → Debug Agent: finds errors
  → Fix Agent: proposes fixes
  → Deep Agent: audits integration
  → Architect Agent: checks structure
  → Memory Agent: updates tasks and stones
  → Final: unified stabilization report
```

---

## ShellX-Superman (Unified Mode)

Combines everything — modules, pipelines, AIWorkers, V3 agents — into one unstoppable mode.

**Trigger:**
```
ShellX-Superman: <goal> --report
```

**Execution flow:**
1. SmartInput classifies the goal
2. Deploys all relevant AIWorkers
3. Builds a dynamic pipeline
4. Runs modules and workers in parallel
5. Merges results into a master report
6. Updates stones, LinkX, tasks

**Detailed 9-step execution:**
1. SmartInput → classify message
2. Deep → full audit
3. Debug → extract errors
4. AutoFix → apply fixes
5. Deep → verify fixes
6. Architect → map system
7. Memory → update tasks
8. AutoStone → create recovery stone
9. Summary → final report

**Output:**
- Plan
- Architecture
- Integration mapping
- Code proposals
- Pipelines
- UI notes
- Risks
- Next steps
- Checklist

**"Fix Everything" preset command:**
```
ShellX-Superman: fix all wiring, workers, pipelines, services, and integration issues in this project so the UI, backend, pipelines, workers, and services all function end-to-end --report
```

---

## Quick Reference

| Command | Description |
|---------|-------------|
| `ShellX: <msg>` | Core full workflow |
| `ShellX-Lite: <msg>` | Short summary |
| `ShellX-Deep: <msg>` | Detailed audit |
| `ShellX-Debug: <msg>` | Diagnostics |
| `ShellX-Fix: <msg>` | Fix suggestions |
| `ShellX-AutoFix: <msg>` | Fix + re-check |
| `ShellX-Memory: <msg>` | Task tracking |
| `ShellX-Architect: <msg>` | System design |
| `ShellX-Refactor: <msg>` | Code improvement |
| `ShellX-Explain: <msg>` | Reasoning |
| `ShellX-Superman: <goal> --report` | Everything |
| `ShellX-V3: <goal>` | Multi-agent |
| `ShellX-Pipeline: <steps>` | Multi-step |
| `ShellX-Daemon: Start\|Stop` | Background |
| `ShellX-UI: Open\|Refresh` | Dashboard |

---

*This document is the master spec for the ShellX cognitive ecosystem.*  
*See [Commands.md](Commands.md) for the 40-command CLI reference.*
