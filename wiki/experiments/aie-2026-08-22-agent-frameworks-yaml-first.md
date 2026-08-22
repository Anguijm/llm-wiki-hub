# Define background agents in Markdown/YAML with cron+event triggers instead of framework code

> Back to [[experiments-index]]

Source: **[Agent Frameworks Considered Harmful — Rémi Louf, .txt](https://www.youtube.com/watch?v=KHudyx5wW3U)** · aie · 2026-08-22

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we define agents as Markdown/YAML files with cron schedules and event subscriptions rather than Python framework code, then non-technical contributors can author agents, diffs are reviewable in PRs, and new agents appear automatically at runtime because the kernel picks them up from the folder without redeployment.

## What they did

Rémi spent two weeks building his own morning-briefing agent system after finding existing frameworks forced him to edit prompts inside code. He settled on: agents defined as plain Markdown/YAML files (droppable into a folder), a lightweight runtime/kernel that schedules them via cron and routes typed events between agents, structured outputs enforced at the kernel boundary (not per-agent), and open-source model backends. After a month in production at his 15-person company, they had 20 agents contributed by both technical and non-technical staff.

## Relevance to YOLO loop

High relevance: our YOLO loop skills and memory files are already Markdown-first. Extending this to event-driven scheduling (voice note dropped → agent runs) and typed inter-agent events would let us move background tasks out of manual Claude Code sessions into always-on background agents.

## Notes

Repo is public (see QR in talk). Key insight: typed events between agents are non-negotiable for reliability — 20% of events were malformed before enforcing structured outputs. Replaced all third-party APIs with open-source models for this use case.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-22 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-22-agent-frameworks-yaml-first` |
| Channel | aie |
| Video | [Agent Frameworks Considered Harmful — Rémi Louf, .txt](https://www.youtube.com/watch?v=KHudyx5wW3U) |
| Published | 2026-08-22 |
| Ingested upstream | 2026-08-22 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
