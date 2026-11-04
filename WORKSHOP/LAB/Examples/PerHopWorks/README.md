# Per-Hop Works

A playable packet factory for learning DiffServ, one small work order at a time. Start with a
plain-language introduction, make a guided first edit, then work through twelve levels. For a
presentation, **Watch the factory** opens the complete Rush Hour showcase immediately.

## Start the game

From the workshop repository root:

```sh
python3 WORKSHOP/LAB/Examples/PerHopWorks/start.py
```

The launcher opens **http://localhost:8000**. Python 3.11+ and a desktop browser are enough to play.
Stop the server with **Ctrl+C**. If port 8000 is busy, add `--port 8001`. Add `--no-browser` to open
the printed address yourself.

From this example directory, `python3 start.py` also works. The direct static-server alternative is
`python3 -m http.server 8000`, followed by opening the address above. Use HTTP: browsers restrict
JavaScript modules and GLB loading when `index.html` is opened as a local file.

No installation, API key, login, build step or runtime internet connection is needed. Everything
used by the game—including Three.js, models, illustrations and lesson data—is local.

## First time here

Choose **Start here** on the welcome screen. Four short steps introduce packets as crates, sharing
a connection, and the six DSCP lights beside two smaller ECN lights. Try toggling an ECN light to
see that the DSCP number stays the same.

The first factory is already connected. Select its sorter, change the first match from **47** to
**46**, apply the configuration and run the trace. The guide remains beside the floor. There is no
time limit: pause, inspect a crate, read a hint, and try again. Technical RFC detail is expandable.
**How to play** reopens the introduction.

Passing all checks unlocks the next work order. Drafts, display settings and earned progress are
saved in this browser's local storage. An unreadable save is preserved until you choose to replace
it. If storage is blocked, the game explains that the current session cannot be saved.

## Present the workshop

Choose **Watch the factory** on the welcome screen, or **Demo mode** in the header. The 85-second
showcase follows a real voice packet, explains each decision, and pulls back to nine service classes
sharing a busy output. The live totals and journey come from the same simulation as the campaign.
The opening close-up isolates the selected crate for readability; factory totals still include all
traffic. The full floor appears as the tour progresses.

| Presenter key | Action |
|---|---|
| Right / Left | Next / previous camera beat; pauses at that beat |
| Space | Pause / resume |
| S | Toggle 3D / schematic |
| Escape | Return to the campaign |

The buttons provide the same controls. **Replay from start** restarts the showcase. Demo is always
available and never awards campaign progress. The browser's reduced-motion setting changes smooth
camera travel to cuts and suppresses decorative motion. A missing WebGL2 context automatically uses
the schematic presentation.

For a projector, use a 1920×1080 browser window. Pause at **Read the lid**, **Keep the promise small**,
and **The whole factory** to explain the three ideas before returning to the beginner campaign.

## Build and inspect

| Control | Action |
|---|---|
| Tab / Shift+Tab | Move between controls; focus is visible |
| Arrow keys on the floor | Move the grid cursor |
| Enter on the floor | Select a machine or place the chosen part |
| R | Rotate the selected unlocked machine |
| Delete / Backspace | Remove it |
| Ctrl+Z / Cmd+Z | Undo an edit |
| Inspector forms | Configure a machine and connect its output ports |
| Run / Pause / Step / timeline | Play, pause, advance one tick, or seek |
| 0.25×–8× speed | Change playback speed without changing the result |
| Crate search | Select any packet and inspect its complete journey |
| Follow selected crate | Follow it in 3D; Build camera restores the overview |

Each class has a color and a distinct pattern, described in the crate legend. Meter states include
text. Check results show expected and measured values, an offending machine when applicable,
affected crate IDs, an explanation and its source. The 3D and SVG views display identical grading.

## What is modeled

Twelve levels cover the DS octet, legacy precedence, classification, marking and trust; single
buckets, RFC 2697 srTCM and RFC 2698 trTCM; policing, FIFO buffers, strict priority, deficit round
robin and AF drop precedence. Prediction answers are computed by the engine. In two-part metering
levels, Part A uses a fixed factory independently of the editable Part B.

