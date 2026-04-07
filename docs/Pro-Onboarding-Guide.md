# ShellX Pro — Onboarding Guide

Welcome to ShellX Pro. This guide walks you from purchase to daily use.

---

## 1. Get Your License Key

After purchasing ShellX Pro, you receive:
- A license key
- Access to the private Pro repository
- Setup instructions

Keep your license key private.

---

## 2. Install ShellX (Open Source Core)

Follow the Quickstart:
- Clone the public repo
- Install dependencies
- Run a basic `shellx` command

See: `docs/Quickstart.md`

---

## 3. Activate ShellX Pro

Run:
```bash
shellx activate SHELLX-PRO-XXXX-XXXX-XXXX
```

This:
- Validates your key
- Stores it locally
- Unlocks Pro modules

Check status:
```bash
shellx pro status
```

---

## 4. Clone the Pro Repository

You'll be granted access to:
```bash
git clone https://github.com/YOURNAME/ShellX-Pro
```

Follow the README there for any Pro-specific setup.

---

## 5. Run Your First Pro Commands

Superman Pro:
```bash
shellx-superman-pro "full system analysis"
```

Architecture Pro:
```bash
shellx architect-pro --deep --graph --export=arch.json
```

Timeline Pro:
```bash
shellx timeline-pro --branch=main --diff
```

---

## 6. Integrate into Your Workflow

Ideas:
- Run Superman Pro before major releases
- Use Stones as recovery points before large refactors
- Use LinkX Pro to understand long-term evolution
- Wire ShellX Pro into CI/CD (see `CI-CD-Pipeline.md`)

---

## 7. Get Help

For support, feature requests, or enterprise questions:
- Open a [GitHub Issue](https://github.com/jimgranitex-eng/Shellx/issues)
- See [Pro FAQ](Pro-FAQ.md)
- See [Pro Enterprise](Pro-Enterprise.md)

---

You're now ready to use ShellX Pro as a core part of your development workflow.
