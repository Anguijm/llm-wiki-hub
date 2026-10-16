# Run a ceiling test (AA test on prod model) before evaluating any prompt optimization candidate

> Back to [[experiments-index]]

Source: **[How to Actually Tokenmaxx and Save Millions — Alvin Pane, OutRival](https://www.youtube.com/watch?v=8g1N_a3h9H0)** · aie · 2026-10-15

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we measure the production model's self-disagreement rate (AA test) before comparing it to a cheaper candidate, then we will avoid falsely rejecting good optimizations because we will know how much variance is inherent to the baseline, making the comparison statistically honest.

## What they did

Alvin's team at OutRival ran their expensive production model three times on the same inputs and found it disagreed with itself ~7% of the time (93% self-agreement). When they then tested a cheaper candidate model, it disagreed with prod ~18% of the time. Without the ceiling test, they would have rejected the candidate as too inaccurate—but 7 of those 18 disagreement points were just baseline model variance, not candidate error. They then used DSPy with a Jeepa optimizer to shrink a 5,000-token classification prompt by 51% in instruction tokens, validated with a shadow deployment, and measured net improvements vs. regressions with a paired confidence interval, requiring the lower bound to be above zero before shipping.

## Relevance to YOLO loop

Directly applicable to our prompt optimization and model-swap decisions in the loop: before accepting or rejecting a cheaper/faster model, we should run a ceiling test on the incumbent to establish honest comparison baselines and avoid rejecting valid optimizations.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-15-ceiling-test-for-prompt-optimization` |
| Channel | aie |
| Video | [How to Actually Tokenmaxx and Save Millions — Alvin Pane, OutRival](https://www.youtube.com/watch?v=8g1N_a3h9H0) |
| Published | 2026-10-15 |
| Ingested upstream | 2026-10-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
