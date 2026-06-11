# Apply Auto Research pattern to optimize Gemini review scores

> Back to [[experiments-index]]

Source: **[Tobi Lutke Made a 20-Year-Old Codebase 53% Faster Overnight](https://www.youtube.com/watch?v=YpPcDHc3e9U)** · nb · 2026-03-25

**Status:** `done` · **Verdict:** `discard` · **Effort:** `medium`

---

## Hypothesis

If we treat Gemini code review scores as a metric and use hill-climbing (iterating on code until the score improves), then average code quality increases because we're optimizing against a measurable target rather than fixing bugs one-off.

## What they did

Nate described Auto Research as metric-driven optimization derived from classical ML. Systems use hill climbing to iteratively improve a measurable number (conversion rate, execution speed, code quality score).

## Actionable steps

- Define a numeric quality metric from Gemini reviews (e.g., bugs found per project, 1-10 score)
- Track the metric across Phase 2 refinements
- Identify patterns in low-scoring projects
- Iterate on the worst performers until metric improves

## Success metric

Average Gemini review score improves by 1+ point over 10 refinement cycles.

## Relevance to YOLO loop

Phase 2 refinement already uses Gemini reviews. Formalizing the score as a metric to optimize against would make the process more systematic.

## Target projects

- [[yolo-projects]] (`yolo-loop-infrastructure`)

## Outcome

Phase 2 refinement implicitly tracked this: each Gemini review found N bugs, fixes were applied, retested. The bug count per project dropped over time as learnings.md accumulated patterns. Formalizing a numeric score would add overhead without clear ROI given Phase 2 is complete. Pattern recognized but not worth formalizing further.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-03-29 | `done` | Evaluated: Phase 2 already tracked bug counts as implicit metric |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-03-25-auto-research-metric-optimization` |
| Channel | nb |
| Video | [Tobi Lutke Made a 20-Year-Old Codebase 53% Faster Overnight](https://www.youtube.com/watch?v=YpPcDHc3e9U) |
| Published | 2026-03-25 |
| Ingested upstream | 2026-03-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
