<p align="center">
  <img src="logo-shellx-v5.jpg" width="220" alt="ShellX V5 Logo">
</p>
<p align="center"><em>Goal‑Driven Cognitive Developer Engine</em></p>

<p align="center">
  <a href="https://www.npmjs.com/package/shellx-dev-cli"><img src="https://img.shields.io/npm/v/shellx-dev-cli" alt="npm"></a>
  <a href="https://www.npmjs.com/package/shellx-dev-cli"><img src="https://img.shields.io/npm/dt/shellx-dev-cli" alt="npm downloads"></a>
  <a href="https://github.com/jimgranitex-eng/Shellx/actions"><img src="https://img.shields.io/github/actions/workflow/status/jimgranitex-eng/Shellx/ci.yml?branch=main" alt="CI"></a>
  <a href="https://github.com/jimgranitex-eng/Shellx/blob/main/LICENSE"><img src="https://img.shields.io/github/license/jimgranitex-eng/Shellx" alt="License"></a>
</p>

# ⚡ ShellX — Cognitive Developer Engine

ShellX is a goal‑driven cognitive developer engine that understands what you are building, why you are building it, and how far along you are. Using a persistent memory system called **LinkX**, ShellX performs safe, incremental, non‑destructive operations that align with your long‑term project goals.

## Quick Start

```bash
npm install -g shellx-dev-cli
shellx --version
shellx linkx init
shellx report
```

## Quick Examples

```bash
# Cognitive mode — describe what you want
shellx --xx "stabilize the rendering pipeline"

# Full multi-agent diagnostic
shellx-superman "audit everything and fix issues"

# Persistent project memory
shellx linkx init && shellx linkx scan

# IDE: detect + open in VS Code
shellx ide detect && shellx ide open vscode

# License status
shellx license status

# Recovery snapshot
shellx stone list
```

## Usage Overview

ShellX is a cognitive developer engine providing:

- **Project memory** — LinkX persistent timeline
- **Diagnostics** — Multi-agent audit & autofix
- **IDE integration** — Detect, open, and manage 8 IDEs
- **Licensing** — ShellX Pro activation & trial
- **Cognitive reasoning** — Natural-language intent processing (V3)
- **Snapshot management** — Stone recovery system
- **Multi-project workflows** — Cross-repo context switching

---

## 📘 Full 40-Command Reference

Commands are grouped into **8 categories**.  
For detailed usage with examples, see [docs/Commands.md](docs/Commands.md).

---

### 1️⃣ Core Commands (7)

| Command | Description |
|---------|-------------|
| `shellx "<intent>"` | Natural-language intent (auto-detected) |
| `shellx --help` | Show full help |
| `shellx --version` | Show version |
| `shellx init` | Initialize project |
| `shellx verify` | System/environment check |
| `shellx doctor` | Run diagnostic doctor |
| `shellx report` | Generate full report |

### 2️⃣ LinkX Memory & Analysis (10)

| Command | Description |
|---------|-------------|
| `shellx linkx init` | Create goal file |
| `shellx linkx scan` | Scan project |
| `shellx linkx show` | Show memory |
| `shellx linkx timeline` | Timeline view |
| `shellx linkx search` | Search memory |
| `shellx linkx diff` | Compare memory states |
| `shellx linkx export` | Export memory |
| `shellx linkx import` | Import memory |
| `shellx linkx purge` | Clear memory |
| `shellx linkx rebuild` | Rebuild memory |

### 3️⃣ Stone System (Project Snapshots) (5)

| Command | Description |
|---------|-------------|
| `shellx stone list` | List stones |
| `shellx stone show` | Show stone details |
| `shellx stone diff` | Compare stones |
| `shellx stone restore` | Restore snapshot |
| `shellx stone create` | Create snapshot |

### 4️⃣ Licensing & Activation (6)

| Command | Description |
|---------|-------------|
| `shellx license status` | Show license state |
| `shellx activate <key>` | Activate license |
| `shellx deactivate` | Remove license |
| `shellx trial status` | Show trial state |
| `shellx trial reset` | Reset trial |
| `shellx license verify` | Validate license |

### 5️⃣ IDE Integration (7)

| Command | Description |
|---------|-------------|
| `shellx ide detect` | Detect installed IDEs |
| `shellx ide list` | List supported IDEs |
| `shellx ide open <ide>` | Open project in IDE |
| `shellx ide vscode install` | Install VS Code extensions |
| `shellx ide vscode tasks` | Show VS Code tasks |
| `shellx ide config` | Show IDE config |
| `shellx ide repair` | Fix IDE integration |

### 6️⃣ Cognitive Modes (4)

| Command | Description |
|---------|-------------|
| `shellx --xx "<intent>"` | XX Intent Processor (V3) |
| `shellx-superman "<intent>"` | Multi-agent orchestration (V2) |
| `shellx deep-audit` | Deep cognitive audit |
| `shellx architect` | Architecture reasoning mode |

### 7️⃣ Developer Tools (5)

| Command | Description |
|---------|-------------|
| `shellx debug` | Debug ShellX internals |
| `shellx collect` | Collect project metadata |
| `shellx look` | Inspect project structure |
| `shellx memory` | Show internal memory |
| `shellx autofix --safe` | Safe auto-fix mode |

### 8️⃣ Multi-Project Commands (3)

| Command | Description |
|---------|-------------|
| `shellx multi scan` | Scan multiple projects |
| `shellx multi link` | Link multiple projects |
| `shellx multi "<intent>"` | Multi-project intent mode |

---

> **Total: 40 commands** — Implemented commands are available now; planned commands are marked as roadmap items in [docs/Commands.md](docs/Commands.md).

---

## Supported IDEs

VS Code, PyCharm, IntelliJ IDEA, WebStorm, Android Studio, Xcode, Sublime Text, Vim/Neovim

---

## License

ShellX uses a **dual-licensing model**:

```
                    ┌───────────────────────┐
                    │     ShellX Engine      │
                    │  (all source code)     │
                    └───────┬───────┬───────┘
                            │       │
                ┌───────────┘       └───────────┐
                ▼                               ▼
    ┌───────────────────────┐     ┌───────────────────────────┐
    │   Open Source Edition │     │   ShellX Pro              │
    │   Free for everyone   │     │   Commercial license      │
    │   GNU GPL v3          │     │   Extra features + support│
    │   Full CLI + LinkX    │     │   Superman Pro, deep audit,│
    │   + Stones + IDE      │     │   enterprise tools,       │
    │   + XX Mode           │     │   priority support        │
    └───────────────────────┘     └───────────────────────────┘
```

- **ShellX (open source)** — [GNU GPL v3](LICENSE) — Use freely, modify, distribute under GPL terms.
- **ShellX Pro** — [Commercial license](LICENSE-PRO.md) — Paid license with advanced features, enterprise tooling, and priority support.

[Sponsor ShellX Pro on GitHub Sponsors](https://github.com/sponsors/jimgranitex-eng) — Get a Pro license and support ongoing development.
