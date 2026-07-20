# Orchestrate heterogeneous coding agents (Claude Code, Codex, Gemini CLI) via tmux pane control

> Back to [[experiments-index]]

Source: **[Tmux + Fable = Cut 35% less token](https://www.youtube.com/watch?v=wCSPgHpcxdc)** · aij · 2026-07-20

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we use a tmux-based orchestration script that lets a master agent spawn and send messages to named panes running different CLI agents (Claude Code, Codex, Haiku), then we can parallelise tasks across the best model for each sub-task without being locked into a single provider, because tmux provides a universal IPC layer that works across any CLI tool.

## What they did

Jason showed a shell script ('open agent team skill') that programmatically creates tmux panes, starts specific CLI agents in each pane (e.g. Codex for one task, Haiku for grammar checking), sends prompts via tmux send-keys, and polls for completion. The master Claude Code session coordinates by reading results back from each pane. He included the script and a reference CLAUDE.md/agent.md delegation section in the AI Builder Club GitHub repo. He also highlighted Orca as a packaged alternative that provides a UI layer over the same orchestration pattern with built-in token tracking.

## Relevance to YOLO loop

Enables our YOLO loop to mix providers per task (e.g. Gemini CLI for front-end, Codex for repo search, Haiku for linting) without a bespoke SDK integration — just shell scripting around existing CLIs.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-20 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aij-2026-07-20-tmux-multi-cli-orchestration` |
| Channel | aij |
| Video | [Tmux + Fable = Cut 35% less token](https://www.youtube.com/watch?v=wCSPgHpcxdc) |
| Published | 2026-07-20 |
| Ingested upstream | 2026-07-20 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
