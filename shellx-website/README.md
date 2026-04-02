# ShellX Website

Private documentation and landing page for ShellX — the Cognitive Developer Engine.

## 🌐 Deployment

### GitHub Pages Setup

1. **Push to Repository**
   ```bash
   git clone https://github.com/jimgranitex-eng/Shellx.git
   cd Shellx
   # Copy these website files to the repo root or gh-pages branch
   cp -r /path/to/shellx-website/* .
   git add .
   git commit -m "Add documentation website"
   git push origin main
   ```

2. **Enable GitHub Pages**
   - Go to repository Settings → Pages
   - Source: Deploy from a branch
   - Branch: `main` (root) or `gh-pages`
   - Save

3. **Custom Domain (Silivus.world/shellx)**
   - Create `CNAME` file in repo root with: `shellx.silivus.world` (subdomain)
   - OR configure path-based routing in your DNS/CDN for `silivus.world/shellx`
   - Add DNS record: CNAME `shellx` → `jimgranitex-eng.github.io`
   - Enable HTTPS in GitHub Pages settings

### Private Access

The site includes a password gate. Default access code:
```
cognitive-engine-2026
```

To change the password, edit `assets/js/main.js`:
```javascript
const ACCESS_CODE = 'your-new-code';
```

### Structure

```
shellx-website/
├── index.html              # Landing page
├── docs/
│   ├── quickstart.html     # Quickstart guide
│   └── commands.html       # Command reference
├── pro/
│   └── license.html        # Commercial license
├── assets/
│   ├── css/style.css       # Stylesheet
│   └── js/main.js          # Interactions & password gate
└── README.md               # This file
```

## 🔒 Privacy Notes

- Password gate is client-side JavaScript (basic obscurity)
- For stronger protection, consider:
  - HTTP Basic Auth at server level
  - Cloudflare Access rules
  - VPN/private network deployment
- The `Silivus.world` domain masking keeps the GitHub origin hidden from end users

## 🎨 Customization

- Colors: Edit CSS variables in `assets/css/style.css` (`:root`)
- Content: Modify HTML files directly
- Links: Update GitHub repo links in navigation

## 📄 License

Website content © 2026 James. All rights reserved.
ShellX software licensing details in `pro/license.html`.
