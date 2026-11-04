# Feature Specification: Per-Hop Works

**Feature Branch**: `001-per-hop-works`  
**Created**: 2026-11-04  
**Status**: Specified; implementation subject to live tool gate  
**Input**: Supplied Per-Hop Works constitution, twelve-level spec, technical plan and five-loop delivery request.

## User Scenarios & Testing

### User Story 1 — Read, classify and mark crates (Priority: P1)

A beginner learns the DS field and builds the datapath for Levels 1–5 using a keyboard.
**Why this priority**: It establishes the knowledge all later levels depend on.
**Independent Test**: Complete L1–L5 in schematic mode, including an incorrect attempt and retry.
**Acceptance Scenarios**:
1. Given a crate with ECN set, when it passes a DSCP sorter, then ECN does not change its route.
2. Given an invalid layout, when Run is pressed, then the error names its location and editing remains available.
3. Given a failed marking check, when the player inspects it, then expected/actual values, harmed crates,
   machine and a sourced explanation appear; the layout survives retry.
4. Given the completed L1 work order, when every applicable check passes, then only its next prerequisite unlocks.

### User Story 2 — See the same factory in 3D (Priority: P2)

A learner follows crate bits and machine state on a spatial factory floor.
**Why this priority**: The visual metaphor makes the pipeline and its consequences visible.
**Independent Test**: Replay the same L1–L5 factory and trace in both views and compare grading.
**Acceptance Scenarios**:
1. Given a saved build, when switching views during pause, then tick, selection, layout and checks are unchanged.
2. Given unavailable WebGL2, when opening the game, then schematic mode supports every core interaction.
3. Given reduced motion, when inspecting a crate, then state remains readable without a moving camera.

### User Story 3 — Engineer congestion behavior (Priority: P2)

A learner predicts meter colors and builds policers, queues, AQM and schedulers for L6–L12.
**Why this priority**: It completes the advertised DiffServ curriculum.
**Independent Test**: Every L6–L12 reference passes and each known-wrong configuration fails its intended check.
**Acceptance Scenarios**:
1. Given a fixed trace, when meter predictions are submitted, then answers come from the engine's run.
2. Given an unpoliced EF flood, when run, then checks identify its effect on other classes.
3. Given overlapping AF thresholds, when run, then the threshold check identifies the violated inequality.
4. Given the Rush Hour reference, when run to completion, then all applicable checks pass.

### User Story 4 — Present the art of the possible (Priority: P1)

A presenter starts the game with one command and demonstrates a full Rush Hour factory.
**Why this priority**: A reliable live demonstration is the requested workshop outcome.
**Independent Test**: From fresh local progress, launch the game and traverse all demo beats using presenter keys.
**Acceptance Scenarios**:
1. Given a checkout with assets, when the documented command runs, then the localhost browser interface opens.
2. Given Demo mode, when stepping forward/backward or pausing, then the factory and dashboard remain coherent.
3. Given completed demo playback, when returning to Campaign, then no completion or unlock was awarded by Demo.
4. Given no internet after startup, when playing any shipped level, then content and art remain available locally.

### Edge Cases

Invalid graphs, off-grid or overlapping placements, palette exhaustion, disconnected ports, cycles,
missing trace docks, duplicate IDs, out-of-range DSCP/ECN, unsupported save versions, storage denial,
missing assets, lost WebGL context, unfinished runs, empty classes, incorrect prediction count and
capacity-incompatible crates MUST produce explicit recoverable errors. Failed validation never awards progress.

## Requirements

### Functional Requirements

