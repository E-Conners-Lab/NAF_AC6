# Implementation Plan: Per-Hop Works

**Branch**: `001-per-hop-works` | **Date**: 2026-11-04 | **Spec**: [spec.md](spec.md)

## Summary

Deliver the supplied twelve-level factory game within this example directory, using one spec and five
ordered implementation loops. Source plan content below is retained, with precise contracts recorded
in `contracts/engine.md`, `contracts/ui.md` and `data-model.md`. `tasks.md` is the execution authority.

## Technical Context

**Language/Version**: Browser JavaScript ES modules, HTML5, CSS; Node 20+ tests, Python 3.11+ serving.  
**Primary Dependencies**: Vendored, pinned Three.js; developer-only RFC MCP, Blender MCP, built-in ChatGPT image generation.  
**Storage**: Static JSON/GLB/WebP plus versioned localStorage saves.  
**Testing**: Node built-in runner, reference/known-wrong integration fixtures, browser keyboard/parity/performance evidence.  
**Target Platform**: Desktop browsers, WebGL2 with full SVG fallback, localhost HTTP.  
**Project Type**: Static educational browser game.  
**Performance Goals**: 60 fps at 1080p, 400 crates, at most 150 draw calls, GLB payload at most 15 MB.  
**Constraints**: No frameworks, bundler, CDN, backend, runtime AI, auth or external traffic.  
**Scale/Scope**: Twelve levels; 17 GLB models; one campaign and one ungraded showcase.

## Constitution Check

Design review: PASS. Deterministic engine, single grader, fact verification, tool provenance,
accessibility, local-only runtime and five gated loops are represented in tasks and contracts.
Execution readiness: NOT YET PASSED. Actual live tools, runtime tests, human asset reviews and
performance evidence must be established; design compliance is not evidence of implementation.

## Project Structure

All paths in the source plan's tree are relative to `WORKSHOP/LAB/Examples/PerHopWorks/`, not the
workshop repository root. Additional artifacts: `clarify.md`, `analysis.md`, `research.md`,
`data-model.md`, `quickstart.md`, `contracts/`, `tasks.md`, `implementation-status.json`, and loop
reports under `research/loops/`. The launcher will be `start.py`, run from any working directory.
Lowercase `constitution.md`, `spec.md` and `plan.md` are canonical; Spec Kit points here via
`.specify/feature.json`.

## Complexity Tracking

No constitution exception is approved. One feature and one deterministic engine serve both renderers.
No runtime package manager or framework is introduced.


## How this plan is executed
- `/speckit.tasks` MUST group every task under five headings, **Loop 1** through **Loop 5**,
  matching "Implementation loops" below. Each task names its loop.
- `/speckit.implement` is run **once per loop (five runs)**. Each loop ends with its exit checklist,
  and the next loop does not start until every exit criterion passes. The loops are the only place
  iteration happens; earlier Spec Kit steps are run once.

## Tech stack
- Vanilla HTML, CSS, and JavaScript (ES modules) only — no frameworks, no build tools, no bundler.
  Diffs stay small and reviewable.
- **Three.js** is the one rendering library, for the 3D factory floor. It is **vendored locally** in
  `/vendor/three/` (core module plus the `GLTFLoader` and `MapControls` addons), loaded through an
  import map, and pinned to one release recorded in `/vendor/three/VERSION`. No CDN at runtime.
- **SVG** for schematic mode, the dashboard, lid-light readouts, and every teaching diagram, all
  generated from data.
- Single entry point `index.html` with linked CSS and JS modules.
- **Served by a local static server**: `python3 -m http.server 8000`, then open
  `http://localhost:8000`. This is a deliberate deviation from double-clicking `index.html`:
  browsers block ES modules and GLB loading from `file://`.
- All game data in `/data/*.json` — structured, auditable, no logic inside.
- `localStorage` for save state. No backend, no auth.
- Engine tests run with Node's built-in runner (`node --test tests/`). Node is a dev tool only; the
  game itself needs nothing but a browser and the static server.
- Assets: GLB (glTF 2.0) models from **Blender via the Blender MCP**; WebP images from the
  **built-in ChatGPT image generation tool**.

## Architecture

