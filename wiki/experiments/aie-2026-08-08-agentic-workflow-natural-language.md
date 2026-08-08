# Define agentic background automation with a Slack-style natural-language spec in a single file

> Back to [[experiments-index]]

Source: **[Realtime multiplayer, automation, and you! — Idan Gazit, GitHub](https://www.youtube.com/watch?v=iQ5xldZ9StU)** · aie · 2026-08-08

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we author a GitHub Copilot agentic workflow using a single markdown/config file that combines a skill-invocation header with a plain-English task description (e.g. 'every day check for new releases, read the changelog, plan the upgrade, open a PR'), then we can eliminate manual dependency-upgrade toil because the agent can execute recurring judgment-requiring tasks with no additional scaffolding beyond that one file.

## What they did

Idan Gazit (GitHub Next) created an agentic workflow for his personal Astro site that auto-monitors Dependabot alerts, reads changelogs and migration docs, plans code changes for breaking upgrades, and opens a PR—all triggered on a schedule. The workflow was defined in a single file with a skill-invocation magic line at the top followed by a natural-language description resembling a Slack message to a junior developer.

## Relevance to YOLO loop

Directly addresses the maintenance tax in our dev loop: dependency upgrades and changelog-driven refactors can be handed to a scheduled agent rather than consuming developer attention, freeing the loop for feature work.

## Notes

GitHub Next's Agentic Workflows is already available for public testing. The 'Aces' multiplayer prototype is entering technical preview later in the month of the talk.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-08 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-08-agentic-workflow-natural-language` |
| Channel | aie |
| Video | [Realtime multiplayer, automation, and you! — Idan Gazit, GitHub](https://www.youtube.com/watch?v=iQ5xldZ9StU) |
| Published | 2026-08-08 |
| Ingested upstream | 2026-08-08 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
