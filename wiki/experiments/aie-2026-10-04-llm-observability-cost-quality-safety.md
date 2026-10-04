# Add Cost, Safety, and Quality Metric Layers to Agent Observability Beyond Traditional Golden Signals

> Back to [[experiments-index]]

Source: **[Your LLM App Returned 200 OK. It Was Still Wrong. — Marina Petzel, Datadog](https://www.youtube.com/watch?v=rTojoVotlD8)** · aie · 2026-10-04

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we instrument our agent systems with cost attribution tags (feature-level, model-level, cache-hit tracking), safety metrics (prompt injection detection, PII in output), and quality metrics (hallucination rate, relevance score, answer completeness via LLM-as-judge), then we will catch production failures that return HTTP 200 but deliver wrong or harmful answers, because these failure modes are invisible to latency/error/traffic/saturation monitoring alone.

## What they did

Marina Petzel outlined three monitoring layers beyond the traditional LETS golden signals for GenAI apps: (1) Cost: tag every request by feature, model, and cache status — token creep (context window quietly inflated 4k→132k = 8x cost), model drift (switching from cheap to expensive model with same volume), and cache misses (70% of spend can be redundant without caching) all require granular attribution to catch. (2) Safety: monitor for prompt injection, jailbreaking attempts, and PII in outputs — none of these surface as 500 errors. (3) Quality: track hallucination rate, relevance scores (embedding similarity), user satisfaction (thumbs/NPS), answer completeness (LLM-as-judge), and RAG retrieval quality (top-K accuracy, NDCG).

## Relevance to YOLO loop

Maps to the evaluation and observability layer of the YOLO loop: without these metrics, agents can silently degrade in production — the YOLO loop's rapid iteration only improves what is measured, making this instrumentation a prerequisite for confident weekly/daily shipping.

## Notes

Start with cost attribution tags and a basic LLM-as-judge quality check — these have the highest ROI. PII detection and hallucination rate monitoring can follow. Datadog LLM Observability offers a free trial per QR code in the talk.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-04 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-04-llm-observability-cost-quality-safety` |
| Channel | aie |
| Video | [Your LLM App Returned 200 OK. It Was Still Wrong. — Marina Petzel, Datadog](https://www.youtube.com/watch?v=rTojoVotlD8) |
| Published | 2026-10-04 |
| Ingested upstream | 2026-10-04 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
