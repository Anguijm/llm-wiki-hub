# Test Grokbot as a Persistent Multi-Agent Team with Shared Plugin Context

> Back to [[experiments-index]]

Source: **[Grok Bot is For Real. What You Need to Know.](https://www.youtube.com/watch?v=PQBYZQqan2g)** · nh · 2026-08-12

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we set up a team of specialized persistent agents in Grokbot (each with a distinct role description), connect shared plugins once, and let agents delegate tasks to each other automatically, then multi-step workflows will complete faster with less manual orchestration because agents route sub-tasks to the most appropriate specialist without human intervention.

## What they did

The speaker walked through setting up Grokbot—a desktop and mobile app where each bot has its own persistent browser/computer session. He created specialized agents (executive assistant 'Klaus', developer 'Dev') with role descriptions that the system uses to auto-route tasks between them. Shared plugins (GitHub, Gmail, Google Calendar) are connected once and shared across all agents. He demonstrated Klaus delegating a UI build task to Dev after receiving brand guidelines, the two agents exchanging messages and iterating on a waitlist form. He also showed the 'teach a task' feature, where recording a browser action auto-generates a reusable skill, and scheduled routines (e.g., 7am daily briefing from calendar + Gmail).

## Relevance to YOLO loop

Offers a mobile-accessible, always-on alternative orchestration layer for our agent team. Worth evaluating whether Grokbot's inter-agent delegation and persistent sessions reduce the overhead of manually coordinating Hermes/Claude Code agents on recurring workflows.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-12 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-08-12-grokbot-persistent-agent-team` |
| Channel | nh |
| Video | [Grok Bot is For Real. What You Need to Know.](https://www.youtube.com/watch?v=PQBYZQqan2g) |
| Published | 2026-08-12 |
| Ingested upstream | 2026-08-12 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