- **FR-001**: Teach the twelve ordered levels and their briefings, layered hints and debriefs; retain the supplied scope below.
- **FR-002**: Show six DSCP bits and two separated ECN bits; edit DSCP without changing ECN and compute names/values/precedence.
- **FR-003**: Support keyboard placement, rotation, connection, deletion, undo, selection and configuration with locked docks and palette limits.
- **FR-004**: Validate the complete factory and run the same input to the same outcome independently of camera, display speed or pause.
- **FR-005**: Implement every named check below in a single grader; a required invalid, missing or unmeasurable check cannot pass.
- **FR-006**: Show each failed check's expected/actual result, culprit, affected crates, diagnostic explanation and source.
- **FR-007**: Preserve drafts, settings and earned progress locally; recover from unavailable or corrupt storage without falsely unlocking levels.
- **FR-008**: Provide 0.25×–8× playback, pause, one-tick step and a complete selectable per-crate event history.
- **FR-009**: Keep 3D and schematic state and grading identical; offer automatic fallback and follow-crate viewing.
- **FR-010**: Cover single bucket, srTCM and trTCM predictions and builds, both meter modes, policing, queues, AQM and scheduling.
- **FR-011**: Provide always-available, ungraded Rush Hour Demo with presenter beats, pause and schematic toggle; Demo cannot award campaign progress.
- **FR-012**: Make every core interaction keyboard accessible with visible focus, color plus shape/pattern, readable contrast and reduced motion.
- **FR-013**: Attach verified provenance to every teaching fact and decorative asset; require actual human review before release.
- **FR-014**: Start from one documented command and work locally without runtime accounts, network services or credentials.
- **FR-015**: Ship passing references and diagnostic-specific failing fixtures for all levels; compute prediction answers instead of storing them.
- **FR-016**: Explain simulation simplifications in each applicable briefing and distinguish game checks from normative RFC recommendations.
- **FR-017**: Deliver only after all five ordered loop exit gates and global acceptance checks pass; report blockers without substitute tools or art.

### Key Entities

Level/work order, traffic trace, crate, machine definition, configured factory, compiled graph,
simulation snapshot, event, class metric, check result, diagnostic, fact verification, asset provenance,
demo beat and local save. Their identities, validation and relationships are in `data-model.md`.

## Success Criteria

### Measurable Outcomes

- **SC-001**: All 12 reference factories pass every listed check and 100% of known-wrong fixtures fail their intended check and diagnostic.
- **SC-002**: Every level can be finished keyboard-only in both views, with identical results for identical factories and traces.
- **SC-003**: Every teaching claim has a matching verification record; every shipped asset and wrong-answer explanation has human review evidence.
- **SC-004**: The 1920×1080 factory sustains 60 fps on a recorded integrated-graphics machine with 400 crates; uses at most 150 draw calls, 15 MB of GLBs and 1024² textures.
- **SC-005**: A presenter starts the local browser interface with one command and completes every demo beat with presenter keys, without earning campaign progress.
- **SC-006**: Identical input produces identical events, snapshots, metrics and grades across repeat runs and both display modes.
- **SC-007**: No missing data, invalid graph, incomplete run or storage failure is presented as success; recovery preserves valid drafts when possible.

## Assumptions

Desktop-first English UI; no mobile touch optimization or audio. The user supplies developer API access
when required; viewers need none. Human reviews remain pending until the owner reviews concrete results.
Demo is immediately available by the user’s confirmed clarification; campaign stays gated.
Performance evidence records hardware/browser and includes a 60-second sustained load after warmup.
One feature directory contains all artifacts; lowercase filenames are canonical on case-sensitive systems.

## Clarifications

### Session 2026-11-04

The supplied brief resolves technology, scope, prerequisites, sources, review gates and five-loop order.
- Q: Should Demo open the full Rush Hour factory immediately while campaign stays gated? → A: Demo always available; campaign stays gated (user confirmed).

FR-011 and US4 encode this answer. See `clarify.md` for Q&A provenance and the coverage assessment.


## What I want to build
A web-based 3D factory-building puzzle game where the player is the plant engineer of a DiffServ
node. Each level is a **work order**: a stream of crates (packets) arriving at input docks, a
contract describing how each traffic class must be treated, and a limited palette of machines. The
player builds the node's datapath on a grid — **Sorters** (classifiers), **Paint Booths**
(markers), **Token Tanks** (meters), **Recyclers** (droppers), **Buffer Belts** (queues), and a
**Priority Merger** (scheduler) — then presses Run.

Every crate wears its DS field on its lid: **six DSCP lights and two smaller, separated ECN
lights.** The simulation plays out deterministically, and an output dashboard grades the run
against checks taken straight from RFC text. For example, RFC 4594 §4.3 says the probability of
loss of AF41 traffic MUST NOT exceed that of AF42, which in turn MUST NOT exceed that of AF43 — so
the game validates the recommended threshold ordering and separately checks loss on its fixed trace.
Finite-trace loss is a teaching measurement, not proof of a stochastic probability guarantee. If a check fails, the factory floor highlights the machine
that caused it and the crates it harmed, and the game explains why, citing the RFC section.

Success means a factory whose measured output meets every check in the work order, followed by a
debrief that traces how each crate got where it went.

