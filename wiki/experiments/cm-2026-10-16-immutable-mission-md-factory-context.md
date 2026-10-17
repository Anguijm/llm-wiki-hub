# Lock mission.md and engineering.md as immutable files the factory agent is explicitly prohibited from editing

> Back to [[experiments-index]]

Source: **[My AI Dark Factory Dream Is Dead (Here's What Actually Works)](https://www.youtube.com/watch?v=GQatuTWSRqY)** · cm · 2026-10-16

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we mark our core context files (mission.md, engineering.md) as write-protected and add a review step that verifies they were never touched by the agent, then the factory cannot drift its own permissions or scope over time because an agent that can rewrite its own rules will eventually do so in ways that violate human intent.

## What they did

Cole Medin described how his software factory uses a mission.md (out-of-scope items, higher-level direction) and an engineering.md (global coding rules) as the stable context layer. He explicitly never allows the factory to edit these files and includes a review checkpoint to verify they were untouched, preventing the system from modifying its own constraints.

## Relevance to YOLO loop

high: immediately actionable—add a post-run hook in our Claude Code harness that asserts CLAUDE.md and engineering context files were not modified during the agent session.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-16 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `cm-2026-10-16-immutable-mission-md-factory-context` |
| Channel | cm |
| Video | [My AI Dark Factory Dream Is Dead (Here's What Actually Works)](https://www.youtube.com/watch?v=GQatuTWSRqY) |
| Published | 2026-10-16 |
| Ingested upstream | 2026-10-16 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
