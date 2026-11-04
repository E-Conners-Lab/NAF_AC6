// Explicit entry supports `node --test tests/` across Node directory-discovery behavior.
import { readdir } from 'node:fs/promises';
for (const file of (await readdir(new URL('.', import.meta.url))).filter(name=>name.endsWith('.test.js')).sort()) {
  await import(new URL(file, import.meta.url));
}
