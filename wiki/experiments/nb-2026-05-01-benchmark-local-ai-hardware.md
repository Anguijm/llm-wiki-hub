# Benchmark Local AI Hardware Options Against Dev Loop Workloads

> Back to [[experiments-index]]

Source: **[RTX 5090, Mac Studio, or DGX Spark? I tried all three.](https://www.youtube.com/watch?v=iUSdS-6uwr4)** · NateBJones · 2026-05-01

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we systematically compare RTX 5090, Mac Studio, and DGX Spark on our actual inference and fine-tuning workloads, then we can identify the best cost-performance option for local AI development because hardware bottlenecks directly constrain iteration speed in the YOLO loop.

## What they did

The creator ran all three hardware platforms (RTX 5090 PC, Apple Mac Studio, and NVIDIA DGX Spark) through AI workloads and compared performance, cost, and practicality for local model inference and development.

## Relevance to YOLO loop

Local inference speed determines how fast we can test prompts, run evals, and iterate on agent behavior without API latency or cost. Choosing the right hardware is a foundational enabler for a fast YOLO loop.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-05-01 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-05-01-benchmark-local-ai-hardware` |
| Channel | NateBJones |
| Video | [RTX 5090, Mac Studio, or DGX Spark? I tried all three.](https://www.youtube.com/watch?v=iUSdS-6uwr4) |
| Published | 2026-05-01 |
| Ingested upstream | 2026-05-01 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
