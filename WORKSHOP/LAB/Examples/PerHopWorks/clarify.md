# Clarification record — Per-Hop Works

Date: 2026-11-04. Single clarify pass; one question asked and answered by the user.
The record separates supplied answers from implementation assumptions.

| Question | Answer / decision | Evidence |
|---|---|---|
| How many specs and implementation loops? | One spec; exactly five ordered loops, each with a hard exit. | Explicit user request and supplied plan. |
| How does the browser start? | Local static server, one documented launcher; never file://. | Supplied plan; launcher is an implementation choice. |
| Can missing tools be substituted? | No. A live tool failure stops Loop 1. | Supplied constitution and tool gate. |
| Is correctness based on factory shape? | No, measured outcomes and RFC-derived checks; many solutions can pass. | Supplied constitution. |
| Where are prediction answers stored? | They are computed by the engine; data stores question descriptors and player responses only. | Supplied plan. |
| Who approves assets and explanations? | A real human reviewer, recorded after reviewing the concrete artifact. | Supplied constitution and level definition of done. |
| Can presenters open Demo immediately while Campaign stays gated? | “Demo always available; campaign stays gated (Recommended).” FR-011 records this answer. | Explicit user reply in this session. |

## Coverage assessment

| Taxonomy | Status | Resolution |
|---|---|---|
| Functional scope and behavior | Clear | Twelve levels, campaign, schematic and ungraded Demo. |
| Domain and data model | Resolved in plan | Stable identities, terminal results, exact meter/scheduler contracts. |
| Interaction and UX | Resolved by user answer | Presenter entry independent of campaign; full keyboard editing. |
| Non-functional quality | Clear | Explicit budgets; offline runtime, deterministic runs, local-only storage. |
| Integrations and dependencies | Clear; gate pending | Three mandatory live services, no substitutions. |
| Edge cases and failure handling | Resolved | Invalid data, graph, saves and incomplete runs fail visibly. |
| Constraints and tradeoffs | Clear | Supplied stack and exclusions retained. |
| Terminology and consistency | Resolved | DSCP versus ECN; measured loss versus probability; cause-exclusive drops. |
| Completion signals | Clear | Per-level, per-loop and global evidence; human review is distinct. |
| Placeholders | Clear | Illustrative plan JSON is not production game data. |

No additional product question blocks planning. Tool access and human reviews are execution gates,
not inferred approvals. Technical choices and contradictions are recorded in `research.md` and
`analysis.md`; implementation must not silently change the specified curriculum.

## Subsequent explicit user direction

“you can use your image api no key needed make the images using chatgpt” replaces the external image
API/key requirement. “what gates install them ... blender cli should be available” authorizes installing
and configuring the required MCP servers/addon. These are volunteered instructions, not additional
clarification questions. Constitution v1.1.0 and plan record the image-provider amendment.

## Implementation clarification and review requests

The user supplied the RFC Editor pages for RFC 4594, RFC 5865 and RFC 8622. All three statuses and
update texts were checked through the real RFC MCP and retained locally. A follow-up question was
asked about L12: use current LE (DSCP 1) with an update note, or present the original CS1 mapping as
historical. **No answer has been received.** Do not record the recommended option as an answer or
silently change the spec's LE exclusion. This affects L12 content, not the completed introductory levels.

After all 17 Blender models were built and reviewed, the user was given the concrete review page
`http://localhost:8000/tools/browser/asset-review.html` and asked to approve the full set or request
specific changes. **Human approval is pending.** The requirement comes from the user's Loop 3 exit,
not an extra approval policy introduced by the implementation. `assets/manifest.json` records null
approvers until an actual answer is received.

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
