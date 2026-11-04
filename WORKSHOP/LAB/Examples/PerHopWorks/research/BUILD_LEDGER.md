# Build time, tokens and cost

This ledger covers the original Per-Hop Works implementation on **November 4, 2026**. The game
started from supplied constitution, specification and planning documents. Their earlier authoring
time and cost are unknown. The later README/accounting update and Git publication are outside this
measurement window.

## Start and finish

| Boundary | UTC | America/Toronto (EST, UTC−05:00) | Evidence |
|---|---|---|---|
| Build request received | 2026-11-04 18:46:43.213 | 2026-11-04 13:46:43.213 | Original user message |
| Completed game reported | 2026-11-04 20:45:16.332 | 2026-11-04 15:45:16.332 | Final assistant response after Loop 5 |
| Elapsed wall time | **1 h 58 min 33.119 s** | **7,113.119 seconds** | Finish minus start |

Wall time includes tool execution, downloads, image generation, testing and the pause for owner
review. It is not a measurement of GPU compute time or human labor. The session itself was created
earlier; session creation is not used as the build start. The final usage record arrived four
milliseconds after the final response; accounting includes records through the task-complete
event at **20:45:16.411 UTC**.

The public progress reports give this approximate timeline. These are reporting timestamps,
not instrumented execution boundaries for individual stages.

| Report time (UTC) | Milestone |
|---|---|
| 18:47:14 | Existing three source documents found; no game implementation yet |
| 19:01:02 | Spec Kit artifacts, analysis and 69 tasks organized into five loops |
| 19:18:51 | Loop 1 exit: engine, 48 facts and 37 passing tests |
| 19:33:38 | Loop 2 exit: first five levels completed by keyboard in schematic mode |
| 19:46:20 | Loop 3 technical checks passed; owner model review remained |
| 20:00:43 | Owner approved models and requested a gentler introduction |
| 20:21:43 | Loop 4 exit: twelve levels, 71 tests and browser checks; Loop 5 underway |
| 20:45:16 | Loop 5 complete: finished game, art, Demo, onboarding and 78 tests |

## Measured model usage

The original session metadata identifies **`gpt-6-astra`**. One planning research helper was used.
Its usage is included separately, without counting its inherited parent history twice.

| Agent | Responses | Input | Cached input (included in input) | Output | Total input + output |
|---|---:|---:|---:|---:|---:|
| Primary | 219 | 30,379,750 | 29,864,192 | 239,449 | 30,619,199 |
| Planning research helper | 7 | 750,105 | 717,312 | 2,550 | 752,655 |
| **Combined** | **226** | **31,129,855** | **30,581,504** | **241,999** | **31,371,854** |

Uncached input is **548,351 tokens**. Approximately **98.2% of input** was cached. The total counts
context processed repeatedly across requests; it does not mean 31 million tokens of new code or
unique prose were written. Output includes **57,325 reasoning tokens**, already counted inside
241,999 output tokens. Neither cached input nor reasoning is added a second time. Recorded cache
write tokens are zero. The largest individual request contained 245,500 input tokens.

The [CSV](build-usage.csv) contains one usage row per response. The [JSON summary](build-usage.json)
contains totals, assumptions, rates and the CSV's SHA-256 hash. No raw conversation logs, private
reasoning text, account balances or credentials are published.

## Estimated money: API-equivalent scenarios

**Actual billed dollars are unavailable.** The following calculation prices the measured text-model
usage as if it had been sent through the API at the published rates. It is not an invoice, a claim
about subscription allowance consumed, or an all-in project cost.

Rates checked on **2026-11-04**: $10 per million uncached input tokens, $1 per million cached input
tokens and $50 per million output tokens for GPT-6 Astra Standard. The published Fast multiplier
is 2×. No recorded request crosses the 272,000-input-token long-context threshold.
[Official model pricing](https://developers.openai.com/api/docs/models/gpt-6-astra).

| Component | Calculation | USD before rounding |
|---|---|---:|
| Uncached input | 548,351 ÷ 1,000,000 × $10 | $5.483510 |
| Cached input | 30,581,504 ÷ 1,000,000 × $1 | $30.581504 |
| Output, including reasoning | 241,999 ÷ 1,000,000 × $50 | $12.099950 |
| **Standard API-equivalent scenario** | Sum | **$48.164964 → $48.16** |
| **Fast API-equivalent scenario** | Standard × 2 | **$96.329928 → $96.33** |

The session does not record its service tier, so these are two illustrative pricing scenarios.
They are not bounds on the actual charge. Subscription usage and API billing are separate, and
image generation also consumes usage. [Official Codex pricing](https://learn.chatgpt.com/docs/pricing).

There were **11 image generations: ten production images and one disposable smoke test**. They
used ChatGPT's built-in image tool following the owner's instruction. It did not expose an image
model ID, image-token count or billed amount. Image-generation cost therefore remains **unknown**
and is excluded from both scenarios; it is not assumed to be free or priced as `gpt-image-2`.
Text-model calls around asset creation remain included in the measured ledger.

Other exclusions are separate tool fees, subscription allocation, taxes, hardware, electricity,
human labor, earlier specification authoring, and later documentation/publication. The finished
game makes no runtime AI/API calls: running the local static game adds no model usage.

## How to reproduce the accounting

The exporter uses Python's standard library. With access to the two original local session logs,
run from the example directory:

```sh
python3 scripts/export_build_usage.py /path/to/primary-session.jsonl /path/to/planning-session.jsonl
```

The [exporter](../scripts/export_build_usage.py) applies the fixed build window, selects only
`token_usage_record` events with the exact owning thread ID, deduplicates response IDs and sums
their individual `usage` fields. It checks the sum against each thread's final cumulative total.
It does not sum cumulative counters or count the forked parent context as fresh helper requests.
Only an allowlist of timestamp, agent label, model and numeric usage fields reaches the CSV.
The committed CSV and JSON are sufficient to independently recompute the published arithmetic;
the private source logs are needed only to re-export those rows.
