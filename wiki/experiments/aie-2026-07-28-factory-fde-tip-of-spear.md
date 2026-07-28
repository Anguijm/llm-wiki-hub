# Instrument autonomy ratio to measure agent-readiness of a codebase

> Back to [[experiments-index]]

Source: **[How Forward Deployed Engineering is done at Factory — Eno Reyes](https://www.youtube.com/watch?v=wpOA-UXynoM)** · aie · 2026-07-28

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we track the ratio of AI-to-human actions before interruption (autonomy ratio) across our codebase, then we can identify which subsystems are agent-ready versus which require human loops, because the ratio surfaces where validators are missing or context is insufficient for autonomous operation.

## What they did

Eno Reyes described Factory's internal metric called the 'autonomy ratio' — the ratio of actions completed by AI systems versus humans before an interruption occurs. Factory runs at roughly 15-20% full autonomy with an autonomy ratio in the upper 80s. He noted that some subsystems like 'legal droid' are 100% autonomous while others like the visual terminal harness cannot be closed because flickering and visual correctness are hard to verify programmatically.

## Relevance to YOLO loop

Directly maps to measuring how much of our dev loop can run without human-in-the-loop checkpoints. Instrumenting this ratio would tell us which stages of our YOLO loop are bottlenecked by missing evals or validators versus model capability.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-28 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-28-factory-fde-tip-of-spear` |
| Channel | aie |
| Video | [How Forward Deployed Engineering is done at Factory — Eno Reyes](https://www.youtube.com/watch?v=wpOA-UXynoM) |
| Published | 2026-07-28 |
| Ingested upstream | 2026-07-28 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
