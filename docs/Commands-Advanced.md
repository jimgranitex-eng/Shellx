# ShellX — Advanced Command Usage

This guide covers advanced patterns, flags, pipelines, and multi-step workflows.

---

# 🧠 1. Cognitive Engine (V3) — Advanced

## Cognitive Mode with Context
```
shellx --xx --context=project.json "optimize the build pipeline"
```

## Cognitive Mode with Strict Parsing
```
shellx --xx --strict "refactor the renderer"
```

---

# 🧩 2. Worker Chaining (V2)

## Run Workers Sequentially
```
shellx deep-audit && shellx debug && shellx verify
```

## Run Workers with Flags
```
shellx autofix --safe --log=verbose
```

---

# 🦸 3. Superman Mode — Advanced

## Superman with Custom Profile
```
shellx-superman --profile=graphics "diagnose rendering issues"
```

## Superman with No Autofix
```
shellx-superman --no-autofix "audit everything"
```

---

# 🧬 4. LinkX — Advanced

## Export Timeline
```
shellx linkx timeline --export=timeline.json
```

## Filter Timeline
```
shellx linkx timeline --filter="renderer"
```

---

# 🪨 5. Stones — Advanced

## Compare Two Stones
```
shellx stone diff 12 47
```

## Restore with Confirmation
```
shellx stone restore 33 --confirm
```

---

# 🧭 6. Multi‑Project Mode — Advanced

## Run Across Multiple Directories
```
shellx multi-project --path=/workspace --include="*.ts"
```

## Multi-Project Cognitive Mode
```
shellx multi-project --xx "audit all repos"
```

---

# 🥇 7. Pro — Advanced

## Pro Worker Flags
```
shellx architect-pro --deep --graph --export=arch.json
```

## Pro Timeline
```
shellx timeline-pro --branch=main --diff
```

---

# 🎯 Summary
These advanced patterns unlock the full power of ShellX.
