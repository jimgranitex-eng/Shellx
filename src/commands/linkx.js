import { existsSync, readFileSync, readdirSync, statSync, writeFileSync } from 'fs';
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

function countTrackedFiles(dir) {
  const ignored = new Set(['.git', 'node_modules', '.linkx', '.reports', '.stones']);
  let total = 0;
  let entries = [];

  try {
    entries = readdirSync(dir);
  } catch (error) {
    console.warn(`⚠️ Skipping unreadable directory: ${dir}`);
    return total;
  }

  for (const entry of entries) {
    if (ignored.has(entry)) continue;
    const fullPath = join(dir, entry);
    let stats;
    try {
      stats = statSync(fullPath);
    } catch (error) {
      console.warn(`⚠️ Skipping inaccessible path: ${fullPath}`);
      continue;
    }

    if (stats.isDirectory()) {
      total += countTrackedFiles(fullPath);
    } else if (stats.isFile()) {
      total += 1;
    }
  }

  return total;
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
    linkx.projectState.filesTracked = countTrackedFiles(process.cwd());
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
