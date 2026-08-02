# Design task rubrics with 20+ sub-criteria and partial-credit scoring for long-horizon agent evals

> Back to [[experiments-index]]

Source: **[Rethinking Environments for Long-Horizon Work — Rayan Garg, Theta Software](https://www.youtube.com/watch?v=2aS7aKoXn64)** · aie · 2026-08-02

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we replace binary pass/fail verifiers with granular rubrics (20 criteria × 10 sub-criteria each) and add partial-credit scoring that grades assumptions independently, then training signal quality will improve for long-horizon tasks because coarse reward signals cause the model to plateau early and the gradient cannot distinguish between a model that failed at step 1 versus step 18.

## What they did

Rayan Garg and Ryan (Theta Software) argued that most published finance benchmarks (GDP-Val, ToolBench, Apex Agents) are not actually long-horizon by current frontier standards — average human task time falls below the meter benchmark thresholds, and pass@1 rates of 57%+ indicate saturation. Their solution: tasks averaging 15 human hours, evaluated with rubrics of ~20 criteria and ~10 sub-criteria per criterion, plus partial-credit scoring that grades each assumption independently (not just the final output). They also run gold/no-op variance tests on rubrics and expert agreement checks. They noted that narrow benchmark domains (only IB for finance) leave important areas (credit, debt, risk) uncovered, limiting learnability.

## Relevance to YOLO loop

YOLO loop evals for complex multi-step tasks currently use coarse correctness checks. Adopting granular rubrics with partial credit would provide much richer training signal for improving agent performance on real 15-hour knowledge-work tasks.

## Notes

Theta's finance data: avg 15 human hours/task over 50-task sample. Models still struggle significantly (mean score far below published benchmark pass rates). Rubric QA tests: gold variance, no-op variance, coverage, expert agreement.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-02 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-02-long-horizon-rubric-granularity` |
| Channel | aie |
| Video | [Rethinking Environments for Long-Horizon Work — Rayan Garg, Theta Software](https://www.youtube.com/watch?v=2aS7aKoXn64) |
| Published | 2026-08-02 |
| Ingested upstream | 2026-08-02 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
