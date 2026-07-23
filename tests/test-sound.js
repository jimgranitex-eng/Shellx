const { execSync } = require('child_process');
const path = require('path');
const fs = require('fs');
const os = require('os');

const CLI = path.join(__dirname, '..', 'bin', 'shellx-dev-cli.js');
const SUPERMAN = path.join(__dirname, '..', 'bin', 'shellx-superman.js');
const PKG = path.join(__dirname, '..', 'package.json');

function tmp(name) {
  const d = fs.mkdtempSync(path.join(os.tmpdir(), `shellx-sound-${name}-`));
  return d;
}

function run(cli, args, opts = {}) {
  const cwd = opts.cwd || process.cwd();
  const timeout = opts.timeout || 15000;
  try {
    const out = execSync(`node ${cli} ${args}`, { cwd, encoding: 'utf8', timeout });
    return { code: 0, stdout: out, stderr: '' };
  } catch (e) {
    return { code: e.status || 1, stdout: e.stdout || '', stderr: e.stderr || e.message };
  }
}

let pass = 0, fail = 0;
function test(name, fn) {
  try {
    fn();
    console.log(`  PASS  ${name}`);
    pass++;
  } catch (e) {
    console.log(`  FAIL  ${name}: ${e.message}`);
    fail++;
  }
}

function assertContains(actual, expected) {
  if (!actual.includes(expected)) throw new Error(`Expected "${actual}" to contain "${expected}"`);
}

function assertNotContains(actual, expected) {
  if (actual.includes(expected)) throw new Error(`Expected "${actual}" to NOT contain "${expected}"`);
}

console.log('\n═══════════════════════════════════════');
console.log('  ShellX Soundness Test Suite');
console.log('═══════════════════════════════════════\n');

// ===========================
// SECTION 1: Help & Info
// ===========================
console.log('── Help & Info ──');

test('--help shows banner with version', () => {
  const r = run(CLI, '--help');
  assertContains(r.stdout, 'v3.1.0');
  assertContains(r.stdout, 'ShellX');
  assertContains(r.stdout, 'Cognitive Developer Engine');
});

test('--help shows all command categories', () => {
  const r = run(CLI, '--help');
  assertContains(r.stdout, 'doctor');
  assertContains(r.stdout, 'activate');
  assertContains(r.stdout, 'ide detect');
  assertContains(r.stdout, 'shellx-superman');
  assertContains(r.stdout, '--xx');
});

test('help command same as --help', () => {
  const r = run(CLI, 'help');
  assertContains(r.stdout, 'ShellX');
});

test('-h flag works', () => {
  const r = run(CLI, '-h');
  assertContains(r.stdout, 'ShellX');
});

test('no args shows help', () => {
  const r = run(CLI, '');
  assertContains(r.stdout, 'USAGE');
});

// ===========================
// SECTION 2: LinkX Commands
// ===========================
console.log('\n── LinkX Commands ──');

test('linkx init creates goal.json', () => {
  const d = tmp('linkx');
  const r = run(CLI, 'linkx init', { cwd: d });
  assertContains(r.stdout, 'LinkX initialized');
  const gf = path.join(d, '.shellx', 'goal.json');
  if (!fs.existsSync(gf)) throw new Error('goal.json not created');
  const g = JSON.parse(fs.readFileSync(gf, 'utf8'));
  if (!g.created) throw new Error('goal.json missing created field');
});

test('linkx scan runs without crash', () => {
  const d = tmp('linkscan');
  const r = run(CLI, 'linkx scan', { cwd: d, timeout: 30000 });
  assertContains(r.stdout, 'LinkX scan');
  assertContains(r.stdout, 'PREFLIGHT');
});

test('linkx with no subcommand shows usage', () => {
  const r = run(CLI, 'linkx');
  assertContains(r.stdout, 'Usage');
});

// ===========================
// SECTION 3: License Commands
// ===========================
console.log('\n── License Commands ──');

test('license status shows unlicensed on fresh install', () => {
  const d = tmp('license');
  const r = run(CLI, 'license status', { cwd: d });
  assertContains(r.stdout, 'Not activated');
});

