# Benchmark Sonnet 5.5 vs Opus 5.5 on Real Dev Tasks

> Back to [[experiments-index]]

Source: **[I Tested Sonnet 5.5 vs Opus 5.5. What You Need to Know.](https://www.youtube.com/watch?v=7eo-11K2e3c)** · nh · 2026-09-29

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we run Sonnet 5.5 and Opus 5.5 side-by-side on our actual coding and reasoning tasks, then we can identify whether the cost premium of Opus is justified for our use cases because real-world task performance often diverges from marketing benchmarks.

## What they did

Nate ran comparative tests between Claude Sonnet 5.5 and Opus 5.5 across a set of tasks to evaluate performance differences, cost-efficiency tradeoffs, and practical guidance on which model to use for which scenarios.

## Relevance to YOLO loop

Directly informs model selection at the LLM call layer of the YOLO loop; choosing the wrong model tier wastes tokens or degrades output quality on agent steps.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-29 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-09-29-sonnet-vs-opus-55-benchmark` |
| Channel | nh |
| Video | [I Tested Sonnet 5.5 vs Opus 5.5. What You Need to Know.](https://www.youtube.com/watch?v=7eo-11K2e3c) |
| Published | 2026-09-29 |
| Ingested upstream | 2026-09-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
