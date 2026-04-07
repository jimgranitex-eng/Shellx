# ShellX — Interactive Mode Guide

This guide covers ShellX's interactive features, prompts, and session-based workflows.

---

# 🎮 What Is Interactive Mode?

Interactive mode lets you work with ShellX in a conversational back-and-forth session rather than running single commands.

Launch interactive mode:

```
shellx interactive
```

Or use the short alias:

```
shellx -i
```

---

# 💬 Interactive Session Basics

Once in interactive mode, ShellX presents a prompt:

```
shellx> _
```

You can type commands or plain-English instructions directly:

```
shellx> audit the renderer module
shellx> what changed in the last Stone?
shellx> show me the LinkX timeline
shellx> run architect
shellx> exit
```

ShellX interprets your input using the Cognitive Engine (V3) and routes it to the appropriate worker or command.

---

# 🧠 Cognitive Prompts

In interactive mode, ShellX accepts natural language prompts:

| You type | ShellX runs |
|----------|------------|
| `audit everything` | `shellx deep-audit` |
| `what's wrong with the renderer?` | `shellx debug` |
| `show me the architecture` | `shellx architect` |
| `fix what's safe` | `shellx autofix --safe` |
| `show my history` | `shellx linkx timeline` |
| `restore last snapshot` | `shellx stone restore <latest>` |

---

# 🦸 Superman Interactive

Run Superman Mode interactively for a guided multi-agent session:

```
shellx> superman
```

ShellX will walk you through each stage and ask for confirmation before applying fixes.

---

# 🧬 LinkX in Interactive Mode

```
shellx> linkx timeline
shellx> linkx search "renderer"
shellx> linkx show 12
```

---

# 🪨 Stones in Interactive Mode

```
shellx> stone list
shellx> stone show 5
shellx> stone diff 4 5
shellx> stone restore 4
```

ShellX will ask for confirmation before restoring:

```
Restore Stone #4? This will revert your project state. [y/N]
```

---

# 🔄 Session Context

Interactive mode maintains context across commands in a session.

Example:

```
shellx> audit the renderer
[ShellX runs deep-audit on the renderer module]

shellx> now fix it
[ShellX runs autofix --safe on the renderer module, using context from the previous command]

shellx> verify
[ShellX runs verify on the same module]
```

---

# 🧭 Multi‑Project Interactive

```
shellx> multi-project /workspace
```

ShellX will scan all projects in `/workspace` and present a menu to select which ones to audit.

---

# 🥇 Pro Interactive Mode

Pro users get an enhanced interactive session with:

- Deeper cognitive routing
- Auto Stone creation at session end
- Timeline auto-update
- Pro worker access

```
shellx> activate SHELLX-PRO-XXXX-XXXX-XXXX
shellx> superman-pro
```

---

# 🚪 Exiting Interactive Mode

```
shellx> exit
```

Or press `Ctrl+C` at any prompt.

ShellX will automatically:
- Create a Stone snapshot of the session
- Update the LinkX timeline
- Save session logs to `.reports/`

---

# 🎯 Summary

Interactive mode is ideal for:
- Exploratory debugging sessions
- Multi-step workflows
- New users learning ShellX commands
- Complex projects requiring iterative analysis

For scripted or automated workflows, use single-command mode instead.  
See [Commands-Full.md](Commands-Full.md) for the complete command reference.
