# Distill LLM reasoning into a lightweight model for low-latency search ranking

> Back to [[experiments-index]]

Source: **[Distill the LLM, Don't Serve It: Search & Personalization at DoorDash — Raghav Saboo, DoorDash](https://www.youtube.com/watch?v=ACPEpji5NV4)** · aie · 2026-09-26

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we use a large LLM to generate training labels or embeddings offline and then distill that knowledge into a smaller production model, then we get LLM-quality search and personalization results at inference costs and latencies suitable for real-time serving because we separate the expensive reasoning step from the hot path.

## What they did

Raghav Saboo from DoorDash described an architecture where LLMs are used in an offline or batch capacity to enrich training data or generate soft labels, and a smaller distilled model is what actually serves search and personalization requests in production, avoiding the cost and latency of serving a full LLM per query.

## Relevance to YOLO loop

High relevance: this pattern directly addresses the cost-vs-quality tradeoff in our dev loop whenever we need LLM intelligence at query time. Distillation could apply to any classification, ranking, or extraction task we currently serve with a large model.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-26 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-26-doordash-distill-llm-search` |
| Channel | aie |
| Video | [Distill the LLM, Don't Serve It: Search & Personalization at DoorDash — Raghav Saboo, DoorDash](https://www.youtube.com/watch?v=ACPEpji5NV4) |
| Published | 2026-09-26 |
| Ingested upstream | 2026-09-26 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
