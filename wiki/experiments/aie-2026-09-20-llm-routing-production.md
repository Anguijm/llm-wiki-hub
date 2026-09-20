# Implement signal-driven LLM routing to balance cost and quality across loop steps

> Back to [[experiments-index]]

Source: **[Routing LLM Inference in Production: From Engine Signals to Policy — Qianru Lao & Lu Zhang, OpenAI](https://www.youtube.com/watch?v=sOB3HSiG8vo)** · aie · 2026-09-20

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we route each YOLO loop LLM call to the appropriate model tier based on runtime signals (task complexity, latency budget, queue depth), then we will reduce average cost per loop run without sacrificing output quality, because not every step in an agentic loop requires the most capable or expensive model.

## What they did

Qianru Lao and Lu Zhang from OpenAI described their production LLM routing system that uses engine-level signals (load, latency, queue state) combined with learned policies to dynamically route inference requests across model variants or serving replicas to optimize for cost, latency, and quality simultaneously.

## Relevance to YOLO loop

The YOLO loop makes heterogeneous LLM calls of varying complexity; intelligent routing between model tiers per call type is a direct mechanism to cut cost while preserving quality where it matters.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-20 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-20-llm-routing-production` |
| Channel | aie |
| Video | [Routing LLM Inference in Production: From Engine Signals to Policy — Qianru Lao & Lu Zhang, OpenAI](https://www.youtube.com/watch?v=sOB3HSiG8vo) |
| Published | 2026-09-20 |
| Ingested upstream | 2026-09-20 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
