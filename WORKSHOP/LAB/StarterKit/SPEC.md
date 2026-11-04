> **Editor note — personalize, then remove this note and the idea menu.**
> This is the input to **specify**. Describe observable behavior and learning;
> save implementation choices for `PLAN.md`. Replace every bracketed field.
> The defaults below deliberately fit a short workshop. Change them explicitly
> if your mechanic needs something else. Resolve grading and scope questions
> during **clarify**, before planning the implementation.

# [GAME NAME] · First playable specification

## The pitch

**[ONE SENTENCE: PLAYER + ACTION + SKILL + VISIBLE CONSEQUENCE].**

The player is [ROLE] in [SETTING]. Each round shows [TECHNICAL EVIDENCE] and asks the player to [DECISION]. A correct decision [VISIBLE RESULT]; an incorrect decision [VISIBLE RESULT AND EXPLANATION]. The session ends when [CONCRETE COMPLETION CONDITION].

## Who this is for

- **Learner:** [AUDIENCE AND EXPERIENCE].
- **Assumed knowledge:** [WHAT THEY ALREADY KNOW; WRITE “NONE” IF APPROPRIATE].
- **What the briefing teaches:** [TERMS AND METHOD NEEDED BEFORE THE FIRST DECISION].
- **Why interaction helps:** [A SPECIFIC MISCONCEPTION THIS GAME MAKES VISIBLE].
- **Session target:** 5–10 minutes for a first playthrough, with unlimited thinking time.

## Learning outcomes and evidence

Use observable verbs such as identify, calculate, order, compare, or diagnose. Replace the rows with your topic's skills.

| ID | After playing, the learner can… | The game asks them to… | Evidence of success |
| --- | --- | --- | --- |
| LO1 | [FOUNDATIONAL SKILL] | [PLAYER ACTION] | [CHECKABLE RESULT] |
| LO2 | [APPLY THE RULE TO COMPETING CHOICES] | [PLAYER ACTION] | [CHECKABLE RESULT] |
| LO3 | [HANDLE AN EXCEPTION OR TRANSFER CASE] | [PLAYER ACTION] | [CHECKABLE RESULT] |

## The technical model

- **Rule being taught:** [PRECISE RULE, INCLUDING ORDER/TIE-BREAKS IF THEY MATTER].
- **Context:** [PROTOCOL VERSION, VENDOR, OR SIMPLIFIED MODEL].
- **Assumptions:** [WHAT IS ALREADY TRUE WHEN A ROUND STARTS].
- **Excluded behavior:** [WHAT A REAL NETWORK MIGHT DO THAT THIS GAME DOES NOT MODEL].
- **Authoritative references:** [URL + SECTION + THE CLAIM IT SUPPORTS].

Tell the learner about these boundaries in plain language. If two answers can both be valid, define how the game accepts them or remove that ambiguity from the first version.

## The repeatable game loop

1. **Brief:** introduce one concept, its terms, and a worked example different from the challenge.
2. **Inspect:** show [PACKET/TABLE/RECORDS/TOPOLOGY] with all decision-relevant values visible.
3. **Choose:** the player [SELECTS/ORDERS/TYPES/BUILDS] and explicitly submits the decision.
4. **Explain:** display the result, the relevant values, and the rule that connects them.
5. **Retry or advance:** a wrong answer leaves the round playable; a correct answer enables Next.
6. **Reflect:** the level summary shows completed rounds, valid attempts, and assistance used.

**Worked interaction:** [WRITE A SHORT SCENE WITH REAL VALUES: WHAT THE PLAYER SEES, A PLAUSIBLE WRONG MOVE, THE EXACT FEEDBACK, AND THE CORRECT MOVE].

## Required stories and acceptance criteria

### US1 · Make and understand a decision — P1

As a learner, I want to apply the rule to visible evidence and understand the result.

- **AC1:** Given a fresh session, when I start, then I see the first briefing before answering a challenge.
- **AC2:** Given [SPECIFIC VALID CHALLENGE], when I submit [CORRECT CHOICE], then [EXACT OUTCOME] and an explanation appear.
- **AC3:** Given that challenge, when I submit [PLAUSIBLE WRONG CHOICE], then feedback identifies [SPECIFIC MISCONCEPTION], completion stays unchanged, and I can retry.
- **AC4:** Given no selection or malformed input, when I submit, then input guidance appears and attempts/completion remain unchanged.

### US2 · Learn from help and finish the game — P1

As a learner, I want help when stuck and a clear view of my progress.

- **AC5:** A hint first explains the method. Further help can show a worked solution; assistance is recorded without marking the round complete.
- **AC6:** Each valid submission counts as one attempt until the round is solved. Correct submission completes it once; repeated submission after success has no effect.
- **AC7:** A level completes after both of its rounds are solved. Next opens the following round or level; the final round opens a session summary.
- **AC8:** Restart asks for confirmation, then clears the current session and returns to the first briefing. Cancel preserves the session.

