# Contributing to ShellX

## Local development

```bash
git clone https://github.com/jimgranitex-eng/Shellx.git
cd Shellx
npm install
```

## Run the CLI

```bash
node bin/shellx.js --version
node bin/shellx.js init
node bin/shellx.js linkx init
node bin/shellx.js linkx scan
node bin/shellx.js linkx show
node bin/shellx.js linkx timeline
node bin/shellx.js verify
node bin/shellx.js report
```

## Publishing

```bash
npm version 3.0.0
npm publish --access public
```