### File structure
```
/
├── index.html
├── style.css
├── main.js                    # bootstraps game, routes views, owns the run loop
├── /engine                    # pure: no DOM, no three.js, no unseeded randomness
│   ├── dsfield.js             # octet ↔ DSCP/ECN, name ↔ codepoint, precedence view
│   ├── factory.js             # grid layout → validated datapath graph (compile + validate)
│   ├── machines.js            # per-tick behavior of every machine
│   ├── meters.js              # token bucket, srTCM (RFC 2697), trTCM (RFC 2698)
│   ├── aqm.js                 # threshold validation + deterministic drop spacing
│   ├── scheduler.js           # strict priority + deficit round robin
│   ├── sim.js                 # deterministic tick loop → snapshots, event log, metrics
│   ├── grader.js              # evaluateRun(level, graph, result) → checks  (single source of truth)
│   ├── diagnostics.js         # static + measured anti-pattern detectors → diagnostic ids
│   └── state.js               # progress, save/load
├── /render                    # display only; never decides correctness
│   ├── scene3d.js             # three.js floor driven by sim snapshots
│   ├── instancing.js          # crates and lid lights as InstancedMesh
│   ├── schematic.js           # SVG top-down view of the same snapshots
│   ├── cameras.js             # build cam, follow-crate cam, demo flyover
│   └── fx.js                  # water levels, sprays, drops; honors reduced motion
├── /ui
│   ├── editor.js              # grid cursor, place / rotate / delete / undo, palette counts
│   ├── inspector.js           # machine configuration panels (DOM forms)
│   ├── dashboard.js           # checks + per-class metrics
│   ├── crateTrace.js          # journey replay for a selected crate
│   └── /views                 # briefing.js, workorder.js, debrief.js, demo.js
├── /data
│   ├── levels.json            # all 12 levels
│   ├── codepoints.json        # DSCP names, values, sources
│   ├── profiles.json          # service class → DSCP mappings (v1: rfc4594 only)
│   ├── machines.json          # machine definitions, ports, config schema, RFC element
│   ├── facts.json             # the fact ledger
│   ├── /traces                # arrival traces per level
│   ├── /solutions             # reference solutions + known-wrong configs per level
│   └── /demos/showcase.json   # demo-mode camera beats + factory
├── /assets
│   ├── /models                # *.glb
│   ├── /images                # *.webp
│   ├── /src/blender           # one bpy script per model (+ .blend sources)
│   ├── /prompts               # one JSON prompt file per generated image
│   ├── style-guide.md
│   └── manifest.json          # provenance for every asset
├── /vendor/three
├── /research
│   ├── /rfc                   # local plain-text copies of Tier-1 RFCs
│   ├── VERIFICATION.md        # log of every RFC MCP verification call
│   └── BOOTSTRAP_REPORT.md    # tool gate results
└── /tests                     # dsfield, meters, aqm, scheduler, sim, grader, levels
```

### Simulation model (`engine/sim.js`)
- **Discrete ticks.** Each level sets `tick_ms`. Crate sizes are integer bytes. Rates are
  bytes per second, converted to tokens per tick with **integer fixed-point arithmetic**
  (milli-bytes) so there is no floating-point drift. Same input, same output, every time.
- **Order within a tick:** (1) arrivals at input docks in trace order, (2) machines processed in
  topological order of the compiled graph, (3) the Priority Merger dequeues up to the output dock's
  byte capacity for the tick, (4) metrics and snapshot recorded.
- **Plain belts** have a transit time in ticks equal to their tile length; FIFO; they never drop.
- **Buffer Belts** have a capacity in crates and tail-drop when full.
- **Spillway (AQM)** — declared simplifications: instantaneous queue depth (no averaging), and
  deterministic drop spacing. Between a DSCP's min and max thresholds the drop probability rises
  linearly to the level's `max_p`; each arrival adds that probability to a per-DSCP accumulator, and
  a crate is dropped when the accumulator reaches 1 (then 1 is subtracted). At or above the max threshold,
  every arriving crate of that DSCP is dropped, as RFC 4594 §4.3 describes.
- **Priority Merger:** the strict-priority input is served whenever non-empty; remaining capacity is
  shared by deficit round robin with quantum proportional to each input's weight.
- **Meters** follow RFC 2697 §3 and RFC 2698 §3 literally, including color-aware mode.
- **Output:** per class — offered, delivered, dropped by cause (policer, tail drop, AQM, recycler),
  loss percentage, queuing delay min / avg / max in ticks; plus a full per-crate event log used by
  Crate Trace and by tests.
