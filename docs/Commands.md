# ShellX — Full Usage Guide (v3.2.0)

Complete command reference for the ShellX Cognitive Developer Engine.

---

## Installation

```bash
npm install -g shellx-dev-cli
```

Verify installation:

```bash
shellx --version
shellx --help
```

---

## Usage Overview

ShellX provides: project memory, diagnostics, IDE integration, licensing,
multi-agent reasoning, snapshot management, and multi-project workflows.

---

## 1. Core Commands

### Run with natural-language intent

```bash
shellx "stabilize the rendering pipeline"
```

### Show help

```bash
shellx --help
```

### Show version

```bash
shellx --version
```

### Initialize project

```bash
shellx init
```

### Verify system

```bash
shellx verify
```

### Run diagnostic doctor

```bash
shellx doctor
```

### Generate full report

```bash
shellx report
```

---

## 2. LinkX Memory & Analysis

### Initialize memory

```bash
shellx linkx init
```

### Scan project

```bash
shellx linkx scan
```

### Show memory

```bash
shellx linkx show
```

### Timeline view

```bash
shellx linkx timeline
```

### Search memory

```bash
shellx linkx search "render"
```

### Compare memory states

```bash
shellx linkx diff
```

### Export memory

```bash
shellx linkx export
```

### Import memory

```bash
shellx linkx import
```

### Clear memory

```bash
shellx linkx purge
```

### Rebuild memory

```bash
shellx linkx rebuild
```

---

## 3. Stone System (Project Snapshots)

### List stones

```bash
shellx stone list
```

### Show stone details

```bash
shellx stone show <id>
```

### Compare stones

```bash
shellx stone diff <id>
```

### Restore snapshot

```bash
shellx stone restore <id>
```

### Create snapshot

```bash
shellx stone create
```

---

## 4. Licensing & Activation

### Show license state

```bash
shellx license status
```

### Activate license

```bash
shellx activate SHELLX-PRO-XXXX-XXXX-XXXX
```

### Remove license

```bash
shellx deactivate
```

### Show trial state

```bash
shellx trial status
```

### Reset trial

```bash
shellx trial reset
```

### Validate license

```bash
shellx license verify
```

---

## 5. IDE Integration

### Detect installed IDEs

```bash
shellx ide detect
```

### List supported IDEs

```bash
shellx ide list
```

### Open project in IDE

```bash
shellx ide open vscode
```

### Install VS Code extensions

```bash
shellx ide vscode install
```

### Show VS Code tasks

```bash
shellx ide vscode tasks
```

### Show IDE config

```bash
shellx ide config
```

### Fix IDE integration

```bash
shellx ide repair
```

---

## 6. Cognitive Modes

### XX Intent Processor (V3)

```bash
shellx --xx "optimize build pipeline"
```

### Superman multi-agent diagnostic (V2)

```bash
shellx-superman "full diagnostic"
```

### Deep cognitive audit

```bash
shellx deep-audit
```

### Architecture reasoning mode

```bash
shellx architect
```

---

## 7. Developer Tools

### Debug ShellX internals

```bash
shellx debug
```

### Collect project metadata

```bash
shellx collect
```

### Inspect project structure

```bash
shellx look
```

### Show internal memory

```bash
shellx memory
```

### Safe auto-fix mode

```bash
shellx autofix --safe
```

---

## 8. Multi-Project Commands

### Scan multiple projects

```bash
shellx multi scan
```

### Link multiple projects

```bash
shellx multi link
```

### Multi-project intent mode

```bash
shellx multi "audit all modules"
```

---

## Command Status Legend

| Status | Meaning |
|--------|---------|
| ✅ Implemented | Available now in v3.2.0 |
| 🚧 Planned | Coming in a future release |

### Implementation Status

| # | Category | Implemented | Planned |
|---|----------|-------------|---------|
| 1 | Core | `--help`, `--version`, `doctor`, `report`, `init`, `verify`, `shellx "<intent>"` | — |
| 2 | LinkX Memory | `init`, `scan`, `show`, `timeline`, `search`, `export` | `diff`, `import`, `purge`, `rebuild` |
| 3 | Stones | `list`, `show`, `diff`, `restore` | `create` |
| 4 | Licensing | `license status`, `activate`, `deactivate` | `trial status`, `trial reset`, `license verify` |
| 5 | IDE | `detect`, `list`, `open`, `vscode install` | `vscode tasks`, `config`, `repair` |
| 6 | Cognitive | `--xx`, `shellx-superman` | `deep-audit`, `architect` |
| 7 | Tools | `doctor`, `report`, `preflight` | `debug`, `collect`, `look`, `memory`, `autofix --safe` |
| 8 | Multi-Project | — | `multi scan`, `multi link`, `multi "<intent>"` |

---

*For the Quickstart guide, see [Quickstart.md](Quickstart.md).*  
*For Pro features, see [Pro-Features.md](Pro-Features.md).*