## Why this exists
DiffServ is taught as a table of numbers. People memorize "EF is 46" without knowing what a router
actually does with the packet. In reality DiffServ is a **per-hop pipeline of independent
elements** — classify, meter, mark, drop, queue, schedule — spread across a dozen RFCs, and the
hard part is the order of operations and the consequences of each choice. A factory *is* a
pipeline. Building the datapath with your own hands makes the order stick (classify before you
meter, meter before you mark, police before the priority lane). Watching a token tank drain, a
buffer belt overflow, or a voice crate stuck behind freight builds intuition about tokens, time,
and starvation that a slide deck can't. And because the RFCs state measurable outcomes, the game
can grade the player's factory on the same terms an engineer would.

## Core learning outcomes
By completing the game, a player should be able to:
- Given a crate lid or a ToS / Traffic Class octet, extract the 6-bit DSCP and the 2-bit ECN field,
  and state the DSCP in decimal and by name.
- Convert between codepoint names and values (CSx = 8x, AFxy = 8x + 2y, EF = 46, DF = 0) and
  predict what a device that reads only IP Precedence (the top three bits) will see.
- Map applications to RFC 4594 service classes and their recommended DSCPs (RFC 4594 Figure 3),
  and mark unmarked traffic at the edge using multi-field classification.
- Decide what must be re-marked or dropped at an untrusted boundary (for example CS6 and CS7 from
  user devices), per RFC 4594 §3.
- Given meter parameters and a packet trace, color each packet under a single-rate token bucket,
  srTCM (RFC 2697), and trTCM (RFC 2698), and choose color-blind or color-aware mode correctly.
- Choose priority versus rate queuing per service class (RFC 4594 Figure 4) and explain why EF
  must be policed before a priority queue.
- Configure AQM thresholds for an AF class that satisfy RFC 4594 §4.3's inequalities, and state
  which classes should not receive AQM.
- Build a complete RFC 4594 enterprise node (Example 3, Figure 7) that passes every check under
  congestion.

## The machines (parts palette)
| Machine | DiffServ element | What the player configures | Grounding |
|---|---|---|---|
| Input Dock | DS boundary ingress | Nothing (trusted / untrusted is set by the level) | RFC 2475; RFC 4594 §3 |
| Sorter | Classifier | BA mode: ordered rules matching DSCP (typed as decimal). MF mode: ordered rules matching shipping-label fields. First match wins. | RFC 2475; RFC 3290 |
| Paint Booth | Marker | The six DSCP bits, set with bit toggles (no name dropdown) | RFC 2475; RFC 3290 |
| Token Tank — Single | Token bucket meter (single rate + burst size) | Rate and bucket size; two outputs (conform / exceed) | RFC 4594 §1.4.3 |
| Token Tank — Cascade | srTCM | CIR, CBS, EBS; color-blind or color-aware; green / yellow / red outputs | RFC 2697 |
| Token Tank — Twin | trTCM | PIR, PBS, CIR, CBS; color-blind or color-aware; green / yellow / red outputs | RFC 2698 |
| Recycler | Dropper | Nothing; counts drops | RFC 3290 |
| Buffer Belt | Queue | Capacity (in crates); tail drop when full | RFC 4594 §1.4.1 |
| Spillway (Buffer Belt add-on) | AQM (RED-style) | Min / max threshold per DSCP | RFC 4594 §1.4.2, §4.3 |
| Priority Merger | Scheduler | One strict-priority input plus weighted inputs (weights per input) | RFC 4594 §1.4.1 |
| Output Dock | Egress link | Nothing (fixed service rate set by the level) | RFC 4594 §1.4.1 |
| Belt | Transport | Path only; plain belts never drop or reorder — all queuing happens on Buffer Belts | Game metaphor (labeled) |

MF classification uses a crate's **shipping label** (application, protocol, port, source dock),
which stands in for the 5-tuple and application identity. This is labeled as a metaphor.

The cascade tank is the visual star of metering: in srTCM the committed tank fills first and its
overflow pours into the excess tank, exactly as RFC 2697 describes the token update.

## Checks (the win conditions)
The grader evaluates these deterministically after every run. Each level's work order lists which
checks apply.