- **Graph validation** (`factory.js`): every machine output connected, no cycles, palette counts
  respected, docks locked. Validation errors are a designed error state, not a crash.

### `codepoints.json` (one entry)
```json
{ "name": "AF41", "binary": "100010", "decimal": 34, "phb": "AF",
  "source": "RFC 2597; RFC 4594 §2.3 Figure 3", "fact": "F-0007" }
```

### `facts.json` (one entry)
```json
{
  "id": "F-0042",
  "claim": "For Multimedia Conferencing, the probability of loss of AF41 MUST NOT exceed AF42, which MUST NOT exceed AF43.",
  "source": "RFC 4594 §4.3",
  "rfc_status_checked": "RFC 4594 Informational; updated by RFC 5865 and RFC 8622 (neither changes this text)",
  "verified_with": "rfc MCP get_rfc_section(number=4594, section=4.3)",
  "verified_on": "YYYY-MM-DD"
}
```

### `levels.json` schema (one level)
```json
{
  "id": "L11",
  "act": 3,
  "title": "Spillway",
  "concept": "AQM drop precedence within one AF class",
  "prerequisites": ["L10"],
  "profile": "rfc4594",
  "type": "build",
  "briefing": {
    "title": "...", "explanation": "...", "example": "...",
    "simplifications": ["Queue depth is instantaneous, not averaged.",
                        "Drops are spaced deterministically, not randomly."],
    "facts": ["F-0042", "F-0043"]
  },
  "work_order": {
    "tick_ms": 1,
    "docks_in": [{ "id": "in1", "trusted": true }],
    "docks_out": [{ "id": "out1", "bytes_per_tick": 1500 }],
    "trace": "traces/L11.json",
    "palette": { "buffer_belt": 2, "spillway": 1, "priority_merger": 1, "sorter": 1, "belt": 30 },
    "locked": ["in1", "out1"],
    "bounds": { "max_p": 0.1 }
  },
  "checks": [
    { "id": "VALID" }, { "id": "CONSERVATION" },
    { "id": "NO-AQM-ON" },
    { "id": "RED-THRESHOLDS", "params": { "class": "AF4" } },
    { "id": "LOSS-ORDER", "params": { "class": "AF4" } }
  ],
  "diagnostics": {
    "thresholds-overlap": {
      "why_wrong": "AF43's max threshold sits above AF42's min, so AF42 starts dropping before AF43 is exhausted.",
      "concept_reinforced": "Higher drop precedence must be dropped first.",
      "source": "RFC 4594 §4.3"
    },
    "aqm-on-ef": {
      "why_wrong": "Voice (EF) is on a Spillway belt. RFC 4594 recommends against AQM for the Telephony service class; this fixed trace does not model sender feedback.",
      "concept_reinforced": "AQM suits traffic that responds to loss.",
      "source": "RFC 4594 §4.1, Figure 4"
    }
  },
  "hints": ["...", "...", "..."],
  "reference_solution": "solutions/L11.json",
  "known_wrong": [
    { "config": "solutions/L11-wrong-overlap.json", "must_fail": "RED-THRESHOLDS", "diagnostic": "thresholds-overlap" },
    { "config": "solutions/L11-wrong-ef-aqm.json",  "must_fail": "NO-AQM-ON",      "diagnostic": "aqm-on-ef" }
  ],
  "source": "RFC 4594 §1.4.2, §4.3, Figure 4; RFC 2597"
}
```
Predict levels add a `predictions` block (the questions the player answers before Run); the
correct answers are **computed by the engine**, never typed into data.

### Grader (`engine/grader.js`) and diagnostics
- `evaluateRun(level, graph, simResult) → { passed, checks: [{ id, passed, expected, actual,
  culprit, crates, diagnostic, source }] }` — a pure function implementing every check in spec.md.
- Diagnostics run twice: statically on the compiled graph (EF on a Spillway, priority input without
  a policer, untrusted dock reaching an output without a re-mark) and on measured results (loss
  order inverted, a class starved).
- The UI, 3D scene, and schematic only render grader output.

### Rendering (`render/`)
- **Scene:** factory hall on a grid, 1 tile = 1 m. Perspective camera with MapControls for building,
  a follow-crate camera, and a scripted spline flyover for Demo mode.
