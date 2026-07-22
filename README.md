<p align="center">
  <img src="logo-shellx-v5.jpg" width="220" alt="ShellX V5 Logo">
</p>
<p align="center"><em>Goal‑Driven Cognitive Developer Engine</em></p>
<p align="center">
  <img src="shellx-banner.png" width="100%" alt="ShellX Banner">
</p>

# ⚡ ShellX — Cognitive Developer Engine

**ShellX is a goal-driven cognitive developer engine** that understands what you are building, why you are building it, and how far along you are. Using a persistent memory system called **LinkX**, ShellX transforms developer workflows into structured, traceable output.

## Install

```bash
npm install -g shellx-dev-cli
```

## Quick Start

```bash
shellx init
shellx linkx init
shellx --xx "stabilize the rendering pipeline"
shellx linkx show
```

## What ShellX does

ShellX turns complex developer workflows into structured output:

- Summary Report
- Detailed Report
- Full Report
- LinkX memory entry
- Stone snapshot

All from a single command.

---

# Core Concepts

## Triple-Context Engine

ShellX evaluates every request using three layers of context:

1. **Immediate Intent** — what you asked for
2. **Long-Term Goal** — stored in LinkX
3. **Actual Project State** — scanned from the codebase

ShellX reconciles all three before taking action, ensuring correctness, continuity, and safety.

## LinkX — Core Memory System

LinkX is the primary memory and goal engine of ShellX.
ShellX boots on top of LinkX and relies on it for context-aware execution.

LinkX stores:

- Project goal
- Project constraints
- Project preferences
- Project state
- Intent history
- Context model
- Stones (restore points)

If LinkX is unavailable, ShellX enters safe mode and refuses destructive operations.

## Builder Mode

ShellX performs safe, incremental modifications:

- Adds
- Extends
- Fixes
- Improves

ShellX does not overwrite, replace, destroy, misplace, or duplicate unless explicitly instructed.

## Superman Mode

Superman orchestrates workers and performs deep diagnostics:

- Loads LinkX
- Confirms the project goal
- Scans the codebase
- Reconciles context
- Runs workers safely
- Updates LinkX
- Creates a Stone

Superman is powerful, precise, and goal-aware.

---

# Getting Started

## Installation

### Global install

```bash
npm install -g shellx-dev-cli
```

### Local development

```bash
git clone https://github.com/jimgranitex-eng/Shellx.git
cd Shellx
npm install
node bin/shellx.js --version
```

## Commands

### Initialize ShellX

```bash
shellx init
```

Creates `.linkx/`, `.reports/`, and `.stones/`.

### Initialize LinkX

```bash
shellx linkx init
```

Initializes the persistent memory system.

### LinkX commands

```bash
shellx linkx scan
shellx linkx show
shellx linkx timeline
```

### Verify installation

```bash
shellx verify
```

### Generate reports

```bash
shellx report
shellx report --format detailed
shellx report --format full
```

### Cognitive mode

```bash
shellx --xx "your intent here"
```

Example:

```bash
shellx --xx "Fix the rendering pipeline and optimize the shader system"
```

---

# Project Structure

```
.
├── bin/
│   └── shellx.js
├── src/
│   ├── index.js
│   └── commands/
│       ├── init.js
│       ├── linkx.js
│       ├── verify.js
│       └── report.js
├── docs/
├── shellx-website/
├── package.json
└── README.md
```

---

# License

- Open source: [GNU GPL v3](LICENSE)
- Commercial: [LICENSE-PRO.md](LICENSE-PRO.md)

---

# Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

---

# In One Sentence

**ShellX is a cognitive developer engine that preserves long-term project goals, analyzes your codebase, and performs safe, incremental operations using a persistent memory system called LinkX.**
