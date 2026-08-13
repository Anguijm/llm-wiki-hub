# Design a Sequential, Sample-Efficiency-First Benchmark for Agent Continual Learning

> Back to [[experiments-index]]

Source: **[Beyond Static Intelligence: Evaluating Continual Learning — Parth Asawa, UC Berkeley](https://www.youtube.com/watch?v=iqloyWCGYQQ)** · aie · 2026-08-13

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we evaluate agent continual learning using a benchmark that measures performance improvement as a function of prior experience within a task sequence (rather than independent point-capability scores), then we will obtain a more accurate signal of true learning ability because the benchmark captures sample efficiency and retention simultaneously, and frontier models cannot game it via pre-training overlap.

## What they did

Parth Asawa argued that existing LLM benchmarks evaluate models as if they forget everything between tasks, making them inappropriate for measuring continual learning. He outlined requirements for a proper continual learning benchmark: tasks must be novel enough that frontier models cannot already solve them via pre-training, sample efficiency must be a first-order metric, and evaluation must track improvement curves across sequential experience rather than independent scores. He introduced CLBench (collaboration across Berkeley, Snorkel, UW Madison) and noted current parametric, in-context, and external-memory approaches all need to be evaluated under this framework.

## Relevance to YOLO loop

Relevant to evaluating YOLO loop agent improvement over time: instead of measuring per-run success rate in isolation, adopting a sequential benchmark design would reveal whether the agent is genuinely learning across runs or just getting lucky, guiding where to invest in memory and adaptation mechanisms.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-13 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-13-continual-learning-benchmark-design` |
| Channel | aie |
| Video | [Beyond Static Intelligence: Evaluating Continual Learning — Parth Asawa, UC Berkeley](https://www.youtube.com/watch?v=iqloyWCGYQQ) |
| Published | 2026-08-13 |
| Ingested upstream | 2026-08-13 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
