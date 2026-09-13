# Replace Monolithic Agents with Skill-Based Architecture Using Progressive Disclosure

> Back to [[experiments-index]]

Source: **[Anthropic Engineer Explains: What to Build Instead of AI Agents](https://www.youtube.com/watch?v=HIRDzMtuWFk)** · nh · 2026-09-13

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we decompose task-specific agent logic into discrete 'skills' with precise YAML front-matter descriptions that a general-purpose agent loads on demand, then we will reduce token waste, improve consistency, and get more reliable outputs because the agent only loads relevant context rather than rebuilding logic from scratch each run.

## What they did

Anthropic engineers Barry Jien and Mahesh Marog stopped rebuilding a separate agent for every job and instead defined reusable 'skills' — each a markdown file with a YAML description, saved scripts, templates, and examples — that a general-purpose agent (Claude Code) loads only when a prompt matches the skill description. Four key practices: (1) Save proven code/scripts inside the skill so Claude never rewrites solved problems (DRY principle). (2) Write precise skill descriptions so progressive disclosure loads only the right skill. (3) Convert one-off corrections into durable instructions appended to the skill file. (4) Bake verification steps (screenshots, source-checking, sub-agent review personas) into the skill so Claude self-reviews before output reaches the human.

## Relevance to YOLO loop

Directly maps to structuring our dev loop's agent layer: instead of ad-hoc prompts per task, we define skills for recurring loop steps (e.g., code review, test generation, PR description) with saved scripts and built-in verification, reducing rework and context bloat across sessions.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-13 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-09-13-skill-based-agent-architecture` |
| Channel | nh |
| Video | [Anthropic Engineer Explains: What to Build Instead of AI Agents](https://www.youtube.com/watch?v=HIRDzMtuWFk) |
| Published | 2026-09-13 |
| Ingested upstream | 2026-09-13 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
