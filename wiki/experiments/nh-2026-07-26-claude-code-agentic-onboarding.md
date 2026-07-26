# Build a local AI operating system in Claude Code with persistent context across all business tools

> Back to [[experiments-index]]

Source: **[This AI Technology Will Replace Millions (Here's How to Prepare)](https://www.youtube.com/watch?v=Ums8suyAG1A)** · nh · 2026-07-26

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we configure Claude Code with a persistent local project that indexes emails, meeting transcripts, calendar, Slack, and YouTube analytics, then the agent's usefulness on every task compounds over time because it accumulates real business context rather than starting cold each session.

## What they did

Nate demonstrated Claude Code (local desktop app working from local files rather than web chat) configured with a project he calls 'Herc 2'—his AI operating system. It reads all his emails, communication, meeting transcripts, and external tool data (YouTube analytics via API connection). He showed a /goal slash command that keeps Claude working until a condition is met, used to pull all Q2 2026 YouTube videos, analyze comments and click-through rates, and produce actionable insights without any manual data export. He outlined a three-step onboarding: (1) start talking to it about your role, goals, and preferences on small tasks; (2) pick one real recurring task and iterate with corrections until output is usable; (3) stack tasks and connect Claude to live tools (Gmail, Slack, calendar) so it can read live business state. He emphasized tracking a before/after metric (e.g., hours saved, leads generated) to validate ROI.

## Relevance to YOLO loop

The persistent-context local agent setup is a prerequisite for any long-horizon YOLO loop—the agent needs stable memory of project state, prior decisions, and tool connections to act autonomously across sessions rather than requiring re-briefing each run.

## Notes

Slash commands (/goal, etc.) used as a lightweight agentic protocol layer worth exploring. The 'manager not operator' framing is useful for calibrating how much autonomy to grant vs. how much review to require in early loop iterations.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-26 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-07-26-claude-code-agentic-onboarding` |
| Channel | nh |
| Video | [This AI Technology Will Replace Millions (Here's How to Prepare)](https://www.youtube.com/watch?v=Ums8suyAG1A) |
| Published | 2026-07-26 |
| Ingested upstream | 2026-07-26 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
