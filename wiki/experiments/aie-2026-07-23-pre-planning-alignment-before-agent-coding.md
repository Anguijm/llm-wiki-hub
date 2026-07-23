# Add structured pre-planning (architecture + program design docs) before every agent coding task

> Back to [[experiments-index]]

Source: **[Harness Engineering is not Enough: Why Software Factories Fail — Dex Horthy, HumanLayer](https://www.youtube.com/watch?v=Ib5GBkD555M)** · aie · 2026-07-23

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we require a human-reviewed architecture doc and program design (component contracts, data models, call stacks, vertical slices) before launching a coding agent, then code review time decreases and rework rate drops because alignment on structure before generation means the agent's output matches expectations rather than requiring re-architecture after the fact.

## What they did

Dex Horthy argued that harness engineering and loop-maxing cannot compensate for the fundamental problem: coding models are trained on benchmarks that don't reflect real production codebase quality, leading to PRs with increased comment counts, more merges without review, and more incidents. His team's solution is a structured pre-planning phase before every agent task: product review with mockups, system architecture docs (component contracts, data models, constraints), and program design (types, method signatures, call stacks, vertical slices with implementation order). He cited Dylan Mullroy's use of call graphs as planning artifacts. He claimed 30 minutes of pre-planning saves hours in review, makes PRs fast to review ('yep, this is exactly what we discussed'), and keeps engineers reading all the code while still moving faster.

## Relevance to YOLO loop

Our yolo loop likely sends tasks directly to coding agents without structured pre-alignment. Adding a lightweight pre-planning doc step — even a 5-minute architecture note and method signature sketch — before each agent coding task would reduce the rework cycles that currently consume loop time and degrade codebase coherence.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-23 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-23-pre-planning-alignment-before-agent-coding` |
| Channel | aie |
| Video | [Harness Engineering is not Enough: Why Software Factories Fail — Dex Horthy, HumanLayer](https://www.youtube.com/watch?v=Ib5GBkD555M) |
| Published | 2026-07-23 |
| Ingested upstream | 2026-07-23 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
