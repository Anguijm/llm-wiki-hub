# Redesign agent UX around async delegation with human-pausable conveyor belt and weekly active sessions metric

> Back to [[experiments-index]]

Source: **[Chat and citations won't save your vertical AI - Atul Ramachandran, Filed Inc](https://www.youtube.com/watch?v=RGiXcVxSD3s)** · aie · 2026-07-11

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we replace synchronous chat-based agent interaction with an async delegation model (conveyor belt) where agents run tasks independently and pause only to surface conflicts for human resolution, then users can delegate and leave the platform — increasing completed task sessions while decreasing required active user time — because the bottleneck shifts from user attention to agent throughput.

## What they did

Atul described Filed's evolution from chat+citations to an async 'conveyor belt' product model for tax professionals. Key patterns: (1) agents run long tasks without requiring user presence; (2) when agents hit ambiguity or conflicts they pause and notify users via Slack-style tagging rather than blocking; (3) irreversible actions (like data entry into tax software) require a pre-approved plan before execution; (4) level-2 (direct-use) features are preserved alongside delegation so users can take back control at any time; (5) success is measured by 'weekly active sessions' (tasks completed by agents) going up while 'weekly active users' (humans on platform) goes down.

## Relevance to YOLO loop

Reframes the YOLO loop's human-in-the-loop touchpoints — instead of synchronous approval gates, users receive async interrupts only for genuine conflicts, maximizing autonomous run time.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-11-conveyor-belt-agentic-delegation` |
| Channel | aie |
| Video | [Chat and citations won't save your vertical AI - Atul Ramachandran, Filed Inc](https://www.youtube.com/watch?v=RGiXcVxSD3s) |
| Published | 2026-07-11 |
| Ingested upstream | 2026-07-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
