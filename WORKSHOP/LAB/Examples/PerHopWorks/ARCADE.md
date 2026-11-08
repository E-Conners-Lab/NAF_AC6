---
# Completed ARCADE submission for the worked example. Facts come from README.md, research/BUILD_LEDGER.md,
# research/build-usage.json and implementation-status.json in this folder.
arcade_version: 1

game:
  title: "Per-Hop Works"
  slug: per-hop-works
  tagline: "A playable packet factory for learning DiffServ, one work order at a time."
  summary: "Players sort, mark, meter, queue and schedule packet crates on a 3D factory floor, then watch a deterministic trace show why each crate was forwarded, delayed or dropped. Twelve levels build from the DS octet to RFC 2697/2698 metering, strict priority, deficit round robin and AF drop precedence."
  topics: [DiffServ, QoS, DSCP, Policing, Queueing, RFC 4594]
  category: network-fundamentals
  skill_level: beginner
  play_minutes: 90
  levels: 12
  card_image: assets/images/title.webp
  card_image_alt: "The Per-Hop Works title scene: a factory floor where coloured packet crates travel along belts."
  repo: "https://github.com/automateyournetwork/NAF_AC6"
  repo_path: "WORKSHOP/LAB/Examples/PerHopWorks"
  license: Apache-2.0

creator:
  name: "John Capobianco"
  github: automateyournetwork
  location: "Toronto, Canada"
  organization: "Itential"
  links: ["https://www.automateyournetwork.ca"]
  first_spec_project: false
  workshop: "NAF AC6"
  consent_to_publish: true

build:
  started: "2026-11-04T18:46:43Z"
  finished: "2026-11-04T20:45:16Z"
  wall_time: "1h58m33s"
  spec_driven:
    framework: "GitHub Spec Kit"
    framework_version: unknown
    artifacts: [constitution, spec, clarify, plan, tasks, analysis, checklists]
    task_count: 69
    loops_or_phases: 5
  model: "gpt-6-astra"
  helper_models: ["one planning research helper (model ID not recorded separately)"]
  harness: "Codex"
  harness_version: unknown
  mcp_servers: ["RFC MCP", "Blender MCP"]
  rag_and_sources: ["RFC 4594", "RFC 2697", "RFC 2698", "RFC 3260", "RFC 4594 status links: RFC 5865 and RFC 8622", "48-entry RFC fact ledger"]
  skills_and_plugins: ["Spec Kit skills (constitution, specify, clarify, plan, tasks, analyze, implement)"]
  other_tools: ["Three.js (vendored, pinned)", "Chrome browser automation", "axe accessibility checks", "Node test runner"]
  human_prompts: unknown
  usage:
    input_tokens: 31129855
    output_tokens: 241999
    cost_note: "Hypothetical API-price comparison only (Standard US$48.16); the actual bill is not available. See research/BUILD_LEDGER.md."
  ai_generated_assets: ["17 procedural 3D models: Blender MCP from saved Python scripts", "10 illustrations: ChatGPT built-in image tool"]

runtime:
  kind: static-web
  stack: [HTML, CSS, "JavaScript ES modules", "Three.js (vendored)", "Python 3.11+ launcher"]
  start: "python3 start.py"
  url_after_start: "http://localhost:8000"
  hosted_url: ""
  static_root: "."
  requires_install: false
  requires_network: false
  requires_api_key: false
  uses_ai_at_runtime: false
  browsers: ["Chrome 156"]
  accessibility: "Keyboard playthroughs of all twelve levels in both renderers; ten states checked with axe (0 violations); reduced-motion setting respected; automatic SVG schematic fallback without WebGL2."
  save_state: "browser localStorage"

verification:
  tests: "node --test tests/"
  tests_passing: 78
  facts_sourced_from: ["RFC 4594", "RFC 2697", "RFC 2698", "RFC 8622", "RFC 5865"]
  known_limits: ["One-hop deterministic teaching model, not a vendor ASIC", "No TCP feedback, ECN marking or admission control", "Follows the historical 2006 RFC 4594 profile; RFC 8622 LE is noted but out of scope"]
---

## In one paragraph

Per-Hop Works turns DiffServ into a factory puzzle. Packets are crates, a sorter reads the DSCP
label, meters decide whether a crate stays in profile, and queues and schedulers decide who waits.
It is aimed at engineers who have seen "QoS" on a slide and never watched one packet make its choices.

## How it was built

The owner supplied a detailed brief with a constitution, specification and plan. Codex used Spec Kit to keep one
specification, record a clarification question, analyze it for inconsistencies and break the work into 69 tasks in five loops, each ending in an exit check.
The first loop built the engine and fact ledger before any graphics. Later loops added the SVG editor, the
3D factory, the advanced levels and the presentation mode. Owner feedback changed the build twice: the image
pipeline switched to the built-in ChatGPT tool, and a gentler welcome screen and guided first edit were added
after the owner found the topic difficult. Full records are in `research/`.

## What we'd tell the next builder

- Write the engine and the grader first; make the 3D and 2D views display the same computed result.
- Record every networking fact against an RFC before it reaches the UI.
- Add a first-edit tutorial early: the topic being hard is a design problem, not a player problem.
