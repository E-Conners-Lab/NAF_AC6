# Planning research — 2026-11-04

This is design research, not the mandatory RFC fact-verification ledger or live bootstrap report.

| Decision | Rationale | Alternatives considered |
|---|---|---|
| Preserve supplied vanilla module/SVG/Three.js architecture | Small local runtime; one engine for two views. | Framework/bundler/CDN excluded by user. |
| One canonical lowercase feature directory | Works with Spec Kit scripts and case-sensitive systems. | Duplicated uppercase/lowercase specs rejected. |
| Stable tick order and exact integer arithmetic | Reproducible fixtures and truthful visual replay. | Wall-clock/random simulation rejected. |
| Separate measurement window from draining | Prevents long draining from hiding starvation. | End-of-run total throughput alone rejected. |
| Explicit queue ownership and exclusive drop causes | Prevents hidden capacity and double-counted loss. | Merger-private unlimited queues rejected. |
| Built-in ChatGPT image generation | User explicitly replaced API/key requirement in this session. | External Images API no longer required; tool model must not be guessed. |
| Five bounded implementation loops with evidence ledger | Preserves the requested sequence and honest completion. | A monolithic implementation or skipped exit rejected. |

## Mandatory MCP integration research

Research used the plan skill's research-agent step. Source inspection is not a passing live tool test.
RFC server release researched: `@mjpitz/mcp-rfc@0.2504.4`. It speaks MCP over stdio and requires
string RFC numbers. `get_rfc` formats are `full`, `metadata`, `sections`; section lookup matches
section titles. Source parsing may return a placeholder title or no sections even after a successful
HTTP response, so the gate MUST assert content. Status/update chains cannot be assumed from success.

Primary sources:
- https://github.com/mjpitz/mcp-rfc/blob/main/src/index.ts
- https://github.com/mjpitz/mcp-rfc/blob/main/src/services/rfcService.ts
- Research source commit: `5e6efbc03d46fc51a5fba8b6d7b8b58f2cecd43f`.

Blender release researched: `mcp-for-blender==2.2.7`; Python >=3.10; stdio server connects to the
Blender addon, normally localhost:9876. `get_addon_status`, `execute_blender_code` and `look` are
real tools. Discover live schemas first. Use `DISABLE_TELEMETRY=true`; run only one MCP process.
Prefer addon-only installation over setup changing unrelated client settings. For multi-angle review,
use `look` with `mode="angles"` and explicit object targets. Preserve any existing user scene.

Primary sources:
- https://github.com/ahujasid/mcp-for-blender
- https://github.com/ahujasid/mcp-for-blender/blob/main/src/blender_mcp/server.py
- https://github.com/ahujasid/mcp-for-blender/blob/main/src/blender_mcp/telemetry.py
- Research source commit: `2e4b0bc294694b1570d76ed01be657c22e6d02a0`.

## Ralph execution capability

The installed Ralph plugin's setup and stop-hook scripts target Claude Code transcripts/session hooks.
This Codex session does not expose that stop-hook runtime. Do not claim automatic re-entry is active
merely because a state file exists. Execute the same five bounded loop prompts directly in this
session and record every invocation/exit in `implementation-status.json` and `research/loops/`.
No loop beyond a failed gate may run. This host limitation is reported, not hidden by a false promise.
