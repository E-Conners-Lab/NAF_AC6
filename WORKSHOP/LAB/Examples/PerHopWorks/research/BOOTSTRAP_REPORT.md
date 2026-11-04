# Bootstrap report — 2026-11-04

Loop 1, T001. Overall gate: **OPEN after documented RFC parser repair and live re-test**.
Original failed calls remain preserved; no substitute verification was used.

| Gate | Result | Evidence |
|---|---|---|
| Node >=20 | PASS | v25.3.0 |
| Python >=3.11 | PASS | 3.14.6 |
| uv / uvx | PASS | uv 0.10.12; uvx successfully installed/launched MCP package |
| specify check | PASS | Exit 0; CLI ready |
| RFC MCP metadata 2474 | PASS | Correct title contains Differentiated Services; `tool-results/rfc-smoke.json` |
| RFC MCP 4594 section 4.3 | FAIL | Numeric lookup returned section not found |
| RFC MCP title retry | PASS after repair | Exact section 4.3 with AF41 returned by upstream MCP plus documented HTML compatibility parser |
| Blender MCP addon | PASS | mcp-for-blender 2.2.7, addon 1.8, protocol 15, Blender 5.2.1 LTS |
| Blender GLB export | PASS | 1784-byte valid glTF binary exported through execute_blender_code, then deleted |
| ChatGPT built-in image tool | PASS | Generated/decoded square RGB image, copied smoke deleted; `tool-results/image-status.json` |

## Installation and environment

Repository `.mcp.json` pins RFC MCP 0.2504.4 and Blender MCP 2.2.7. The Blender addon was installed,
enabled and started in a new Blender session via `scripts/enable_blender_mcp.py`. No human reload was
needed. Only one Blender MCP process was used at a time. Telemetry is disabled in both server and
addon; no third-party libraries or model generators are enabled.

The user explicitly replaced the external Images API/key gate with built-in ChatGPT generation.
Actual generated size was 1254×1254 despite requesting 1024×1024; the live-generation/decode gate
passes for a square smoke artifact, with actual dimensions recorded. No specific model ID is exposed.
The original generated image remains in the tool output location; it is not a production asset.

The first smoke client run used the old SDK isError attribute and failed after a real tool response.
The local client was corrected to support the installed is_error field and the checks rerun. Those
client errors were not presented as server passes. The live RFC section failure persists after repair.

## Required next step

Investigate genuine RFC MCP retrieval/parsing and log any repair/version change explicitly. Do not
write data/facts.json from an empty/error response. No placeholder fact or alternate-tool result can
open this gate.

## Successful repair

`tools/rfc-mcp/compat.mjs` extends the installed upstream parser for the current RFC Editor
numbered-anchor HTML. MCP tool implementations and network fetch remain upstream. No RFC words
or answers are hardcoded. Live re-test returned the exact section 4.3 via title. Numeric substring
lookup instead matched 1.4.3, so title lookup is the supported form and returned numbers must be
checked. Original failed response: `tool-results/rfc-upstream-failure.json`; successful response:
`tool-results/rfc-smoke.json`. User supplied authoritative RFC Editor links for 4594, 5865, 8622.
