# ShellX — Quickstart Guide

Get up and running with ShellX in under 5 minutes.

---

## Prerequisites

- Node.js 16+ (or later)
- npm or yarn
- A terminal
- A Git project (optional, but recommended)

---

## Installation

### Option 1 — Global Install (Recommended)

```bash
npm install -g shellx
shellx --version
```

### Option 2 — Local Development

```bash
git clone https://github.com/jimgranitex-eng/Shellx.git
cd Shellx
npm install
node bin/shellx.js --version
```

### Option 3 — Local npm Link

```bash
git clone https://github.com/jimgranitex-eng/Shellx.git
cd Shellx
npm install
npm link
shellx --version
```

---

## First Steps (5 minutes)

### 1. Initialize ShellX in Your Project

```bash
cd your-project
shellx init
```

This creates:
- `.linkx/` — LinkX memory system
- `.reports/` — Generated reports
- `.stones/` — Snapshot checkpoints

**Recommended:** Add these to `.gitignore`:

```bash
echo ".linkx" >> .gitignore
echo ".reports" >> .gitignore
echo ".stones" >> .gitignore
git add .gitignore
git commit -m "Add ShellX directories to gitignore"
```

### 2. Initialize LinkX

```bash
shellx linkx init
```

This activates LinkX memory for your project.

### 3. Verify Installation

```bash
shellx verify
```

You should see:
```
✅ .linkx directory
✅ .reports directory
✅ .stones directory
✅ LinkX core.json

4/4 checks passed
🎯 All checks passed! ShellX is ready to use.
```

---

## Core Commands

### Cognitive Mode (Recommended)

Describe what you want in natural language:

```bash
shellx --xx "analyze the project structure"
```

Example with real intent:

```bash
shellx --xx "Fix the rendering pipeline and optimize shader performance"
```

Output:
```
🧠 ShellX Cognitive Mode
Intent: "Fix the rendering pipeline and optimize shader performance"

🔍 Analyzing intent...
📊 Scanning project...
⚙️  Running pipeline...
✅ Complete

Summary:
1. What you wanted: Fix the rendering pipeline and optimize shader performance
2. What ShellX did: Deep audit → Scan → Analyze
3. What changed: Project analyzed, LinkX updated
```

---

### LinkX Commands

#### View LinkX State

```bash
shellx linkx show
```

Output:
```
📖 LinkX Memory State:

Core Information:
  Version: 1.0.0
  Created: 2026-07-22T20:00:00Z
  Goal: Define your project goal

Project State:
  Status: active
  Files Tracked: 42
  Last Scanned: 2026-07-22T20:05:30Z

Stones:
  Count: 0
```

#### Scan Project

```bash
shellx linkx scan
```

Scans your project and updates LinkX memory.

#### View Timeline

```bash
shellx linkx timeline
```

Shows intent history and stones created.

---

### Generate Reports

#### Quick Summary (Default)

```bash
shellx report
```

#### Detailed Report

```bash
shellx report --format detailed
```

#### Full Comprehensive Report

```bash
shellx report --format full
```

Reports are saved to `.reports/`.

---

## Workflow Example

Here's a typical ShellX workflow:

```bash
# 1. Initialize
shellx init
shellx linkx init

# 2. Describe what you're working on
shellx --xx "Refactor the authentication module for better performance"

# 3. Check the results
shellx linkx show
shellx report

# 4. View history
shellx linkx timeline

# 5. Make code changes based on ShellX insights
# (your work here)

# 6. Run cognitive mode again
shellx --xx "Verify the authentication refactor is complete"
```

---

## Output Structure

Every ShellX run generates:

| Output | Location | What's Inside |
|--------|----------|---------------|
| **Reports** | `.reports/report-*.txt` | Human-readable analysis |
| **LinkX Memory** | `.linkx/core.json` | Project history & goals |
| **Stones** | `.stones/` | Snapshot checkpoints |

### Viewing Raw Data

```bash
# View LinkX memory
cat .linkx/core.json | json_pp

# View latest report
cat .reports/latest.txt

# List all stones
ls -la .stones/
```

---

## Tips & Best Practices

### 1. Define Your Project Goal

Edit `.linkx/core.json` and set your project goal:

```json
{
  "projectGoal": "Build a high-performance rendering engine",
  "projectConstraints": [
    "No breaking changes to public API",
    "Must maintain backward compatibility"
  ]
}
```

### 2. Use Cognitive Mode for Complex Tasks

```bash
# Good
shellx --xx "Stabilize the rendering pipeline"

# Also good
shellx --xx "Find and fix performance bottlenecks in the shader system"
```

### 3. Check LinkX Timeline Regularly

```bash
shellx linkx timeline
```

This shows your project's decision history.

### 4. Keep .gitignore Updated

```bash
# Add ShellX artifacts
.linkx/
.reports/
.stones/
```

### 5. Use Stones for Milestones

Stones are automatic snapshots. You can restore them later.

---

## Troubleshooting

### `shellx: command not found`

**Solution:** Install globally:

```bash
npm install -g shellx
```

### `LinkX not initialized`

**Solution:** Run initialization:

```bash
shellx init
shellx linkx init
```

### `Permission denied`

**Solution:** Ensure the CLI is executable:

```bash
chmod +x ./bin/shellx.js
```

### Verification failed

**Solution:** Re-initialize:

```bash
rm -rf .linkx .reports .stones
shellx init
shellx verify
```

---

## Next Steps

- 📖 [Command Reference](Commands.md) — all available commands
- 🎯 [LinkX Architecture](LinkX-Architecture.md) — how memory works
- 💼 [Pro Features](Pro-Features.md) — advanced capabilities
- 🤝 [Contributing](../CONTRIBUTING.md) — help improve ShellX

---

**Questions?** Open an issue on [GitHub](https://github.com/jimgranitex-eng/Shellx/issues).
