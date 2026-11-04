# Tasks — Per-Hop Works

Single feature: `spec.md`. Prerequisites: `plan.md`, `research.md`, `data-model.md`, `contracts/`.
All paths are relative to this example except `.mcp.json` (repository root). The user’s five-loop
structure overrides the generic story-phase template. Every task names its loop and requirements.
No implementation task is complete without evidence; human approvals cannot be inferred.

Execution: invoke speckit-implement for Loop 1 only, then Loop 2 only, through Loop 5. Within a loop
repeat implement → verify → fix until its exit passes. Record each loop in `implementation-status.json`
and `research/loops/loop-N.md`. Stop at a failed live gate or pending required human review.
Exactly five loop scopes exist; a stopped invocation resumes its current loop instead of skipping it.

Dependencies: Loop 1 → Loop 2 (US1) → Loop 3 (US2) → Loop 4 (US3) → Loop 5 (US4).
US4 startup infrastructure starts in Loop 1; its complete presentation experience is delivered in Loop 5.
Within each loop follow listed order; tests precede matching engine implementation. Independent reads
and tests may run concurrently; shared-file mutations stay sequential. No task is marked [P] because
these steps include evidence and shared-data dependencies. The schematic slice is an intermediate
checkpoint, not the requested final delivery. Runtime teaching answers never come from fixtures.

## Loop 1 — Foundations

- [X] T001 Loop 1: Install/configure genuine RFC and Blender MCP tools in `.mcp.json`; record live get_rfc/title and section/AF41 checks, Blender addon/GLB export/delete, built-in image generation/decode/delete, and toolchain checks in `research/BOOTSTRAP_REPORT.md`; halt on any failure. (FR-017)
- [X] T002 Loop 1: Create skeleton, ES-module `package.json`, project `.gitignore`, and localhost launcher `start.py`; document `README.md` startup and errors. (FR-014 SC-005)
- [X] T003 Loop 1: Vendor a pinned Three.js release, GLTFLoader, MapControls and transitive imports with license into `vendor/three/`; record `VERSION` and hashes. (FR-009 FR-014)
- [X] T004 Loop 1: Fetch all ten Tier-1 RFC text copies into `research/rfc/`; verify statuses including 2598/5865/8622 and log every MCP call in `research/VERIFICATION.md`. (FR-013 FR-016)
- [X] T005 Loop 1: Inventory every claim for all twelve levels; verify each via RFC MCP before authoring `data/facts.json`; include briefing, hint, machine and diagnostic facts. (FR-013 SC-003)
- [X] T006 Loop 1: Author audited `data/codepoints.json`, `data/profiles.json`, `data/machines.json`; include ports/config schemas, sources, facts and supported legacy sorter mode. (FR-002 FR-003 FR-010)
- [X] T007 Loop 1: Write seed and boundary fixtures first in `tests/dsfield.test.js`, `tests/meters.test.js`, `tests/aqm.test.js`, `tests/scheduler.test.js`; record failing-before-implementation results in `research/loops/loop-1.md`. (FR-002 FR-004 FR-010 SC-006)
- [X] T008 Loop 1: Implement octet/codepoint/precedence validation and round trips in `engine/dsfield.js`; test all 256 octets, 64 DSCPs and ECN preservation. (FR-002)
- [X] T009 Loop 1: Implement single token bucket, literal srTCM/trTCM aware/blind logic and exact refill clocks in `engine/meters.js`; include full/empty/overflow/same-tick boundary cases. (FR-010)
- [X] T010 Loop 1: Implement threshold validation and exact deterministic accumulators in `engine/aqm.js`; test equality, reset and exactly one invalid fixture inequality. (FR-010 FR-016)
- [X] T011 Loop 1: Implement strict priority/DRR in `engine/scheduler.js`; verify mixed sizes, persistent deficits, cursor, empty queues and capacity fit. (FR-010)
- [X] T012 Loop 1: Write graph/event/conservation/grader negative tests in `tests/factory.test.js`, `tests/sim.test.js`, `tests/grader.test.js` before modules; include all 15 check IDs and anti-vacuous cases. (FR-004 FR-005 SC-007)
- [X] T013 Loop 1: Implement spatial ports, stable compilation and designed validation errors in `engine/factory.js`; respect palette, docks, overlaps and cycles. (FR-003 FR-004)
- [X] T014 Loop 1: Implement every machine and deterministic run lifecycle in `engine/machines.js` and `engine/sim.js`; exact terminal events, measurement windows, drain failure and snapshots. (FR-004 FR-008 FR-010 SC-006)
- [X] T015 Loop 1: Implement every check and static/measured diagnostic API in `engine/grader.js` and `engine/diagnostics.js`; validate unknown checks, required deliveries and positive cohorts. (FR-005 FR-006)
- [X] T016 Loop 1: Implement pure save schema validation/serialization in `engine/state.js` with `tests/state.test.js`; no browser globals in engine. (FR-007)
- [X] T017 Loop 1: Exit: prove all live gates PASS, `node --test tests/` green, every fact has matching evidence and all 15 grader checks have pass/fail coverage in `research/loops/loop-1.md`; only then release Loop 2. (FR-017 SC-006 SC-007)

