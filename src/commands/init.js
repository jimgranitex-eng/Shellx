import { existsSync, mkdirSync, writeFileSync } from 'fs';
import { join } from 'path';

export async function initCommand() {
  console.log('\n⚡ Initializing ShellX...');

  const cwd = process.cwd();
  const linkxDir = join(cwd, '.linkx');
  const reportsDir = join(cwd, '.reports');
  const stonesDir = join(cwd, '.stones');

  // Create directories
  if (!existsSync(linkxDir)) {
    mkdirSync(linkxDir, { recursive: true });
    console.log(`✅ Created ${linkxDir}`);
  }

  if (!existsSync(reportsDir)) {
    mkdirSync(reportsDir, { recursive: true });
    console.log(`✅ Created ${reportsDir}`);
  }

  if (!existsSync(stonesDir)) {
    mkdirSync(stonesDir, { recursive: true });
    console.log(`✅ Created ${stonesDir}`);
  }

  // Initialize LinkX core file
  const linkxCore = join(linkxDir, 'core.json');
  if (!existsSync(linkxCore)) {
    const linkxData = {
      version: '1.0.0',
      created: new Date().toISOString(),
      projectGoal: 'Define your project goal',
      projectConstraints: [],
      projectPreferences: {},
      projectState: {
        status: 'initialized',
        lastScanned: null,
        filesTracked: 0,
      },
      intentHistory: [],
      contextModel: {},
      stones: [],
    };
    writeFileSync(linkxCore, JSON.stringify(linkxData, null, 2));
    console.log(`✅ Created ${linkxCore}`);
  }

  console.log('\n🎯 ShellX initialized successfully!');
  console.log('Next steps:');
  console.log('  1. Run: shellx linkx init');
  console.log('  2. Run: shellx --xx "your intent here"');
  console.log('  3. Run: shellx verify\n');
}
