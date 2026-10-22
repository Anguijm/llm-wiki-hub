# Add an architecture-validation gate to agent workflows

> Back to [[experiments-index]]

Source: **[The Tech Market Changed. Here's How to Survive It.](https://www.youtube.com/watch?v=RNwuFcQ6VmY)** · pl · 2026-10-18

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we add a verification step to Claude Code workflows that makes a separate reviewer agent check each change against stated architectural principles (dependency injection, system design, unit-test coverage) before merge, then unsound architectural direction will be caught earlier because coding agents act as confident yes-men that speed up work but don't judge whether the direction is sound.

## What they did

Philipp Lackner described using agentic coding tools to generate boilerplate, pull requests and automated code reviews across several platforms. He said one generalist developer could replace a 5-person team split across native iOS, native Android and backend. He warned that agents accelerate work but do not validate whether the architectural direction is sound, so engineers must keep and apply architectural fundamentals (dependency injection, architecture, system design, unit testing) to oversee the work. This was DESCRIBED only, with no concrete demo of the workflow.

## Relevance to YOLO loop

high: It directly addresses the yes-man failure mode in agent workflows and could be implemented as a skill, hook or council reviewer in a verification loop.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-21 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `pl-2026-10-18-architecture-review-gate-for-agents` |
| Channel | pl |
| Video | [The Tech Market Changed. Here's How to Survive It.](https://www.youtube.com/watch?v=RNwuFcQ6VmY) |
| Published | 2026-10-18 |
| Ingested upstream | 2026-10-21 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
