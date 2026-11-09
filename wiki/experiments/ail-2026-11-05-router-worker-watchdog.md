# Trial a no-code router agent with a 10-minute watchdog

> Back to [[experiments-index]]

Source: **[Deepseek Just Released The Greatest Claude Code Workflow Ever](https://www.youtube.com/watch?v=3DklR44DHnM)** · ail · 2026-11-05

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we make the ops session a router that only reads a board.md of tickets (each with rd.md and eval.md), dispatches them to Sonnet workers in separate git worktrees, and add a watchdog that checks every 10 minutes for hung sessions, then more parallel work finishes with fewer stalled sessions because the coordinator never gets pulled into implementation and hung workers are caught on a timer.

## What they did

The video implements DeepSeek's 'Super Agent' pattern in Claude Code. Tickets are folders holding rd.md (requirements) and eval.md (test criteria). A board.md lists tickets by solo or team mode and by dependency order. A lead router is told by its system prompt not to write code. Sonnet workers run each ticket in an isolated git worktree. A Sonnet watchdog with a 150k token memory cap runs every 10 minutes to unblock hung sessions. Merger and checker agents combine finished worktrees into main and verify them with Agent Browser. The speaker cites DeepSeek's result that the slowest task took 15.7 minutes against 29.5 minutes for a single session. In the speaker's own test the router finished three tickets in an hour (26, 11 and 17 minutes). Caveats: it uses many more tokens because each worker has its own context, and the router can only be restricted by prompt, not by removing tools.

## Relevance to YOLO loop

high: a coordinator forbidden from writing code, paired with a timed watchdog for hung workers, is not covered by the existing fresh-context reviewers, outcome-stopped loops, or per-thread task practices.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-11-08 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `ail-2026-11-05-router-worker-watchdog` |
| Channel | ail |
| Video | [Deepseek Just Released The Greatest Claude Code Workflow Ever](https://www.youtube.com/watch?v=3DklR44DHnM) |
| Published | 2026-11-05 |
| Ingested upstream | 2026-11-08 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
