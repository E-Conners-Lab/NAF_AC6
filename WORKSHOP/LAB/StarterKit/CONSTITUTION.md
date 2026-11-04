> **Editor note — personalize, then remove this note.**
> This is the input to the **constitution** step. Replace the bracketed fields,
> keep the principles you intend to enforce, and agree on any changes with your
> group. Each principle includes evidence: your agent should know how to check it.
> Read the lab guide before running commands. A completed example is available
> in `WORKSHOP/LAB/Examples/PrefixQuest/` in the workshop repository.

# [GAME NAME] · Project constitution

**Purpose:** help [TARGET LEARNER] practice [ONE NETWORKING SKILL] through [CORE PLAYER ACTION].

**First release:** one core mechanic, three short levels, a browser, and a 60-minute workshop build. Change this budget only by updating the agreed scope.

## C1 · Technical truth is a release requirement

The game must never reward a technically incorrect answer. Grading must be reproducible from a documented rule and the challenge inputs. Unsupported or ambiguous content is an authoring error: show an explanation that the challenge is unavailable and prevent grading it.

Document the model being taught: [PROTOCOL/VENDOR CONTEXT, ASSUMPTIONS, AND IMPORTANT EXCLUSIONS]. Simplifications must appear in the briefing and README wherever they affect what the player can conclude. Fictional worlds and animations may illustrate a rule; they must not change it.

**Evidence:** hand-checked correct, incorrect, and boundary cases; a source link and section for each networking rule; review of all shipped briefings and explanations. Expected results are recorded independently of the implementation under test.

## C2 · Every round teaches through a decision

The player's main action must exercise the target skill. Introduce a concept before testing it, and show the values needed to reason about the answer. A wrong answer explains the specific mistake and gives the player a useful next step. A correct answer explains why it works.

Use this learning sequence: [FOUNDATION] → [APPLICATION] → [TRANSFER OR EDGE CASE]. Hints reveal a method first, then a worked step. Worked solutions are available when a learner is stuck; viewing one is recorded as assistance, never as independent mastery.

**Evidence:** a teammate can connect each player action to a learning outcome and describe what they learned from a deliberately wrong choice.

## C3 · Progress is honest and retry is safe

A round completes only on a valid, correct submission. Incorrect answers keep the challenge available. Empty or malformed submissions give input guidance without counting as a wrong attempt. Repeated Submit actions cannot award progress twice.

No lives, countdown, or speed bonus in this first version. Hints and retries have no penalty. Show completed rounds, attempts, and assistance separately; completion is not proof of independent mastery. The specification must say exactly what advances a round, finishes a level, and resets a session.

**Evidence:** wrong-answer, repeated-submit, hint, completion, and reset checks match the specification.

## C4 · Access is part of the core game

All core actions must be usable by keyboard with visible focus, readable labels, and an understandable order. Explain success and failure with text as well as color. Provide a text equivalent for essential diagrams. Respect reduced-motion preferences; animation must never delay the availability of feedback or controls.

Keep the challenge usable on a typical laptop and a narrow browser window. Dense technical data may scroll within its own labeled container, without hiding the action buttons.

**Evidence:** a keyboard-only playthrough, a narrow-window check, and a reduced-motion check. Record what was actually checked; do not claim full accessibility certification.

## C5 · The first version is deterministic and self-contained

Ship authored content and deterministic domain logic. The game requires no account, backend, live device connection, model, or API key. AI may help write code and assets during development; its output receives the same review as any other contribution.

Runtime AI tutoring, generated questions, and free-text AI grading are stretch work. Adding them requires an explicit change to the constitution, specification, and verification approach before implementation.

**Evidence:** a clean browser session can play using only the project's static files; no external content service decides an answer.

## C6 · Content and logic can be reviewed separately

Store level content, hints, sources, and difficulty in editable data. Keep domain rules separate from rendering and progress tracking. Validate data before presenting a challenge. Feedback must agree with the evaluator's reasoning; a hand-authored answer key cannot silently override the rule engine.

Adding another challenge that uses the existing mechanic should require a data change and its checks, not a new scoring path or a new screen implementation.

**Evidence:** inspect one level's data, trace one answer through the evaluator, and add a trial challenge without modifying the rule engine.

## C7 · Done is demonstrated

Ship only the agreed scope. Requirements, plan, tasks, and README must describe the same game. A feature is complete when its acceptance criteria pass and its actual status is recorded. A screenshot, a checked task box, or the agent saying “done” is insufficient by itself.

When time is short, reduce scope explicitly. Fix incorrect teaching and broken core interactions before adding visual effects. Keep failed and untested checks visible.

**Evidence:** reproducible run/test commands, recorded verification results, a fresh-start playthrough, and a README another attendee can follow.

## How we change these rules

For any material change, record the reason, update the affected spec and plan, and rerun analysis. A conflict with this constitution is resolved openly; the build agent must not weaken a principle merely to make its implementation pass.