### US3 · Play with accessible controls — P1

As a keyboard user, I want to inspect the challenge, choose, submit, get help, and advance without a mouse.

- **AC9:** All core controls have visible focus and accessible names; keyboard interaction reaches every core action.
- **AC10:** Correct/incorrect feedback includes text, remains available to read, and is announced to assistive technology. Motion can be reduced without losing information.

## Version-one content

Default: **three levels, two rounds per level, six rounds total**. Use one new example per round and the same core mechanic throughout. Change these counts and AC7 together if you choose a smaller scope.

| Level | New concept | Prerequisite | Misconception to expose |
| --- | --- | --- | --- |
| 1 | [FOUNDATION / LO1] | [STARTING KNOWLEDGE] | [COMMON ERROR] |
| 2 | [APPLICATION / LO2] | Level 1 | [COMMON ERROR] |
| 3 | [TRANSFER OR EDGE CASE / LO3] | Level 2 | [COMMON ERROR] |

**Progression:** sequential on first playthrough; retry without penalty. Completion requires a correct submission in every round. Hints remain available. No points, lives, timer, leaderboard, or streak mechanic in v1.

**Session behavior:** progress is held for the current page session; reload starts again. Saving across reloads is a stretch feature and must be specified before it is added.

## Cases the implementation must satisfy

Write these before generating code. Use real values and independently checked expected results. Include additional cases for every shipped round.

| Case | Input state | Player action | Expected result | Why / source |
| --- | --- | --- | --- | --- |
| Correct | [CONCRETE VALUES] | [ACTION] | [RESULT] | [RULE + REFERENCE] |
| Plausible mistake | [CONCRETE VALUES] | [ACTION] | [RESULT AND EXPLANATION] | [MISCONCEPTION] |
| Boundary | [EXACT BOUNDARY VALUES] | [ACTION] | [RESULT] | [RULE + REFERENCE] |
| Unsupported content | [INVALID OR AMBIGUOUS AUTHOR DATA] | Open round | Visible content error; no grading or progress | Authoring error, not learner failure |

## Experience direction

- **Visual metaphor:** [WHAT MAKES THE CONCEPT VISIBLE].
- **One memorable moment:** [A SMALL EFFECT THAT REVEALS CAUSE AND EFFECT].
- **Always visible:** [VALUES AND LABELS NEEDED TO REASON].
- **Feedback voice:** patient and specific; explain the observed choice before offering the next step.
- **Layout:** challenge first, action next, explanation beside or below it. Don't hide technical values behind hover-only interactions.

## Non-goals

No user accounts, multiplayer, backend, live infrastructure access, runtime AI, leaderboard, or level editor. No simulation of [ADJACENT SYSTEM OR PROTOCOL BEHAVIOR]. Visual polish must fit the existing mechanic.

## Open decisions for clarify

- [QUESTION THAT COULD CHANGE A RULE, A LEARNING OUTCOME, OR THE SCOPE].
- [QUESTION THAT COULD CHANGE WHAT COUNTS AS CORRECT].

Delete this section when resolved, or record the answer beside each question. Don't let unresolved decisions become silent implementation guesses.

## Release evidence

All required acceptance criteria must have a recorded result. All six rounds and their explanations must be checked against the references. A teammate must complete the core flow using only the keyboard. The README must describe implemented behavior, exact run/test commands, and any remaining limits.

---

## Idea menu · remove before using this file as your specification

| Concept | Playful action | Good first scope | Write down before building |
| --- | --- | --- | --- |
| IPv4 routing | Send packets through labeled gates | Choose from an installed forwarding table | Matching rule; default route; no-match behavior; tie assumptions |
| Subnetting | Fit teams into address blocks | Allocate a few fixed requirements | Address model; reserved addresses; whether /31 and /32 are included |
| ACLs | Admit or stop packets at a checkpoint | Evaluate one ordered stateless list | Supported fields; matching semantics; default action |
| DNS | Trace a lookup like a detective | Resolve one name through a staged scenario | Cache state; record types; which actor sends each query |
| NAT/PAT | Repair a translation ledger | Translate a small fixed set of flows | Direction; mapping model; address/port fields |
| VLANs | Dispatch frames through labeled doors | Access/trunk decisions on a tiny topology | Vendor assumptions; tagging rules; allowed VLANs |
| BGP | Compare route cards | A declared subset of one vendor's selection process | Eligible routes; attribute comparison order; excluded tie-breaks |
| QoS | Dispatch traffic into queues | One explicitly modeled scheduling policy | Queue policy; units; offered load; what happens when capacity is exceeded |
| Packet analysis | Assemble evidence for a diagnosis | One curated trace and one fault | What the trace proves; what remains unknown |

Choose the action that makes the networking decision enjoyable. Keep the first version small enough to explain, build, and verify in the workshop.
