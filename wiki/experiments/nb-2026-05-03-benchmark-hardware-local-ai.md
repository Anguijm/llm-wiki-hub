# Benchmark Local AI Hardware Options for Dev Loop Inference

> Back to [[experiments-index]]

Source: **[RTX 5090, Mac Studio, or DGX Spark? I tried all three.](https://www.youtube.com/watch?v=iUSdS-6uwr4)** · NateBJones · 2026-05-03

**Status:** `deferred` · **Effort:** `high`

---

## Hypothesis

If we systematically compare RTX 5090, Mac Studio, and DGX Spark on real AI workloads, then we can identify the best price-performance option for local model inference in our dev loop because raw specs alone do not reflect real-world throughput or latency.

## What they did

Speaker acquired and tested all three hardware platforms (RTX 5090, Mac Studio, DGX Spark) running AI workloads, comparing them on practical performance metrics relevant to local inference and development.

## Relevance to YOLO loop

Choosing local inference hardware directly affects iteration speed in the YOLO loop; faster local inference means tighter feedback cycles without API latency or cost.

## Notes

[2026-05-06T19:43:19Z] DEFER: Big purchase decision, not a code experiment. Defer until there's a clear cost/latency case for moving inference local.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-05-03 | `backlog` | Extracted from YouTube RSS |
|  | `` | Triage 2026-05-05: Big purchase decision, not a code experiment. Defer until there's a clear cost/latency case for moving inference local. |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-05-03-benchmark-hardware-local-ai` |
| Channel | NateBJones |
| Video | [RTX 5090, Mac Studio, or DGX Spark? I tried all three.](https://www.youtube.com/watch?v=iUSdS-6uwr4) |
| Published | 2026-05-03 |
| Ingested upstream | 2026-05-03 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
