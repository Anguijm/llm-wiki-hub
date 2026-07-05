# Build a meta-harness that watches, scores, and auto-PRs fixes for production agent sessions

> Back to [[experiments-index]]

Source: **[The Missing Layer After Launch - Raphael Kalandadze, Wandero AI](https://www.youtube.com/watch?v=kZsf_Sfm7RU)** · aie · 2026-07-05

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we build an observability meta-harness that continuously analyzes production agent session logs (scoring trajectories, detecting silent failures, running computer-use regression checks, and auto-generating fix PRs), then we will catch hidden agent degradation faster than unit tests or dashboards alone, because LLM agents are non-deterministic, their failures are often silent, and production is the only place where the full coverage of real user behavior is revealed.

## What they did

Raphael described Wandero AI's 'missing layer' architecture built after shipping a travel-planning agent. They found that unit tests, regex checks, and simulated conversations caught only a slice of real failures—agents would silently struggle mid-task, recover via lucky workarounds, and report success while giving wrong results (e.g., wrong price calculations). Their solution is a three-component meta-harness: (1) a trajectory-analysis agent that ingests session logs and flags specific failure instances with root-cause descriptions and affected session counts; (2) a high-level pattern dashboard that runs periodically, clusters failures across hundreds of sessions, scores sentiment and tool-call success rates, and surfaces systemic issues; (3) a computer-use agent that opens a real browser, logs in, sends test messages, and checks UI artifacts to catch problems invisible in logs. All three components feed back into a loop that can send automatic PRs or notifications. He emphasized the meta-harness needs access to trajectories, database, and UI—same context a human would need.

## Relevance to YOLO loop

Addresses the yolo-loop blind spot that exists after a task completes: the loop currently has no signal on whether the shipped agent is actually working correctly in production. This meta-harness pattern adds a continuous outer loop—observe → score → cluster → auto-fix—that closes the gap between 'task finished' and 'task successful for users'.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-05 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-05-post-launch-agent-observability` |
| Channel | aie |
| Video | [The Missing Layer After Launch - Raphael Kalandadze, Wandero AI](https://www.youtube.com/watch?v=kZsf_Sfm7RU) |
| Published | 2026-07-05 |
| Ingested upstream | 2026-07-05 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
