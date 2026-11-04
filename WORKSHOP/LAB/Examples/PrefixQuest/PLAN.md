# Prefix Quest · Implementation plan

**Status:** a complete implementation brief for an attendee's build. The workshop example does not include an application or test runner.

## Technical decisions

Use semantic HTML, CSS, and native JavaScript modules. Render the table and choices with DOM elements and the station with lightweight SVG. No third-party dependencies, build step, persistence, backend, or runtime model are needed.

Load `data/levels.json` over HTTP using a relative path. Validate it before rendering the first briefing. Keep all content local and use relative asset URLs so the game can run at a GitHub Pages repository subpath.

After implementation, serve the repository root with:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Open **http://127.0.0.1:8000**; on Windows use `py` instead of `python3`. The module-based app uses a web server. [MDN module guidance](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules).

## Proposed layout

```text
index.html
style.css
main.js
engine/
  rules.js                IPv4 parsing, membership, lookup, answer evaluation
  content.js              Content validation
  state.js                Session transitions and counters
  feedback.js             Explain evaluator evidence
ui/
  render.js               Briefing, challenge, feedback, summary, error views
  controls.js             Events and focus management
data/
  levels.json             Three levels and six rounds
tests/
  index.html              Browser test runner
  acceptance-cases.json   Copy of the supplied independent fixtures
  rules.test.js
  state.test.js
  content.test.js
README.md
```

## Content shape

The following is valid sample JSON for **R3 only**, demonstrating the structure. The implementation must author all three levels and six rounds from `SPEC.md`; a one-round data file does not satisfy the release.

```json
{
  "schemaVersion": 1,
  "sources": {
    "lookup": {
      "title": "RFC 1812",
      "url": "https://www.rfc-editor.org/rfc/rfc1812.html#section-5.2.4.3",
      "section": "5.2.4.3",
      "claim": "Prefix membership and longest matching prefix in the declared lookup model"
    }
  },
  "levels": [{
    "id": "level-02",
    "title": "Find the closer fit",
    "learningOutcome": "LO2",
    "sourceIds": ["lookup"],
    "briefing": {
      "explanation": "Compare prefix lengths only among routes containing the destination.",
      "example": "198.51.100.200 matches both 198.51.100.0/24 and 198.51.100.128/25; select the /25."
    },
    "rounds": [{
      "id": "R3",
      "challenge": {
        "destination": "192.0.2.130",
        "routes": [
          {"id": "A", "prefix": "192.0.2.0/24", "exit": "North"},
          {"id": "B", "prefix": "192.0.2.128/25", "exit": "East"},
          {"id": "C", "prefix": "203.0.113.0/24", "exit": "West"}
        ]
      },
      "hints": [
        "First find the prefixes containing 192.0.2.130. Compare their lengths.",
        "A and B match. B has the longer prefix: /25. Select B, then Submit."
      ]
    }]
  }]
}
```

The first hint is the method; the second is the worked solution. Add the remaining source records, briefings, and hints during implementation. The content file does not store a correct-answer field; independent expected results live in the tests.

## Validation and domain contracts

Accept canonical dotted-decimal IPv4 strings: exactly four decimal octets from 0 through 255, without whitespace, signs, or leading zeros except the single digit `0`. Prefixes use a canonical network address and an integer length from 0 through 32; reject host bits in the network address. These are authoring format constraints, not a claim that every network tool uses the same input syntax.

Validate schema version, required fields, unique level/round IDs, nonempty text, resolvable source IDs, two hints per round, and unique route IDs/prefixes within each challenge. An empty route list is valid for the evaluator and means no match. The shipped curriculum still has exactly R1–R6 in the specified order, two per level. Reject the reserved route ID `drop`.

```text
parseIPv4(text) → unsigned integer, or validation error
parsePrefix(text) → {network, length, mask}, or validation error
lookup(challenge) → {
  status: "route" | "drop" | "content-error",
  routeId: string | null,
  matchingRouteIds: string[],
  reasonCode: string
}
evaluate(challenge, choice) → {
  status: "correct" | "incorrect" | "invalid-input" | "content-error",
  expectedRouteId: string | null,
  reasonCode: string,
  evidence: {destination, selectedPrefix, winningPrefix, matchingRouteIds}
}
```

