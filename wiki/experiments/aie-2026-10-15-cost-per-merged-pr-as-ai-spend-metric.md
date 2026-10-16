# Track cost-per-merged-PR (salary + AI spend) as the primary AI investment metric instead of token bill

> Back to [[experiments-index]]

Source: **[Tokens Are the Cheap Part — Steve Jamison, Jellyfish](https://www.youtube.com/watch?v=U7ZYBCcdJPg)** · aie · 2026-10-15

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we combine developer salary and AI spend into a single 'intelligence cost per merged PR' metric and track it monthly, then we will make better decisions about AI investment levels because this composite metric reveals whether throughput gains are outpacing cost increases, which token spend alone cannot show.

## What they did

Steve Jameson analyzed the Jellyfish platform's engineering workflow and AI telemetry dataset. Key findings: AI spend rose 60x YoY while merged PRs per engineer rose 43%. When salary is included, AI is only ~2.5% of the total cost to produce a merged PR (under 10% even for the heaviest spenders). The dollar cost per merged PR fell 26% over the same period across 83% of companies studied. Heavy AI spenders (top quintile, ~2.5B tokens/dev/month) saw 67% PR throughput gains and 32% cost-per-PR reduction vs ~40% throughput and ~25% cost reduction for lower spenders. There are diminishing returns at very high token volumes. He recommended tracking: AI spend per PR, PRs per engineer, and cost per merged PR monthly, alongside quality/revert metrics as a counterweight.

## Relevance to YOLO loop

The YOLO loop can instrument this metric by logging AI API costs per PR/task alongside cycle time. Reframes the loop's cost accounting from 'how much did we spend on tokens' to 'what did it cost to ship a unit of work'.

## Notes

Data from Jellyfish platform (proprietary dataset). The diminishing-returns curve at high token volumes is an important counterpoint—more spend keeps paying until it doesn't. Monitor revert rate and quality metrics alongside throughput to avoid AI slop inflating PR counts.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-15-cost-per-merged-pr-as-ai-spend-metric` |
| Channel | aie |
| Video | [Tokens Are the Cheap Part — Steve Jamison, Jellyfish](https://www.youtube.com/watch?v=U7ZYBCcdJPg) |
| Published | 2026-10-15 |
| Ingested upstream | 2026-10-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
