# Route each factory node to the cheapest model sufficient for that node's task rather than using the best model everywhere

> Back to [[experiments-index]]

Source: **[My AI Dark Factory Dream Is Dead (Here's What Actually Works)](https://www.youtube.com/watch?v=GQatuTWSRqY)** · cm · 2026-10-16

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we assign lightweight models (e.g. Sonnet) to simple routing and dispatch nodes and reserve frontier models (Opus, GPT-6) only for planning and complex reasoning nodes, then we can run hundreds of factory laps per week without hitting rate limits or budget ceilings, because most factory steps do not require maximum reasoning capability.

## What they did

Cole Medin described optimising his software factory for token efficiency by using different models and providers per node: Opus 5.5 or GPT-6 Astra for planning, Sonnet for individual task nodes, and even smaller models for simple dispatch steps. He reported running hundreds of laps per week without hitting rate limits.

## Relevance to YOLO loop

high: directly applicable to our multi-agent harness—mapping each Claude Code sub-task type to an appropriate model tier to control cost and rate limits.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-16 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `cm-2026-10-16-token-efficient-model-routing-per-node` |
| Channel | cm |
| Video | [My AI Dark Factory Dream Is Dead (Here's What Actually Works)](https://www.youtube.com/watch?v=GQatuTWSRqY) |
| Published | 2026-10-16 |
| Ingested upstream | 2026-10-16 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