The final task is this loop’s exit checklist; every clause must pass with linked evidence.

## Loop 2 — Playable schematic slice

- [X] T018 [US1] Loop 2: Write data/level integration harness in `tests/levels.test.js` and schema checks in `tests/data.test.js`; compute reference predictions in tests, never store answers. (FR-001 FR-015 SC-001)
- [X] T019 [US1] Loop 2: Complete L01 Six Lights in `data/levels.json`, `data/traces/L01.json`, `data/solutions/L01*.json`; ECN routing case, layered hints and diagnostic-specific wrong fixture. (FR-001 FR-002 FR-015)
- [X] T020 [US1] Loop 2: Complete L02 Codepoint Forge in `data/levels.json`, `data/traces/L02.json`, `data/solutions/L02*.json`; bit-toggle targets and known-wrong marking. (FR-001 FR-002 FR-015)
- [X] T021 [US1] Loop 2: Complete L03 Old Sorter in `data/levels.json`, `data/traces/L03.json`, `data/solutions/L03*.json`; fixed legacy sorter, query descriptors, complete prediction grading. (FR-001 FR-002 FR-015)
- [X] T022 [US1] Loop 2: Complete L04 Who Goes Where in `data/levels.json`, `data/traces/L04.json`, `data/solutions/L04*.json`; all supplied applications and MF first-match diagnostics. (FR-001 FR-015)
- [X] T023 [US1] Loop 2: Complete L05 Trust Boundary in `data/levels.json`, `data/traces/L05.json`, `data/solutions/L05*.json`; trusted/untrusted CS6/CS7, re-mark/drop obligations and wrong fixtures. (FR-001 FR-015)
- [X] T024 [US1] Loop 2: Build semantic shell, routing, resource loading and explicit failure states in `index.html`, `style.css`, `main.js`; preserve draft on errors. (FR-007 FR-014 SC-007)
- [X] T025 [US1] Loop 2: Render data-driven SVG floor, patterned crates and 6+2 lid ticks in `render/schematic.js`; show compiler/grader culprits and selection. (FR-002 FR-006 FR-009)
- [X] T026 [US1] Loop 2: Implement keyboard spatial editing, palette counts, rotating ports, connection, locked docks, delete/undo and focus in `ui/editor.js`. (FR-003 FR-012)
- [X] T027 [US1] Loop 2: Implement validated machine forms, typed DSCP rules and DSCP bit toggles in `ui/inspector.js`; preserve ECN and invalidate prior grades on edit. (FR-002 FR-003)
- [X] T028 [US1] Loop 2: Create teaching SVG briefings, work orders, captured predictions, hints and retry/debrief in `ui/views/briefing.js`, `ui/views/workorder.js`, `ui/views/debrief.js`. (FR-001 FR-006 FR-016)
- [X] T029 [US1] Loop 2: Add 0.25×–8× playback, pause/step in `main.js`; render checks/metrics from grader in `ui/dashboard.js` and complete event replay in `ui/crateTrace.js`. (FR-005 FR-006 FR-008)
- [X] T030 [US1] Loop 2: Wire browser storage through `main.js` using pure engine save validation; handle denial/corruption/version mismatch and earned prerequisite unlocks. (FR-007 SC-007)
- [X] T031 [US1] Loop 2: Record keyboard-only L01–L05 completion, reference/wrong integration results and retry persistence in `research/loops/loop-2.md`. (FR-012 FR-015 SC-001)
- [X] T032 Loop 2: Exit: L01–L05 complete keyboard-only in SVG; all references pass and every known-wrong fixture fails intended check/diagnostic, recorded in `research/loops/loop-2.md`; release Loop 3. (FR-017 SC-001)

The final task is this loop’s exit checklist; every clause must pass with linked evidence.

## Loop 3 — 3D factory and Blender assets