test('activate with invalid key returns error', () => {
  const r = run(CLI, 'activate INVALID-KEY-TEST');
  assertContains(r.stdout, 'Invalid license key');
  assertNotContains(r.stdout, 'success');
});

test('activate with no key shows usage', () => {
  const r = run(CLI, 'activate');
  assertContains(r.stdout, 'Usage');
});

test('deactivate on unlicensed system shows message', () => {
  const d = tmp('deactivate');
  const r = run(CLI, 'deactivate', { cwd: d });
  assertContains(r.stdout, 'No active license');
});

test('license with bad subcommand exits gracefully', () => {
  const r = run(CLI, 'license badcommand');
  assertContains(r.stdout, 'Usage');
});

// ===========================
// SECTION 4: IDE Commands
// ===========================
console.log('\n── IDE Commands ──');

test('ide list shows all 8 IDEs', () => {
  const r = run(CLI, 'ide list');
  assertContains(r.stdout, 'vscode');
  assertContains(r.stdout, 'pycharm');
  assertContains(r.stdout, 'android-studio');
  assertContains(r.stdout, 'intellij');
  assertContains(r.stdout, 'webstorm');
  assertContains(r.stdout, 'xcode');
  assertContains(r.stdout, 'sublime');
  assertContains(r.stdout, 'vim');
});

test('ide detect runs without crash', () => {
  const r = run(CLI, 'ide detect', { timeout: 10000 });
  if (r.code !== 0 && !r.stdout.includes('No supported IDEs')) {
    throw new Error(`ide detect failed: ${r.stderr}`);
  }
});

test('ide open with invalid IDE shows error', () => {
  const r = run(CLI, 'ide open nonexistent-ide');
  assertContains(r.stdout, 'Unknown IDE');
});

test('ide with no subcommand shows help', () => {
  const r = run(CLI, 'ide');
  assertContains(r.stdout, 'Usage');
});

test('ide help shows usage', () => {
  const r = run(CLI, 'ide help');
  assertContains(r.stdout, 'Usage');
});

test('ide vscode with no args shows error', () => {
  const r = run(CLI, 'ide vscode');
  assertContains(r.stdout, 'Unknown VS Code action');
});

// ===========================
// SECTION 5: XX Intent Mode
// ===========================
console.log('\n── XX Intent Mode ──');

test('--xx with intent shows processing', () => {
  const d = tmp('xx');
  const r = run(CLI, '--xx "analyze the project"', { cwd: d, timeout: 30000 });
  assertContains(r.stdout, 'XX Intent Processor');
  assertContains(r.stdout, 'analyze');
});

test('--xx with no intent shows usage', () => {
  const r = run(CLI, '--xx');
  assertContains(r.stdout, 'Usage');
});

test('bare text treated as intent mode', () => {
  const d = tmp('intent');
  const r = run(CLI, '"stabilize the build"', { cwd: d, timeout: 30000 });
  assertContains(r.stdout, 'Processing intent');
});

// ===========================
// SECTION 6: Superman Mode
// ===========================
console.log('\n── Superman Mode ──');

test('shellx-superman runs without crash', () => {
  const d = tmp('superman');
  const r = run(SUPERMAN, '"test diagnostic"', { cwd: d, timeout: 30000 });
  assertContains(r.stdout, 'Superman Mode');
  assertContains(r.stdout, 'Multi-Agent');
});

test('shellx-superman with no args shows usage', () => {
  const r = run(SUPERMAN, '');
  assertContains(r.stdout, 'Usage');
});

// ===========================
// SECTION 7: Python Modes
// ===========================
console.log('\n── Python Modes ──');

test('preflight runs without crash', () => {
  const d = tmp('preflight');
  const r = run(CLI, 'preflight', { cwd: d, timeout: 30000 });
  assertContains(r.stdout, 'PREFLIGHT');
});

test('report runs full doctor flow without crash', () => {
  const d = tmp('report');
  const r = run(CLI, 'report', { cwd: d, timeout: 60000 });
  assertContains(r.stdout, 'ShellX: Running doctor');
  assertContains(r.stdout, 'BLACKBOX');
});

