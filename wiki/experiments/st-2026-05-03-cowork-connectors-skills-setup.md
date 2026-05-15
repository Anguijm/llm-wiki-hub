# Configure Claude CoWork with project-scoped skills and scheduled tasks to replace recurring manual workflows

> Back to [[experiments-index]]

Source: **[Claude Cowork Explained in 29 Minutes (for non-coders)](https://www.youtube.com/watch?v=u_8NdSf2VV4)** · @ShawTalebi · 2026-05-03

**Status:** `deferred` · **Effort:** `medium`

---

## Hypothesis

If we set up Claude CoWork with project-specific instructions, memories, and skills plus scheduled tasks for recurring prompts, then daily operational overhead will decrease because Claude will auto-execute routine workflows (e.g., morning briefings, analytics reports) without manual invocation and with context scoped appropriately per project.

## What they did

Speaker walked through setting up Claude CoWork (desktop app, paid plan) with connectors to external services, custom skills scoped to individual projects rather than globally, and scheduled tasks that run prompts at fixed intervals (e.g., executive briefing at 6:30am daily). He also demonstrated sub-agents for long-running tasks, dispatch via mobile for remote task creation, and live artifact dashboards that update automatically. He emphasized progressive disclosure for context management—storing supporting context in external files (Notion, Obsidian) rather than bloating the context window.

## Relevance to YOLO loop

Maps directly to the orchestration and scheduling layer of the dev loop; project-scoped skills prevent context pollution across workstreams, and scheduled tasks eliminate the manual trigger step for known recurring jobs.

## Notes

Deferred 2026-05-10: connector/skills demo is interesting but the concrete skill-creator + plan-first prototypes are already in the tick queue (nh-2026-05-03-claude-code-skill-creator, nh-2026-05-03-superpowers-plan-first-skill). Revisit only if those land and we want to layer connectors.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-05-03 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `st-2026-05-03-cowork-connectors-skills-setup` |
| Channel | @ShawTalebi |
| Video | [Claude Cowork Explained in 29 Minutes (for non-coders)](https://www.youtube.com/watch?v=u_8NdSf2VV4) |
| Published | 2026-05-03 |
| Ingested upstream | 2026-05-03 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
