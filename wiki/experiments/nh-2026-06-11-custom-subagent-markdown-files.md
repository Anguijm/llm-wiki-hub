# Build reusable custom sub-agent files with YAML front-matter for repeatable specialist tasks

> Back to [[experiments-index]]

Source: **[How to Build Claude Subagents Better Than 99% of People](https://www.youtube.com/watch?v=e18sdZLwP7o)** · nh · 2026-06-11

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we define custom sub-agents as markdown files with YAML front-matter (name, model, tools, description) stored in .claude/agents/, then we get consistent, invokable specialist agents that can be shared across the team via the repo and reused across projects, because Claude Code reads these files automatically and makes them available as slash commands.

## What they did

Nate opened VS Code, navigated to .claude/skills (agents), and showed the agent-builder skill as a markdown file with YAML front-matter specifying persona, tools, and instructions. He distinguished built-in generic agents (invoked with a prompt) from custom agent files (markdown in .claude/agents). He explained that project-level agents live in the repo for team sharing, while personal agents live in the home folder for cross-project personal use. He also covered dynamic workflows triggered by the word 'workflow' (rainbow highlight in terminal) and the 'ultra code' effort mode as x-high + auto-workflow.

## Relevance to YOLO loop

Standardises specialist agents (e.g. code reviewer, test writer, doc generator) as portable files that slot into any project's YOLO loop without re-prompting from scratch each session.

## Notes

YAML front-matter is mandatory. Global personal agents go in ~/. Project agents go in <repo>/.claude/agents/. Dynamic workflows store as JS in .claude/workflows/.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-06-11-custom-subagent-markdown-files` |
| Channel | nh |
| Video | [How to Build Claude Subagents Better Than 99% of People](https://www.youtube.com/watch?v=e18sdZLwP7o) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
