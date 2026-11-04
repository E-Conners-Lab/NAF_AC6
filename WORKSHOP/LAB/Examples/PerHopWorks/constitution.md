<!--
Sync Impact Report — 2026-11-04
Version: unratified template → 1.0.0 adoption → 1.1.0 user-directed image-provider amendment.
Modified principles: imported all supplied Per-Hop Works principles without weakening them.
Added sections: Core Principles grouping, Delivery Constraints, Development Workflow, Governance.
Removed sections: template placeholder examples only.
Templates: ✅ plan-template.md; ✅ spec-template.md; ✅ tasks-template.md.
Commands: no .specify/templates/commands directory exists; installed skills remain unchanged.
Follow-up: live tool and human asset/content approval gates remain implementation requirements.
Scope: Per-Hop Works feature; other workshop examples retain their own constitutions.
-->
# Per-Hop Works Constitution

## Core Principles

### Purpose
Build a web-based, visually rich 3D factory-building puzzle game that teaches **Differentiated
Services (DiffServ) QoS — the DS field and DSCP codepoints, traffic classification, marking,
metering and policing (token bucket, srTCM, trTCM), queuing, active queue management, and
scheduling** through interactive gameplay. Each factory floor is one DiffServ node: the player
builds the router's datapath out of machines, and crates (packets) flow through it. The game must
be both accurate and engaging. It functions as a teacher: it never guesses, never invents answers,
and never allows a player to progress on incorrect knowledge.

### The non-negotiable rule
**The game must never present incorrect information, even under time pressure or to be "more
fun."** If a mechanic requires an answer, that answer must be deterministically correct or
deterministically incorrect — no fuzzy grading, no partial-credit ambiguity that could reinforce
misconceptions. When in doubt, the game waits, not guesses.

In this game, "correct" means the factory's measured output satisfies checks derived from RFC
text, computed by the simulation engine. It is never a judgment call and never depends on luck.

### Sources of truth
1. **Current IETF RFC text**, checked for "Obsoleted by" and "Updated by" status before use.
   Example: RFC 4594 is updated by RFC 5865 and RFC 8622; RFC 2598 is obsoleted by RFC 3246.
2. **The IANA DSCP registry** for codepoint values.
3. **Vendor documentation** only for vendor-specific behavior (not used in v1).

Model memory, blogs, Wikipedia, and forum posts are never a source for game data. They may inspire
a misconception that a wrong-answer diagnostic addresses, but the diagnostic's explanation must
still cite an RFC. Copyrighted books may be cited by chapter as human background reading; their
text is never copied into the repo or the data files.

### Learning design principles
1. **Correctness over completion** — a player who hasn't learned the concept cannot advance. This
   is a feature, not a bug.
2. **Immediate, specific feedback** — wrong answers always explain *why* they are wrong, not just
   that they are wrong. A failed check names the machine that caused it and the crates it harmed.
3. **Layered complexity** — a player cannot encounter metering (token bucket → srTCM → trTCM),
   AQM thresholds, or priority scheduling before they can read the DS field, compute codepoint
   names, and classify and mark traffic. The dependency chain is the level order in spec.md.
4. **Recall over recognition where possible** — players type DSCP values, toggle bits, build
   working factories, and predict outcomes before running them. Multiple choice is avoided.
5. **Real-world grounding** — every machine maps to a named datapath element from RFC 2475 and
   RFC 3290 (classifier, marker, meter, dropper, queue, scheduler). The factory is a metaphor for a
   router, and the game labels it as one everywhere the real term matters.

### DiffServ correctness rules
- **The DS field is six bits plus two.** The DSCP is the upper six bits of the former IPv4 ToS /
  IPv6 Traffic Class octet; the lower two bits are ECN. The game never calls the whole octet "the
  DSCP." Values are shown as binary, decimal, and name together wherever space allows.
- **Normative language fidelity.** RFC 4594 is Informational: its MUST/SHOULD statements are
  recommendations for its service classes. Game copy says "RFC 4594 recommends…" and never
  upgrades a SHOULD to a MUST or downgrades a MUST to a SHOULD.
- **Current status only.** Obsoleted RFC text appears only in a clearly labeled History note.
- **Engines are the RFC algorithms.** Token bucket, srTCM (RFC 2697), and trTCM (RFC 2698) are
  implemented step by step from the RFC text. Animation may slow time down; it never changes an
  outcome.
- **Declared simplifications.** Wherever the simulation simplifies reality (tick-based time, fixed
  traffic traces with no TCP feedback, instantaneous queue depth instead of RED's averaged depth,
  deterministic drop spacing instead of random drops), the level briefing states it as a model
  simplification. Grading never depends on anything a simplification distorts.
- **No invented priority.** Visuals never imply a priority the configuration doesn't create. For
  example, AF4x is not drawn as "better" than AF1x unless the player's scheduler weights make it so.
- **Declared profile.** Every level declares its marking profile. v1 uses only `rfc4594`.
- **RFC vocabulary beside factory vocabulary.** "Sorter (classifier)", "Token Tank (meter)", and
  so on, using the terms from RFC 2475, RFC 3260, and RFC 3290.

### Gameplay principles
- Progress is earned, not gifted. No "try again and we'll lower the bar."
- Mistakes are learning moments, not punishments. Tone is calm and explanatory, never scolding.
- **Many factories can be correct.** Grading is on measured outputs and RFC-derived checks, never
  on matching one specific layout.
- No speed bonuses in v1; speed is not the skill being taught. Optional efficiency stars (fewest
  parts) may be shown but never gate progress.