| Check | Passes when | Source |
|---|---|---|
| VALID | The factory compiles: every output connected, no cycles, palette limits respected | Game rule |
| CONSERVATION | Every offered crate has exactly one terminal result: delivered, policer-dropped, tail-dropped, AQM-dropped, or recycler-dropped; unfinished runs fail | Game rule |
| ROUTE | Every offered crate reaches its assigned dock; missing deliveries or drops fail this routing exercise | RFC 2474 §3 |
| PREDICT | The player's pre-run predictions match the engine's outcome | Level-specific |
| MARK | Every required crate is delivered and carries its level profile target (including meter-color mapping); only explicitly permitted drops are exempt | RFC 4594 Figure 3 |
| TRUST | No CS6 or CS7 crate from an untrusted dock is delivered still carrying that marking | RFC 4594 §3.1, §3.2 |
| METER-PREDICT | Predicted colors match the RFC algorithm's colors for the trace | RFC 2697 §3; RFC 2698 §3 |
| METER-MODE | Color-aware is used only where trusted marking is to be preserved; color-blind otherwise | RFC 4594 §4.3 |
| POLICE-EF | EF reaches the priority input only through a policer, and excess EF is dropped | RFC 4594 §1.5.3, §4.1 |
| DELAY-BOUND | EF maximum queuing delay stays within the work order's bound | RFC 4594 §4.1 |
| MIN-SHARE | Every rate-queued class receives at least its assured share under congestion | RFC 4594 §1.4.1.2 |
| STANDARD-PRESENT | Default (DF) traffic has its own queue with a share | RFC 4594 §1.3, §1.5.1 |
| NO-AQM-ON | No class that RFC 4594 Figure 4 lists without AQM (EF, CS5, CS4, CS3) sits on a Spillway | RFC 4594 Figure 4 |
| RED-THRESHOLDS | AFx3 min < AFx3 max ≤ AFx2 min < AFx2 max ≤ AFx1 min < AFx1 max ≤ queue capacity | RFC 4594 §4.3, §4.5 |
| LOSS-ORDER | On the declared fixed trace, measured loss fractions AFx1 ≤ AFx2 ≤ AFx3; all compared populations must be nonzero | RFC 4594 §4.3, §4.5 |

## Gameplay loop
1. **Briefing** — the concept, explained before the test with an animated SVG example, the RFC
   citation, and any simulation simplifications that apply to this level.
2. **Work order** — the challenge state: an incoming traffic manifest (classes, crate sizes,
   rates), the contract (which checks apply and any bounds), the parts palette with counts, and
   locked docks.
3. **Build or predict** — the player places and configures machines on the grid, or, in predict
   levels, records predictions for a fixed factory before running it.
4. **Run** — the deterministic simulation plays with speed controls (0.25× to 8×), pause, and
   single-step, plus a follow-crate camera.
5. **Grade** — the dashboard shows every check with expected versus actual values.
6. **Correct** → the level is complete, and each passed check shows a one-line explanation of why
   it mattered.
7. **Incorrect** → the failing check is highlighted, the responsible machine glows on the floor,
   the harmed crates are listed, a diagnostic explains the specific mistake with its RFC source,
   and the player retries with their layout preserved.
