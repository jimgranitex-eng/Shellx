# ShellX — Commands Tutorial

This tutorial walks you through ShellX from first run to advanced usage.

---

# 🚀 Step 1: First Run

After installing ShellX, verify your environment:

```
shellx preflight
```

You should see a green ✅ for each check. If anything is missing, ShellX will tell you what to install.

---

# 📋 Step 2: Your First Report

Run ShellX with a plain-English description of what you're working on:

```
shellx "I'm refactoring the renderer module"
```

ShellX will:
1. Parse your intent
2. Collect project metadata
3. Generate a structured report in `.reports/`

View the report immediately:

```
shellx look
```

---

# 🧩 Step 3: Running Workers

Workers are focused diagnostic tools. Run them individually as needed.

## Deep Audit
```
shellx deep-audit
```
Scans for structural issues, dead code, and anti-patterns.

## Debug Worker
```
shellx debug
```
Traces errors and pinpoints root causes.

## Architecture Worker
```
shellx architect
```
Maps your project structure and dependency graph.

## Memory Worker
```
shellx memory
```
Analyzes memory usage patterns.

## Safe Autofix
```
shellx autofix --safe
```
Applies safe, non-destructive fixes automatically.

## Verify
```
shellx verify
```
Confirms that fixes and changes are valid.

---

# 🦸 Step 4: Superman Mode

When you want everything at once, use Superman Mode:

```
shellx-superman "audit everything and fix what's safe"
```

This runs all workers in sequence:
1. Smart input
2. Deep audit
3. Debug
4. Architect
5. Memory
6. Autofix (safe)
7. Verify
8. Stone creation
9. LinkX update

---

# 🧠 Step 5: Cognitive Engine (V3)

For the most intelligent analysis, use the `--xx` flag:

```
shellx --xx "optimize the rendering pipeline"
```

ShellX will produce a structured 1-2-3 summary:

1. **What you wanted** — your goal, in plain English
2. **What ShellX did** — the actions taken
3. **What changed** — the outcome

---

# 🧬 Step 6: LinkX Memory

ShellX remembers your work history in the LinkX memory graph.

## View your history
```
shellx linkx timeline
```

## Search for a past task
```
shellx linkx search "renderer"
```

## View a specific entry
```
shellx linkx show 7
```

---

# 🪨 Step 7: Stones (Recovery Snapshots)

Stones are automatic snapshots created at key moments.

## List snapshots
```
shellx stone list
```

## Inspect a snapshot
```
shellx stone show 3
```

## Compare two snapshots
```
shellx stone diff 3 7
```

## Restore a snapshot
```
shellx stone restore 3 --confirm
```

---

# 🧭 Step 8: Multi‑Project Mode

Working across multiple repos or directories? Use multi-project mode:

```
shellx multi-project "audit all repos in /workspace"
```

---

# 🥇 Step 9: ShellX Pro

Activate Pro for enterprise-grade features:

```
shellx activate SHELLX-PRO-XXXX-XXXX-XXXX
```

Then run Pro workers:

```
shellx architect-pro
shellx deep-audit-pro
shellx-superman-pro "full enterprise analysis"
```

---

# 🎯 What's Next

- Read [Commands-Full.md](Commands-Full.md) for the complete command reference
- Read [Commands-Flags.md](Commands-Flags.md) for all available flags
- Read [Commands-Advanced.md](Commands-Advanced.md) for power-user patterns
- Read [Commands-Pro.md](Commands-Pro.md) for Pro-only commands
