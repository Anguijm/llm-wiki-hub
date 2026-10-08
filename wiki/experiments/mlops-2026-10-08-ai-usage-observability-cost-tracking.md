# Use AI to Hunt Its Own Cost-Saving Metrics Inside Your Observability Platform

> Back to [[experiments-index]]

Source: **[How a Logistics Giant Keeps AI Data Locked Down](https://www.youtube.com/watch?v=oYlb1Wv6Vkk)** · mlops · 2026-10-08

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we use an LLM agent to query our own LLM observability platform for unknown metrics, then we can surface cost-reduction opportunities (prompt verbosity, cache hit rate, reasoning ratio) we would not have found manually, because the agent can traverse metric catalogs faster than a human analyst.

## What they did

Jason Ward at CH Robinson used the LLM agent built into their observability platform to discover metrics he did not know existed, then used those metrics to build dashboards around AI spend. Specifically he tracked 'verbosity' (chattiness / prompt bloat via calls per trace), cache hit rate (achieving 60-70% savings on cached prompts), and reasoning token ratio (reasoning vs non-reasoning tokens). He described the workflow as 'AI hacking AI' to find the right scorecard.

## Relevance to YOLO loop

Directly applicable to our dev loop cost governance: we can point an agent at our own LLM observability tool (e.g. LangSmith, Helicone, or similar) to auto-discover high-impact cost metrics before we manually instrument them.

## Notes

Key metrics to replicate: verbosity score (tokens/calls per trace), prompt cache hit %, reasoning vs non-reasoning token split. CH Robinson uses Azure OpenAI primarily but also tests GCP Vertex Anthropic models for data residency.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-08 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-10-08-ai-usage-observability-cost-tracking` |
| Channel | mlops |
| Video | [How a Logistics Giant Keeps AI Data Locked Down](https://www.youtube.com/watch?v=oYlb1Wv6Vkk) |
| Published | 2026-10-08 |
| Ingested upstream | 2026-10-08 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
