# Prefix Quest · First playable specification

**Read the table. Choose the exit. Explain the route.**

## The experience

The player is a packet dispatcher at a small routing station. A packet arrives with a destination address; a table lists installed prefixes and labeled exits. The player selects the route that should be used, or chooses “No matching route,” then submits the decision.

A correct route lights its exit and moves the packet one step toward it. A correct no-match decision places the packet in a visibly labeled drop area. An incorrect choice keeps the packet at the station and explains the mistake. These are illustrations of one lookup, not an end-to-end network simulation.

## Learner and outcomes

The learner recognizes an IPv4 address but is new to CIDR and forwarding-table lookup. The first briefing explains prefix notation and address membership with a worked example. No mental binary arithmetic or prior routing-protocol knowledge is required.

Target play time is 5–10 minutes, with no timer.

| ID | The learner can… | Evidence in play |
| --- | --- | --- |
| LO1 | Identify a prefix containing a destination | Choose the matching /24 in rounds R1 and R2 |
| LO2 | Select the most specific matching prefix | Choose the /25 in R3, and reject it when it does not match in R4 |
| LO3 | Distinguish a default fallback from no available route | Use the default in R5, then identify no match in R6 |

## Model boundaries

All listed prefixes are already installed and their exits are available. IPv4 unicast lookup uses prefix membership and specificity. There is at most one route for each prefix; the authoring format rejects duplicates. The game does not model route installation, administrative distance, metrics, ECMP, BGP selection, policy routing, TTL, ARP, ICMP generation, or end-to-end reachability.

A visible model note states: “This station practices one lookup in an installed table. Choosing an exit does not prove the destination is reachable.” A no-match outcome shows a drop; ICMP behavior is outside the game.

Rule reference: [RFC 1812 §5.2.4.3](https://www.rfc-editor.org/rfc/rfc1812.html#section-5.2.4.3). The example destinations use documentation address blocks from [RFC 5737 §3](https://www.rfc-editor.org/rfc/rfc5737.html#section-3).

## One round, in detail

1. Read the level briefing, then select Start level.
2. Inspect the packet's destination and the complete table.
3. Select one route or “No matching route.” Selection alone does not submit.
4. Select Submit. The explanation appears immediately and remains visible.
5. If incorrect, change the selection and retry. If correct, Submit is disabled and Next becomes available.
6. After the last round of a level, Next opens the next level's briefing; after R6, Next opens the session summary.

**Example from R3:** destination `192.0.2.130`; routes include `192.0.2.0/24` and `192.0.2.128/25`. Choosing the /24 produces: “Your /24 matches this destination, but the /25 also matches and is more specific. Compare matching prefixes before choosing an exit.” Choosing the /25 completes the round and highlights that row. It never says that an unrelated route wins simply because its prefix is longer.

## Three levels, six fixed rounds

Route IDs and cases are defined in [acceptance-cases.json](acceptance-cases.json). These are verification inputs; the implementation must add the teaching content described here.

| Level | Briefing and worked example | Rounds | Misconception |
| --- | --- | --- | --- |
| 1 · Find the neighborhood | Teach /24 membership using `203.0.113.25` and `203.0.113.0/24` | R1, R2 | Selecting an exit from its name or screen position |
| 2 · Find the closer fit | Teach specificity using `198.51.100.200`, `198.51.100.0/24`, and `198.51.100.128/25` | R3, R4 | Choosing the largest prefix length without first checking membership |
| 3 · Know when to stop | Teach fallback and no-match with a destination absent from the nondefault routes | R5, R6 | Assuming an exit must always exist |

| Round | Destination | Route IDs and prefixes | Expected decision |
| --- | --- | --- | --- |
| R1 | `192.0.2.42` | A: `192.0.2.0/24`; B: `198.51.100.0/24` | A |
| R2 | `198.51.100.14` | A: `192.0.2.0/24`; B: `198.51.100.0/24` | B |
| R3 | `192.0.2.130` | A: `192.0.2.0/24`; B: `192.0.2.128/25`; C: `203.0.113.0/24` | B |
| R4 | `192.0.2.126` | Same table as R3 | A |
| R5 | `203.0.113.9` | A: `192.0.2.0/24`; D: `0.0.0.0/0` | D |
| R6 | `203.0.113.9` | A: `192.0.2.0/24` | No matching route |

Display every route's ID, prefix, and exit. Always include a separate “No matching route” option. Show table order as authored; tests will reorder it to ensure position has no influence on correctness.

## Required stories

### US1 · Inspect and decide — P1

- **AC1:** A fresh session opens the first briefing. Starting displays R1's destination, complete table, and labeled decision controls.
- **AC2:** Each R1–R6 correct decision completes that round once and displays a rule-based explanation.
- **AC3:** Every other offered decision gives specific feedback and leaves completion unchanged. In R3, A produces “less specific”; C produces “does not match”; no-match produces “a matching route exists.”
- **AC4:** Submit with no selection provides guidance and does not increase attempts.
- **AC5:** Missing, malformed, or unsupported content produces a content error with a round identifier where available. No grading occurs.

### US2 · Get help and progress — P1

- **AC6:** Hint reveals the level's method reminder; Show solution reveals the worked decision for the round. Either marks the round assisted. Neither submits an answer or completes a round.
- **AC7:** Each valid submission while unsolved adds one attempt. A correct submission locks grading for that round; repeated Submit cannot change totals.
- **AC8:** Next remains unavailable before success. After success it advances in R1–R6 order, showing a briefing when entering a new level. After R6 it opens the summary.
- **AC9:** The summary shows completed rounds out of six, total valid attempts, number of assisted rounds, and a short recap of the three skills. It awards no mastery label.
- **AC10:** Restart opens a confirmation. Confirm resets all state to the first briefing; Cancel returns to the prior view without changing state. Reload starts a new session and this is explained beside the progress indicator.

### US3 · Play accessibly — P1

- **AC11:** The learner can finish the core flow using keyboard selection, Submit, Hint, Show solution, Next, and Restart. Controls have visible focus and readable names; feedback is announced and stays on screen.
- **AC12:** At 1280×800 and 390×844, essential data and controls remain reachable. Text accompanies status colors. Reduced motion uses an immediate static packet/exit update, with identical grading and controls.

## State and scoring decisions

No points, countdown, lives, shuffle, unlock animation, or persistence. Progress counts completed rounds. Attempts are valid submissions, including correct submissions. Assisted rounds count each round once even if both help actions are used. All help and retries are free.

The success state remains visible until the learner selects Next. There is no automatic advance. Reset confirmation is the only destructive session action.

## Visual direction

Build a compact routing station: a clearly labeled incoming packet, a readable table, and named exit gates. Use a dark ink background, light text, cyan for the selected path, and amber for feedback needing attention; text labels carry the same information as color.

The memorable moment is the selected prefix lighting up at the same time as the matching exit. Keep the diagram subordinate to the real address values. Place feedback beside the table on a laptop and below it on narrow screens. Avoid decorative dashboards, fake telemetry, or moving scenery that competes with the decision.

## Completion and next work

All twelve acceptance criteria and the fixture cases must be checked. A human reviews the briefing examples, help, feedback, and model boundaries. A teammate completes the keyboard flow. The README records actual results and limitations.

Out of scope: runtime AI tutor, live packet capture, route editing, multiplayer, audio, saved progress, and procedural levels. A possible later release adds a new independently checked curriculum using the existing mechanic. There are no unresolved product decisions in this example.
