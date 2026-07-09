# Run one high-focus task plus many background agent tasks in parallel

> Back to [[experiments-index]]

Source: **["Stop prompting, start building LOOPS." - swyx](https://www.youtube.com/watch?v=EWk9PBbKqzc)** · do · 2026-07-09

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we designate one high-concentration foreground task while simultaneously running multiple background agent tasks for repetitive or research work, then overall throughput will increase without sacrificing quality on the critical path, because attention is the real bottleneck rather than compute or tokens.

## What they did

swyx described his personal working habit of keeping one high-focus task front-and-center while spawning background agents to handle repetitive, research, or prototyping work in parallel. He uses Devin, Claude, and Codex-style tools across Slack and terminal. He noted that most default engineers hate slop but that embracing slop and filtering for the useful parts is underrated and non-consensus.

## Relevance to YOLO loop

Directly maps to the orchestration layer of the yolo loop: instead of sequential human-in-the-loop prompting, the loop runs background agent threads autonomously while the developer steers only the high-value foreground task, reducing idle time between loop iterations.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-09 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-07-09-stop-prompting-start-loops` |
| Channel | do |
| Video | ["Stop prompting, start building LOOPS." - swyx](https://www.youtube.com/watch?v=EWk9PBbKqzc) |
| Published | 2026-07-09 |
| Ingested upstream | 2026-07-09 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
