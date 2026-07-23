# ShellX Ecosystem — Master Specification

**Version:** 3.2.0  
**Purpose:** Defines the complete ShellX module system, pipeline architecture, AIWorker agents, and future roadmap.

---

## Overview

ShellX is more than a CLI — it's a **cognitive engine ecosystem** with:

- **Modules** — Individual mode commands (Lite, Deep, Debug, Fix, etc.)
- **Pipelines** — Multi-step automation chains
- **AIWorkers** — Specialized mini-agents deployed automatically
- **ShellX-Superman** — Unified mode combining all capabilities
- **ShellX-V3** — Multi-agent parallel system (future)

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
```

**Advanced modifiers:**
- `Repeat(n)` — repeat previous step n times
- `UntilClean` — repeat until no errors remain

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

## ShellX-V3 (Multi-Agent System)

Runs multiple specialized agents in parallel for comprehensive analysis.

**Agents:** Debug, Fix, Architect, Memory, Refactor

**Flow:**
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

**Trigger:** `ShellX-Superman: <goal> --report`

**Execution flow:**
1. SmartInput classifies the goal
2. Deploys all relevant AIWorkers
3. Builds a dynamic pipeline
4. Runs modules and workers in parallel
5. Merges results into a master report
6. Updates stones, LinkX, tasks

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

---

*This document is the master spec for the ShellX cognitive ecosystem.*  
*See [Commands.md](Commands.md) for the 40-command CLI reference.*
