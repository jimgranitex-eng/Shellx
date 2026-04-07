# ShellX — Full Commands Reference
The complete authoritative list of all ShellX commands across V1, V2, V3, Pro, and V4 roadmap.

ShellX commands fall into these categories:

- Core Commands (V1)
- Worker Commands (V2)
- Cognitive Engine (V3)
- Superman Mode
- LinkX Memory
- Stones (Recovery Snapshots)
- Multi‑Project Mode
- ShellX Pro Commands
- V4 Reserved Commands
- Developer / Internal Commands

This page documents every command, its purpose, and usage examples.

---

# 🧱 1. Core Commands (V1)

### `shellx "<message>"`
Runs the classic ShellX report generator.

### `shellx preflight`
Runs basic environment checks.

### `shellx report`
Generates a standard ShellX report.

### `shellx collect`
Collects system and project metadata.

### `shellx look`
Displays the most recent ShellX report.

---

# 🧩 2. Worker Commands (V2)

These commands run individual workers manually.

### `shellx deep-audit`
Runs the deep audit worker.

### `shellx debug`
Runs the debug worker.

### `shellx architect`
Runs the architecture analysis worker.

### `shellx memory`
Runs the memory worker.

### `shellx autofix --safe`
Runs safe-mode autofix (no destructive writes).

### `shellx verify`
Runs verification checks.

---

# 🦸 3. Superman Mode (V2/V500)

### `shellx-superman "<message>"`
Runs the full multi-agent diagnostic pipeline:

- Smart input
- Deep audit
- Debug
- Architect
- Memory
- Safe-mode autofix
- Verify
- Stone creation
- LinkX update

This is the "all-systems" mode.

---

# 🧠 4. Cognitive Engine Commands (V3)

### `shellx --xx "<message>"`
Runs the V3 Cognitive Reporting Engine.

Produces the 1‑2‑3 summary:

1. What you wanted  
2. What ShellX did  
3. What changed  

Also generates:

- Full report (`.reports/`)
- LinkX update
- Stone snapshot

---

# 🧬 5. LinkX Memory Commands

### `shellx linkx timeline`
Shows the full LinkX memory timeline.

### `shellx linkx show <id>`
Shows a specific LinkX entry.

### `shellx linkx search "<query>"`
Searches the LinkX memory graph.

---

# 🪨 6. Stone Commands (Recovery Snapshots)

### `shellx stone list`
Lists all Stones.

### `shellx stone show <id>`
Shows details for a Stone.

### `shellx stone diff <id>`
Shows diffs between Stones.

### `shellx stone restore <id>`
Restores a Stone snapshot.

---

# 🧭 7. Multi‑Project Mode

### `shellx multi-project "<instructions>"`
Runs ShellX across multiple repositories or directories.

---

# 🥇 8. ShellX Pro Commands (Commercial Edition)

These commands unlock after activation.

---

## 🔐 Activation

### `shellx activate <license-key>`
Activates ShellX Pro.

---

## 🧩 Pro Workers

### `shellx architect-pro`
Advanced architecture mapping.

### `shellx memory-pro`
Enterprise memory graph analysis.

### `shellx deep-audit-pro`
Enhanced deep audit.

### `shellx autofix-pro`
Autofix+ (safe + aggressive modes).

### `shellx verify-pro`
Pro-level verification.

### `shellx timeline-pro`
Enterprise LinkX timeline tools.

---

## 🦸 Superman Pro

### `shellx-superman-pro "<message>"`
The most powerful diagnostic mode available.

---

## 🧰 Pro Utilities

### `shellx pro status`
Shows Pro activation status.

### `shellx pro diagnostics`
Runs Pro-level diagnostics.

### `shellx pro update`
Updates Pro modules.

---

# 🧪 9. V4 Reserved Commands (Future Engine)

These commands are placeholders for the V4 modular engine.

### `shellx plugin install <name>`
Installs a ShellX plugin.

### `shellx plugin list`
Lists installed plugins.

### `shellx engine status`
Shows engine health and worker registry.

### `shellx engine reload`
Reloads the engine configuration.

### `shellx engine workers`
Lists all workers (core + plugins).

---

# 🧰 10. Developer / Internal Commands

Used for debugging ShellX itself.

### `shellx dev dump`
Dumps internal state.

### `shellx dev workers`
Lists all worker modules.

### `shellx dev pipeline`
Shows the active pipeline.

### `shellx dev config`
Displays configuration details.

---

# 📘 Summary Table

| Category | Commands |
|---------|----------|
| **Core (V1)** | `shellx`, `preflight`, `report`, `collect`, `look` |
| **Workers (V2)** | `deep-audit`, `debug`, `architect`, `memory`, `autofix`, `verify` |
| **Superman** | `shellx-superman` |
| **Cognitive (V3)** | `shellx --xx` |
| **LinkX** | `linkx timeline`, `linkx show`, `linkx search` |
| **Stones** | `stone list`, `stone show`, `stone diff`, `stone restore` |
| **Multi‑Project** | `multi-project` |
| **Pro (Commercial)** | `activate`, `architect-pro`, `memory-pro`, `superman-pro`, etc. |
| **V4 Reserved** | `plugin install`, `engine status`, etc. |
| **Internal** | `dev dump`, `dev workers`, etc. |

---

# 🎯 Final Notes
This page is the canonical reference for all ShellX commands.  
Update it whenever new workers, pipelines, or Pro modules are added.
