# Invest more time in markdown context files than in code execution

> Back to [[experiments-index]]

Source: **[$75M founder reveals his Agentic Engineering setup](https://www.youtube.com/watch?v=QBfXiWvM0qc)** · do · 2026-08-20

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we spend the majority of engineering time crafting structured markdown context files (skills, architecture, process docs) rather than directly executing code, then agents will produce more consistent, on-target output because the quality of context provided to the agent is the primary determinant of output quality.

## What they did

Alex Lieberman (Morning Brew, 10X) and Dan (director of engineering) described their agentic engineering setup where every coding agent session starts with a 'senior engineer hook' that loads structured markdown files containing project context, architecture, and a 10X process skill. They emphasized spending more time on markdown engineering than on code execution, treating each session as if the agent is a senior engineer who immediately knows the codebase. They use CLAUDE.md-style files, a process skill that tells the agent what to work on next, and a hook that runs at session start to prime context.

## Relevance to YOLO loop

Directly maps to the context-priming phase of our dev loop — improving AGENTS.md, skills files, and session hooks to reduce ramp-up time and improve consistency across agent sessions.

## Notes

Key quote: 'The percentage of time that you spend on engineering the markdown should be higher than the percentage of time that you spend on actually executing the code.' Also emphasized that every session should have the agent start as a senior engineer with full project context via a startup hook.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-20 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-08-20-agentic-engineering-markdown-context` |
| Channel | do |
| Video | [$75M founder reveals his Agentic Engineering setup](https://www.youtube.com/watch?v=QBfXiWvM0qc) |
| Published | 2026-08-20 |
| Ingested upstream | 2026-08-20 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
