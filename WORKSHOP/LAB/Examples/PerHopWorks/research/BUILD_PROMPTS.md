# How the prompts became a working game

Per-Hop Works began with a detailed owner-supplied brief and three supplied planning documents.
The coding agent used Spec Kit skills to turn those inputs into one maintained specification,
an explicit clarification record, an implementation plan and five sets of tasks with exit checks.
The agent wrote and tested the code, used the RFC and Blender tools, and generated the art. The
owner set scope, answered questions, reviewed the work and changed the beginner experience.

## Original request and follow-ups

Read the [complete original build prompt](prompts/00-build-request.md) and
[verbatim follow-up prompts](prompts/01-owner-follow-ups.md). These are historical inputs; the
current constitution and README incorporate subsequent decisions. Times below are UTC on
November 4, 2026.

| Time | Prompt or decision | Effect on the build |
|---|---|---|
| 18:46:43 | Detailed technical plan; use Spec Kit from constitution through implementation, one spec, five loops, easy startup | Adopted the supplied documents, recorded requirements and organized 69 tasks |
| 18:52:19 | “Demo always available; campaign stays gated” | Presentation access works immediately while earned campaign progress remains separate |
| 18:53:59 | Confirm use of constitution, spec, plan and tasks | Maintained the canonical workflow artifacts and explicit completion evidence |
| 18:55:17 | “make the images using chatgpt” | Replaced the external image API/key gate with the built-in tool; constitution v1.1.0 records it |
| 18:56:06 | Install required gates and report any needed Blender reload | Installed and smoke-tested real tools; repaired the RFC parser incompatibility |
| 19:04:12–19:05:07 | Supplied RFC 4594, 5865 and 8622 status links | Recorded the historical profile and its later updates explicitly |
| 20:00:43 | Approved models; said the topic was difficult and asked for a splash introduction | Added the welcome screen, four-step introduction and guided first sorter edit |

The clarification question asked whether the full Rush Hour factory should open immediately for
presentations while campaign levels remained pass-gated. The owner chose that behavior. The full
question, answer, assumptions and later resolutions are in [clarify.md](../clarify.md).

## Spec Kit and the five implementation loops

The sequence was `speckit-constitution` → `speckit-specify` → `speckit-clarify` → `speckit-plan` →
`speckit-tasks` → `speckit-analyze`, followed by one bounded `speckit-implement` scope per loop.
These names identify agent skills; they are not shell commands to paste into a terminal. Earlier
steps established the artifacts once; subsequent owner decisions amended those artifacts.

| Stage | What readers can inspect |
|---|---|
| Constitution | [constitution.md](../constitution.md): correctness, provenance, technology and acceptance rules |
| Specification | [spec.md](../spec.md): twelve levels, player behavior and checks |
| Clarification | [clarify.md](../clarify.md): Q&A, assumptions and owner decisions |
| Plan | [plan.md](../plan.md), [data-model.md](../data-model.md), [contracts/](../contracts/): architecture and interfaces |
| Tasks | [tasks.md](../tasks.md): all 69 tasks grouped under Loop 1 through Loop 5 |
| Analysis | [analysis.md](../analysis.md): findings, fixes and consistency review |
| Implementation | [implementation-status.json](../implementation-status.json), [loop reports](loops/): completed scopes and exit evidence |

The deterministic engine and shared grader came first. The SVG slice made the first five levels
playable before 3D was added. Blender assets and the renderer consumed the same simulation
snapshots, then advanced content filled out all twelve levels. The last loop added art, the Demo,
beginner onboarding and final accessibility, resilience and fact checks.

The Claude-specific Ralph stop hook was unavailable in the Codex host. The agent executed five
bounded Ralph-style scopes directly, checking each exit before advancing. This record does not
claim an automatic hook ran. One research helper supported planning; implementation remained in
the primary session. [BUILD_LEDGER.md](BUILD_LEDGER.md) includes both agents' usage.

## Art prompts and model recipes

The [style guide](../assets/style-guide.md) established the palette, silhouettes and no-text rule.
The [manifest](../assets/manifest.json) records provenance, output dimensions, hashes and review
status. Each image has its own saved prompt:

| Asset | Prompt |
|---|---|
| Disposable tool smoke test | [smoke.json](../assets/prompts/smoke.json) |
| Title key art | [title.json](../assets/prompts/title.json) |
| Act cards | [Act 1](../assets/prompts/act-1.json), [Act 2](../assets/prompts/act-2.json), [Act 3](../assets/prompts/act-3.json) |
| Factory backdrop | [hall-backdrop.json](../assets/prompts/hall-backdrop.json) |
| Briefing plates | [Plate 1](../assets/prompts/briefing-1.json), [Plate 2](../assets/prompts/briefing-2.json), [Plate 3](../assets/prompts/briefing-3.json) |
| App icon | [icon.json](../assets/prompts/icon.json) |
| Loading screen | [loading.json](../assets/prompts/loading.json) |

The title prompt describes a welcoming low-poly factory, matte machines, luminous crate sockets,
translucent token water and space for UI text added separately. Later prompts use the title image
as the visual reference. The production images are local WebP files. The built-in tool's underlying
model ID was not exposed, so the manifest does not invent one.

The seventeen 3D models were built procedurally through Blender MCP. Their reproducible inputs
are the [individual bpy scripts and saved .blend sources](../assets/src/blender/), with
[build results and review sheets](assets/). Named nodes connect moving parts to simulation state.
The owner approved the model set; later assistant inspections under continuing authorization are
identified separately in the review records.

## What made the process useful

The prompt supplied concrete seed fixtures, known-wrong configurations, asset contracts and
measurable exit criteria. Those became tests and evidence instead of remaining prose. Tool failures
were investigated: the RFC server's HTML parser needed a compatibility repair, and numeric section
lookup required a title-based fallback. [The tool README](../tools/rfc-mcp/README.md) and
[bootstrap report](BOOTSTRAP_REPORT.md) retain that history.

Human feedback also changed the product. “This is very hard” became a simpler entrance to the
subject: a four-step explanation, an already-connected first factory and one small change before
the first run. That decision is as much a part of the build as the original technical plan.