This is a deterministic teaching model of one hop. Rates use integer fixed-point token credit;
traces are fixed; plain belts take one tick per tile; buffers tail-drop when full. AQM uses
instantaneous queue depth and deterministic probability accumulation. It does not simulate TCP
feedback, ECN marking, admission control or a vendor ASIC. Applicable simplifications are listed in
each briefing.

The profile follows the **historical 2006 RFC 4594** curriculum. It explicitly notes that
[RFC 8622](https://www.rfc-editor.org/info/rfc8622/) replaces the former CS1 recommendation for
Low-Priority Data with LE (DSCP 1). [RFC 5865](https://www.rfc-editor.org/info/rfc5865/) adds
capacity-admission guidance. Those newer behaviors are outside this game's v1 scope.

## How this was built

The owner supplied a detailed technical prompt plus constitution, specification and planning
documents. Codex used Spec Kit to maintain **one specification**, record clarification Q&A, analyze
inconsistencies and execute **69 tasks in five implementation loops**. Each loop ended with an exit
check before the next began. The coding model recorded in the build session was `gpt-6-astra`;
one research helper supported planning.

| Loop | Built | Exit evidence |
|---|---|---|
| 1 — Foundations | Real tool gates, RFC fact ledger, pure engine, shared grader, pinned Three.js | [37 tests and tool checks](research/loops/loop-1.md) |
| 2 — Playable schematic | SVG editor, inspector, controls, saves, Crate Trace, Levels 1–5 | [49 tests and keyboard playthrough](research/loops/loop-2.md) |
| 3 — 3D factory | 17 procedural Blender models, instanced crates, cameras and fallback | [51 tests, model review and rendering checks](research/loops/loop-3.md) |
| 4 — Advanced content | Meters, queues, scheduling, diagnostics and Levels 6–12 | [71 tests and twelve-level playthroughs](research/loops/loop-4.md) |
| 5 — Presentation and polish | Ten illustrations, beginner introduction, Demo, accessibility and final fact audit | [78 tests and final acceptance report](research/loops/loop-5.md) |

The engine computes outcomes once; 3D and SVG display the same results. Blender MCP produced the
models from saved Python scripts. ChatGPT's built-in image tool produced the illustrations after
the owner replaced the original external image API requirement. RFC MCP supplied the research
evidence. The finished game needs none of those development services to run.

The follow-up prompts mattered: **Demo always available; campaign stays gated** established the
presentation flow. **Make the images using ChatGPT** changed the art pipeline. The owner's feedback
that the topic was difficult led to the welcome screen, four-step introduction and guided first
edit. Read the [prompt-by-prompt build story](research/BUILD_PROMPTS.md),
[complete original request](research/prompts/00-build-request.md),
[owner follow-ups](research/prompts/01-owner-follow-ups.md), and
[saved image prompts](assets/prompts/). The [Blender scripts](assets/src/blender/) preserve each
model's construction recipe.

## Build time, tokens and estimated cost

These measurements cover the original game build, including tool waits and owner review. They
exclude earlier preparation of the supplied documents and this later README/publication work.

| Measurement | Recorded value |
|---|---|
| Start | **2026-11-04 13:46:43.213 EST** / 18:46:43.213 UTC |
| Finish | **2026-11-04 15:45:16.332 EST** / 20:45:16.332 UTC |
| Elapsed wall time | **1 hour, 58 minutes, 33 seconds** |
| Model responses, including planning helper | **226** |
| Total input + output tokens | **31,371,854** |
| Input tokens | 31,129,855, including 30,581,504 cached tokens |
| Output tokens | 241,999, including reasoning |
| Estimated text-model API equivalent, Standard | **US$48.16** |
| Estimated text-model API equivalent, Fast | **US$96.33** |

Approximately 98.2% of input was cached context reused across calls. The token total measures
repeated processing, not unique words or lines of code. The money figures are **hypothetical
API-price comparisons, not the actual bill**. The calculation uses the recorded model's published
rates checked November 4, 2026; the session's service tier was not recorded.
[Official model pricing](https://developers.openai.com/api/docs/models/gpt-6-astra).

Image costs are unknown: ten production images and one disposable smoke image were generated,
but the built-in tool exposed no image-token or billing totals. The estimates exclude image
generation, separate tool fees, subscription allocation, tax, hardware and human labor. Subscription
usage follows its own billing rules. [Official Codex pricing](https://learn.chatgpt.com/docs/pricing).

The [full build ledger](research/BUILD_LEDGER.md) explains the boundaries and arithmetic. Its
[per-response CSV](research/build-usage.csv), [JSON summary](research/build-usage.json) and
[metadata-only exporter](scripts/export_build_usage.py) make the totals auditable without
publishing private session logs. Playing the completed game makes no AI/API calls.

## Verification and development

Node 20+ is used only for tests. From this directory:

```sh
node --test tests/
```

Developer browser checks use the separate `tools/browser` dependencies and an installed Chrome:

```sh
npm ci --prefix tools/browser
node tools/browser/keyboard.mjs 3d
node tools/browser/keyboard.mjs schematic
node tools/browser/polish.mjs
node tools/browser/accessibility.mjs
node tools/browser/resilience.mjs
node tools/browser/demo-rehearsal.mjs
node tools/browser/benchmark.mjs --shadows
```

These scripts expect the server on port 8000. The checked-in scripts currently select Chrome's
macOS application path; change `executablePath` for another developer machine. Browser-test
packages are not loaded by the game. Run performance checks alone for meaningful frame timing.

The engine suite verifies seed fixtures, integer refill, aware/blind modes, deterministic AQM,
scheduler behavior, conservation, diagnostics, every reference solution, every known-wrong fixture,
asset contracts and source provenance. Browser reports and screenshots are in `research/browser/`.
Measured hardware is an Apple M4 Pro with integrated 20-core GPU, 48 GB, Chrome 156. Performance
measurements describe that machine; they do not guarantee the same frame rate on every computer.

At completion, all **78 engine/content/asset tests** passed. Keyboard playthroughs covered all
twelve levels in both renderers. Ten representative accessibility states reported zero axe
violations, and eight resilience scenarios passed. The 400-crate, shadows-on benchmark at
1920×1080 recorded at most **72 draw calls** and **16.7 ms median/p95 frame time** on the hardware
above. See the [final loop report](research/loops/loop-5.md) for the scope and evidence.

The game code is divided into pure `engine/`, display-only `render/`, DOM `ui/`, and auditable
`data/*.json`. Three.js r180 is vendored with a version, license and checksums. All 17 models were
made through Blender MCP; scripts, `.blend` sources, GLBs and review sheets are retained. All ten
illustrations were generated with ChatGPT's built-in image tool. Prompts, hashes, dimensions,
provenance and review status are in `assets/manifest.json`. No third-party model or art was imported.

The source of truth for the workshop's SDD process is the single [spec](spec.md), supported by
[constitution](constitution.md), [clarification Q&A](clarify.md), [plan](plan.md), [tasks](tasks.md),
and [analysis findings and fixes](analysis.md). Five bounded implementation loops are recorded in
[implementation-status.json](implementation-status.json) and `research/loops/`. The Claude-specific
Ralph stop hook was unavailable in Codex; the five scopes were executed directly with explicit exit
checks. No extra spec-generation iteration or automatic-hook execution is claimed.

RFC verification uses actual MCP calls, including the final audit of all 48 facts. See
[verification log](research/VERIFICATION.md), [final fact audit](research/FINAL_FACT_AUDIT.md),
[bootstrap report](research/BOOTSTRAP_REPORT.md) and [content review](research/content-review.md).
Owner approval and later assistant inspections under continuing authorization are distinguished in
the records.
