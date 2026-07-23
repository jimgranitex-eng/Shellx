ShellX — Universal patch bundle
===============================

Drop-in files to make a minimal, reusable ShellX sidebar + pipeline runner available inside any VS Code extension.

Files
- `shellxProvider.js` — Tree provider implementation (sidebar items & commands).
- `extension-snippet.js` — Activation/install snippet that registers the provider and commands and exposes `runPipelineSequence` and `showShellXReport` helpers.
- `package-snippet.json` — `package.json` snippet showing `viewsContainers` / `views` addition.

How to use
1. Copy `shellxProvider.js` and `extension-snippet.js` into your extension project (e.g. into `src/` or `out/`).
2. In your extension `activate(context)` require and install the snippet:

```js
const shellx = require('./path/to/extension-snippet');
const shellxApi = shellx.install(context);
// optionally use shellxApi.attachWebviewHandler(panel) for any webview
```

3. Merge `package-snippet.json` into your extension `package.json` under `contributes`.

4. The default commands registered are:
   - `multiAiIntegrator.shellxLogin`
   - `multiAiIntegrator.shellxChat`
   - `multiAiIntegrator.runSuperman`
   - `multiAiIntegrator.runAutoFix`
   - `multiAiIntegrator.runPipelineSequence`

5. The pipeline runner accepts a simple `→`-delimited sequence or a single step. Append `--report` to render a report in the `ShellX Report` output channel.

Example
```
runPipelineSequence('Superman → AutoFix → Debug --report')
```

Notes
- This bundle is intentionally lightweight and project-agnostic — adapt `runWorker` inside `extension-snippet.js` to call your real workers, tasks or CLI tooling.
- If you want, I can inject this into a target extension in this workspace (tell me the extension entry file and I will apply the patch and register the snippets).
