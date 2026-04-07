# ⚡ ShellX — Cognitive Developer Engine

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-3.0.0-brightgreen.svg)](https://github.com/jimgranitex-eng/Shellx/releases)
[![GitHub Stars](https://img.shields.io/github/stars/jimgranitex-eng/Shellx?style=social)](https://github.com/jimgranitex-eng/Shellx/stargazers)

> **Human-readable intelligence for code, diagnostics, and automation.**  
> One command. Full pipeline. Clean summary.

ShellX is a cognitive developer engine that transforms complex developer workflows into simple, actionable intelligence. You type what you want. ShellX figures out how to do it, runs the full pipeline, and tells you exactly what happened — in plain language.

---

## 📋 Table of Contents

- [Why ShellX?](#-why-shellx)
- [Quick Start](#-quick-start)
- [The Three Modes](#-the-three-modes)
- [What Every Run Produces](#-what-every-run-produces)
- [ShellX vs ShellX Pro](#-shellx-vs-shellx-pro)
- [ShellX Pro Pricing](#-shellx-pro-pricing)
- [Advanced Workers (Pro)](#-advanced-workers-pro)
- [Contributing](#-contributing)
- [Documentation](#-documentation)
- [License](#-license)

---

## 💡 Why ShellX?

Modern development is noisy:

- Codebases grow faster than documentation can keep up
- Debugging takes hours when it should take minutes
- Architecture drifts without anyone noticing
- Refactoring is risky without proper snapshots
- Teams lose context as projects evolve

**ShellX fixes all of this with one command.**

```
1. What you wanted
2. What ShellX did
3. What changed
```

Zero confusion. Zero walls of log output. Just clarity.

---

## 🚀 Quick Start

### Prerequisites

- Node.js 18+
- Git
- A terminal

### Installation

```bash
# Clone the repository
git clone https://github.com/jimgranitex-eng/Shellx.git
cd Shellx
npm install
```

> Global install via `npm install -g shellx` is coming soon.

### Activate ShellX Pro (if you have a license)

```bash
shellx activate SHELLX-PRO-XXXX-XXXX-XXXX
```

See [docs/Quickstart.md](docs/Quickstart.md) for the full setup guide.

---

## 🧩 The Three Modes

ShellX has evolved through three versions. Pick the one that fits your workflow.

---

### ⭐ Mode 1 — Simple Report (V1)

For quick tasks and straightforward fixes.

```bash
shellx "Fix the shader logic and update the color pipeline."
```

**What happens:**
- Reads your message
- Executes the task
- Generates a timestamped report
- Saves it to your project

---

### ⭐ Mode 2 — Multi-Agent Diagnostic / Superman (V2)

For deep audits, architecture analysis, and complex stabilization.

```bash
shellx-superman "audit everything and stabilize the engine"
```

**What happens:**
- Deep audit
- Architecture mapping
- Memory analysis
- Safe-mode autofix
- Verification pipeline
- Stone snapshot creation
- LinkX timeline update

---

### ⭐ Mode 3 — Cognitive Summary (V3 · Recommended)

The most powerful and readable mode. ShellX reads your intent, runs the full pipeline, and compresses everything into a clean 1-2-3 summary.

```bash
shellx --xx "Fix the rendering pipeline and update the shader logic."
```

**What you see:**

```
✅ 1. What you wanted:  Fix rendering pipeline & update shaders
✅ 2. What ShellX did:  Deep audit → Debug → Autofix → Verify
✅ 3. What changed:     12 files modified, 3 stones created
```

**What ShellX does behind the scenes:**
1. Reads your entire message
2. Extracts the real intent
3. Runs the full ShellX pipeline
4. Collects all worker outputs
5. Compresses everything into a simple summary
6. Saves the full report
7. Updates LinkX
8. Creates a Stone

---

## 📁 What Every Run Produces

No matter which mode you use, ShellX always generates structured output:

| Output | Location |
|--------|----------|
| Full report | `reports/YYYY-MM-DD-HH-MM-SS.md` |
| Stone snapshot | `stones/stone-YYYY-MM-DD.json` |
| LinkX timeline update | `linkx/timeline.json` |

---

## 🆚 ShellX vs ShellX Pro

| Feature | ShellX (Free) | ShellX Pro |
|---------|:---:|:---:|
| V1 simple report | ✅ | ✅ |
| V2 Superman diagnostic | ✅ | ✅ |
| V3 cognitive mode (`--xx`) | ✅ | ✅ |
| Stone snapshots | ✅ | ✅ |
| LinkX basic timeline | ✅ | ✅ |
| **Superman Pro** (enhanced, multi-threaded) | ❌ | ✅ |
| **Advanced workers** (`architect-pro`, `memory-pro`, `deep-audit-pro`, `autofix-pro`, `verify-pro`) | ❌ | ✅ |
| **Deep architecture mapping** | ❌ | ✅ |
| **Enterprise LinkX timeline** (multi-project, diff visualization) | ❌ | ✅ |
| **Stone diff viewer** (visual compare & time-travel) | ❌ | ✅ |
| **VS Code interactive panels** (live diagnostics, dashboards) | ❌ | ✅ |
| **V4 early access** | ❌ | ✅ |
| Priority support | ❌ | ✅ |

See [docs/Pro-Features.md](docs/Pro-Features.md) for the full feature breakdown.

---

## 💳 ShellX Pro Pricing

| Plan | Price | Seats | Best For |
|------|-------|-------|----------|
| **Starter** | $10/month | 1 | Solo developers |
| **Professional** | $25/month | Up to 5 | Small teams & power users |
| **Enterprise** | $99/month | Unlimited | Organizations & production |

**Enterprise includes:** custom worker development, dedicated support, SLA-backed response times, deployment consulting, and private feature requests.

> 14-day no-questions-asked refund. Annual billing discounts available.

### How to Buy

- **[➡ GitHub Sponsors](https://github.com/sponsors/jimgranitex-eng)** — easiest method, automatic repo access
- **Stripe Checkout** — contact for a payment link
- **Direct commercial licensing** — see [docs/Pro-Enterprise.md](docs/Pro-Enterprise.md)

See [docs/Pro-Pricing.md](docs/Pro-Pricing.md) for the full plan comparison and [LICENSE-PRO.md](LICENSE-PRO.md) for licensing terms.

---

## 🛠 Advanced Workers (Pro)

| Worker | Purpose |
|--------|---------|
| `architect-pro` | Deep architecture mapping across your entire codebase |
| `memory-pro` | Memory graph, reference analysis, and data flow tracking |
| `deep-audit-pro` | Comprehensive codebase audit beyond standard V3 reports |
| `autofix-pro` | Aggressive safe-mode autofixer with rollback support |
| `verify-pro` | Multi-threaded parallel verification pipeline |

**Superman Pro** — the most advanced diagnostic mode:

```bash
shellx-superman-pro "full diagnostic and stabilize everything"
```

Runs: deep audit + architecture mapping + memory graph + autofix + verification. Everything in one command.

---

## 🤝 Contributing

We welcome contributions to ShellX core — bug fixes, new workers, documentation, and tooling.

```bash
# Fork the repo, then:
git checkout -b feature/my-change
# Make your changes and open a pull request against main
```

Read [CONTRIBUTING.md](CONTRIBUTING.md) for the full guide, style guidelines, and PR checklist.

For security issues, see [SECURITY.md](SECURITY.md) — please do not report vulnerabilities through public issues.

---

## 📚 Documentation

| Resource | Link |
|----------|------|
| Quickstart Guide | [docs/Quickstart.md](docs/Quickstart.md) |
| Pro Features | [docs/Pro-Features.md](docs/Pro-Features.md) |
| Pro Pricing | [docs/Pro-Pricing.md](docs/Pro-Pricing.md) |
| Enterprise | [docs/Pro-Enterprise.md](docs/Pro-Enterprise.md) |
| FAQ | [docs/Pro-FAQ.md](docs/Pro-FAQ.md) |
| Changelog | [CHANGELOG.md](CHANGELOG.md) |
| Website | [shellx-website/](shellx-website/) |

---

## 🔍 Topics

`shellx` · `developer-tools` · `ai-engine` · `cognitive-engine` · `multi-agent` · `diagnostics` · `automation` · `workflow`

---

## 📄 License

ShellX (open source) is licensed under the [GNU GPL v3](LICENSE).  
ShellX Pro is a commercially licensed product — see [LICENSE-PRO.md](LICENSE-PRO.md).  
Enterprise inquiries: open an issue or see [docs/Pro-Enterprise.md](docs/Pro-Enterprise.md).