- [X] T033 [US2] Loop 3: Finalize `assets/style-guide.md` before production art: Okabe–Ito colors plus unique patterns, silhouettes, roughness, emissive rules and no glyphs. (FR-009 FR-012 FR-013)
- [X] T034 [US2] Loop 3: Through Blender MCP create `assets/src/blender/phw_floor_tile.py`, `phw_belt_straight.py`, `phw_belt_corner.py`; save matching .blend/GLB, review angles and manifest records. (FR-009 FR-013)
- [X] T035 [US2] Loop 3: Through Blender MCP create `assets/src/blender/phw_buffer_belt.py`, `phw_sorter.py`, `phw_paint_booth.py`; preserve all named animated nodes and triangle budgets; save/review .blend/GLB. (FR-009 FR-013)
- [X] T036 [US2] Loop 3: Through Blender MCP create `assets/src/blender/phw_tank_single.py`, `phw_tank_cascade.py`, `phw_tank_twin.py`; named water/spout nodes, transforms, saved .blend/GLB and angle reviews. (FR-009 FR-013)
- [X] T037 [US2] Loop 3: Through Blender MCP create `assets/src/blender/phw_recycler.py`, `phw_priority_merger.py`, `phw_dock_in.py`, `phw_dock_out.py`; named hatch/gates/doors, saved .blend/GLB and reviews. (FR-009 FR-013)
- [X] T038 [US2] Loop 3: Through Blender MCP create `assets/src/blender/phw_crate_s.py`, `phw_crate_m.py`, `phw_crate_l.py`, `phw_hall.py`; all eight bit socket empties, budgets, saved .blend/GLB and reviews. (FR-002 FR-009 FR-013)
- [X] T039 [US2] Loop 3: Verify all 17 model budgets, animated nodes, +Y up/meters/origins/applied transforms and no lights/cameras in `tests/assets.test.js`; store provenance and actual human approvals in `assets/manifest.json`. (FR-013 SC-003 SC-004)
- [X] T040 [US2] Loop 3: Implement GLTFLoader factory, lighting/shadow toggle and snapshot-driven machine transforms in `render/scene3d.js`; handle load/context loss and dispose resources. (FR-009 SC-004)
- [X] T041 [US2] Loop 3: Implement three crate-size InstancedMeshes and instanced separated 6+2 lid lights using setColorAt in `render/instancing.js`; interpolate positions independently of engine. (FR-002 FR-009 SC-004)
- [X] T042 [US2] Loop 3: Implement MapControls build camera, follow-crate camera and reduced-motion visual effects in `render/cameras.js` and `render/fx.js`. (FR-008 FR-009 FR-012)
- [X] T043 [US2] Loop 3: Wire 3D/SVG toggle and automatic WebGL2 fallback in `main.js`; preserve tick, layout, selected crate and grader result. (FR-009 SC-002 SC-006)
- [X] T044 [US2] Loop 3: Measure 1080p/400-crate sustained performance and render parity for L01–L05; record hardware, browser, timings/draw calls in `research/loops/loop-3.md`. (SC-002 SC-004)
- [X] T045 Loop 3: Exit: L01–L05 keyboard-playable in 3D with SVG-identical grades, all budgets met and every model approved in `assets/manifest.json`; record in `research/loops/loop-3.md` before Loop 4. (FR-017 SC-003 SC-004)

The final task is this loop’s exit checklist; every clause must pass with linked evidence.

## Loop 4 — Metering, queuing and scheduling content

