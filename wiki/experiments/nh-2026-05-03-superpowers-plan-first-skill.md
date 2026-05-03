# Add Superpowers skill to enforce plan-then-test coding discipline in Claude Code

> Back to [[experiments-index]]

Source: **[I Tried 100+ Claude Code Skills. These 6 Are The Best](https://www.youtube.com/watch?v=eRS3CmvrOvA)** · @NateHerk · 2026-05-03

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we install the Superpowers plugin on all production-bound Claude Code projects, then output code quality and reliability will improve because the skill forces Claude to plan in an isolated environment, write tests before code, and perform two-stage review before delivering results.

## What they did

Speaker installed the Superpowers plugin which overrides Claude Code's default sprint-to-code behavior. It requires Claude to plan the full solution first, work in an isolated environment to protect the main project, write tests before implementation, brainstorm edge cases, and review output against both the spec and code quality standards. He applied it to client-facing automations (HVAC dispatch systems, agency reporting tools) to prevent edge-case failures in production.

## Relevance to YOLO loop

Addresses the most common failure mode in rapid agentic dev loops—rushed code that passes surface inspection but breaks in production; adds a structured quality gate without requiring manual review steps.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-05-03 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-05-03-superpowers-plan-first-skill` |
| Channel | @NateHerk |
| Video | [I Tried 100+ Claude Code Skills. These 6 Are The Best](https://www.youtube.com/watch?v=eRS3CmvrOvA) |
| Published | 2026-05-03 |
| Ingested upstream | 2026-05-03 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
