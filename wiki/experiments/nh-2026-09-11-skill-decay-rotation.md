# Audit and Prune Agent Skills Every Six Months to Prevent Harness Bloat

> Back to [[experiments-index]]

Source: **[How to Actually Choose the Right AI Agent](https://www.youtube.com/watch?v=6LNlCpQPYFc)** · nh · 2026-09-11

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we schedule a regular (approximately every 6 months) full audit and deletion of accumulated agent skills/rules, then agent performance per project will improve or at least stabilize because stale, contradictory, or redundant skills create silent interference that is hard to attribute to any single cause.

## What they did

Mark Kashef referenced Boris Churnney's recommendation to delete all agent skills every six months, arguing that skills decay rapidly as models and tooling evolve. Mark's own approach: treat everything as project-scoped by default, promote to global only when proven, and maintain a meta-audit system that reviews all operating systems periodically to surface needed improvements. The goal is to control bloat and maintain a small blast radius so that experimental changes in one project folder don't contaminate others.

## Relevance to YOLO loop

Our YOLO loop accumulates CLAUDE.md entries, custom rules, and MCP configs over time. Scheduling periodic prune passes — and tracking which rules were removed and why — would give us a cleaner signal when diagnosing whether a regression is model-related or harness-related.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-09-11-skill-decay-rotation` |
| Channel | nh |
| Video | [How to Actually Choose the Right AI Agent](https://www.youtube.com/watch?v=6LNlCpQPYFc) |
| Published | 2026-09-11 |
| Ingested upstream | 2026-09-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
