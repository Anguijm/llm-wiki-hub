# Schedule per-module security sweep loops on one repo

> Back to [[experiments-index]]

Source: **[Everything Is Getting Hacked (it’s over)](https://www.youtube.com/watch?v=wuv61uEq7uY)** · do · 2026-10-23

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we split a repo into 5 to 10 architectural modules and run a scheduled agent sweep on each at a priority-based cadence, then real issues will be found sooner and with less noise because each agent works on a smaller scope and quiet threads are auto-archived.

## What they did

Chunked codebases into modules such as authentication, billing, API endpoints, front-end and back-end. Scheduled cloud agent loops at different cadences (every 4 hours, hourly, every 10 minutes) by priority P1 to P4. Used frontier models at maximum reasoning effort. Archived threads that found nothing and alerted on verified issues. Also ran a dependency-diet sweep that recommended removing and replacing 21 packages with first-party code.

## Relevance to YOLO loop

high: It gives a concrete pattern for scheduled, scoped agent loops with auto-archive of empty results and alerts only on verified findings.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-23 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-10-23-module-chunked-scheduled-sweeps` |
| Channel | do |
| Video | [Everything Is Getting Hacked (it’s over)](https://www.youtube.com/watch?v=wuv61uEq7uY) |
| Published | 2026-10-23 |
| Ingested upstream | 2026-10-23 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
