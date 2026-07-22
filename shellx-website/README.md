# ShellX Website

Private documentation and landing page for ShellX.

## CLI Alignment

The website documentation should match the published CLI package and commands:

```bash
npm install -g shellx-dev-cli
shellx init
shellx linkx init
shellx linkx scan
shellx linkx show
shellx linkx timeline
shellx verify
shellx report
shellx --xx "your intent here"
```

## Deployment

### GitHub Pages

1. Push the website files to the repository or a gh-pages branch.
2. Enable GitHub Pages in repository settings.
3. Set the custom domain if needed.

### Private access

The site includes a password gate.

### Structure

```text
shellx-website/
├── index.html
├── docs/
├── pro/
└── assets/
```

## Customization

- Edit `assets/css/style.css` for colors
- Edit HTML files for content
- Edit `assets/js/main.js` for password gate behavior

## License

Website content © 2026 James. ShellX software licensing details are in `pro/license.html`.
