# Add a centralized MCP gateway with PII blocking and context optimizer to reduce token cost 70-90%

> Back to [[experiments-index]]

Source: **[Paving the Road to Production: Governed Enterprise AI Agents — Harish Gaggar, Credit Karma](https://www.youtube.com/watch?v=tZycGA_Fbfo)** · aie · 2026-10-15

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we route all agent tool calls through a centralized MCP gateway that strips PII before LLM submission and compresses context via relevance ranking and deduplication, then token costs will drop 70-90% per query and sensitive data leakage to LLMs will be prevented, because most production queries contain redundant and sensitive payload that can be trimmed without losing task-relevant information.

## What they did

Harish described the full framework at Intuit Credit Karma: a LangGraph agent registers with a dev portal that scaffolds memory, tracking/eval, context optimizer, and PII-blocking frameworks into the repo automatically. The MCP gateway authenticates every tool call and routes it to the right MCP server. The context optimizer selects payload by token limit, re-ranks for relevance, deduplicates, and compresses before sending to the LLM. He demoed the same JFrog Artifactory query going from 24,000 tokens to 2,400 tokens (90% reduction) with the optimizer enabled, and a Slack bot query going from 24,000 to 1,500 tokens. In most cases they observed 70-78% savings.

## Relevance to YOLO loop

Maps to our agent infrastructure layer: adding a gateway with context optimization would directly reduce our per-run LLM costs at scale, and the PII blocking layer addresses compliance requirements for any enterprise customer use cases we support.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-15-mcp-gateway-with-pii-blocking-and-context-optimizer` |
| Channel | aie |
| Video | [Paving the Road to Production: Governed Enterprise AI Agents — Harish Gaggar, Credit Karma](https://www.youtube.com/watch?v=tZycGA_Fbfo) |
| Published | 2026-10-15 |
| Ingested upstream | 2026-10-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
