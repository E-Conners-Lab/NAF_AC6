# Prefix Quest · Project constitution

**Purpose:** help networking learners make an IPv4 forwarding-table lookup by inspecting the destination, comparing prefixes, and choosing an exit.

**Scope:** three levels, six rounds, one lookup mechanic, and a static browser game suitable for the workshop's 60-minute build block. This document specifies a proposed implementation; the example package contains no game code.

## C1 · Every graded answer has a reproducible basis

Grade only the declared lookup model: match an IPv4 destination against already-installed prefixes, select the longest match, or report no matching route. All exits are assumed available. Duplicate prefixes are rejected in authored content; equal-prefix alternatives, policy routing, and control-plane selection are outside this model.

The evaluator must not infer the answer from visual position or a stored answer label. Invalid or unsupported content blocks the challenge with a visible authoring error. It never counts against the learner.

**Evidence:** the independent expectations in `acceptance-cases.json`, plus source review of the briefings. The model is based on [RFC 1812 §5.2.4.3](https://www.rfc-editor.org/rfc/rfc1812.html#section-5.2.4.3).

## C2 · The interaction practices the skill

Every round shows the destination and the full table. The learner selects a route or “No matching route,” then submits. Feedback identifies the chosen prefix, matching prefixes, and the reason for the result. Briefings teach membership before specificity, then fallback/no-match behavior.

Hints have two steps: a method reminder and a worked solution. Both remain available without penalty. Help is recorded separately from completion.

**Evidence:** each round maps to a learning outcome, and a teammate can explain a wrong choice using the displayed feedback.

## C3 · Progress means completed practice

A correct submission completes a round exactly once. Incorrect submissions permit retry. Empty input does not consume an attempt. A solved round cannot accept further submissions. Each level requires both rounds; the session requires all six.

There are no points, lives, countdowns, or speed bonuses. The summary reports rounds completed, valid attempts, and rounds assisted. It does not label a helped or retried run as independent mastery.

**Evidence:** repeated-submit, retry, hint, Next, final-summary, and restart/cancel checks pass.

## C4 · The game is usable without a mouse or animation

Use native, labeled controls, visible focus, textual feedback, and text labels for exits. Keyboard interaction must reach selection, submission, help, advance, and restart. Essential data remains available outside the diagram. Reduced motion replaces packet movement with a static state change.

**Evidence:** keyboard-only playthrough, checks at 1280×800 and 390×844, and a reduced-motion check. These checks do not constitute a full accessibility audit.

## C5 · A static game is the complete first release

No backend, account, runtime model, external quiz service, telemetry, or live device connection. All playable content ships with the project. Development may use a coding agent; the game itself never asks an AI whether an answer is correct.

**Evidence:** browser requests during play are limited to the hosted project files; all six rounds work in a fresh session.

## C6 · Content, rules, and state remain reviewable

Level data contains briefings, destination/prefix values, labels, hints, and source references. Pure domain functions perform validation and lookup. A separate state module owns attempts and completion. Explanations use the evaluator's evidence rather than an unrelated answer key.

**Evidence:** reorder a table without changing its result, then add another round using the same content structure without changing grading logic.

## C7 · Verification precedes completion claims

The implementation must satisfy the specification and test cases. Record passed, failed, and unrun checks separately. A visual demo is useful evidence for interaction; it cannot establish networking correctness by itself.

If the build budget runs short, reduce the agreed content count explicitly and update the spec, plan, and tasks together. Do not lower the accuracy or feedback requirements.

**Evidence:** recorded case results, human content review, browser observations, and reproducible README instructions.

## Change policy

Record the reason for changes to the model or scope. Update dependent artifacts and rerun analysis before continuing implementation. Keep the README's status aligned with the implementation and the checks actually performed.
