# Start all tasks at low effort and escalate only on evidence of inadequacy

> Back to [[experiments-index]]

Source: **[THIS Is the AI Setting Everyone Gets Wrong](https://www.youtube.com/watch?v=4__5q76f04s)** · mk · 2026-07-13

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we default to low effort on frontier models and only escalate to medium/high/extra-high when output quality is demonstrably insufficient, then we preserve tokens and latency with negligible quality loss on the majority of tasks, because frontier model weights alone already exceed the capability of lower models on max effort, and overthinking on simple tasks degrades output.

## What they did

Mark ran the same task across 12 effort levels across two providers (Claude and GPT 5.6 family) and found negligible functional differences between medium, high, and extra-high outputs for a dashboard generation task, while extra-high and max consumed 4-5x more tokens. He uses Fable 5 on low effort for most tasks. His framework: low/medium for known tasks on frontier models, default high for standard daily work, high+ only for tasks with unknown unknowns, extra-high only for long-running tasks needing milestone-by-milestone introspection, and max almost never.

## Relevance to YOLO loop

Token budget management is critical in the YOLO loop. Defaulting to low effort and escalating programmatically could be implemented as a retry policy: run at low, evaluate output quality score, escalate if below threshold—reducing cost per loop iteration significantly.

## Notes

Mark notes that chaining multiple medium-effort prompts (do this, check your work, consider that) can match a single extra-high prompt at lower total token cost. Worth benchmarking in our loop.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-13 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mk-2026-07-13-effort-level-calibration` |
| Channel | mk |
| Video | [THIS Is the AI Setting Everyone Gets Wrong](https://www.youtube.com/watch?v=4__5q76f04s) |
| Published | 2026-07-13 |
| Ingested upstream | 2026-07-13 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
