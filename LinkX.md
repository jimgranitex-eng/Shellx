# LinkX — Integration Map & Link Tracker

> **Purpose:** Central registry of all component links, wiring paths, recovery stones, and session history for the ShellX project.

---

## INTEGRATION MAP

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
Service Adapter
  ↓
Return result to UI / Dashboard
```

---

## FILE → FUNCTION → CALL CHAIN

| File | Function / Component | Calls | Triggered By |
|------|---------------------|-------|-------------|
| `SHELLX.md` | Master spec | All modules | User command |
| `LinkX.md` | This file — integration tracker | — | ShellX-Superman, ShellX-Memory |
| `REPORT.md` | Summary/Detailed/Full reports | — | ShellX-Core, ShellX-Superman |
| `.repair_backups/` | Recovery stones | — | ShellX-AutoStone |

---

## RECOVERY STONES

| Stone | Timestamp | Title | Status |
|-------|-----------|-------|--------|
| [20260401T064800](/.repair_backups/20260401T064800_SHELLX_INIT.md) | 2026-04-01T06:48:00Z | ShellX Init — Repo Bootstrap | ✅ Done |

---

## SESSIONS

| Session | Date | Key Actions | Outcome |
|---------|------|-------------|---------|
| Session 1 | 2026-04-01 | Created SHELLX.md, LinkX.md, REPORT.md, recovery stone | ✅ Complete |

---

## PENDING ACTIONS

| # | Task | Owner | Status |
|---|------|-------|--------|
| 1 | Add `particle_sphere.glb` to `dist/resources/models/` | Dev | ⬜ Needs action |
| 2 | Native dependency scan for QtQuick3D plugin | Dev | ⬜ Needs action |
| 3 | Re-run packaged diagnostics; confirm mesh loads | Dev | ⬜ Needs action |

---

*Updated by ShellX-Memory on 2026-04-01T06:48:00Z*
