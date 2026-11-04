# Prefix Quest

**Read the table. Choose the exit. Explain the route.**

A proposed browser game where you dispatch packets through a routing station and practice IPv4 prefix lookup. The destination and installed table are always visible. Every submitted choice gets an explanation you can use on the next attempt.

> **Workshop example · planning complete, game not implemented.**
> This folder contains completed Spec Kit inputs and independent test fixtures.
> It includes no `index.html`, application code, or test runner. The gameplay
> described below is the agreed design, not a claim that a playable build exists.

## What's in this example

| File | Purpose |
| --- | --- |
| [CONSTITUTION.md](CONSTITUTION.md) | Seven principles with concrete verification evidence |
| [SPEC.md](SPEC.md) | Three learning outcomes, six rounds, and twelve acceptance criteria |
| [PLAN.md](PLAN.md) | Implementation design, sample data, domain contracts, and verification plan |
| [acceptance-cases.json](acceptance-cases.json) | Fixed lookup expectations and malformed-content cases for the future test runner |

Use these to see how the three documents agree with each other. For a README to personalize in your own repository, start with the [attendee README template](../../StarterKit/README.md).

## A moment from the game

A packet for **192.0.2.130** arrives. Which exit should it use?

| Route | Prefix | Exit |
| --- | --- | --- |
| A | `192.0.2.0/24` | North |
| B | `192.0.2.128/25` | East |
| C | `203.0.113.0/24` | West |

The intended answer is **B**. A matches too, but B is more specific. If you choose A, the game should explain the competing matches and let you retry. If you choose C, the explanation should identify a membership error. These two mistakes deserve different feedback.

This is the first two lookup filters in our simplified model, grounded in [RFC 1812 §5.2.4.3](https://www.rfc-editor.org/rfc/rfc1812.html#section-5.2.4.3).

## The planned learning journey

| Level | What you practice | What changes |
| --- | --- | --- |
| Find the neighborhood | Identify a matching /24 | The destination changes; the table stays easy to inspect |
| Find the closer fit | Compare only prefixes that match | Overlapping prefixes introduce a more specific option |
| Know when to stop | Recognize fallback and no match | A default route is available, then absent |

Six short rounds. No timer, points, or lost lives. Hints teach the method; worked solutions explain the decision. The summary separates completion, attempts, and assistance.

## Intended controls

Select a route or “No matching route,” then Submit. Native radio controls support keyboard selection; buttons support activation through the keyboard or pointer. Hint leads to Show solution. Next advances after a correct answer. Restart asks before clearing the session. Reload starts again.

These controls still require implementation and a real keyboard playtest.

## Model and limitations

The table contains already-installed IPv4 prefixes with available exits. The game illustrates one lookup and does not simulate routing-protocol decisions or end-to-end packet delivery. Duplicate prefixes are an authoring error in this first version. No runtime AI, backend, account, or live network is involved.

The destinations use the documentation blocks described in [RFC 5737 §3](https://www.rfc-editor.org/rfc/rfc5737.html#section-3). Boundary fixtures check numeric membership, not host-address usability.

## Build your own version

1. Create your own repository using the [lab walkthrough](../../README.md).
2. Copy this example's `CONSTITUTION.md`, `SPEC.md`, and `PLAN.md` into your repository's `StarterKit/` folder.
3. Copy `acceptance-cases.json` alongside those inputs in `StarterKit/`. The implementation plan asks the agent to copy it into `tests/` when building the test runner.
4. Copy the [attendee README](../../StarterKit/README.md) to your repository root and personalize it for Prefix Quest.
5. Run the seven Spec Kit steps. Ask the agent to preserve the supplied cases and implement the test runner described in the plan.

Review source references and expected results with your group. Adopt the example as a whole before changing its scope; then update all affected artifacts together.

## Run after implementation

Once your repository contains the generated `index.html`, start a server in its root:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

On Windows use `py` instead of `python3`. Open **http://127.0.0.1:8000** for the game and **http://127.0.0.1:8000/tests/** for the planned test runner. Stop the server with Ctrl+C. These are instructions for the future implementation; this example folder cannot run a game.

## Verification status

| Evidence | Status |
| --- | --- |
| Independent expected lookup cases | Supplied in the fixture file; review before adopting |
| Application evaluator tests | Not run — evaluator not implemented |
| AC1–AC12 behavior checks | Not run — game not implemented |
| Teaching content review in the built UI | Not run |
| Keyboard, responsive layout, and reduced motion | Not run |
| Live deployment | Not published |

A good post-build README replaces these statuses with observed results, includes a real screenshot if available, and links to a working demo only after it has been tested.

## Credits

An illustrative project for the [NAF AC6 workshop](../../../../README.md), led by John Capobianco, Joksan Flores, and Elliot Conner, using [GitHub Spec Kit](https://github.com/github/spec-kit). This example is part of the workshop repository and its [Apache 2.0 license](../../../../LICENSE).