test('doctor runs without crash', () => {
  const d = tmp('doctor');
  const r = run(CLI, 'doctor', { cwd: d, timeout: 60000 });
  assertContains(r.stdout, 'BLACKBOX');
});

// ===========================
// SECTION 8: Edge Cases
// ===========================
console.log('\n── Edge Cases ──');

test('unknown command shows help hint', () => {
  const r = run(CLI, 'some-nonsense');
  assertContains(r.stdout, 'Processing intent');
});

test('unknown flag exits gracefully', () => {
  const r = run(CLI, '--bogus-flag');
  if (r.code !== 0 && r.code !== 1) throw new Error(`Unexpected exit code: ${r.code}`);
});

test('empty args help handler', () => {
  const r = run(CLI, '');
  assertContains(r.stdout, 'USAGE');
});

// ===========================
// SECTION 9: Package Integrity
// ===========================
console.log('\n── Package Integrity ──');

test('package.json has required fields', () => {
  const p = JSON.parse(fs.readFileSync(PKG, 'utf8'));
  if (!p.name) throw new Error('Missing name');
  if (!p.version) throw new Error('Missing version');
  if (!p.description) throw new Error('Missing description');
  if (!p.bin) throw new Error('Missing bin');
  if (!p.license) throw new Error('Missing license');
  if (!p.repository) throw new Error('Missing repository');
});

test('package.json has all 3 bins', () => {
  const p = JSON.parse(fs.readFileSync(PKG, 'utf8'));
  if (!p.bin.shellx) throw new Error('Missing shellx bin');
  if (!p.bin['shellx-dev-cli']) throw new Error('Missing shellx-dev-cli bin');
  if (!p.bin['shellx-superman']) throw new Error('Missing shellx-superman bin');
});

test('all bin files exist on disk', () => {
  const p = JSON.parse(fs.readFileSync(PKG, 'utf8'));
  for (const [name, binPath] of Object.entries(p.bin)) {
    const full = path.join(__dirname, '..', binPath);
    if (!fs.existsSync(full)) throw new Error(`Bin file not found: ${binPath}`);
  }
});

test('package.json has zero dependencies', () => {
  const p = JSON.parse(fs.readFileSync(PKG, 'utf8'));
  if (p.dependencies && Object.keys(p.dependencies).length > 0) {
    throw new Error(`Has dependencies: ${Object.keys(p.dependencies).join(',')}`);
  }
});

test('package.json engines requires node >= 18', () => {
  const p = JSON.parse(fs.readFileSync(PKG, 'utf8'));
  if (!p.engines || !p.engines.node) throw new Error('Missing engines.node');
  if (!p.engines.node.includes('>=18')) throw new Error('Node version too low');
});

test('package.json has cross-platform os field', () => {
  const p = JSON.parse(fs.readFileSync(PKG, 'utf8'));
  if (!p.os || p.os.length < 3) throw new Error('Missing cross-platform os field');
});

test('npmignore exists and excludes git and node_modules', () => {
  const ni = fs.readFileSync(path.join(__dirname, '..', '.npmignore'), 'utf8');
  if (!ni.includes('.git')) throw new Error('.npmignore missing .git');
  if (!ni.includes('node_modules')) throw new Error('.npmignore missing node_modules');
});

test('gitignore exists', () => {
  const gi = path.join(__dirname, '..', '.gitignore');
  if (!fs.existsSync(gi)) throw new Error('.gitignore missing');
});

// ===========================
// SECTION 10: CLI Scripts
// ===========================
console.log('\n── Package Scripts ──');

test('npm run scripts exist', () => {
  const p = JSON.parse(fs.readFileSync(PKG, 'utf8'));
  if (!p.scripts) throw new Error('Missing scripts');
  const expected = ['preflight', 'doctor', 'launcher', 'report', 'lint', 'test', 'postinstall'];
  for (const s of expected) {
    if (!p.scripts[s]) throw new Error(`Missing script: ${s}`);
  }
});

// ===========================
// SUMMARY
// ===========================
console.log('\n═══════════════════════════════════════');
console.log(`  Results: ${pass} passed, ${fail} failed`);
console.log('═══════════════════════════════════════\n');

process.exit(fail > 0 ? 1 : 0);