- [X] T046 [US3] Loop 4: Extend `tests/levels.test.js` with two-part meter progression, static bypass paths, measured starvation and AF cohort loss cases before data/UI wiring. (FR-010 FR-015 SC-001)
- [X] T047 [US3] Loop 4: Complete L06 Water Tower in `data/levels.json`, `data/traces/L06.json`, `data/solutions/L06*.json`; predict/build parts, contractual EF and flood excess diagnostics. (FR-001 FR-010 FR-015)
- [X] T048 [US3] Loop 4: Complete L07 Cascade in `data/levels.json`, `data/traces/L07.json`, `data/solutions/L07*.json`; srTCM predictions and color-to-AF2x marking. (FR-001 FR-010 FR-015)
- [X] T049 [US3] Loop 4: Complete L08 Twin Towers in `data/levels.json`, `data/traces/L08.json`, `data/solutions/L08*.json`; trusted-aware/untrusted-blind trTCM, predictions and AF4x marking. (FR-001 FR-010 FR-015)
- [X] T050 [US3] Loop 4: Complete L09 Express Lane in `data/levels.json`, `data/traces/L09.json`, `data/solutions/L09*.json`; EF flood, policing, bounded delay and congestion-window share. (FR-001 FR-010 FR-015)
- [X] T051 [US3] Loop 4: Complete L10 Shares in `data/levels.json`, `data/traces/L10.json`, `data/solutions/L10*.json`; DRR byte shares and dedicated positive DF queue. (FR-001 FR-010 FR-015)
- [X] T052 [US3] Loop 4: Complete L11 Spillway in `data/levels.json`, `data/traces/L11.json`, `data/solutions/L11*.json`; ordered thresholds, nonempty loss cohorts and all prohibited AQM classes. (FR-001 FR-010 FR-015)
- [X] T053 [US3] Loop 4: Complete L12 Rush Hour in `data/levels.json`, `data/traces/L12.json`, `data/solutions/L12*.json`; Example 3 nine classes and every applicable check under congestion. (FR-001 FR-010 FR-015)
- [X] T054 [US3] Loop 4: Complete meter/mode, recycler, buffer/threshold and merger-weight forms in `ui/inspector.js`; explanatory state and parameters from data. (FR-003 FR-010)
- [X] T055 [US3] Loop 4: Bind all token levels, overflow spout, recycler hatch, queue fill/threshold markers and merger gates to snapshots in `render/scene3d.js` and `render/fx.js`. (FR-009 FR-010)
- [X] T056 [US3] Loop 4: Finish feasible-path/static and result-based diagnostics in `engine/diagnostics.js`; reject all-drop shortcuts and inspect harmed crates in `ui/dashboard.js`. (FR-005 FR-006)
- [X] T057 [US3] Loop 4: Incorporate the user-approved beginner orientation and guided first task; Audit all twelve briefings/hints/diagnostics and simplifications against `data/facts.json`; obtain actual human why_wrong reviews in `research/content-review.md`. (FR-013 FR-016 SC-003)
- [X] T058 [US3] Loop 4: Verify every level keyboard-only in both views, all reference/wrong tests and budgets during each trace in `research/loops/loop-4.md`. (FR-012 FR-015 SC-001 SC-002 SC-004)
- [X] T059 Loop 4: Exit: all twelve per-level definitions of done pass, including human content reviews, recorded in `research/loops/loop-4.md`; release Loop 5. (FR-017)

The final task is this loop’s exit checklist; every clause must pass with linked evidence.

## Loop 5 — Art, Demo mode and polish

- [X] T060 [US4] Loop 5: Save title prompt in `assets/prompts/title.json`; generate title key art through built-in ChatGPT image tool, inspect, convert to `assets/images/title.webp` and review under the owner’s continuing authorization before using as reference. (FR-013 SC-003)
- [X] T061 [US4] Loop 5: Generate three act cards, hall backdrop, three briefing plates, icon and loading screen through built-in image tool with approved title reference; save individual `assets/prompts/*.json`, `assets/images/*.webp` and manifest provenance/reviews. (FR-013 SC-003)
- [X] T062 [US4] Loop 5: Complete a plain-language splash introduction and replayable topic walkthrough; Validate no text/digits/glyph-like marks, <=2048px/400KB WebPs in `tests/assets.test.js`; assemble title/act/loading screens in `ui/views/briefing.js` and `style.css`. (FR-012 FR-013 SC-003)
- [X] T063 [US4] Loop 5: Author `data/demos/showcase.json` from verified L12 reference with lid-closeup, pipeline journey and factory pullback camera beats; no grading/progress side effects. (FR-011)
- [X] T064 [US4] Loop 5: Implement scripted flyover/seeking, always-available Demo entry and presenter controls in `ui/views/demo.js`, `render/cameras.js`, `main.js`; support reduced-motion cuts. (FR-011 FR-012 SC-005)
- [X] T065 [US4] Loop 5: Run full focus/order/contrast/pattern/reduced-motion audit and repair browser UI in `ui/`, `style.css` and render modules; record evidence in `research/accessibility.md`. (FR-012 SC-002)
- [X] T066 [US4] Loop 5: Finish loading/error/empty states, storage and asset failure recovery, offline runtime checks and launcher port/browse errors in `main.js` and `start.py`. (FR-007 FR-014 SC-007)
- [X] T067 Loop 5: Re-check every factual source through RFC MCP and verify matching records in `research/VERIFICATION.md` and `data/facts.json`; log corrections and rerun affected tests. (FR-013 FR-016 SC-003)
- [X] T068 [US4] Loop 5: Write final play/presenter/startup/testing/provenance instructions in `README.md`; verify one-command launch and full Demo from fresh progress at 1920×1080. (FR-014 SC-005)
- [X] T069 Loop 5: Exit: run all tests, twelve-level keyboard/parity checks, full budget audit, fact/asset/content human review, offline/error recovery and presenter rehearsal; record all global acceptance evidence in `research/loops/loop-5.md` before declaring complete. (FR-017 SC-001 SC-002 SC-003 SC-004 SC-005 SC-006 SC-007)

The final task is this loop’s exit checklist; every clause must pass with linked evidence.
