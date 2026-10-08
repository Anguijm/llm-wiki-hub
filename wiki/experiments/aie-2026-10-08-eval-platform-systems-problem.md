# Close the Production-to-Eval Loop by Letting Coding Agents Auto-Generate Eval Cases from Failure Traces

> Back to [[experiments-index]]

Source: **[Why Building an Eval Platform Is Harder Than It Looks — Braintrust](https://www.youtube.com/watch?v=mUQoVz7THu0)** · aie · 2026-10-08

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we wire a coding agent with access to production traces and eval infrastructure so it can automatically identify failure modes, create new test cases from those failures, run evals offline, and propose agent implementation changes—with humans only reviewing diffs—then the improvement loop will run faster and surface unknown failure patterns that manual review would miss, because the agent can process trace volume at a scale no human team can match.

## What they did

Braintrust's Hussein described the evolution of eval platforms from spreadsheet-based scoring toward a fully automated improvement loop. The North Star pattern is: observe production failure modes → extract them as test cases → iterate offline to improve the agent → validate no regressions → deploy → repeat. He described how coding agents with access to tracing data and eval infrastructure can now execute this loop: querying traces in natural language, running evals, logging results, and proposing changes. Humans review the outcome (which iteration is best) rather than driving the loop. He also detailed the systems challenges: real-time ingest of large semi-structured payloads (tens to hundreds of MB), deeply nested data that is hard to query, mixed read patterns (real-time monitoring vs. long-running fine-tuning queries), and the need for a custom query abstraction (BTQL) to serve both AI engineers and non-technical stakeholders like PMs and SMEs.

## Relevance to YOLO loop

This is the meta-loop for our YOLO loop. If we instrument our agents to log traces into an eval store, we can bootstrap the automated improvement loop: agent failures in production become test cases, coding agents propose prompt/config fixes, we review diffs. The specific insight that large semi-structured trace payloads need a different storage and query strategy than traditional observability is actionable for how we design our trace store.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-08 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-08-eval-platform-systems-problem` |
| Channel | aie |
| Video | [Why Building an Eval Platform Is Harder Than It Looks — Braintrust](https://www.youtube.com/watch?v=mUQoVz7THu0) |
| Published | 2026-10-08 |
| Ingested upstream | 2026-10-08 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
