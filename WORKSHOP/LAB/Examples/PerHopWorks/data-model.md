# Data model

| Entity | Identity and fields | Relationships / validation |
|---|---|---|
| Level | L01–L12; act, title, concept, type, profile, briefing, hints, checks | Prerequisites form the fixed ordered curriculum; facts cover copy. |
| Work order | tick_ms, input/output docks, palette, locked IDs, bounds, measurement window, drain limit | References one arrival trace; declares all numeric check parameters. |
| Trace arrival | crate ID, tick, input dock, size bytes, octet, shipping label, initial color | Unique IDs, stable order, positive bytes, valid dock, tick >=0. |
| Machine definition | type, footprint, ports, config schema, element/source/facts, model | Ports rotate with placement; all factual descriptions verified. |
| Placement | machine ID, type, x/y, rotation, config | Within bounds, no overlap, palette limits; locked docks immutable. |
| Factory graph | nodes, typed spatial edges, stable topological order | Output completeness, no cycles, semantic path analysis. |
| Crate state | ID, immutable ingress/class/original octet; current DSCP/ECN/color/location | Preserves identity/cohort through marking; ECN is read-only. |
| Snapshot | tick, crate positions, machine tokens/queues/gates, cumulative metrics | Display-only immutable record; no renderer correctness logic. |
| Event | monotonic sequence, tick, crate, machine, action, before/after, cause | Complete trace; terminal events exclusive and unique. |
| Class metric | offered/delivered counts and bytes, cause-specific drops, loss fraction, delays | Measurement-window throughput separate from final totals. |
| Prediction | question ID, query descriptor, player response | No correct answer literal in level or solution data; engine resolves query. |
| Check result | ID, passed, expected, actual, culprit, crates, diagnostic, source | Unknown/undefined required check fails; single grader. |
| Diagnostic | ID, why_wrong, concept_reinforced, source, facts, human review | Static and measured rules identify IDs, UI displays source data. |
| Fact | F-NNNN, claim, source, RFC status, verification ID, verified_with/on | Only authored after successful live RFC MCP verification. |
| Verification | V-NNNN, time, tool/version, exact args, response artifact/hash, assertion | Append-only evidence; errors are logged but never qualify a fact. |
| Solution fixture | factory/config; known-wrong intended check + diagnostic | Reference predictions computed at test time; fixtures never drive runtime answers. |
| Asset | ID, path, tool, model/version if exposed, prompt/script, timestamp, license, approver | SHA-256, dimensions/triangles, budgets, review status; unknown model never invented. |
| Demo beat | ID, start/end ticks, camera control points, target crate/machine | Showcase references L12 factory; no campaign write path. |
| Save | schema/content version, completed levels, drafts, settings | Plain validation in engine; browser adapter owns storage. |

Run lifecycle: editing → validating → running ↔ paused → complete → graded → retry/debrief.
Invalid validation returns to editing. Drain timeout produces an incomplete failed result.
Any edit after a run invalidates its captured result. UI and rendering cannot advance campaign state
without a passing grader result for the current submission.
