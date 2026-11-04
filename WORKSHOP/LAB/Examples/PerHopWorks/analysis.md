# Specification analysis — Per-Hop Works

Date: 2026-11-04. One cross-artifact analysis after task generation. The user explicitly requested
findings AND fixes; remediation is authorized. Original source contradictions identified during
specification/planning and corrections are retained here. No implementation completion is implied.

| ID | Severity | Location | Finding | Remediation | Status |
|---|---|---|---|---|---|
| C01 | HIGH | spec.md / plan.md / contracts/engine.md | Recycler loss missing from conservation. | One exclusive cause per terminal event, including recycler; timeout cannot pass. | Fixed |
| C02 | HIGH | spec.md checks / contracts/engine.md | Measured finite-trace loss equated to probability ordering. | Explain the distinction, preserve both threshold and measured checks, require nonzero cohorts. | Fixed |
| C03 | HIGH | plan.md simulation / contracts/engine.md | Congestion measurement window and drain bound absent. | Measure service bytes only in declared congestion interval, then bounded drain. | Fixed |
| C04 | HIGH | contracts/engine.md | Dropped-all and empty-population vacuous success. | Required delivery obligations, complete predictions, explicit missing-denominator failures. | Fixed |
| C05 | HIGH | contracts/engine.md | AQM max equality and floating accumulator ambiguous. | Depth before enqueue, forced drop at max, exact rational accumulator and reset rules. | Fixed |
| C06 | HIGH | contracts/engine.md | Invisible merger queues could bypass buffer limits. | Buffer owns queue; merger pulls; scheduler packet-fit and deficits specified. | Fixed |
| C07 | MEDIUM | contracts/engine.md / data-model.md | Re-marking could move packets out of loss denominators. | Immutable service class and stable AF ingress cohort identity. | Fixed |
| C08 | HIGH | constitution.md / plan.md | Image API key requirement superseded by explicit user instruction. | Constitution v1.1.0 names built-in ChatGPT image tool; no invented model ID. | Fixed by user direction |
| C09 | MEDIUM | spec.md / clarify.md | Demo entry versus earned progress unspecified. | User confirmed always-available Demo with gated campaign. | Fixed by user answer |
| C10 | MEDIUM | plan.md / contracts/engine.md | Pure engine versus localStorage I/O conflict. | Engine serializes/validates plain saves; main owns browser I/O. | Fixed |
| C11 | MEDIUM | spec.md / plan.md / .specify/feature.json | Generic Spec Kit paths and headings conflict with supplied example location. | One lowercase canonical feature, five loop headings, all paths example-relative. | Fixed |
| C12 | HIGH | plan.md seed fixtures | Pre-existing seed verification claimed without session evidence. | Label as supplied expectations pending independent RFC/hand/reference verification. | Fixed |
| C13 | MEDIUM | AGENTS.md | Generated context incorrectly prescribed pytest/ruff under src. | Replace with actual example directory and Node test command. | Fixed |
| C14 | HIGH | research.md / implementation-status.json | Installed Ralph plugin uses Claude stop hooks unavailable in this host. | Use directly executed bounded loop scopes with persistent evidence; do not claim automatic callback. | Host limitation disclosed |
| C15 | HIGH | research/BOOTSTRAP_REPORT.md | Live MCP/image results and human reviews do not yet exist. | Execute T001; do not mark any exit complete until real evidence and reviews exist. | Execution gate, pending |

## Coverage

| Requirement | Tasks |
|---|---|
| FR-001 | T018, T019, T020, T021, T022, T023, T028, T047, T048, T049, T050, T051, T052, T053 |
| FR-002 | T006, T007, T008, T019, T020, T021, T025, T027, T038, T041 |
| FR-003 | T006, T013, T026, T027, T054 |
| FR-004 | T007, T012, T013, T014 |
| FR-005 | T012, T015, T029, T056 |
| FR-006 | T015, T025, T028, T029, T056 |
| FR-007 | T016, T024, T030, T066 |
| FR-008 | T014, T029, T042 |
| FR-009 | T003, T025, T033, T034, T035, T036, T037, T038, T040, T041, T042, T043, T055 |
| FR-010 | T006, T007, T009, T010, T011, T014, T046, T047, T048, T049, T050, T051, T052, T053, T054, T055 |
| FR-011 | T063, T064 |
| FR-012 | T026, T031, T033, T042, T058, T062, T064, T065 |
| FR-013 | T004, T005, T033, T034, T035, T036, T037, T038, T039, T057, T060, T061, T062, T067 |
| FR-014 | T002, T003, T024, T066, T068 |
| FR-015 | T018, T019, T020, T021, T022, T023, T031, T046, T047, T048, T049, T050, T051, T052, T053, T058 |
| FR-016 | T004, T010, T028, T057, T067 |
| FR-017 | T001, T017, T032, T045, T059, T069 |
| SC-001 | T018, T031, T032, T046, T058, T069 |
| SC-002 | T043, T044, T058, T065, T069 |
| SC-003 | T005, T039, T045, T057, T060, T061, T062, T067, T069 |
| SC-004 | T039, T040, T041, T044, T045, T058, T069 |
| SC-005 | T002, T064, T068, T069 |
| SC-006 | T007, T014, T017, T043, T069 |
| SC-007 | T012, T017, T024, T030, T066, T069 |

