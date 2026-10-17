# Build a pre-task checklist that surfaces unknown unknowns before handing work to an agent

> Back to [[experiments-index]]

Source: **[Matt Pocock: The Most Valuable Skill to Learn in the Age of AI](https://www.youtube.com/watch?v=Z8lf5oWKfj0)** · nh · 2026-10-16

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we create a structured checklist of unknown-unknown categories (security, deployment, edge cases, dependencies) that a human reviews before initiating an agent task, then agent failure modes from unarticulated assumptions will decrease because the agent will have explicit constraints to work within rather than making things up.

## What they did

Matt Pocock identified awareness of unknown unknowns as the core human skill in the agent era—things like security implications, deployment requirements, or unanticipated interactions that the human hasn't thought of. He said if you're not careful about surfacing these before the agent starts, the agent will simply invent answers to fill the gaps, leading to compounding problems.

## Relevance to YOLO loop

high: directly applicable to Claude Code task initiation—adding a pre-flight unknown-unknowns checklist to our harness before each major agent task.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-16 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-10-16-unknown-unknowns-communication-skill` |
| Channel | nh |
| Video | [Matt Pocock: The Most Valuable Skill to Learn in the Age of AI](https://www.youtube.com/watch?v=Z8lf5oWKfj0) |
| Published | 2026-10-16 |
| Ingested upstream | 2026-10-16 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