- **Crates:** an InstancedMesh per crate size, plus one InstancedMesh for lid lights (eight per
  crate, colored per bit with `setColorAt`). The two ECN lights are smaller and set apart by a gap.
- **Machines:** one GLB each. Animated parts are named nodes driven by sim snapshots (see the asset
  contract below).
- **Interpolation:** the sim runs at tick rate; the renderer interpolates crate positions between
  snapshots at 60 fps. Speed 0.25× to 8×, pause, and single-step.
- **Budgets:** 60 fps at 1920×1080 on integrated graphics with 400 crates in flight; at most 150
  draw calls; total GLB payload at most 15 MB; textures at most 1024².
- **Lighting:** hemisphere light plus one directional light with toggleable shadows. No
  post-processing in v1.
- **Schematic mode:** SVG top-down grid, crates as squares with six-plus-two bit ticks, full
  keyboard editing, identical state. Automatic fallback if WebGL2 is unavailable.

## Asset pipeline

### Style guide first (`assets/style-guide.md`)
Written before any asset is made: a colorblind-safe palette (Okabe–Ito based) for service classes
with a matching pattern per class; low-poly, flat-shaded PBR materials (roughness around 0.6);
emissive accents reserved for things that carry data (lid lights, water, active machine states);
silhouette rules so every machine is identifiable from the zoom-out demo shot; **no text, digits,
or glyph-like marks anywhere in art.**

### 3D models via Blender MCP
Server `mcp-for-blender` (tools include `execute_blender_code`, `look`, `get_scene_info`,
`get_addon_status`). Telemetry disabled with `DISABLE_TELEMETRY=true`. Blender must be open with the
"MCP for Blender" addon enabled; only one MCP server instance at a time.

| Asset | Triangle budget | Animated nodes (contract with `scene3d.js`) |
|---|---|---|
| `phw_floor_tile`, `phw_belt_straight`, `phw_belt_corner` | 300 each | belt texture scroll is done in three.js |
| `phw_buffer_belt` | 1,500 | `fill_marker`, `threshold_min`, `threshold_max` |
| `phw_sorter` | 4,000 | `flap` |
| `phw_paint_booth` | 4,000 | `nozzle`, `spray` |
| `phw_tank_single` | 3,000 | `water` (scaled on Y by token count) |
| `phw_tank_cascade` | 5,000 | `water_committed`, `water_excess`, `overflow_spout` |
| `phw_tank_twin` | 5,000 | `water_peak`, `water_committed` |
| `phw_recycler` | 3,000 | `hatch` |
| `phw_priority_merger` | 5,000 | `gate_priority`, `gate_weighted` |
| `phw_dock_in`, `phw_dock_out` | 3,000 each | `door` |
| `phw_crate_s`, `phw_crate_m`, `phw_crate_l` | 400 each | 8 empties `bit_7` … `bit_0` marking light sockets |
| `phw_hall` (shell + decor) | 20,000 | none |

Process for every model:
1. Write a procedural `bpy` script in `assets/src/blender/<asset>.py`.
2. Run it with `execute_blender_code`.
3. Review with `look` (multi-angle sheet) and fix.
4. Export GLB: +Y up, transforms applied, meters, origin at tile center on the floor, no cameras or
   lights.
5. Save the `.blend`, add a `manifest.json` entry, and get human approval.

`generate_3d` and third-party model imports are off by default; they may be used only with explicit
human approval and the license recorded. CC0 HDRIs from Poly Haven are allowed, with the license
recorded.

### 2D art via built-in ChatGPT image generation (user amendment)
- The user explicitly authorized the built-in ChatGPT image tool on 2026-11-04. No API key is required.
  Record the actual tool and any exposed model/version; never assert an unexposed model identity.
  A failed live generation still stops the gate; no raster substitutes are permitted.
- Images: title key art (16:9), three act cards, a factory-hall backdrop plate, subtle briefing
  background plates, the favicon / app icon, and a loading screen.
- One prompt file per image in `assets/prompts/*.json`. Every prompt includes "no text, no
  letters, no numbers." After the key art is approved, later images pass it as a reference image
  for style consistency.
- Convert outputs to WebP (at most 2048 px on the long side, at most 400 KB) and log provenance.
- Human review rejects any image containing text, digits, or glyph-like marks.

