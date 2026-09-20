# Audit current inference stack against latest inference engineering best practices

> Back to [[experiments-index]]

Source: **[What's New in Inference Engineering — Philip Kiely, Baseten](https://www.youtube.com/watch?v=75ckHC2LU_0)** · aie · 2026-09-20

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we review our inference configuration against the current state-of-the-art techniques (speculative decoding, continuous batching tuning, disaggregated prefill), then we will identify at least one optimization that reduces latency or cost by >10%, because the inference engineering field moves fast and default configurations are rarely optimal.

## What they did

Philip Kiely from Baseten surveyed the current landscape of inference engineering advances, covering what has changed recently in production inference optimization including new serving techniques, hardware utilization strategies, and deployment patterns that practitioners should adopt.

## Relevance to YOLO loop

The YOLO loop's performance ceiling is set by inference speed and cost; staying current with inference engineering best practices is directly applicable to loop throughput.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-20 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-20-whats-new-inference-engineering` |
| Channel | aie |
| Video | [What's New in Inference Engineering — Philip Kiely, Baseten](https://www.youtube.com/watch?v=75ckHC2LU_0) |
| Published | 2026-09-20 |
| Ingested upstream | 2026-09-20 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
