// Usage: copy contents into your extension's activate(context) or require this file and call install(context)
const vscode = require('vscode');
const { ShellXProvider } = require('./shellxProvider');

let shellxReportChannel = null;

function showShellXReport(reportText) {
    if (!shellxReportChannel) shellxReportChannel = vscode.window.createOutputChannel('ShellX Report');
    shellxReportChannel.clear();
    shellxReportChannel.appendLine('===== SHELLX REPORT =====');
    shellxReportChannel.appendLine(reportText);
    shellxReportChannel.appendLine('==========================');
    shellxReportChannel.show(true);
}

async function runWorker(mode) {
    // Placeholder worker runner. Replace with project-specific logic.
    await new Promise(r => setTimeout(r, 150));
    return `Worker ${mode} completed`;
}

function generateReport(results) {
    return results.map(r => `Step: ${r.step}\nResult: ${r.result}\n`).join('\n');
}

async function runPipelineSequence(sequenceString) {
    const cleaned = (sequenceString || '').replace('--report', '').trim();
    const steps = cleaned.includes('→') ? cleaned.split('→').map(s => s.trim()) : [cleaned];
    const results = [];
    for (const step of steps) {
        const result = await runWorker(step);
        results.push({ step, result });
    }
    if (sequenceString && sequenceString.includes('--report')) {
        const report = generateReport(results);
        showShellXReport(report);
    }
    return results;
}

function install(context) {
    const shellxProvider = new ShellXProvider(context);
    context.subscriptions.push(vscode.window.registerTreeDataProvider('shellx', shellxProvider));

    context.subscriptions.push(vscode.commands.registerCommand('multiAiIntegrator.shellxLogin', () => vscode.window.showInformationMessage('ShellX Login (stub)')));
    context.subscriptions.push(vscode.commands.registerCommand('multiAiIntegrator.shellxChat', () => vscode.window.showInformationMessage('ShellX Chat (stub)')));
    context.subscriptions.push(vscode.commands.registerCommand('multiAiIntegrator.runSuperman', () => runPipelineSequence('Superman --report')));
    context.subscriptions.push(vscode.commands.registerCommand('multiAiIntegrator.runAutoFix', () => runPipelineSequence('AutoFix --report')));
    context.subscriptions.push(vscode.commands.registerCommand('multiAiIntegrator.runPipelineSequence', async () => {
        const input = await vscode.window.showInputBox({ prompt: 'Enter ShellX Pipeline' });
        if (input) runPipelineSequence(input + ' --report');
    }));

    // Example webview message handler helper you can wire into any webview
    function attachWebviewHandler(panel) {
        panel.webview.onDidReceiveMessage(msg => {
            if (msg && msg.text && msg.text.includes('ShellX-Pipeline')) {
                runPipelineSequence(msg.text + ' --report');
            }
        }, null, context.subscriptions);
    }

    return { showShellXReport, runPipelineSequence, attachWebviewHandler };
}

module.exports = { install };
