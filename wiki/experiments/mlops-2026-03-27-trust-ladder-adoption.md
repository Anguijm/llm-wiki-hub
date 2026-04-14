# Apply the trust ladder to increase agent autonomy incrementally

> Back to [[experiments-index]]

Source: **[Lessons from 25 Trillion Tokens — Scaling AI-Assisted Development at Kilo](https://www.youtube.com/watch?v=tG1CSRaJhKQ)** · @MLOps · 2026-03-27

**Status:** `done` · **Verdict:** `discard` · **Effort:** `low`

---

## Hypothesis

If we gradually increase agent autonomy (autocomplete → chat → single agent → orchestration) based on measured trust metrics (bug rate, rework rate), then we avoid the pitfall of over-trusting agents that produce slop code.

## What they did

Kilo found developers climb a trust ladder: autocomplete → chat → single agents → orchestration. Trust breaks on latency, bad context, or high review load. Target 2-3x speedup, not 10x — the latter produces slop requiring more rework than manual coding.

## Actionable steps

- Define current trust level for each YOLO loop phase
- Identify one phase to promote to the next trust level
- Measure: does the higher autonomy produce same quality at faster speed?
- If quality drops, step back down

## Success metric

One phase successfully promoted to higher autonomy without quality regression.

## Relevance to YOLO loop

Phase 2 refinement was essentially single-agent trust level. Could we promote some tasks to orchestration (parallel agents) without quality loss?

## Target projects

- [[yolo-projects]] (`yolo-loop-infrastructure`)

## Outcome

Parked — already operating at max autonomy (hourly cron, bypass permissions, auto-ship). Trust ladder assumes incremental ramp-up which we skipped entirely.

## Notes

Parked, not discarded permanently. Revisit if we ever need to dial back autonomy.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-03 | `done` | Parked — already at max autonomy |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-03-27-trust-ladder-adoption` |
| Channel | @MLOps |
| Video | [Lessons from 25 Trillion Tokens — Scaling AI-Assisted Development at Kilo](https://www.youtube.com/watch?v=tG1CSRaJhKQ) |
| Published | 2026-03-27 |
| Ingested upstream | 2026-03-30 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