## Findings and fixes validation

- 17 functional requirements and 7 measurable outcomes; 69 tasks, all mapped.
- 100% requirement/outcome task coverage; 0 unmapped tasks.
- Exactly five task headings and counts: 17, 15, 13, 14, 10.
- All 15 grader check IDs retained; all 12 levels and 17 model contracts covered.
- No unresolved product clarification, no duplicated authoritative spec, no unexplained constitution placeholders.
- Constitution copies match byte-for-byte; v1.1.0 records the explicit image-provider amendment.
- No unresolved critical design violation. Tool execution, performance and actual human review remain gates.
- Human approval has not occurred; none is fabricated. No game tests have run yet.

Next action: execute speckit-implement for Loop 1 only. A failed mandatory tool gate stops its
remaining tasks and prevents Loops 2–5. Record live output and remediation needs rather than claiming
that successful package installation proves a tool can perform the required operation.

## Implementation findings and fixes — 2026-11-04

This adds execution evidence to the original analysis; it is not a second Spec Kit analyze pass.

| Finding | Correction | Evidence |
|---|---|---|
| RFC MCP upstream HTML parsing returned no sections and numeric 4.3 could match 1.4.3. | Documented compatibility repair; validate returned section number and use exact title lookup. | `research/BOOTSTRAP_REPORT.md`, `tools/rfc-mcp/README.md`, genuine MCP response artifacts. |
| RFC 8622 changes the low-priority class in the original nine-class Example 3. | Recorded the current LE update in the fact ledger; historical CS1 versus current LE presentation remains a content clarification before L12 authoring. | `research/rfc/rfc8622-mcp.json`, F-0035, `clarify.md`. |
| Dock locking also prevented repairing its outgoing connection. | Lock position/configuration; allow connection edits in build levels. | `tests/editor.test.js`, keyboard browser rehearsal. |
| A grade appeared before visual playback finished. | Show current snapshot counters during playback and reveal the single grader's report at the end. | `main.js`, `research/browser/keyboard-3d.json`. |
| Machine rotation initially affected its appearance without constraining belt endpoints. | Shared rotated input/output directions now constrain path routing; duplicate inputs and mismatched ports fail validation. | `tests/factory.test.js`; all reference/wrong tests remain green. |
| Blender look captures included the unrelated default cube, hiding the target. | Isolate only the generated collection for each actual `look` call and restore prior visibility afterward. | `scripts/build_models_mcp.py`, all 17 MCP look records and review sheets. |
| Hall crossbeams concealed parts of the playable floor. | Keep perimeter framing and an open roof; regenerate/review the hall through MCP. | `assets/src/blender/common.py`, `research/assets/phw_hall-look.json`. |
| The first corner belt's rollers overlapped. | Revise the radial roller positions inside the tile and regenerate/review through MCP. | `research/assets/phw_belt_corner-angles-0.png`. |
| WebGL fallback notice disappeared when reopening the work order. | Persist the fallback explanation across shell renders while retaining the same layout and state. | `research/browser/recovery.json`. |
| Playback used an implicit 70 ms constant. | Introductory work orders explicitly declare tick_ms=70; playback uses the declared tick duration. Meter arithmetic remains based on each level's own tick_ms. | `main.js`, `data/levels.json`, pure engine tests. |

Current evidence: 51 Node tests pass; five levels complete by keyboard in both views; view switches
preserve identical grade objects; 400-crate 1080p rendering uses 71 calls with ~16.7 ms median frame
interval on Apple M4 Pro, with and without shadows. The final game is not complete. Model human
approval is pending; Loops 4 and 5 have not started. Final twelve-level, content and art audits remain.

## Implementation audit findings and fixes — Loop 5

- **A018, fixed:** Repeated 3D/SVG switching leaked WebGL contexts. Reuse the probe context, release
  disposed contexts, and assert a real 3D renderer in every level rehearsal.
- **A019, fixed:** Saved draft validation initially used the wrong property name. It now validates
  the actual `links` schema, with a valid-draft round-trip test and browser persistence checks.
- **A020, fixed:** Invalid saves could be overwritten during startup. They are now preserved until
  the user chooses replacement; storage denial has a persistent session-only notice.
- **A021, fixed:** CS7 and RED source wording lost distinctions present in the RFCs. Final live MCP
  audit corrected F-0018/F-0032 and expanded F-0025's section references; see FINAL_FACT_AUDIT.md.
- **A022, fixed:** Two service classes shared the same pattern. Historical Low Priority now uses a
  chevron; dark crates use light pattern ink. A legend describes both color and pattern.
- **A023, fixed:** Supporting text failed contrast checks. Darkened text and increased key labels;
  automated WCAG checks are rerun after the changes.
- **A024, clarified:** Demo follows the actual L12 packet order (sort, mark, meter, queue, merger),
  rather than inventing a tank-before-marker event. Camera choreography never changes the result.
- **A025, refined by owner:** A plain-language illustrated welcome and replayable introduction now
  precede the first work order. A guided first edit lowers the initial learning burden.