Choices are a route ID or the reserved token `drop`. Missing or unknown choices produce `invalid-input`; they cannot change progress. Invalid challenge data takes precedence and produces `content-error`. Keep every function pure.

**Lookup algorithm:** validate input, parse the destination, retain matching prefixes, and select the one with maximum prefix length. No matches returns `drop`. Reject duplicate prefixes before lookup, so the declared model has no tied winning entries. Route display order never determines the outcome.

**JavaScript details:** use unsigned 32-bit normalization with `>>> 0` for addresses and masked values. Handle prefix length zero explicitly; a shift by 32 does not produce a /0 mask in JavaScript. Include /32 and addresses with the high bit set in tests. Numeric boundary fixtures test prefix membership only; they do not teach whether an address is usable as a host.

## Explain the actual decision

| Evaluator situation | Reason code | Feedback content |
| --- | --- | --- |
| Correct route | `best-match` | Destination, winning prefix, and why competing matches lose |
| Selected route doesn't contain destination | `not-matching` | Selected prefix and destination; invite the learner to check membership |
| Selected route matches but is less specific | `less-specific` | Selected and winning prefixes and their lengths |
| Selected drop while a match exists | `route-exists` | Identify the matching route and explain why drop is inappropriate |
| Selected route when none match | `not-matching` | Explain that this route does not match; the table offers no usable lookup result |
| Correct drop | `no-match` | No listed prefix contains the destination; the model drops the packet |

Generate explanations from structured evidence and fixed, reviewed wording. Never use a model or an unrelated answer label to generate grading explanations.

## State and interface

State stores `view`, current level/round, selected choice, attempts by round, assisted round IDs, completed round IDs, and feedback. A reset dialog preserves the previous view until the learner confirms. Reload recreates the initial state.

Render choices as native radio inputs in a labeled fieldset. Use labeled buttons for Submit, Hint, Show solution, Next, and Restart. Show solution becomes available after Hint. Empty selection gives guidance; wrong choices remain editable; correct submission locks input and enables Next. Disable controls and enforce the same guards in state logic. Next follows the sequence in the specification.

Use a live region for feedback, focus the new view's heading after navigation, and return focus appropriately when canceling restart. The SVG is a redundant visual summary; the HTML table and status text contain all essential information. Animate only successful route selection, never block interaction on animation completion, and honor reduced motion.

## Build slices and verification

| Slice | Deliverable | Evidence |
| --- | --- | --- |
| 1 | Domain functions and browser tests | All supplied lookup fixtures; every offered choice in R1–R6; missing/unknown input |
| 2 | R1 from briefing through Next | Correct choice, wrong choice, no choice, help, duplicate Submit |
| 3 | All six authored rounds and summaries | Counts/order/source validation; AC2–AC10 |
| 4 | Visual station and accessible interactions | AC11–AC12 and a human content review |
| 5 | README and optional static hosting | Reproducible run path, actual results, published-path check if deployed |

Copy the supplied `acceptance-cases.json` into `tests/`. Implement `tests/index.html` as a dependency-free module runner with visible totals and failed case IDs. Load fixtures via a relative URL. Treat failed fixture loading or zero discovered assertions as failure. Open **http://127.0.0.1:8000/tests/** to run it after implementation.

For each valid round fixture, assert that the expected route/drop choice is correct and every other offered choice is incorrect. Repeat with reversed route order. Test missing/unknown choices separately. For invalid fixtures, assert `content-error` before any grading.

State tests cover one attempt per valid unsolved submission, no counter change for empty input or post-success submission, assistance counted once per round, explicit Next, transitions between levels, the sixth-round summary, and restart/cancel. Content tests include missing source references, wrong round counts, and missing hints.

Record a result for AC1–AC12 with date, browser/OS, and evidence. Human checks include all briefings/help/feedback, keyboard play, 1280×800 and 390×844 layouts, and reduced motion. Browser tests verify code; they do not certify the prose or visual experience.

No application or implementation checks have been run in this example package. Add actual results only after building and running the checks.