- Every level must be completable with zero prior knowledge if the player reads all available
  hints. The game teaches; it does not assume.

### Code quality standards
- All level, codepoint, machine, and fact data lives in separate, editable JSON files. No hardcoded
  Q&A or thresholds inside game logic.
- **The simulation is pure and deterministic**: no DOM, no rendering code, no unseeded randomness.
  The same factory plus the same trace always produces the same result.
- **The grader is the single source of truth.** The UI and the 3D renderer only display the
  grader's output; they never decide correctness.
- **Every level ships with a reference solution that must pass and known-wrong configurations
  that must fail** with the intended diagnostic. Both are enforced by automated tests.
- Every factual claim in the game data includes a `source` field with RFC number **and section**,
  and a matching entry in `data/facts.json` recording how and when it was verified.
- Difficulty is data-driven. Adding a new level means editing data, not code.
- No external quiz APIs, AI-generated answers, or runtime-fetched content for question
  correctness — the ground truth is local, static, and audited by a human before it ships.

### Visual and asset principles
- **Spectacle serves the lesson.** Every animated element reflects simulation state: tank water
  level is the token count, buffer belt fill is queue depth, lid lights are the DS bits. Decoration
  never looks like it carries data.
- **Numbers never live in art.** All values, labels, and bit patterns are rendered by code from
  data. Blender models and generated images contain no text, digits, or glyph-like marks.
- **Generated images are decorative only** (key art, backdrops, act cards), never teaching
  diagrams. Teaching diagrams are SVG generated from data.
- **Provenance for every asset** in `assets/manifest.json`: tool, model/version, prompt or script,
  date, license, and human approver.
- **Original look.** Genre-inspired, not a clone: no names, art, UI, or signature designs taken
  from existing factory games.
- **Schematic parity.** Every 3D view has an SVG top-down schematic showing identical state. Every
  decision can be made in schematic mode, and the game falls back to it automatically if WebGL2 is
  unavailable.
- **Color is never the only channel.** Meter colors also carry a shape and a text label; service
  class colors come from a colorblind-safe palette plus patterns.
- `prefers-reduced-motion` is honored.

### Builder-agent tooling rules
- **The RFC MCP is mandatory for facts.** Every fact is checked with `get_rfc` or
  `get_rfc_section` before it is written to data, and the check is recorded in `data/facts.json`.
- **Blender MCP** produces the 3D models; the **built-in ChatGPT image generation tool** produces 2D art, as explicitly authorized by the user on 2026-11-04.
  Every Blender script and image prompt is saved in the repo so assets are reproducible.
- **Tool gate.** At the start of implementation, the RFC MCP, Blender MCP, and built-in image tool are each
  verified with a live call. If any check fails, stop and report it. Never stub, mock, or silently
  substitute a tool.
- Secrets (API keys) come from environment variables only and are never committed.
- **Iteration happens only inside `/speckit.implement`**, in the five loops defined in plan.md.
  The constitution, spec, and plan are not rewritten during implementation, except to fix a
  contradiction found by `/speckit.analyze` or a verified fact error, and every such change is
  logged.

### UX standards
- Runs in desktop browsers with WebGL2, served from a local static server. No install.
- Keyboard navigable for all core interactions: grid cursor, place, rotate, delete, undo,
  configure, run, pause, and step.
- Feedback copy is written in plain English, not jargon — unless teaching the jargon is the point
  of the question.
- Loading states, error states (for example, an invalid factory with an unconnected output), and
  empty states all have explicit designs.

### What this game is not
- Not a trivia app that happens to have DiffServ questions on a conveyor belt.
- Not a flashcard deck with a progress bar.
- Not a sandbox that rewards building big factories without meeting the RFC-derived checks.
- Not a router emulator and not a vendor CLI trainer.

The game should feel like the best professor you ever had — patient, precise, and genuinely
delighted when you get it right — on the most satisfying factory floor you've ever built.

## Delivery Constraints

This constitution governs `WORKSHOP/LAB/Examples/PerHopWorks/`. Its runtime MUST use local
HTML, CSS, JavaScript modules, vendored Three.js and data-generated SVG, served over localhost.
The delivered game MUST make no external runtime requests. The player's browser requires no
Node installation, backend, account or API credentials. Development tool credentials MUST never
enter browser code, saved progress, reports or version control.

## Development Workflow

Constitution, specify, clarify, plan, tasks and analyze run once for this single feature.
`clarify.md` MUST distinguish user answers from documented assumptions; `analysis.md` MUST
record findings, fixes and unresolved gates. All tasks MUST sit under exactly Loop 1 through
Loop 5, name their loop, and map to requirements. Each implementation invocation handles one
loop. Fix/test/review iteration occurs only inside that loop. A failed gate MUST stop progression;
an attempted task is not a completed task. Human approval means actual recorded human review,
never an inferred approval or an agent-generated approver name.

## Governance

Version 1.0.0 adopted the supplied constitution on 2026-11-04. Version 1.1.0 records the user’s explicit replacement of the external image API/key dependency with built-in ChatGPT image generation; all provenance and review obligations remain. The authoritative copy is
`.specify/memory/constitution.md`; the example copy MUST remain identical. Changes require the
owner's direction, a dated rationale and a sync impact report. Major versions change governing
principles incompatibly; minor versions add obligations; patches clarify wording. Every analysis
and loop exit MUST check compliance, provenance, test evidence and remaining human review.
The provided technical plan and explicit user instructions resolve implementation choices.
Any verified factual correction MUST update affected copy, fixtures and verification records.

**Version**: 1.1.0 | **Ratified**: 2026-11-04 | **Last Amended**: 2026-11-04