8. **Debrief** — a per-class results table and **Crate Trace**: select any crate to replay its
   journey (for example "Sorter rule 2 → Cascade tank: yellow → Paint Booth: AF22 → Buffer Belt:
   waited 3 ticks → Priority Merger: weighted input B → Output Dock").

## Content scope (version 1)
Twelve levels in three acts, each introducing exactly one new concept. This list is the
prerequisite chain.

**Act I — Read the Crate**
1. **Six Lights** — DS field anatomy. Configure a BA Sorter by typing DSCP values read from lid
   lights. One crate has ECN bits set and must still sort by DSCP alone. Checks: ROUTE.
   Source: RFC 2474 §3; RFC 3168 §5.
2. **Codepoint Forge** — CS, AF, and EF naming math. Paint Booths with bit toggles must produce
   named targets (EF, AF41, AF31, CS6, CS1). Checks: MARK. Source: RFC 2474 §4.2.2; RFC 2597;
   RFC 3246; RFC 4594 Figure 3.
3. **The Old Sorter** — IP Precedence compatibility. A fixed legacy sorter reads only the top three
   bits; predict which dock each crate reaches (AF41, AF43, EF, CS5, AF11, CS1, DF). Checks: PREDICT.
   Source: RFC 2474 §4.2.2; RFC 4594 §1.5.4.

**Act II — The Edge**
4. **Who Goes Where** — MF classification and marking. Unmarked crates with shipping labels
   (VoIP bearer, SIP signaling, rate-adaptive video conferencing, interactive gaming, buffered
   streaming video, broadcast TV, web ordering, SNMP, file backup, undifferentiated web) must be
   sorted and painted per RFC 4594. Checks: MARK. Source: RFC 4594 §2.3 Figure 3, §4.
5. **Trust Boundary** — a trusted dock (neighbor router, real CS6 routing crates) and an untrusted
   dock (user access, crates falsely claiming CS6 and CS7). Re-mark or drop only at the untrusted
   ingress. Checks: TRUST, MARK. Source: RFC 4594 §3.1, §3.2.
6. **The Water Tower** — single-rate token bucket policer on EF. Part A: predict conform / exceed
   for a short trace. Part B: set rate and bucket size so contracted voice passes and the flood's
   excess goes to the Recycler. Checks: METER-PREDICT, POLICE-EF. Source: RFC 4594 §1.4.3,
   §1.5.3, §4.1.
7. **Cascade** — srTCM. Part A: predict green / yellow / red for a trace. Part B: color
   Low-Latency Data and paint green → AF21, yellow → AF22, red → AF23. Checks: METER-PREDICT,
   MARK. Source: RFC 2697 §3; RFC 4594 Figure 4, §4.7.
8. **Twin Towers** — trTCM. Part A: predict colors for a trace. Part B: Multimedia Conferencing
   arrives from a trusted dock (marking to be preserved) and an untrusted dock; choose
   color-aware versus color-blind correctly and mark AF41 / AF42 / AF43. Checks: METER-PREDICT,
   METER-MODE, MARK. Source: RFC 2698 §3; RFC 4594 §4.3.

**Act III — The Floor**
9. **Express Lane** — strict priority. Voice goes to the priority input. The trace includes an EF
   flood that starves every other class unless a policer guards the priority input. Checks:
   POLICE-EF, DELAY-BOUND, MIN-SHARE. Source: RFC 4594 §1.4.1.1, §1.5.3, §4.1.
10. **Shares** — rate queuing. Set merger weights so every class gets its assured share during
    congestion, including Default. Checks: MIN-SHARE, STANDARD-PRESENT. Source: RFC 4594
    §1.4.1.2, §1.3, §1.5.1.
11. **Spillway** — AQM drop precedence for AF4x, and AQM placement (none on EF, CS5, CS4, CS3).
    Checks: RED-THRESHOLDS, LOSS-ORDER, NO-AQM-ON. Source: RFC 4594 §1.4.2, §4.3, Figure 4.
12. **Rush Hour** (boss) — the RFC 4594 Example 3 enterprise node: nine service classes, a full
    parts palette, and a congestion trace. Every applicable check must pass. The reference solution
    becomes the Demo mode showcase. Source: RFC 4594 §2.4.3, Figure 7.

Every level has:
- A pre-level briefing that teaches the concept before testing it.
- No time pressure. Players take as long as they need.
- A hint system that reveals one layer of the decision at a time, never the full answer outright.

**Modes**
- **Campaign** — the twelve levels above.
- **Schematic mode** — a toggle (and automatic fallback) to an SVG top-down view with identical
  state and full keyboard control.
- **Demo mode** — for presenting on a projector: loads the Rush Hour showcase factory and plays a
  scripted camera sequence. It opens close on one crate's lid lights, follows that crate through
  sorter, booth, tank, buffer belt, and merger in its recorded event order, then pulls back to a full-factory zoom-out with the
  dashboard live. Presenter keys: next / previous beat, pause, toggle schematic.

## What the game explicitly does not do
- Does not emulate a real router: no vendor buffer carving, ASIC queue models, or real-time
  serialization of a specific platform. Time is ticks, and every simplification is declared.
- Does not model TCP or other elastic senders reacting to loss. Traffic traces are fixed.
- Does not mark ECN. ECN lights are shown and taught in Level 1 but are read-only in v1.
- Does not include shaping, multi-node domains, peering, tunnels, MPLS, or Wi-Fi mapping. Those are
  separate future content.
- Does not teach or grade vendor CLI syntax.
- Does not offer a free sandbox in v1 (Demo mode is the only non-graded mode).
- Does not connect to external systems or require login.
- Does not use AI to generate questions at runtime — all content is pre-authored and verified by a
  human before it ships.

**Future content, explicitly out of v1:** Lower Effort PHB (RFC 8622), VOICE-ADMIT (RFC 5865), NQB
(RFC 9956), the Cisco RFC 4594-based 12-class profile, multi-factory domains and aggregation
(RFC 5127, RFC 8100), tunnels (RFC 2983), MPLS Traffic Class (RFC 3270, RFC 5462), and DSCP to
802.11 mapping (RFC 8325).

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
