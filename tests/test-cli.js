const { execSync } = require('child_process');
const path = require('path');
const fs = require('fs');

const CLI = path.join(__dirname, '..', 'bin', 'shellx-dev-cli.js');
const tmpDir = fs.mkdtempSync(path.join(require('os').tmpdir(), 'shellx-test-'));
const originalCwd = process.cwd();

function run(args) {
  try {
    return execSync(`node ${CLI} ${args}`, { cwd: tmpDir, encoding: 'utf8', timeout: 15000 });
  } catch (e) {
    return e.stdout || e.message;
  }
}

let passed = 0;
let failed = 0;

function test(name, fn) {
  try {
    fn();
    console.log(`  ✅ ${name}`);
    passed++;
  } catch (e) {
    console.log(`  ❌ ${name}: ${e.message}`);
    failed++;
  }
}

console.log('\nShellX CLI Tests\n');

test('--help shows usage', () => {
  const out = run('--help');
  if (!out.includes('ShellX')) throw new Error('Help missing ShellX header');
});

test('linkx init creates goal file', () => {
  const out = run('linkx init');
  const goalFile = path.join(tmpDir, '.shellx', 'goal.json');
  if (!fs.existsSync(goalFile)) throw new Error('goal.json not created');
});

test('license status shows unlicensed', () => {
  const out = run('license status');
  if (out.includes('active')) throw new Error('Should show unlicensed');
});

test('ide list shows supported IDEs', () => {
  const out = run('ide list');
  if (!out.includes('VS Code')) throw new Error('Missing VS Code');
  if (!out.includes('PyCharm')) throw new Error('Missing PyCharm');
});

test('activate with invalid key shows error', () => {
  const out = run('activate INVALID-KEY');
  if (out.includes('success')) throw new Error('Should not succeed');
});

test('package.json has correct bins', () => {
  const pkg = require('../package.json');
  if (!pkg.bin.shellx) throw new Error('Missing shellx bin');
  if (!pkg.bin['shellx-superman']) throw new Error('Missing shellx-superman bin');
});

console.log(`\n${passed} passed, ${failed} failed\n`);

process.exit(failed > 0 ? 1 : 0);
