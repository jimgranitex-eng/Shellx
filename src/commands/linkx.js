import { existsSync, readFileSync, writeFileSync } from 'fs';
import { join } from 'path';

const linkxPath = join(process.cwd(), '.linkx', 'core.json');

function ensureLinkX() {
  if (!existsSync(linkxPath)) {
    console.error('\n❌ LinkX not initialized. Run: shellx init');
    process.exitCode = 1;
    return null;
  }
  return JSON.parse(readFileSync(linkxPath, 'utf8'));
}

function saveLinkX(data) {
  writeFileSync(linkxPath, JSON.stringify(data, null, 2));
}

export const linkxCommand = {
  init() {
    console.log('\n🧠 Initializing LinkX...');
    const linkx = ensureLinkX();
    if (!linkx) return;
    linkx.projectState.status = 'active';
    linkx.projectState.lastScanned = new Date().toISOString();
    saveLinkX(linkx);
    console.log('✅ LinkX initialized');
    console.log(`📍 Location: ${linkxPath}\n`);
  },

  scan() {
    console.log('\n📊 Scanning project with LinkX...');
    const linkx = ensureLinkX();
    if (!linkx) return;
    linkx.projectState.lastScanned = new Date().toISOString();
    linkx.projectState.filesTracked = Math.floor(Math.random() * 100) + 10; // Mock
    saveLinkX(linkx);
    console.log(`✅ Scan complete`);
    console.log(`📁 Files tracked: ${linkx.projectState.filesTracked}`);
    console.log(`🕐 Last scanned: ${linkx.projectState.lastScanned}\n`);
  },

  show() {
    console.log('\n📖 LinkX Memory State:');
    const linkx = ensureLinkX();
    if (!linkx) return;
    console.log('\nCore Information:');
    console.log(`  Version: ${linkx.version}`);
    console.log(`  Created: ${linkx.created}`);
    console.log(`  Goal: ${linkx.projectGoal}`);
    console.log('\nProject State:');
    console.log(`  Status: ${linkx.projectState.status}`);
    console.log(`  Files Tracked: ${linkx.projectState.filesTracked}`);
    console.log(`  Last Scanned: ${linkx.projectState.lastScanned || 'never'}`);
    console.log('\nStones:');
    console.log(`  Count: ${linkx.stones.length}`);
    if (linkx.stones.length > 0) {
      linkx.stones.slice(-3).forEach((stone) => {
        console.log(`    - ${stone.id}: ${stone.description}`);
      });
    }
    console.log();
  },

  timeline() {
    console.log('\n⏳ LinkX Timeline:');
    const linkx = ensureLinkX();
    if (!linkx) return;
    console.log(`\nIntent History (${linkx.intentHistory.length} entries):`);
    if (linkx.intentHistory.length === 0) {
      console.log('  (no history yet)');
    } else {
      linkx.intentHistory.slice(-5).forEach((entry) => {
        console.log(`  [${entry.timestamp}] ${entry.intent}`);
      });
    }
    console.log(`\nStones Created (${linkx.stones.length}):`);
    if (linkx.stones.length === 0) {
      console.log('  (no stones yet)');
    } else {
      linkx.stones.slice(-5).forEach((stone) => {
        console.log(`  [${stone.created}] ${stone.id}: ${stone.description}`);
      });
    }
    console.log();
  },
};
