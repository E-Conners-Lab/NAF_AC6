# RFC MCP verification ledger

Every row is a real live MCP call. Full returned text is preserved for claim review.
Retrieval alone does not certify a claim; facts reference a record only after inspecting its text.
Bootstrap get_rfc/get_rfc_section calls, including failures, are separately retained in
`tool-results/rfc-upstream-failure.json` and `tool-results/rfc-smoke.json`.

| ID | Time UTC | Tool and arguments | Artifact | SHA-256 |
|---|---|---|---|---|
| V-0001 | 2026-11-04T19:07:28.458811+00:00 | get_rfc {"number": "2474", "format": "full"} | [rfc/rfc2474-mcp.json](rfc/rfc2474-mcp.json) | 5cc9df96e64ee4ce89ea512e4feb3cc2131eb4b2e0dee54079cc9091bb426991 |
| V-0002 | 2026-11-04T19:07:29.451513+00:00 | get_rfc {"number": "2475", "format": "full"} | [rfc/rfc2475-mcp.json](rfc/rfc2475-mcp.json) | 4161e2a81b908fd1ecc6878c7cfda857ea95b0a6c9e804c9a333617006a53546 |
| V-0003 | 2026-11-04T19:07:30.144190+00:00 | get_rfc {"number": "2597", "format": "full"} | [rfc/rfc2597-mcp.json](rfc/rfc2597-mcp.json) | 6cd81fc021b724e47a7e0f1e7b8b532898fb6166c07386b423c4792b5867f0df |
| V-0004 | 2026-11-04T19:07:30.791990+00:00 | get_rfc {"number": "2697", "format": "full"} | [rfc/rfc2697-mcp.json](rfc/rfc2697-mcp.json) | e3aed68074b0be9293316eddd70f5e14bffd9bce27da5b72affe155ecc4d4d44 |
| V-0005 | 2026-11-04T19:07:31.580701+00:00 | get_rfc {"number": "2698", "format": "full"} | [rfc/rfc2698-mcp.json](rfc/rfc2698-mcp.json) | 4ec9520ceed497e38db4f5c5802b924ea3344308672b687f62f3ce7dbe2afe66 |
| V-0006 | 2026-11-04T19:07:33.035985+00:00 | get_rfc {"number": "3168", "format": "full"} | [rfc/rfc3168-mcp.json](rfc/rfc3168-mcp.json) | ec9e38eff5a1f544bcc4bc37b6655c47128cbec8e67ee2e0b576adb49432ded5 |
| V-0007 | 2026-11-04T19:07:33.896101+00:00 | get_rfc {"number": "3246", "format": "full"} | [rfc/rfc3246-mcp.json](rfc/rfc3246-mcp.json) | d95ace92e32c36d6fa339e60ee3ce65d8ad8dcf2ff4431ea2b842e9161796aa2 |
| V-0008 | 2026-11-04T19:07:34.645533+00:00 | get_rfc {"number": "3260", "format": "full"} | [rfc/rfc3260-mcp.json](rfc/rfc3260-mcp.json) | 63b8aeb4c481c483c2c361ce2dcab4cff2f195915d52ebfbc67b1c4677ec9ee0 |
| V-0009 | 2026-11-04T19:07:35.721411+00:00 | get_rfc {"number": "3290", "format": "full"} | [rfc/rfc3290-mcp.json](rfc/rfc3290-mcp.json) | 26b619de51f940ec7dde34dee4e3d42157531df19db8fb63acd4d29d92548bcc |
| V-0010 | 2026-11-04T19:07:36.771157+00:00 | get_rfc {"number": "4594", "format": "full"} | [rfc/rfc4594-mcp.json](rfc/rfc4594-mcp.json) | 410f179330eb6ae1f4cb09e38998c32530033defe25f8e4362f55b93a8c04348 |
| V-0011 | 2026-11-04T19:07:37.542057+00:00 | get_rfc {"number": "2598", "format": "full"} | [rfc/rfc2598-mcp.json](rfc/rfc2598-mcp.json) | 7efc0f476e12872b0fd3d9b2bc044c5ab1985532cfc2472b97b1c8367c73e31b |
| V-0012 | 2026-11-04T19:07:38.266967+00:00 | get_rfc {"number": "5865", "format": "full"} | [rfc/rfc5865-mcp.json](rfc/rfc5865-mcp.json) | 8bbd1f99d5e3fcc0cc0211ad2185e43b01768eca0a31c60d1cc7db2c2326b64a |
| V-0013 | 2026-11-04T19:07:39.117241+00:00 | get_rfc {"number": "8622", "format": "full"} | [rfc/rfc8622-mcp.json](rfc/rfc8622-mcp.json) | 46a9aa4cbb8b7dbf52696f2528841bf940606ea407e2d45750367be56af7c9d0 |
| V-0014 | 2026-11-04T20:28:41.505419+00:00 | get_rfc {"number": "2474", "format": "full"} (final audit) | [rfc/final/rfc2474-mcp.json](rfc/final/rfc2474-mcp.json) | 5cc9df96e64ee4ce89ea512e4feb3cc2131eb4b2e0dee54079cc9091bb426991 |
| V-0015 | 2026-11-04T20:28:42.156684+00:00 | get_rfc {"number": "2475", "format": "full"} (final audit) | [rfc/final/rfc2475-mcp.json](rfc/final/rfc2475-mcp.json) | 4161e2a81b908fd1ecc6878c7cfda857ea95b0a6c9e804c9a333617006a53546 |
| V-0016 | 2026-11-04T20:28:42.586196+00:00 | get_rfc {"number": "2597", "format": "full"} (final audit) | [rfc/final/rfc2597-mcp.json](rfc/final/rfc2597-mcp.json) | 6cd81fc021b724e47a7e0f1e7b8b532898fb6166c07386b423c4792b5867f0df |
| V-0017 | 2026-11-04T20:28:42.940355+00:00 | get_rfc {"number": "2697", "format": "full"} (final audit) | [rfc/final/rfc2697-mcp.json](rfc/final/rfc2697-mcp.json) | e3aed68074b0be9293316eddd70f5e14bffd9bce27da5b72affe155ecc4d4d44 |
| V-0018 | 2026-11-04T20:28:43.334431+00:00 | get_rfc {"number": "2698", "format": "full"} (final audit) | [rfc/final/rfc2698-mcp.json](rfc/final/rfc2698-mcp.json) | 4ec9520ceed497e38db4f5c5802b924ea3344308672b687f62f3ce7dbe2afe66 |
| V-0019 | 2026-11-04T20:28:44.486839+00:00 | get_rfc {"number": "3168", "format": "full"} (final audit) | [rfc/final/rfc3168-mcp.json](rfc/final/rfc3168-mcp.json) | ec9e38eff5a1f544bcc4bc37b6655c47128cbec8e67ee2e0b576adb49432ded5 |
| V-0020 | 2026-11-04T20:28:45.046932+00:00 | get_rfc {"number": "3246", "format": "full"} (final audit) | [rfc/final/rfc3246-mcp.json](rfc/final/rfc3246-mcp.json) | d95ace92e32c36d6fa339e60ee3ce65d8ad8dcf2ff4431ea2b842e9161796aa2 |
| V-0021 | 2026-11-04T20:28:45.597453+00:00 | get_rfc {"number": "3260", "format": "full"} (final audit) | [rfc/final/rfc3260-mcp.json](rfc/final/rfc3260-mcp.json) | 63b8aeb4c481c483c2c361ce2dcab4cff2f195915d52ebfbc67b1c4677ec9ee0 |
| V-0022 | 2026-11-04T20:28:46.674049+00:00 | get_rfc {"number": "3290", "format": "full"} (final audit) | [rfc/final/rfc3290-mcp.json](rfc/final/rfc3290-mcp.json) | 26b619de51f940ec7dde34dee4e3d42157531df19db8fb63acd4d29d92548bcc |
| V-0023 | 2026-11-04T20:28:47.926375+00:00 | get_rfc {"number": "4594", "format": "full"} (final audit) | [rfc/final/rfc4594-mcp.json](rfc/final/rfc4594-mcp.json) | 410f179330eb6ae1f4cb09e38998c32530033defe25f8e4362f55b93a8c04348 |
| V-0024 | 2026-11-04T20:28:48.391449+00:00 | get_rfc {"number": "2598", "format": "full"} (final audit) | [rfc/final/rfc2598-mcp.json](rfc/final/rfc2598-mcp.json) | 7efc0f476e12872b0fd3d9b2bc044c5ab1985532cfc2472b97b1c8367c73e31b |
| V-0025 | 2026-11-04T20:28:48.839031+00:00 | get_rfc {"number": "5865", "format": "full"} (final audit) | [rfc/final/rfc5865-mcp.json](rfc/final/rfc5865-mcp.json) | 8bbd1f99d5e3fcc0cc0211ad2185e43b01768eca0a31c60d1cc7db2c2326b64a |
| V-0026 | 2026-11-04T20:28:49.441325+00:00 | get_rfc {"number": "8622", "format": "full"} (final audit) | [rfc/final/rfc8622-mcp.json](rfc/final/rfc8622-mcp.json) | 46a9aa4cbb8b7dbf52696f2528841bf940606ea407e2d45750367be56af7c9d0 |
