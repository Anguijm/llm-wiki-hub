# Implement Structured CLAUDE.md Memory Layering for the YOLO Loop

> Back to [[experiments-index]]

Source: **[Every Claude Code Memory Pattern Explained](https://www.youtube.com/watch?v=OMkdlwZxSt8)** · nb · 2026-04-22

**Status:** `adopted` · **Verdict:** `adopt` · **Effort:** `medium`

---

## Hypothesis

If we structure our CLAUDE.md files using the layered memory patterns described (project-level, task-level, and ephemeral), then context will be more precisely scoped per task and we will reduce prompt bloat and irrelevant context injection, because hierarchical memory separation prevents earlier session knowledge from polluting new task contexts.

## What they did

Speaker systematically explained every memory pattern available in Claude Code including CLAUDE.md at repo root, nested CLAUDE.md files per subdirectory, in-conversation memory injection, and ephemeral vs persistent memory strategies, with concrete examples of when to use each.

## Relevance to YOLO loop

The YOLO loop relies on context management for multi-step coding tasks; adopting structured CLAUDE.md layering would give us finer control over what the agent knows at each stage and reduce the likelihood of stale context causing incorrect code generation.

## Notes

Backlog triage 2026-06-24 (owner-preference model). Context/memory discipline on the Claude stack — extends the hot-cache + build_memory patterns already adopted.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-22 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-04-22-claude-code-memory-patterns` |
| Channel | nb |
| Video | [Every Claude Code Memory Pattern Explained](https://www.youtube.com/watch?v=OMkdlwZxSt8) |
| Published | 2026-04-22 |
| Ingested upstream | 2026-04-22 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
