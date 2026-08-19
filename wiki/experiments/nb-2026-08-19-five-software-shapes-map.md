# Use a 'wish-to-shape' framing exercise before choosing a build tool

> Back to [[experiments-index]]

Source: **[Nobody Laid Out The Five Kinds Of Software You Can Make. So I Did.](https://www.youtube.com/watch?v=joRXo6x7Pgk)** · nb · 2026-08-19

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we run a structured 'desired change → information source → who sees it → failure cost' framing exercise before selecting a builder or stack, then we will choose the right software shape (local tool, web app, sensor-connected app, mobile app, or API service) faster and with fewer wasted pivots, because the constraints of the problem naturally eliminate most wrong choices before any code is written.

## What they did

Nate described a five-category taxonomy of software shapes (local tool, web app, sensor-connected app, mobile-first app, background service/API) and walked through two concrete examples—a ferry tracker and a house maintenance app—showing how answering four questions (what changes, where does the info come from, what screen shows it and why, what breaks if it fails) reveals the correct shape before touching any builder or AI coding agent. He recommended Lovable as the default starting point for non-technical builders of private web apps.

## Relevance to YOLO loop

Directly improves the planning phase of our dev loop: running this framing exercise before spinning up a coding agent reduces scope drift and mis-matched tool selection, which are common causes of mid-loop restarts.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-19 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-08-19-five-software-shapes-map` |
| Channel | nb |
| Video | [Nobody Laid Out The Five Kinds Of Software You Can Make. So I Did.](https://www.youtube.com/watch?v=joRXo6x7Pgk) |
| Published | 2026-08-19 |
| Ingested upstream | 2026-08-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
