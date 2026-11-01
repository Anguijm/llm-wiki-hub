# Run a reasoning-effort cost ladder on one repeatable task

> Back to [[experiments-index]]

Source: **[Every Claude 2.0 Concept Explained for Non-Coders](https://www.youtube.com/watch?v=tcb5q_6jwvY)** · nh · 2026-10-30

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we run the same scoped task at low, medium, extra-high and max reasoning effort and record time, cost and defects, then we can set a per-task-type default effort (likely medium) that cuts spend without losing quality, because the speaker saw max overthink and cost about double extra-high with no better output.

## What they did

Nate Herk ran a controlled test on Opus 5.5. Low effort finished in 17 minutes for under $4 but had bugs. Extra high took 1.5 hours for $26 and gave the best output. Max took 2.5 hours for $50 and overthought. He recommends medium as the everyday default and warns that max can cause subtle code regressions.

## Relevance to YOLO loop

high: Per-task-type effort calibration with a measured cost, time and defect table is not among the existing practices, which cover gates, reviewers and stop rules but not effort-level tuning.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-31 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-10-30-effort-level-cost-ladder` |
| Channel | nh |
| Video | [Every Claude 2.0 Concept Explained for Non-Coders](https://www.youtube.com/watch?v=tcb5q_6jwvY) |
| Published | 2026-10-30 |
| Ingested upstream | 2026-10-31 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
