# Loop 3 — 3D factory and Blender assets

Status: PASS. The owner approved all 17 models on 2026-11-04.
Date: 2026-11-04. Scope: T033–T045, one speckit-implement invocation for this loop.

## Asset evidence

All 17 original models were generated through `execute_blender_code`, inspected through actual
`look(mode="angles")` calls, and saved as individual Python recipes, .blend sources and local GLBs.
The common procedural geometry helper is also retained. Build and look responses are under
`research/assets/`; the complete provenance and hashes are in `assets/manifest.json`.

- Total GLB payload: 658,064 bytes (limit 15 MB).
- Total model triangles: 6,280; every individual model is below its own budget.
- All required named animation nodes and eight crate sockets exist.
- GLBs contain no cameras, lights or texture payloads; transform scales are applied.
- Multi-angle review: [review page](../../tools/browser/asset-review.html). Human review status is
  pending for all 17 models, with no fabricated approver.

## Browser and rendering evidence

- `node --test tests/`: 51 passed, 0 failed, including model contracts and revised spatial port rules.
- `node tools/browser/keyboard.mjs 3d`: all L01–L05 passed using only keyboard gameplay actions;
  each level switched to SVG and back with deep-equal grade objects. No page/console errors.
- `node tools/browser/recovery.mjs`: automatic WebGL2-unavailable fallback preserves the work order;
  keyboard rotation, deletion/undo and placement/palette-error/undo verified.
- `node tools/browser/follow.mjs`: selected-crate camera and return to build camera preserve the tick
  and grade; switching to schematic also preserves the paused tick.
- 400-crate, 1920×1080 stress fixture on the actual L04 factory: 71 draw calls, median frame interval
  16.7 ms, 95th percentile 16.8 ms over approximately 10 seconds, both shadows off and on.
  Recorded hardware: MacBook Pro Mac16,7, Apple M4 Pro, integrated 20-core GPU, 48 GB RAM.
  Browser: headless Chrome 156. Performance is measured on this machine, not inferred for other GPUs.
  See `research/browser/benchmark.json` and `benchmark-shadows.json`.

The stress fixture is a developer-only renderer test with 400 synthetic crate positions, not a
campaign level and not an alternative simulation. Runtime 3D/SVG views consume the same engine
snapshots. Local GLTFLoader, instanced belts/crates/lid lights, MapControls, follow camera, machine
animations, class patterns, and reduced-motion handling are implemented.

## Exit checklist

- [X] L01–L05 keyboard-playable in 3D.
- [X] Grader results identical when changing between 3D and schematic.
- [X] Model, texture, draw-call and measured frame budgets met.
- [X] Every model has an actual human approver in `assets/manifest.json`.

Loop 4 remains not started until the final item passes. The pending review is required by the user's
plan, which says “every model in manifest.json with an approver.”

Owner approval: “all models all things approved”. Exact message is retained in assets/manifest.json. Loop 4 is released. The earlier pending text records the prior state.
