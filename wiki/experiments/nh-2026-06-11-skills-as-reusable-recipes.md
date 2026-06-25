# Build a personal skill library as markdown recipes to replace repetitive prompts with slash commands

> Back to [[experiments-index]]

Source: **[I Tested Every Claude Code Feature, These 12 Are the Best](https://www.youtube.com/watch?v=vfWTyEreOEc)** · nh · 2026-06-11

**Status:** `adopted` · **Verdict:** `adopt` · **Effort:** `medium`

---

## Hypothesis

If we encode every repeated multi-step workflow as a markdown skill file with a slash command, then Claude Code executes those workflows more consistently and with less token waste than ad-hoc prompting, because the agent reads the recipe fresh each invocation rather than relying on in-context instruction drift.

## What they did

Nate ranked Claude Code features in a tiered list and named Skills as his #1 feature. He showed his .claude/skills folder containing dozens of markdown skill files covering tasks like session handoff, thumbnail generation, video trimming, Excalidraw presentations, and agent building. He explained skills can be simple (4-sentence prompt turned into a slash command) or complex (multi-step workflows that chain to other skills). He demonstrated /context and /usage slash commands for session visibility, and the status-line customisation showing model, effort level, and context % — all implemented as skills. Skills work identically in Claude Code terminal, desktop app, VS Code extension, and Claude Chat/Co-work.

## Relevance to YOLO loop

Skills are the primary mechanism for encoding loop steps (plan, execute, review, handoff) as reusable, shareable, version-controlled artifacts that any agent in the loop can invoke.

## Notes

Top 12 ranked features: #1 Skills, #2 Status line, #3 /context + /usage visibility, #4 Sub-agents, #5 Session handoff skill, #6 Hooks, #7 Git worktrees, #8 Dynamic workflows, #9 Deep research workflow, #10 MCP, #11 Web search/fetch, #12 CLAUDE.md. D-tier: themes, file uploads, fast mode, permissions.

Backlog triage 2026-06-24 (owner-preference model). Direct match to adopted pre-wired recipes + skill files.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-06-11-skills-as-reusable-recipes` |
| Channel | nh |
| Video | [I Tested Every Claude Code Feature, These 12 Are the Best](https://www.youtube.com/watch?v=vfWTyEreOEc) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
