> **For the attendee — remove this block before publishing.**
> Copy this file to **`README.md` in the root of your own game repository**.
> Replace every `[BRACKETED PLACEHOLDER]`. Keep the status honest: a plan is not
> an implementation, and an unrun check is not a pass. Delete sections you don't
> use. Add a screenshot or live link only after the file/site exists.

# [GAME NAME]

**[A SHORT, MEMORABLE LINE ABOUT THE PLAYER'S ACTION AND THE SKILL IT TEACHES].**

[GAME NAME] is a browser game for [TARGET LEARNER]. You play as [ROLE], making [CORE DECISION] to [VISIBLE GOAL]. Each round explains the result so you can use what you learned on the next challenge.

A project from **NAF AC6 — Loop Engineering, Spec-Driven Development & the Future of VibeOps**.

| Project | Details |
| --- | --- |
| Status | Planning — update to prototype/playable/verified only when accurate |
| Networking topic | [TOPIC AND TECHNICAL CONTEXT] |
| Typical session | [EXPECTED PLAY TIME] |
| Live demo | Not published yet |
| Built by | [NAME(S) / GITHUB HANDLE(S)] |

<!-- Optional after implementation: add ![Describe the game screen](docs/gameplay.png)
     only after committing a real screenshot at that path. Replace the demo text
     above with a working Markdown link after testing the deployed game. -->

## The challenge

[DESCRIBE ONE ROUND IN TWO OR THREE SENTENCES USING REAL NETWORK VALUES. SAY WHAT THE PLAYER SEES, WHAT THEY DECIDE, AND WHAT THE GAME SHOWS AFTER THE DECISION].

For example, a routing game might ask you to inspect a destination and several routes, choose an exit, then explain the matching prefix. Replace this example with your game's actual experience.

## What you'll learn

| By the end, you can… | You'll practice by… |
| --- | --- |
| [OBSERVABLE SKILL 1] | [PLAYER ACTION 1] |
| [OBSERVABLE SKILL 2] | [PLAYER ACTION 2] |
| [OBSERVABLE SKILL 3] | [PLAYER ACTION 3] |

**Before playing:** [PRIOR KNOWLEDGE, OR “NO PRIOR KNOWLEDGE; THE FIRST BRIEFING TEACHES THE BASICS”].

## Play locally

These instructions apply after the game has been implemented and `index.html` exists. Download this repository or clone it using the URL from GitHub's **Code** button, then open a terminal in the project root.

For the starter plan's static HTML/CSS/JavaScript build:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

On Windows with the Python launcher:

```powershell
py -m http.server 8000 --bind 127.0.0.1
```

Open **http://127.0.0.1:8000** in your browser. Keep the terminal running; **Ctrl+C** stops the server. If port 8000 is busy, use 8001 in both the command and URL.

The starter build loads JavaScript modules and JSON over HTTP. Use the server URL to preview it. If you chose a different stack, replace these instructions with the commands you actually tested. [Why modules need serving](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules).

## How to play

1. Read the briefing and inspect [THE CHALLENGE DATA].
2. [MAKE THE CORE CHOICE] and submit it.
3. Read the explanation. A wrong answer lets you retry; a correct answer enables Next.
4. Use a hint or worked solution when you need help. Assistance is recorded separately from completion.
5. Finish [NUMBER OF LEVELS/ROUNDS] to reach the session summary.

| Control | Action |
| --- | --- |
| [ACTUAL POINTER CONTROL] | [ACTION] |
| [ACTUAL KEYBOARD CONTROL] | [ACTION] |
| Hint / solution | [ACTUAL HELP BEHAVIOR] |
| Restart | [ACTUAL RESET AND CONFIRMATION BEHAVIOR] |

**Progress:** [WHAT IS COUNTED, WHEN A ROUND COMPLETES, AND WHAT HAPPENS ON RELOAD].

## What this game models

[STATE THE PRECISE TECHNICAL MODEL AND TWO OR THREE IMPORTANT ASSUMPTIONS].

**Outside the model:** [ADJACENT BEHAVIOR THE GAME DOES NOT SIMULATE].

| Reference | What it supports |
| --- | --- |
| [AUTHORITATIVE TITLE, URL, AND SECTION] | [SPECIFIC RULE OR CLAIM] |

## How it was built

The project follows the workshop's Spec Kit workflow: **constitution → specify → clarify → plan → tasks → analyze → implement**. The verification section below records which behaviors have actually been checked.

- **Stack:** [ACTUAL LANGUAGES/LIBRARIES].
- **Build tools:** [CODING AGENT / SPEC KIT VERSION / OPTIONAL TOOLS ACTUALLY USED].
- **Runtime:** [WHAT A PLAYER'S BROWSER NEEDS; DEFAULT IS STATIC FILES WITH NO MODEL OR API KEY].
- **Planning inputs:** `StarterKit/CONSTITUTION.md`, `StarterKit/SPEC.md`, `StarterKit/PLAN.md`.
- **Working artifacts:** [ACTUAL GENERATED CONSTITUTION, SPEC, PLAN, AND TASK PATHS].
- **One useful design decision:** [A CONCRETE QUESTION OR ANALYSIS FINDING THAT CHANGED THE BUILD].

## Verification

**Last checked:** [DATE, BROWSER/OS, AND COMMIT OR BUILD IDENTIFIER].

For the starter plan, run the local server and open **http://127.0.0.1:8000/tests/** after the agent has implemented the test runner. Replace this instruction if your project uses a different test command. Record test totals and failures; an empty test suite is not success.

| Check | Result | Evidence / notes |
| --- | --- | --- |
| Correct, incorrect, and boundary cases | Not run | [CASE IDS AND RESULT OR FAILURE] |
| Briefings and explanations checked against sources | Not run | [REVIEWER / REFERENCE NOTES] |
| Retry, hint, duplicate Submit, completion, restart | Not run | [OBSERVED BEHAVIOR] |
| Keyboard-only core playthrough | Not run | [BROWSER / OBSERVATIONS] |
| Narrow layout and reduced motion | Not run | [VIEWPORT / OBSERVATIONS] |
| Fresh checkout run instructions | Not run | [COMMAND / RESULT] |
| Published demo, if used | Not run | [URL / RESULT, OR REMOVE ROW] |

## Known limitations and next steps

- **Known limitation:** [SPECIFIC UNIMPLEMENTED OR IMPERFECT BEHAVIOR].
- **Next improvement:** [ONE SMALL CHANGE AND WHY IT HELPS LEARNING].

Found an incorrect answer or unclear explanation? Open an issue with the level/round, input values, your choice, expected result, actual result, and a reference if available.

## Credits

Created by [AUTHORS]. Workshop by John Capobianco, Joksan Flores, and Elliot Conner. Adapted from the [NAF AC6 workshop materials](https://github.com/automateyournetwork/NAF_AC6) and [Networking Video Game Starter Kit](https://github.com/automateyournetwork/NetworkingVideoGameStarterKit), using [GitHub Spec Kit](https://github.com/github/spec-kit).

**Assets and dependencies:** [CREDIT THE ACTUAL SOURCES, OR STATE THAT THE GAME USES ONLY ORIGINAL ASSETS].

**License:** [NAME THE LICENSE INCLUDED IN THIS REPOSITORY; ADD A LINK TO THE ACTUAL FILE].
