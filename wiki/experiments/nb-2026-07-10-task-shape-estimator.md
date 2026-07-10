# Build a task-shape estimator to route work to chat, single-agent, multi-agent, or human

> Back to [[experiments-index]]

Source: **[1.6M agents registered for OpenClaw and did NOTHING.](https://www.youtube.com/watch?v=PRqiGS6fnIM)** · nb · 2026-07-10

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we build a structured estimator that scores tasks on four dimensions (size, independence, separation of concerns, verifiability) plus two cost dials (recurrence, value of a good answer), then we can reliably route each task to the correct execution tier because these dimensions describe the work itself rather than any specific tooling.

## What they did

Nate built an interactive tool where users describe a task, set four estimation sliders (task size, independence, separation of concerns, verifiability) and two cost dials (recurrence frequency and value of a correct answer), and receive a verdict of chat / single-agent / multi-agent / human-only plus a one-click next step into the appropriate tool. He validated the framework by running three concrete tasks on camera: a scheduling task (single agent), a pile-processing task (multi-agent), and a judgment call (human), confirming the estimator produced correct verdicts including a 'do not use AI' recommendation.

## Relevance to YOLO loop

The YOLO loop currently starts tasks without a routing decision, leading to over- or under-engineered agent setups. Adding an estimation gate before task execution would let us deliberately choose single-agent Claude Code runs vs. multi-agent orchestration vs. direct human action, reducing wasted token spend and failed runs.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-10 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-07-10-task-shape-estimator` |
| Channel | nb |
| Video | [1.6M agents registered for OpenClaw and did NOTHING.](https://www.youtube.com/watch?v=PRqiGS6fnIM) |
| Published | 2026-07-10 |
| Ingested upstream | 2026-07-10 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
