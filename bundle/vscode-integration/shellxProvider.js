const vscode = require('vscode');

class ShellXItem extends vscode.TreeItem {
    constructor(label, commandId) {
        super(label, vscode.TreeItemCollapsibleState.None);
        this.command = {
            command: commandId,
            title: label,
            arguments: []
        };
    }
}

class ShellXProvider {
    constructor(context) {
        this.context = context;
        this._onDidChangeTreeData = new vscode.EventEmitter();
        this.onDidChangeTreeData = this._onDidChangeTreeData.event;
    }

    refresh() {
        this._onDidChangeTreeData.fire();
    }

    getTreeItem(element) {
        return element;
    }

    getChildren() {
        return [
            new ShellXItem('Login', 'multiAiIntegrator.shellxLogin'),
            new ShellXItem('Chat', 'multiAiIntegrator.shellxChat'),
            new ShellXItem('Run Superman', 'multiAiIntegrator.runSuperman'),
            new ShellXItem('Run AutoFix', 'multiAiIntegrator.runAutoFix'),
            new ShellXItem('Run Pipeline', 'multiAiIntegrator.runPipelineSequence')
        ];
    }
}

module.exports = { ShellXProvider, ShellXItem };
