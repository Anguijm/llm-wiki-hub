# Add Negative Prompting Layer to All Agent Instructions

> Back to [[experiments-index]]

Source: **[5000 Hours of Building AI in Just 17 Minutes](https://www.youtube.com/watch?v=7WZ6XldxX0U)** · nh · 2026-08-04

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we systematically add 'do not do X' clauses to every agent skill and system prompt, then we will reduce recurring failure modes because explicit prohibitions encode hard-won failure experience directly into the instruction set, preventing the AI from repeating known landmines.

## What they did

Nate described a practice he calls 'negative prompting' where, across all 5000+ hours of builds, he continuously appends a list of don'ts to every skill, system, and instruction set. He frames this list as his personal failure history written down — things that broke in production — converted into explicit prohibitions that prevent the AI from making the same mistakes on future runs.

## Relevance to YOLO loop

Directly applicable to the YOLO loop's agent instruction files. Every skill or sub-agent prompt in the loop can receive a curated 'never do' section. As the loop surfaces new failure modes during runs, those get appended to the relevant instruction file, making the system self-hardening over time.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-04 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-08-04-negative-prompting-system` |
| Channel | nh |
| Video | [5000 Hours of Building AI in Just 17 Minutes](https://www.youtube.com/watch?v=7WZ6XldxX0U) |
| Published | 2026-08-04 |
| Ingested upstream | 2026-08-04 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
