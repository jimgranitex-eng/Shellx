const { execSync } = require('child_process');
const path = require('path');
const fs = require('fs');

const IDES = {
  vscode: {
    name: 'VS Code',
    cmd: process.platform === 'win32' ? 'code' : 'code',
    configDir: '.vscode',
    extensions: true,
  },
  pycharm: {
    name: 'PyCharm',
    cmd: process.platform === 'win32' ? 'pycharm' : 'pycharm',
    configDir: '.idea',
    extensions: false,
  },
  'android-studio': {
    name: 'Android Studio',
    cmd: process.platform === 'win32' ? 'studio64' : 'studio',
    configDir: '.idea',
    extensions: false,
  },
  intellij: {
    name: 'IntelliJ IDEA',
    cmd: process.platform === 'win32' ? 'idea64' : 'idea',
    configDir: '.idea',
    extensions: false,
  },
  webstorm: {
    name: 'WebStorm',
    cmd: process.platform === 'win32' ? 'webstorm' : 'webstorm',
    configDir: '.idea',
    extensions: false,
  },
  xcode: {
    name: 'Xcode',
    cmd: 'xed',
    configDir: null,
    extensions: false,
  },
  sublime: {
    name: 'Sublime Text',
    cmd: process.platform === 'win32' ? 'subl' : 'subl',
    configDir: null,
    extensions: false,
  },
  vim: {
    name: 'Vim/Neovim',
    cmd: 'nvim',
    configDir: null,
    extensions: false,
  },
};

function detectIDEs() {
  const found = [];
  for (const [id, ide] of Object.entries(IDES)) {
    try {
      execSync(`${ide.cmd} --version`, { stdio: 'ignore', timeout: 3000 });
      found.push({ id, name: ide.name });
    } catch {}
  }

  if (process.env.TERM_PROGRAM === 'vscode') {
    if (!found.find(f => f.id === 'vscode')) {
      found.push({ id: 'vscode', name: 'VS Code' });
    }
  }

  return found;
}

function openProject(ideId, projectPath) {
  const ide = IDES[ideId];
  if (!ide) return { success: false, message: `Unknown IDE: ${ideId}. Supported: ${Object.keys(IDES).join(', ')}` };

  const target = projectPath || process.cwd();
  if (!fs.existsSync(target)) return { success: false, message: `Path does not exist: ${target}` };

  try {
    execSync(`${ide.cmd} "${target}"`, { stdio: 'inherit', timeout: 10000 });
    return { success: true, message: `Opened ${target} in ${ide.name}` };
  } catch (e) {
    return { success: false, message: `Failed to open ${ide.name}: ${e.message}` };
  }
}

function listCommands() {
  return `
  Usage:
    shellx ide detect              Detect installed IDEs
    shellx ide list                List supported IDEs
    shellx ide open <ide> [path]   Open project in specific IDE
    shellx ide vscode <action>     VS Code actions (install-extension, list-extensions)
  `;
}

function vscodeAction(action, arg) {
  switch (action) {
    case 'install-extension':
      if (!arg) return { success: false, message: 'Usage: shellx ide vscode install-extension <extension-id>' };
      try {
        execSync(`code --install-extension "${arg}"`, { stdio: 'inherit', timeout: 30000 });
        return { success: true, message: `Installed extension: ${arg}` };
      } catch (e) {
        return { success: false, message: `Failed to install extension: ${e.message}` };
      }
    case 'list-extensions':
      try {
        const output = execSync('code --list-extensions', { encoding: 'utf8', timeout: 10000 });
        return { success: true, extensions: output.trim().split('\n') };
      } catch (e) {
        return { success: false, message: `Failed to list extensions: ${e.message}` };
      }
    default:
      return { success: false, message: `Unknown VS Code action: ${action}. Use: install-extension, list-extensions` };
  }
}

function handle(args) {
  const sub = args[0] || 'help';

  if (sub === 'detect') {
    const found = detectIDEs();
    if (found.length === 0) return console.log('No supported IDEs detected.');
    console.log('Detected IDEs:');
    found.forEach(f => console.log(`  - ${f.name} (${f.id})`));
    return;
  }

  if (sub === 'list') {
    console.log('Supported IDEs:');
    for (const [id, ide] of Object.entries(IDES)) {
      console.log(`  ${id.padEnd(20)} ${ide.name}`);
    }
    return;
  }

  if (sub === 'open') {
    const result = openProject(args[1], args[2]);
    console.log(result.message);
    return;
  }

  if (sub === 'vscode') {
    const result = vscodeAction(args[1], args.slice(2).join(' '));
    if (result.extensions) {
      console.log('Installed extensions:');
      result.extensions.forEach(e => console.log(`  ${e}`));
    } else {
      console.log(result.message);
    }
    return;
  }

  if (['help', '--help', '-h'].includes(sub)) {
    console.log(listCommands());
    return;
  }

  console.log(`Unknown ide subcommand: ${sub}`);
  console.log(`\n  Usage:\n    shellx ide <subcommand> [args]\n`);
  console.log(listCommands());
}

module.exports = { handle, detectIDEs, openProject };
