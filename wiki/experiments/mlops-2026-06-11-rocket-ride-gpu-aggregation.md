# Use shared-inference model server to cut LLM inference costs via GPU aggregation

> Back to [[experiments-index]]

Source: **[AI Is Fast. AI Projects Are Slow. Let's Fix That.](https://www.youtube.com/watch?v=3xZ78HHdqAk)** · mlops · 2026-06-11

**Status:** `discarded` · **Verdict:** `discard` · **Effort:** `high`

---

## Hypothesis

If we route inference for common models (e.g., OCR, Whisper, small LLMs) through a shared model server that batches requests across customers and dynamically scales instances, then per-request GPU cost will drop significantly compared to dedicated per-customer GPU allocation because idle GPU time is eliminated and compute is shared at the batch level.

## What they did

Rocket Ride described a model server architecture that aggregates inference across 100+ customers sharing a single GPU-loaded model instance (e.g., EasyOCR). Requests are batched in groups of 64 or 128, processed together, then split back out. When queue depth grows, additional model instances are spun up dynamically; when demand drops, instances are removed. Data isolation is maintained at the GPU channel level. This contrasts with on-prem setups where a customer pays 24/7 for a GPU that may run a model only 8–10 hours per day.

## Relevance to YOLO loop

Relevant if we operate our own inference infrastructure. The batching and dynamic scaling pattern is applicable to any shared inference layer in our pipeline, reducing cost per experiment run.

## Notes

Backlog triage 2026-06-24 (owner-preference model). Shared-GPU inference cost-cutting — enterprise infra; cost is not a constraint.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-06-11-rocket-ride-gpu-aggregation` |
| Channel | mlops |
| Video | [AI Is Fast. AI Projects Are Slow. Let's Fix That.](https://www.youtube.com/watch?v=3xZ78HHdqAk) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
