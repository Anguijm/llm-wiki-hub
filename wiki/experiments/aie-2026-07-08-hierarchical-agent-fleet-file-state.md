# Externalize all agent state to disk files and use context reset instead of compaction to enable crash-resilient long-running agent fleets

> Back to [[experiments-index]]

Source: **[I Run a Fleet of AI Agents Across Three Machines. Here's What Broke. - Kyle Jaejun Lee, KRAFTON](https://www.youtube.com/watch?v=4kYl2_mqmnQ)** · aie · 2026-07-08

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we store all agent state (mission, current status, handoff artifacts) in structured files on disk rather than in context windows, and reset context by re-reading those files rather than compacting, then agent work survives crashes and context exhaustion because the authoritative state is never only inside the model.

## What they did

Kyle runs a fleet of agents daily across 3 machines (MacBook, Linux A, Linux B). He moved all agent state to a disk directory structure: per-entity workspace with mission file, status file, and handoff folder; shared context in a shared directory; machine-specific state under a machines directory. Instead of using Claude's built-in compact (which discards history unpredictably), he does a full context reset and has the agent re-read its own handoff and history files. He built a review gateway where any agent layer submits a plan and blocks until approved via a web inbox, then a hook auto-fires the work. To move context between machines he commits files to git and uses tmux send-keys over SSH to trigger pulls on remote machines. He resolved git conflicts by separating per-machine directories and routing shared state through pull requests.

## Relevance to YOLO loop

High relevance: externalizing state to files and using reset-over-compact is a pattern we can apply immediately to make our yolo-loop agents resumable after crashes or context overflow without losing work.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-08 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-08-hierarchical-agent-fleet-file-state` |
| Channel | aie |
| Video | [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke. - Kyle Jaejun Lee, KRAFTON](https://www.youtube.com/watch?v=4kYl2_mqmnQ) |
| Published | 2026-07-08 |
| Ingested upstream | 2026-07-08 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
