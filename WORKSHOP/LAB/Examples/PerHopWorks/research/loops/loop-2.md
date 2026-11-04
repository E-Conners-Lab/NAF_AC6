# Loop 2 — Playable schematic slice

Status: PASS, 2026-11-04. Scope: T018–T032, one continued speckit-implement invocation.

- `node --test tests/`: 49 passed, 0 failed. Includes all five real reference factories and all five intended wrong-check/diagnostic assertions. Prediction answers are computed by the engine inside the harness.
- `node tools/browser/keyboard.mjs`: fresh Chrome session at 1920×1080, only Tab/Enter/arrows/text keys for gameplay. L01 3/3, L02 3/3, L03 3/3, L04 3/3, L05 4/4. See [machine-readable evidence](../browser/keyboard.json) and per-level screenshots in `research/browser/`.
- The incorrect initial L01 failed without unlocking L02. The rehearsal corrected the actual form, completed each level in order, sought a Crate Trace event, reloaded, and verified all five earned unlocks and drafts persisted.
- Browser console and page errors: none. Static server is the only runtime dependency. Browser automation dependencies are development-only in `tools/browser/`.
- Review fixes: dock positions/configuration remain locked while outgoing connections can be repaired; fixed prediction factories reject altered layouts; selection does not invalidate a run; configuration edits do invalidate it; final answers are revealed only when playback finishes; per-class crate patterns complement color; unavailable/invalid storage has a visible notice.
- Keyboard editor tests also cover locked docks, reconnection, undo, and read-only prediction factories.

All Loop 2 exit criteria pass. Human content review and 3D parity remain explicit later-loop gates; this intermediate result is not the final game.
