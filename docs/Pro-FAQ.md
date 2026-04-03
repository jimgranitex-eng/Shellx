# ShellX Pro — Frequently Asked Questions

---

## General

### What is ShellX Pro?

ShellX Pro is the commercial edition of the ShellX Cognitive Developer Engine. It includes advanced diagnostics, multi-agent workers, enterprise memory tracking, and premium support — features not available in the open-source edition.

---

### What is the difference between ShellX and ShellX Pro?

**ShellX (open source) includes:**
- Cognitive reporting (V3)
- Core workers
- LinkX basic timeline
- Stone snapshots
- Standard reports

**ShellX Pro adds:**
- Superman Pro (enhanced deep diagnostics)
- Advanced multi-agent workers (`architect-pro`, `memory-pro`, `deep-audit-pro`, `autofix-pro`, `verify-pro`)
- Deep architecture mapping
- Enterprise LinkX timeline
- Stone diff viewer
- VS Code interactive panels
- Priority support
- Early access to V4 modules

---

### Is ShellX Pro open source?

No. ShellX Pro is a commercially licensed product. The source code is available only to paying customers in a private repository. See [LICENSE-PRO.md](../LICENSE-PRO.md).

---

## Licensing & Pricing

### How much does ShellX Pro cost?

| Plan | Price |
|------|-------|
| Starter | $10/month |
| Professional | $25/month |
| Enterprise | $99/month |

See [Pro-Pricing.md](Pro-Pricing.md) for full plan details.

---

### How do I purchase ShellX Pro?

- **[GitHub Sponsors](https://github.com/sponsors/jimgranitex-eng)** — easiest method, automatic repo access
- **Stripe Checkout** — contact for a payment link
- **Direct licensing** — open an issue for enterprise quotes

---

### Can I use ShellX Pro in closed-source projects?

Yes. ShellX Pro is licensed for commercial, closed-source use. See [LICENSE-PRO.md](../LICENSE-PRO.md) for full terms.

---

### What is your refund policy?

14-day no-questions-asked refund. Contact via GitHub Issues.

---

## Setup & Activation

### How do I activate ShellX Pro?

```bash
shellx activate SHELLX-PRO-XXXX-XXXX-XXXX
```

See [Pro-Activation-System.md](Pro-Activation-System.md) for full details.

---

### Where is my license key stored?

```
~/.shellx/license.key
```

The file is stored with restricted permissions (readable only by your user).

---

### How do I access the private Pro repository?

After purchase you receive an invitation to the private `ShellX-Pro` GitHub repository. Then:

```bash
git clone https://github.com/jimgranitex-eng/ShellX-Pro.git
```

---

### What happens if I cancel my subscription?

Your existing installation continues to work. You lose access to future updates and the private repository. See [LICENSE-PRO.md](../LICENSE-PRO.md).

---

## Enterprise

### Do you offer enterprise support?

Yes. Enterprise plans include:
- Unlimited seats
- Dedicated support channel
- SLA-backed response times
- Custom worker development
- Deployment consulting

See [Pro-Enterprise.md](Pro-Enterprise.md).

---

### Can I get a custom worker built for my codebase?

Yes — this is available on the Enterprise plan. Open an issue to discuss requirements.

---

## Support

### How do I get help?

- Open an issue: [github.com/jimgranitex-eng/Shellx/issues](https://github.com/jimgranitex-eng/Shellx/issues)
- See [SECURITY.md](../SECURITY.md) for security issues
