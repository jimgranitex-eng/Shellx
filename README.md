<p align="center">
  <img src="logo-shellx-v5.jpg" width="220" alt="ShellX V5 Logo">
</p>
<p align="center"><em>Goal‑Driven Cognitive Developer Engine</em></p>
<p align="center">
  <img src="shellx-banner.png" width="100%" alt="ShellX Banner">
</p>

# ⚡ ShellX — Cognitive Developer Engine

**ShellX is a goal-driven cognitive developer engine** that understands what you are building, why you are building it, and how far along you are. Using a persistent memory system called **LinkX**, ShellX transforms complex developer workflows into structured intelligence.

![npm version](https://img.shields.io/npm/v/shellx?label=version)
![License](https://img.shields.io/badge/license-GPL--3.0-green)
![Node.js](https://img.shields.io/badge/node-%3E%3D16.0.0-brightgreen)
![Status](https://img.shields.io/badge/status-production%20ready-blue)

## Quick Start

```bash
# Install globally
npm install -g shellx

# Initialize in your project
shellx init
shellx linkx init

# Run cognitive mode
shellx --xx "stabilize the rendering pipeline"

# Check the results
shellx linkx show
```

---

# 🎯 What ShellX Does

ShellX transforms complex developer workflows into **structured intelligence**, producing:

- **Summary Report** — 1-2-3 clean summary
- **Detailed Report** — full technical analysis
- **LinkX Memory Entry** — persistent project history
- **Stone Snapshot** — recoverable checkpoint
- **Verification Report** — project integrity check

All from a single command.

---

# 🧠 Core Concepts

## Triple‑Context Engine

ShellX evaluates every request using three layers of context:

1. **Immediate Intent** — what you asked for  
2. **Long‑Term Goal** — stored in LinkX  
3. **Actual Project State** — scanned from the codebase  

ShellX reconciles all three before taking action, ensuring correctness, continuity, and safety.

---

## LinkX — Core Memory System

LinkX is the **primary memory and goal engine** of ShellX. ShellX boots on top of LinkX and relies on it for context‑aware execution.

LinkX stores:

- Project goal  
- Project constraints  
- Project preferences  
- Project state  
- Intent history  
- Context model  
- Stones (restore points)  

If LinkX is unavailable, ShellX enters **safe mode** and refuses destructive operations.

---

## Builder Mode (Non‑Destructive Execution)

ShellX performs safe, incremental modifications:

**Does:**
- Adds new features
- Extends existing systems
- Fixes broken logic
- Improves performance

**Never:**
- Overwrites existing code
- Deletes files without explicit instruction
- Destroys project state
- Misplaces or duplicates

Builder Mode ensures ShellX behaves like a **craftsman**, not a rewriter.

---

## Superman Mode — Deep Multi‑Agent Diagnostics

Superman is the orchestrator that coordinates all workers and performs comprehensive analysis:

- Loads LinkX  
- Confirms the project goal  
- Scans the codebase  
- Reconciles context  
- Runs workers safely  
- Updates LinkX  
- Creates a Stone snapshot  

Superman is powerful, precise, and fully goal‑aware. It operates under the Triple‑Context Engine and refuses to proceed if contexts don't align.

---

# 🚀 Installation & Usage

## Installation

### Global (Recommended)
```bash
npm install -g shellx
shellx --version
```

### Local Development
```bash
git clone https://github.com/jimgranitex-eng/Shellx.git
cd Shellx
npm install
node bin/shellx.js --version
```

---

## Commands

### Initialize ShellX
```bash
shellx init
```
Creates `.linkx/`, `.reports/`, and `.stones/` directories in your project.

### Initialize LinkX
```bash
shellx linkx init
```
Initializes the persistent memory system.

### LinkX Commands

```bash
# Scan your project
shellx linkx scan

# View LinkX state
shellx linkx show

# View project timeline
shellx linkx timeline
```

### Verification
```bash
shellx verify
```
Verifies ShellX installation and configuration.

### Generate Reports
```bash
# Summary report (default)
shellx report

# Detailed report
shellx report --format detailed

# Full comprehensive report
shellx report --format full
```

### Cognitive Mode (Recommended)
```bash
shellx --xx "your intent here"
```
Natural language intent extraction. Describe what you need, and ShellX runs the full pipeline, delivering a clean 1-2-3 summary.

Example:
```bash
shellx --xx "Fix the rendering pipeline and optimize the shader system"
```

Output:
```
1. What you wanted: Fix the rendering pipeline and optimize the shader system
2. What ShellX did: Deep audit → Scan → Analyze → Memory update
3. What changed: Project analyzed, LinkX updated with findings
```

---

# 📁 Project Structure

```
.
├── bin/
│   └── shellx.js              CLI entry point
├── src/
│   ├── index.js               CLI router
│   └── commands/
│       ├── init.js            Project initialization
│       ├── linkx.js           LinkX memory commands
│       ├── verify.js          Verification pipeline
│       └── report.js          Report generation
├── docs/                      Documentation suite
├── shellx-website/            GitHub Pages website
├── package.json               npm package definition
└── README.md                  This file
```

---

# ⚠️ Safety Notice: Superman Mode

Superman is the most capable operator in ShellX and performs deep diagnostics, multi-agent orchestration, and large-scale project analysis. Superman **does work**, and it works extremely well — but with safeguards.

**Superman will never:**
- Act on its own  
- Overwrite files randomly  
- Delete code without explicit instruction  
- Ignore the project goal  
- Bypass LinkX  
- Skip safety checks  

Superman only performs modifications when ShellX gives **precise, validated, goal-aligned commands**. It uses the Triple‑Context Engine and requires all three contexts to align before proceeding.

### Safe Mode Behavior

If LinkX is missing or corrupted:
- No destructive actions are taken  
- No architecture rewrites occur  
- No autofixes are applied  
- Superman produces a **diagnostic-only report** and LinkX integrity notice

---

# ✅ What ShellX Excels At

### Code Diagnostics
- Broken logic detection
- Missing imports
- Type mismatches
- Dependency issues
- Architectural inconsistencies
- Structural drift

### Goal‑Aware Development
- Tracks long-term intent
- Preserves project direction
- Maintains continuity and context

### Safe Incremental Updates
- Adds features safely
- Extends systems intelligently
- Fixes components without side effects
- Refactors with verification

### Deep Multi‑Agent Analysis
- Full project audits
- Architecture mapping
- Hidden issue detection
- Stone creation and management
- LinkX memory updates

### Human‑Readable Intelligence
- Summary reports (1-2-3 format)
- Detailed technical reports
- Full comprehensive analysis
- Searchable history via LinkX
- Persistent decision timeline

---

# 🧩 What ShellX Is NOT

- **Not a code generator** — ShellX analyzes and improves existing code
- **Not a code replacement engine** — It preserves your intent and direction
- **Not a black box** — All actions are logged, traceable, and reversible via Stones
- **Not dangerous** — It respects LinkX goals and requires context alignment

ShellX is a **cognitive assistant** that helps you build and maintain complex systems safely and intelligently.

---

# 📦 Output Artifacts

Every ShellX operation generates:

| Artifact | Location | Purpose |
|----------|----------|----------|
| Reports | `.reports/` | Human-readable summaries and analysis |
| Stones | `.stones/` | Immutable snapshots for recovery |
| LinkX Memory | `.linkx/core.json` | Persistent project timeline |

---

# 🔗 LinkX Integration

LinkX is ShellX's **persistent memory layer**. It tracks:

- **Project Goals** — what you're building
- **Constraints** — what you can't change
- **Preferences** — how you like to work
- **Intent History** — every decision made
- **Stones** — recovery points at key milestones

Access LinkX data:

```bash
shellx linkx show              # View all memory
shellx linkx timeline          # View history
cat .linkx/core.json           # Raw data
```

---

# 📄 License

ShellX is dual-licensed:

- **Open Source**: Licensed under [GNU GPL v3](LICENSE)
- **Commercial**: Licensed under [Commercial License](LICENSE-PRO.md)

For commercial licensing, see [ShellX Pro](docs/Pro-Pricing.md).

---

# 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Quick Start for Contributors

```bash
git clone https://github.com/jimgranitex-eng/Shellx.git
cd Shellx
npm install

# Test the CLI
node bin/shellx.js --version
node bin/shellx.js init

# Make changes, then test
npm test

# Submit a PR
```

---

# 🎯 Roadmap

## V3.0 (Current)
✅ Cognitive mode with natural language processing
✅ LinkX memory system
✅ Stone snapshots
✅ Multi-command CLI
✅ Report generation

## V4.0 (Coming)
🚀 Plugin system
🚀 Worker registry
🚀 Cloud LinkX timeline
🚀 Stone diff viewer
🚀 VS Code extension
🚀 ShellX Pro modules

---

# 📚 Documentation

- [Quick Start Guide](docs/Quickstart.md)
- [Command Reference](docs/Commands.md)
- [LinkX Architecture](docs/LinkX-Architecture.md)
- [Pro Features](docs/Pro-Features.md)
- [Pro Pricing](docs/Pro-Pricing.md)
- [Contributing Guide](CONTRIBUTING.md)

---

# 🎯 In One Sentence

**ShellX is a cognitive developer engine that preserves your long‑term project goals, analyzes your codebase intelligently, and performs safe, incremental operations using a persistent memory system called LinkX.**

---

**Created by [James](https://github.com/jimgranitex-eng) • Part of the KickerOS ecosystem • [GitHub](https://github.com/jimgranitex-eng/Shellx)**
