# Audit custom CUDA kernel implementations for weight-folding and stream-ordering bugs that silently corrupt model outputs

> Back to [[experiments-index]]

Source: **[Weight Folding, CUDA Streams, and the Bug That Made My Model Speak Backwards — Filip Makraduli](https://www.youtube.com/watch?v=c1hGBoWw20A)** · aie · 2026-09-19

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we add output-order and weight-magnitude sanity checks to custom CUDA inference kernels, then we can catch silent correctness bugs early because weight-folding optimizations and concurrent CUDA streams can introduce subtle tensor ordering errors that degrade model outputs without raising exceptions.

## What they did

Based on title inference only — no transcript available. Filip Makraduli presented on weight folding techniques for inference optimization, CUDA stream concurrency, and a specific debugging case where a model produced reversed/backwards outputs traced to a bug in custom kernel implementation.

## Relevance to YOLO loop

Relevant if the YOLO loop runs self-hosted inference with custom CUDA kernels — provides a debugging checklist pattern for silent correctness failures in optimized inference backends.

## Notes

No transcript available; inferred from title. Low confidence on specifics. Skip if team does not operate custom CUDA inference.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-19 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-19-weight-folding-cuda-streams` |
| Channel | aie |
| Video | [Weight Folding, CUDA Streams, and the Bug That Made My Model Speak Backwards — Filip Makraduli](https://www.youtube.com/watch?v=c1hGBoWw20A) |
| Published | 2026-09-19 |
| Ingested upstream | 2026-09-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
