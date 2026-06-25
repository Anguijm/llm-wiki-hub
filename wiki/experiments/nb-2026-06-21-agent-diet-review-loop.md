# Implement a Scheduled Diet Audit for Agent Context Sources

> Back to [[experiments-index]]

Source: **[Most Teams Skip This Critical AI Agent Skill in 2026](https://www.youtube.com/watch?v=rh_PcL26zls)** · nb · 2026-06-21

**Status:** `adopted` · **Verdict:** `adopt` · **Effort:** `medium`

---

## Hypothesis

If we schedule a regular review of each agent's input sources (docs, examples, instructions) to check for staleness or bad examples, then agent output quality will stay consistent over time because agents degrade when their context diet becomes outdated or contains incorrect examples.

## What they did

Nate described the concept of an agent's 'diet' — the documents, tickets, transcripts, repo instructions, and examples fed to the agent as context. He emphasized that stale or messy diets cause agents to produce stale, messy, or incorrect outputs, and that this degrades silently. He recommended treating diet maintenance as an ongoing operational responsibility, not a one-time setup task, and called this the '2026 skill' of agent maintenance distinct from the 2023 prompting skill and 2025 delegation skill.

## Relevance to YOLO loop

Our YOLO loop agents consume context from repo files, docs, and prior outputs. Setting up a periodic diet audit cadence (e.g., weekly check of system prompts and attached files for staleness) maps directly to keeping our coding and review agents accurate and trustworthy.

## Notes

Backlog triage 2026-06-24 (owner-preference model). Scheduled staleness review of context sources — context hygiene + cadence; mirrors learnings-staleness concern.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-21 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-06-21-agent-diet-review-loop` |
| Channel | nb |
| Video | [Most Teams Skip This Critical AI Agent Skill in 2026](https://www.youtube.com/watch?v=rh_PcL26zls) |
| Published | 2026-06-21 |
| Ingested upstream | 2026-06-21 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
