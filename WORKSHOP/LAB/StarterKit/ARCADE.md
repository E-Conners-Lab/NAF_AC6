---
# ARCADE SUBMISSION — fill this file in, commit it to the ROOT of your game repository as ARCADE.md,
# then send John your GitHub URL. Everything between the two --- lines is machine-read.
#
# INSTRUCTIONS FOR THE BUILD AGENT (the coding agent that built this game):
#  1. You were there. Fill every field from your own session, your files and your tool list.
#  2. Do NOT invent. If something was not recorded or you do not know it, write "unknown".
#     A truthful "unknown" is better than a confident guess. Never estimate tokens or cost.
#  3. Ask the human ONLY for the fields marked (HUMAN): name, location, links, consent, first-project.
#  4. Keep strings on one line, quote any value containing a colon. Lists use [a, b, c] or "- item".
#  5. Do not put secrets, API keys, tokens, private URLs or file paths from the human's machine here.
#  6. Run the game once yourself and confirm the Runtime section is correct before you finish.
#  7. Then fill in the three short prose sections below the frontmatter. Plain language, no hype.
arcade_version: 1

game:
  title: ""                  # Display name, e.g. "Per-Hop Works"
  slug: ""                   # lowercase-with-dashes, e.g. per-hop-works
  tagline: ""                # One line, under 90 characters
  summary: ""                # 2-3 sentences: what the player does and what they learn
  topics: []                 # e.g. [DiffServ, QoS, RFC 4594]. 2-6 short tags
  category: ""               # network-fundamentals | routing | switching | security | automation | observability | wireless | cloud | other
  skill_level: ""            # beginner | intermediate | advanced   (the PLAYER's level)
  play_minutes: 0            # rough time for one sitting
  levels: 0                  # number of levels / scenarios / rounds
  card_image: ""             # path in this repo to a 16:9 image, webp/png/jpg, under 1 MB. e.g. assets/images/title.webp
  card_image_alt: ""         # one sentence describing the image for screen readers
  repo: ""                   # https://github.com/<user>/<repo>
  repo_path: ""              # only if the game lives in a sub-folder of the repo, else ""
  license: ""                # SPDX id, e.g. Apache-2.0 or MIT

creator:                     # (HUMAN) ask the human for every field here
  name: ""                   # name to show on the card (a handle or first name is fine)
  github: ""                 # GitHub username
  location: ""               # "City, Country" or just "Country" — optional, leave "" to hide
  organization: ""           # optional
  links: []                  # optional, e.g. [https://linkedin.com/in/you, https://youtube.com/@you]
  first_spec_project: true   # (HUMAN) true if this is their first spec-driven project
  workshop: "NAF AC6"        # where the project began; change if different
  consent_to_publish: false  # (HUMAN) set true ONLY if they agree to this card appearing on automateyournetwork.ca/arcade

build:                       # the BUILD environment — what made the game
  started: ""                # ISO date or datetime if recorded, else "unknown"
  finished: ""
  wall_time: ""              # e.g. "1h58m" — only if recorded, else "unknown"
  spec_driven:
    framework: ""            # e.g. GitHub Spec Kit, or "custom" / "none"
    framework_version: ""    # output of `specify version` if used, else "unknown"
    artifacts: []            # which exist in the repo: [constitution, spec, clarify, plan, tasks, analysis, checklists]
    task_count: 0            # tasks in tasks.md, 0 if none
    loops_or_phases: 0       # how many build loops/phases, 0 if not used
  model: ""                  # exact model ID the session reported, e.g. "claude-sonnet-5-5". Not a marketing name
  helper_models: []          # any sub-agents / secondary models, with IDs
  harness: ""                # the tool the agent ran in: Claude Code, Codex, Cursor, Copilot, Gemini CLI, OpenCode, Kiro ...
  harness_version: ""        # if known else "unknown"
  mcp_servers: []            # every MCP server connected during the build, e.g. [RFC MCP, Blender MCP, Playwright MCP]
  rag_and_sources: []        # documents, RFCs, specs, vendor docs, knowledge bases, web pages the agent drew on
  skills_and_plugins: []     # agent skills, slash commands, plugins, hooks used
  other_tools: []            # image generators, test runners, linters, browsers, CLIs
  human_prompts: 0           # how many prompts the human sent, 0 if unknown
  usage:                     # ONLY if measured by the harness. Otherwise leave "unknown"
    input_tokens: unknown
    output_tokens: unknown
    cost_note: ""            # e.g. "subscription, not metered" — never estimate
  ai_generated_assets: []    # e.g. [images: ChatGPT, 3D models: Blender MCP scripts, audio: none]

runtime:                     # what someone needs to PLAY the finished game
  kind: ""                   # static-web | node-app | python-app | docker | cli | other
  stack: []                  # e.g. [HTML, ES modules, Three.js 0.x]
  start: ""                  # exact command from repo root, e.g. python3 start.py
  url_after_start: ""        # e.g. http://localhost:8000
  hosted_url: ""             # public URL if it is deployed (GitHub Pages etc), else ""
  static_root: ""            # folder that can be served as-is by any web server, e.g. "." — "" if not static
  requires_install: false    # does the player need npm/pip install?
  requires_network: false    # internet needed while playing?
  requires_api_key: false    # any API key / login needed while playing?
  uses_ai_at_runtime: false  # does the finished game call a model?
  browsers: []               # tested browsers e.g. [Chrome 156]
  accessibility: ""          # keyboard play? reduced motion? screen reader? say what was actually tested
  save_state: ""             # e.g. "browser localStorage", "none"

verification:
  tests: ""                  # command that runs tests, e.g. node --test tests/
  tests_passing: 0           # count from the last run, 0 if no tests
  facts_sourced_from: []     # authoritative sources for the networking facts (RFCs, vendor docs)
  known_limits: []           # honest list of what the game simplifies or does not model
---

## In one paragraph

<!-- The human or agent: what is this game and who should play it? 3-5 sentences. -->

## How it was built

<!-- The BUILD AGENT writes this from its own record, in first person plural or neutral voice.
     Cover: the order the spec artifacts were written; where the human changed direction; what
     broke and how it was fixed; what you would tell the next builder. 120-250 words. No invented numbers. -->

## What we'd tell the next builder

<!-- 3 bullet points. Specific and practical. -->
-
-
-
