// Entry for "Meme Sprint 3: AI Agent Goes Rogue".
// The committed picture is the whole entry: the grader runs this with no network
// and no third-party packages, so only the Node standard library is used here.
// The illustration is rendered at authoring time by gen_meme.py and committed.

import { copyFileSync, mkdirSync, readFileSync, statSync } from 'node:fs';
import { join } from 'node:path';

const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const picture = new URL('./entry.png', import.meta.url);
const target = join(outputDir, 'entry.png');

mkdirSync(outputDir, { recursive: true });
copyFileSync(picture, target);

const written = statSync(target);
if (written.size < 1024 || written.size > 1048576) {
  throw new Error('meme is outside the 1 MiB gate');
}

// The gate also requires exactly 1024 by 1024 pixels. Read the IHDR fields
// straight out of the copy so a bad rebuild fails here instead of at grading.
const head = readFileSync(target).subarray(0, 24);
if (head.subarray(1, 4).toString('latin1') !== 'PNG') {
  throw new Error('the committed picture is not a PNG');
}
if (head.readUInt32BE(16) !== 1024 || head.readUInt32BE(20) !== 1024) {
  throw new Error('the committed picture is not 1024 by 1024');
}

console.log('meme written:', written.size, 'bytes,', head.readUInt32BE(16), 'x', head.readUInt32BE(20));