## Research and fact verification
- **RFC MCP:** `@mjpitz/mcp-rfc` (tools `get_rfc`, `search_rfcs`, `get_rfc_section`).
- **Tier-1 RFCs** (verify every fact the twelve levels use; keep local copies in `research/rfc/`):
  2474, 2475, 2597, 2697, 2698, 3168, 3246, 3260, 3290, 4594. Status-only checks: 2598 (obsoleted by
  3246), 5865 and 8622 (both update 4594).
- Local copies: `for n in 2474 2475 2597 2697 2698 3168 3246 3260 3290 4594; do curl -fsSL
  https://www.rfc-editor.org/rfc/rfc$n.txt -o research/rfc/rfc$n.txt; done`
- Every MCP verification call is logged in `research/VERIFICATION.md` and referenced from
  `data/facts.json`.

**Seed fixtures** — supplied expectations, not yet independently verified in this run.
Verify by RFC MCP text, hand trace and an independent reference implementation in Loop 1 before
accepting them as tests:
- **RFC 4594 Figure 3 binaries:** CS6 110000, EF 101110, CS5 101000, AF41 100010, AF42 100100,
  AF43 100110, CS4 100000, AF31 011010, AF32 011100, AF33 011110, CS3 011000, AF21 010010,
  AF22 010100, AF23 010110, CS2 010000, AF11 001010, AF12 001100, AF13 001110, DF 000000,
  CS1 001000. All match CSx = 8x, AFxy = 8x + 2y, EF = 46.
- **Octet split:** ToS 0xB8 → DSCP 46, ECN 0. ToS 0xB9 → DSCP 46, ECN 1.
- **Precedence view:** AF41 → 4; EF → 5.
- **srTCM, color-blind** (CIR 1000 B/s, CBS 1500, EBS 3000; start full). Arrivals (ms, bytes):
  (0,1000) ×5, then (1000,1000). Expected: green, yellow, yellow, yellow, red, green.
- **trTCM, color-blind** (PIR 4000 B/s, PBS 3000, CIR 1000 B/s, CBS 1500; start full). Arrivals:
  (0,1000) ×4, then (500,1000). Expected: green, yellow, yellow, red, green.
- **RED thresholds** (queue capacity 64): AF43 [10,20], AF42 [20,30], AF41 [30,40] is valid.
  AF43 [10,25] with the same others fails exactly one rule: max AF43 ≤ min AF42.

