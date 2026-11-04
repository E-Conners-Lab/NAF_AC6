# RFC MCP compatibility repair

Upstream: `@mjpitz/mcp-rfc@0.2504.4`, Apache-2.0 (original package license retained in installed dependency).
Install: `npm ci --ignore-scripts` here. Launch: `node compat.mjs` (MCP stdio).
This is developer tooling, never loaded by the game.

The unmodified server retrieved correct HTML but returned no sections because it looked only for
HTML `section` elements. The current RFC Editor legacy document presentation uses numbered anchors
inside preformatted page blocks. `compat.mjs` extends only that parser when no sections were found,
using the real document anchors and DOM ranges. It imports and runs the unchanged upstream MCP
server; no RFC wording, claimed facts or answers are hardcoded. Returned metadata identifies the patch.

The upstream numeric substring matcher remains ambiguous (4.3 may match 1.4.3); use exact section
titles and inspect returned number/title. The bootstrap gate explicitly allows the title fallback.
Raw original failed calls are retained as `research/tool-results/rfc-upstream-failure.json`.
Validate repair against real current HTML and live MCP calls; package startup is insufficient.
