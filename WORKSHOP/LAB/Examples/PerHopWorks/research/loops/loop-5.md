# Loop 5 — Art, Demo and beginner polish

Scope: T060–T069. Fifth and final bounded `speckit-implement` invocation, 2026-11-04.
Prerequisite check passed with all 16 specification checklist items complete. Optional git commit
hooks were not run; unrelated repository changes were left alone.

## Delivered

- Illustrated welcome with a clear beginner path and immediately available Demo. Four replayable
  teaching steps, ECN toggle, persistent first-edit guide, and plain-language advanced guidance.
- Ten actual ChatGPT-generated images, each visually inspected, converted to WebP and referenced
  from the app. Prompts, output paths, hashes and truthful review provenance are retained.
- An 85-second scripted tour of the real Rush Hour simulation, ten presenter beats, live SVG
  delivery chart, one packet's journey, pause/seeking, 3D/SVG toggle and reduced-motion cuts.
- Save schema validation, preservation of corrupt saves, session-only storage-denied mode,
  explicit data errors, graphics fallback and usable interfaces without decorative images.
- One-command launcher, play and presentation instructions, developer reproduction commands.
- Thirteen fresh live RFC MCP calls and a reviewed audit of all 48 facts. Wording fixes are
  documented in `research/FINAL_FACT_AUDIT.md` and `analysis.md`.

## Evidence

- `loop-5-tests.txt`: Node engine/content/asset tests, including every reference and intended
  known-wrong diagnostic, deterministic results and seed fixtures.
- `research/browser/keyboard-3d.json` and `keyboard-schematic.json`: complete keyboard campaigns,
  deep-equal view grading, trace seeking and reload persistence.
- `research/browser/polish.json`: introduction interaction and ten Demo beats, keyboard only,
  unchanged progress. Screenshots include welcome, bit example, lid close-up and factory pullback.
- `research/browser/demo-rehearsal.json`: uninterrupted 85-second presentation at 1920×1080,
  entered and exited with presenter keys from fresh progress; no awards or page errors. Maximum
  610 live crates and 96 draw calls. The final timing window has median/p95 16.7/16.7 ms.
- `research/browser/accessibility.json`: zero automated WCAG A/AA violations in ten representative
  states; `research/accessibility.md` distinguishes automation from manual visual/keyboard review.
- `research/browser/resilience.json`: eight successful scenarios covering no external runtime
  requests, corrupt/denied storage, missing model/image/data/trace, and WebGL2-free Demo.
- `research/launcher-checks.json`: invalid/busy port guidance, alternate port, startup from another
  working directory, and JavaScript MIME serving.
- `research/assets/image-review.md`, `assets/manifest.json`, `research/content-review.md`: actual
  owner model approval and assistant inspection of later art/text under continuing authorization.

Models total 658,064 bytes and 6,280 triangles. No textures are embedded. Ten WebPs total 995,678
bytes; the largest is 159,352 bytes, and no image exceeds 1672 pixels on its long side. All are
inside the stated limits. Performance hardware is Apple M4 Pro, integrated 20-core GPU, 48 GB,
Chrome 156. These measurements describe the tested machine rather than all integrated GPUs.

## Global exit checklist

- [X] SC-001: All twelve references and all intended wrong diagnostics verified.
- [X] SC-002: Full keyboard campaigns in both views; presentation controls verified.
- [X] SC-003: Every fact has live verification; assets/content reviewed under owner direction.
- [X] SC-004: Final sustained 400-crate frame check and all payload/draw budgets pass.
- [X] SC-005: One-command launch and complete presenter rehearsal from fresh progress.
- [X] SC-006: Repeat-run determinism and exact view-grade parity verified.
- [X] SC-007: Invalid/missing/failed states never award success; recovery scenarios pass.
- [X] Final loop complete; all 69 tasks accounted for under exactly five loop headings.

Final sustained result: 3601 frames in 60 seconds after 3-second warmup; median 16.70 ms, p95 16.70 ms, 72 draw calls, 400 crates, 1920×1080, shadows on. Evidence: `research/browser/benchmark-shadows.json`.

Final Node result: 78 passed, zero failures. Status: PASS. All five loops complete.