## Tool gate (first tasks of Loop 1)
Results go to `research/BOOTSTRAP_REPORT.md`. Any failure stops the loop and is reported to the
human; nothing is stubbed.
1. **RFC MCP:** add it (`claude mcp add rfc -- npx -y @mjpitz/mcp-rfc`, or a project `.mcp.json`).
   Call `get_rfc(number="2474", format="metadata")` and confirm the title contains "Differentiated
   Services". Call `get_rfc_section(number="4594", section="4.3")` and confirm the text mentions
   AF41. If a section lookup by number fails, retry by title ("Multimedia Conferencing Service
   Class") and record which form works.
2. **Blender MCP:** install (`uvx mcp-for-blender setup`, or `claude mcp add blender uvx
   mcp-for-blender` plus `uvx mcp-for-blender install-addon`), open Blender, and enable the addon.
   Call `get_addon_status`. Then create a cube with `execute_blender_code`, export it to
   `assets/models/_smoke.glb`, confirm the file exists, and delete it.
3. **Built-in image tool:** generate one square smoke image (request 1024×1024) with ChatGPT image generation, copy it to
   `assets/images/_smoke.png`, confirm it decodes, record provenance, and delete it.
4. **Toolchain:** Node 20+, Python 3.11+, `uv`/`uvx`, and `specify check`.

## Implementation loops

### Loop 1 — Foundations
Tool gate; repo skeleton; vendored three.js with `VERSION`; local server instructions; local RFC
copies; `facts.json` for every fact used by all twelve levels, each verified through the RFC MCP;
`codepoints.json`, `profiles.json`, `machines.json`; all `/engine` modules; tests for dsfield,
meters, aqm, scheduler, sim, and grader using the seed fixtures.
**Exit:** tool gate open; `node --test` green; every fact has a verification record; the grader
implements all checks in spec.md.

### Loop 2 — Playable schematic slice
SVG schematic floor; grid editor (keyboard cursor, place, rotate, delete, undo); machine inspector
panels; run controls; dashboard; briefing, work order, and debrief views; Crate Trace; save/load;
Levels 1–5 complete with traces, reference solutions, known-wrong configs, hints, and diagnostics.
**Exit:** Levels 1–5 completable keyboard-only in schematic mode; level tests prove every reference
solution passes and every known-wrong config fails with its intended diagnostic.

### Loop 3 — 3D factory and Blender assets
Style guide; every Blender model in the asset table, built through the Blender MCP with saved
scripts; `scene3d.js` bound to sim snapshots; instanced crates with lid lights; build and
follow-crate cameras; 3D / schematic toggle and WebGL2 fallback; animations wired for every machine
used in Levels 1–5.
**Exit:** Levels 1–5 playable in 3D with grader output identical to schematic mode; performance
budget met; every model in `manifest.json` with an approver.

### Loop 4 — Metering, queuing, and scheduling content
Token Tank (single, cascade, twin), Recycler, Buffer Belt, Spillway, and Priority Merger fully
wired in UI and 3D (water levels, overflow spout, gates, hatch, threshold markers); static and
measured diagnostics; Levels 6–12 complete with traces, reference solutions, known-wrong configs,
hints, and briefings that list their simplifications.
**Exit:** all twelve levels meet the per-level definition of done below.

### Loop 5 — Art, Demo mode, and polish
ChatGPT-generated image assets (title, act cards, backdrop, briefing plates, icon, loading screen); title and
act screens; Demo mode with the Rush Hour showcase and scripted camera beats; accessibility pass
(keyboard, focus order, contrast, color plus shape, reduced motion); loading, error, and empty
states; final fact audit re-checking every `source` against the RFC MCP; README with run
instructions.
**Exit:** global definition of done met; Demo mode runs start to finish at 1920×1080 using only
presenter keys.

## What I am deliberately not building in v1
- User accounts or leaderboards
- Mobile touch optimization (desktop-first)
- Audio
- A level editor UI (edit `levels.json` directly)
- A free sandbox (Demo mode is the only ungraded mode)
- The future content listed at the end of spec.md

## Definition of done for each level
- Every fact in its briefing, hints, and diagnostics exists in `facts.json` with an RFC MCP
  verification record.
- The reference solution passes every listed check (automated test).
- Every known-wrong config fails its intended check with its intended diagnostic (automated test).
- Predict-level answers are computed by the engine, not stored as data.
- The briefing lists every simulation simplification that applies.
- All `why_wrong` explanations reviewed by a human.
- Playable start to finish keyboard-only in both 3D and schematic modes, with identical grader
  output in both.
- Meets the rendering budget during its trace.

## Resolved execution contracts

See `contracts/engine.md` for tick/refill ordering, threshold equality, scheduling, congestion
windows and incomplete-run behavior. `contracts/ui.md` defines keyboard controls, presenter keys
and save recovery. `analysis.md` records the source contradictions and their fixes. All RFC claims
remain subject to the mandated live verification before entering production data.

## User-directed amendment — 2026-11-04

The user replaced the external Images API dependency with built-in ChatGPT image generation,
removing the API-key gate. This changes the provider only; saved prompts, local WebP assets,
no text in art, visual inspection and human approval remain mandatory. Constitution v1.1.0 records it.

## Owner direction — beginner onboarding and approval, 2026-11-04

The owner approved “all models all things” and requested a gentler splash-style introduction to
the topic. Add a replayable introduction before the first work order: packet/crate, shared-link
congestion, six DSCP lights versus two ECN lights, and one guided routing edit. Explanations use
plain language first, with RFC details available as a secondary layer. Preserve the curriculum and
actual grading. This is a refinement of FR-001/FR-006/FR-012 within the remaining loops, not another
Spec Kit generation pass. The approval permits continuing asset/content work without repeated
confirmation; later artifacts record assistant inspection and this advance authorization truthfully.

For the original RFC 4594 profile, retain CS1 in the historical nine-class Example 3 and explicitly
state that RFC 8622 replaces it with LE (DSCP 1). LE behavior remains outside v1 as specified. This
resolves implementation scope without claiming CS1 is the current low-effort recommendation.
