# ShellX — Command Flags Reference

This page lists all flags available across ShellX commands.

---

# 🧠 Cognitive Engine Flags (V3)

### `--xx`
Enable cognitive mode.

### `--strict`
Enforce strict parsing.

### `--context=<file>`
Load external context from a JSON file.

---

# 🧩 Worker Flags (V2)

### `--log=verbose`
Enable detailed logging.

### `--export=<file>`
Export worker output to a file.

### `--safe`
Run in safe mode (autofix only).

---

# 🦸 Superman Flags

### `--no-autofix`
Disable autofix stage.

### `--profile=<name>`
Use a custom diagnostic profile.

### `--strict`
Enforce strict parsing in Superman mode.

---

# 🧬 LinkX Flags

### `--export=<file>`
Export timeline or entry to a file.

### `--filter=<query>`
Filter timeline results by keyword.

---

# 🪨 Stone Flags

### `--confirm`
Require confirmation before restoring a Stone.

### `--dry-run`
Preview the restore without making changes.

---

# 🧭 Multi‑Project Flags

### `--path=<dir>`
Set the root directory for multi-project mode.

### `--include=<pattern>`
Include files matching a glob pattern.

### `--exclude=<pattern>`
Exclude files matching a glob pattern.

### `--xx`
Run cognitive mode across all projects.

---

# 🥇 Pro Flags

### `--deep`
Enable deep analysis (Pro workers).

### `--graph`
Generate a graph output.

### `--branch=<name>`
Target a specific branch (timeline-pro).

### `--diff`
Show diff output (timeline-pro).

---

# 📘 Flag Summary Table

| Flag | Applies To | Description |
|------|-----------|-------------|
| `--xx` | Cognitive, Multi-Project | Enable cognitive mode |
| `--strict` | Cognitive, Superman | Enforce strict parsing |
| `--context=<file>` | Cognitive | Load external context |
| `--safe` | autofix | Safe mode (no destructive writes) |
| `--log=verbose` | Workers | Enable verbose logging |
| `--export=<file>` | Workers, LinkX | Export output to file |
| `--no-autofix` | Superman | Disable autofix stage |
| `--profile=<name>` | Superman | Use custom profile |
| `--filter=<query>` | LinkX | Filter results |
| `--confirm` | Stones | Require confirmation |
| `--dry-run` | Stones | Preview without changes |
| `--path=<dir>` | Multi-Project | Set root directory |
| `--include=<pattern>` | Multi-Project | Include file pattern |
| `--exclude=<pattern>` | Multi-Project | Exclude file pattern |
| `--deep` | Pro Workers | Enable deep analysis |
| `--graph` | Pro Workers | Generate graph output |
| `--branch=<name>` | timeline-pro | Target branch |
| `--diff` | timeline-pro | Show diff output |

---

# 🎯 Summary
Use flags to customize and extend ShellX command behavior.  
Combine flags freely unless otherwise noted.
