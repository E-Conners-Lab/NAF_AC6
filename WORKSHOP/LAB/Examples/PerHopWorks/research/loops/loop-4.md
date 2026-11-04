# Loop 4 — Metering, queuing, scheduling, and beginner orientation

Scope: T046–T059. One bounded `speckit-implement` invocation, 2026-11-04.

All twelve reference factories pass all checks. Every known-wrong fixture fails its intended check
and diagnostic. Fixed prediction factories keep Part A independent of editable Part B. The real
engine computes every answer. `loop-4-before.txt` records the initial missing-content failures;
`loop-4-tests.txt` records 71 passing tests, zero failures.

Both `research/browser/keyboard-3d.json` and `keyboard-schematic.json` record complete keyboard-only
campaigns, earned unlocks after reload, Crate Trace navigation, and deep-equal grades after view
switching. The 3D test asserts the renderer remains 3D in every level. Repeated view changes exposed
a WebGL context leak; reusing the probe context and releasing disposed contexts fixed it. No browser
page errors remain. Actual traces at 1920×1080 measured:

| Level | Peak draw calls | Peak visible crates | p95 frame interval, ms |
|---|---:|---:|---:|
| L01 | 20 | 4 | 16.7 |
| L02 | 43 | 5 | 16.7 |
| L03 | 19 | 5 | 16.7 |
| L04 | 57 | 8 | 16.8 |
| L05 | 19 | 3 | 16.7 |
| L06 | 17 | 6 | 16.7 |
| L07 | 24 | 5 | 16.7 |
| L08 | 43 | 10 | 16.7 |
| L09 | 31 | 53 | 16.8 |
| L10 | 42 | 186 | 16.7 |
| L11 | 29 | 101 | 16.8 |
| L12 | 96 | 610 | 16.7 |

Peak crate count can vary slightly with playback sampling; L12 reaches 610 and remains under the
150-draw-call limit. The dedicated 400-crate stress fixture supplies the sustained frame check.
The machine is an Apple M4 Pro with integrated 20-core GPU, 48 GB, Chrome 156. Results apply to this
machine and browser; no claim is made for every integrated GPU.

All 17 Blender models are approved in the manifest. Content review and the owner's continuing
approval are recorded in `research/content-review.md`; newly authored copy is assistant-reviewed
under that authorization, not represented as individually read by the owner. The owner's request
for a gentler start is implemented as four plain-language SVG steps and a persistent first-task
guide. Technical detail remains available. Meter water, overflow, gates, hatch, queue fill and
threshold markers follow actual snapshots.

Exit checklist:

- [X] Twelve reference solutions pass; all wrong fixtures fail as specified.
- [X] All teaching facts resolve; simplifications are listed per level.
- [X] Why-wrong explanations reviewed under the owner's continuing authorization.
- [X] All twelve levels keyboard-completable in both views with identical grading.
- [X] Every actual trace fits the draw-call budget; models total 658,064 bytes, with no textures.
- [X] Sustained 400-crate frame budget verified for 60 seconds after warmup.
- [X] Loop 4 exits and releases Loop 5.

Sustained result: 3601 frames measured over 60 seconds after 3 seconds warmup; median 16.7 ms, p95 16.7 ms; 71 draw calls, shadows enabled. Evidence: `research/browser/benchmark-shadows.json`. Status: PASS.
