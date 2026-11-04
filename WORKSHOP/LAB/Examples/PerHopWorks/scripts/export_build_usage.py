#!/usr/bin/env python3
"""Export usage metadata only from the two local Codex build logs; no transcript bodies."""

import argparse
import csv
import hashlib
import io
import json
from datetime import datetime
from decimal import Decimal
from pathlib import Path

START = "2026-11-04T18:46:43.213Z"
FINISH = "2026-11-04T20:45:16.332Z"
# The final response's usage and task-complete records follow its visible message.
CUTOFF = "2026-11-04T20:45:16.411Z"
KEYS = ("input_tokens", "cached_input_tokens", "cache_write_input_tokens",
        "output_tokens", "reasoning_output_tokens", "total_tokens")


def read_usage(path, label):
    events = [json.loads(line) for line in path.read_text().splitlines()]
    meta = next(e["payload"] for e in events if e["type"] == "session_meta")
    models = {e["payload"]["model"] for e in events if e["type"] == "turn_context"
              and START <= e["timestamp"] <= CUTOFF}
    if models != {"gpt-6-astra"}:
        raise ValueError(f"Unexpected models for {label}: {models}")
    unique = {}
    for event in events:
        if event["type"] != "token_usage_record" or not START <= event["timestamp"] <= CUTOFF:
            continue
        payload = event["payload"]
        if payload["thread_id"] != meta["id"]:
            continue  # Forked parent history is not new delegate usage.
        response_id = payload["response_id"]
        if response_id in unique and unique[response_id]["payload"]["usage"] != payload["usage"]:
            raise ValueError("Conflicting duplicate usage record")
        unique[response_id] = event
    records = sorted(unique.values(), key=lambda e: e["timestamp"])
    if not records:
        raise ValueError(f"No usage records for {label}")
    totals = {key: sum(e["payload"]["usage"][key] for e in records) for key in KEYS}
    if totals != records[-1]["payload"]["thread_token_usage"]:
        raise ValueError(f"Per-response and thread totals disagree for {label}")
    rows = []
    for event in records:
        usage = event["payload"]["usage"]
        if usage["total_tokens"] != usage["input_tokens"] + usage["output_tokens"]:
            raise ValueError("Invalid token subtotal")
        if not 0 <= usage["cached_input_tokens"] <= usage["input_tokens"]:
            raise ValueError("Invalid cache subtotal")
        rows.append({"timestamp_utc": event["timestamp"], "agent": label,
                     "model": "gpt-6-astra", **{key: usage[key] for key in KEYS}})
    return rows, {"agent": label, "response_count": len(rows), "usage": totals,
                  "reconciled_with_thread_total": True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("parent_log", type=Path)
    parser.add_argument("research_log", type=Path)
    parser.add_argument("--output-dir", type=Path,
                        default=Path(__file__).resolve().parents[1] / "research")
    args = parser.parse_args()
    rows, agents = [], []
    for path, label in [(args.parent_log, "primary"), (args.research_log, "plan_research")]:
        agent_rows, agent = read_usage(path, label)
        rows.extend(agent_rows)
        agents.append(agent)
    rows.sort(key=lambda row: (row["timestamp_utc"], row["agent"]))
    totals = {key: sum(row[key] for row in rows) for key in KEYS}
    uncached = totals["input_tokens"] - totals["cached_input_tokens"]
    maximum = max(row["input_tokens"] for row in rows)
    if maximum > 272000 or totals["cache_write_input_tokens"]:
        raise ValueError("Pricing assumptions need updating")
    standard = (Decimal(uncached) * 10 + Decimal(totals["cached_input_tokens"])
                + Decimal(totals["output_tokens"]) * 50) / 1000000
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=["timestamp_utc", "agent", "model", *KEYS],
                            lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    csv_bytes = stream.getvalue().encode()
    summary = {
        "scope": "Original game build; excludes later documentation and publication work",
        "start_utc": START, "finish_utc": FINISH, "usage_cutoff_utc": CUTOFF,
        "elapsed_seconds": (datetime.fromisoformat(FINISH) - datetime.fromisoformat(START)).total_seconds(),
        "model": "gpt-6-astra", "service_tier": "not recorded",
        "agents": agents, "response_count": len(rows), "usage": totals,
        "uncached_input_tokens": uncached, "maximum_request_input_tokens": maximum,
        "cached_input_is_subset_of_input": True, "reasoning_output_is_subset_of_output": True,
        "image_generations": {"production": 10, "disposable_smoke": 1,
                              "model": "not exposed by tool", "image_token_usage": None},
        "pricing": {
            "checked_on": "2026-11-04", "currency": "USD",
            "kind": "Hypothetical text-model API-equivalent scenarios, not actual billed cost",
            "source": "https://developers.openai.com/api/docs/models/gpt-6-astra",
            "subscription_source": "https://learn.chatgpt.com/docs/pricing",
            "standard_rates_per_million": {"uncached_input": 10, "cached_input": 1, "output": 50},
            "standard_usd": str(standard), "fast_usd": str(standard * 2),
            "actual_billed_usd": None,
            "excluded": ["image generation", "separate tool fees", "subscription allocation",
                         "tax", "hardware and electricity", "human labor", "prior specification authoring",
                         "post-build documentation and Git publication"]
        },
        "csv": {"path": "build-usage.csv", "sha256": hashlib.sha256(csv_bytes).hexdigest()},
        "method": "Unique token_usage_record response IDs, exact thread ID, inclusive time window; sums reconciled against each thread total. Only allowlisted usage metadata is exported."
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "build-usage.csv").write_bytes(csv_bytes)
    (args.output_dir / "build-usage.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps({"responses": len(rows), "total_tokens": totals["total_tokens"],
                      "elapsed_seconds": summary["elapsed_seconds"], "standard_usd": str(standard)}))


if __name__ == "__main__":
    main()
