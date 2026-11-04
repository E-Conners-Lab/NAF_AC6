# Engine and data contracts

These are deterministic game conventions unless explicitly tied to a verified fact. They do not
claim to reproduce a vendor router. All referenced RFC algorithms require live verification in Loop 1.

## Compilation and validation

`compileFactory(level, layout, definitions)` returns `{ valid, graph, errors }`. Errors are structured
`{ code, machine, port, message }`; invalid compilation cannot start a run. Stable topological order
uses placement ID as the final tie-breaker. Validate IDs, grid bounds, collisions, integer rotation,
known types/config, legal ports, every required output, cycles, input multiplicity, palette counts,
locked dock positions/config and trace-to-dock references. A Recycler and output dock have no outputs.
Belt connections are spatial adjacent compatible ports after rotation; editor and compiler share
this rule. A merger pulls from explicit Buffer Belts; it does not hide an unbounded queue.

## Crates, cohorts and terminal outcomes

Crates have unique IDs, positive integer bytes, immutable source dock, application/service class,
original octet and arrival index; mutable DSCP, ECN, meter color and location are separate. Marking
preserves ECN. Metric service-class cohorts never change when DSCP is re-marked. AF loss cohorts are
captured when entering the assessed AF queue; re-marking after that cannot change the denominator.
Each crate receives exactly one terminal event: delivery or a drop with one exclusive cause:
`policer`, `tail_drop`, `aqm`, `recycler`. A Recycler reached on an excess policing branch records
`policer`, not two causes. A debug snapshot may include in-flight crates, but a final passing run may not.

## Tick order, meter arithmetic and completion

Each trace defines integer `tick_ms`, arrivals in stable input order, `measurement_start_tick`,
`measurement_end_tick` (exclusive) and `max_drain_ticks`. Arrivals and capacity are fixed data.
At tick start, refill meters for elapsed simulated time; tick zero starts with full buckets. Process
arrivals, then machines in stable topological order, then output scheduling, then snapshot/metrics.
Zero-time processing across machines is allowed within this order; an L-tile belt adds L ticks.

Rates are integer bytes/second; rates × elapsed milliseconds accumulate integer milli-byte credit.
For RFC meters, credit produces whole byte tokens at the rate clock; retain the sub-byte remainder.
Apply committed-before-excess overflow for srTCM and independent peak/committed clocks for trTCM.
Saturating full buckets discard surplus whole-byte credit; exact boundary tests establish behavior.
Reject values whose safe-integer arithmetic could overflow. No wall-clock reads or randomness.

After the measurement window stops offering arrivals, continue until all crates terminate or the
bounded drain limit expires. An expired run returns `complete:false`, an in-flight inventory and a
failure diagnostic. No artificial delivery or drop is invented to make conservation pass.

## Queues, capacity and scheduling

Buffer Belts own FIFO storage and count capacity in crates; full admission tail-drops. Plain belts
are lossless transit. Queuing delay sums waiting ticks in explicit Buffer Belts, excluding belt
transit and zero-time processing. Every metered service path to a merger uses an explicit buffer.
A direct output path in introductory levels is validated against its fixed trace/capacity; overload
without an explicit queue is an invalid work-order/layout combination, never an invisible drop.

The output capacity is integer bytes per tick, reset each tick without carry. Reject an offered crate
larger than its eligible output's complete tick capacity. Priority is served before weighted inputs;
if the priority head cannot fit the remaining budget, service stops for that tick. Weighted inputs
use persistent DRR deficits and a persistent round-robin cursor; quantum is a declared base byte
quantum times a positive integer weight. Add quantum once per queue visit, retain deficit while
backlogged, reset it when empty, and never reorder a queue to fit a smaller packet. An unaffordable
weighted head advances the cursor; bounded empty scans prevent a spinning tick. A packet that has
enough deficit but cannot fit remaining capacity waits for the next tick with deficit preserved.
The precise cursor transition is covered by mixed-size golden event sequences.

## AQM

Depth q is sampled before enqueue. Validate `0 <= min < max <= capacity` and the complete AF
inequality chain. If q <= min, probability is zero; if min < q < max, probability rises linearly to
max_p; if q >= max, drop deterministically. Represent probabilities/accumulators as exact rational
integer values (BigInt where necessary, serialize as decimal strings), not repeated float addition.
Each DSCP owns an accumulator, initialized/reset only at run start. A forced maximum drop leaves the
accumulator unchanged. Otherwise accumulate the fraction, drop at >=1 and subtract 1. AQM admission
runs before capacity admission, giving one exclusive drop cause. Loss order uses all terminal drops
in the declared AF cohorts and explicitly requires positive offered counts for each compared DSCP.
The briefing explains that these finite-trace checks do not establish random loss probabilities.

## Grading and diagnostics

`runSimulation(level, graph, trace, submission)` returns plain serializable snapshots/events/metrics.
`evaluateRun(level, graph, result)` returns `{passed, checks:[{id,passed,expected,actual,culprit,
crates,diagnostic,source}]}`. Submission is captured with the run; changing predictions or layout
invalidates any old grade. Unknown checks and absent required parameters fail visibly.

| Check | Additional contract |
|---|---|
| VALID | Compiler success, locked docks and valid trace included. |
| CONSERVATION | Complete run; unique terminal IDs equal the offered set; no duplication. |
| ROUTE | Every required crate delivered to assigned dock; drops fail. |
| PREDICT | Complete engine-computed route/precedence answers equal all submitted answers. |
| MARK | Profile targets, including meter-color variants, match; required deliveries cannot be dropped away. |
| TRUST | No prohibited original untrusted marking survives; trusted/contracted delivery obligations still apply. |
| METER-PREDICT | Complete engine color sequence, including two-part levels, matches captured submissions. |
| METER-MODE | Trusted-preservation paths use aware; untrusted paths use blind, from work-order policy. |
| POLICE-EF | All paths to priority have effective policing; required contracted EF passes; excess is dropped. |
| DELAY-BOUND | Required EF delivered, max explicit queuing delay <= declared tick bound. |
| MIN-SHARE | Delivered bytes during measurement window meet per-class minimum byte budgets; draining cannot help. |
| STANDARD-PRESENT | A reachable dedicated DF buffer and positive weighted service allocation exist. |
| NO-AQM-ON | Analyze feasible classifier paths for prohibited classes; do not inspect only machines used by this trace. |
| RED-THRESHOLDS | Return each failed inequality individually with configured values and queue capacity. |
| LOSS-ORDER | Nonempty cohorts; exact cross-multiplied fractions ordered AFx1 <= AFx2 <= AFx3. |

Static path analysis covers feasible first-match routes, trust preservation, policing and AQM
placement. Measured diagnostics detect starvation, loss inversion and delay. Diagnostics reference
fact IDs, never invent a source. Each failed fixture asserts both check ID and diagnostic ID.
`engine/state.js` only validates/serializes plain saves; `main.js` performs localStorage I/O.
