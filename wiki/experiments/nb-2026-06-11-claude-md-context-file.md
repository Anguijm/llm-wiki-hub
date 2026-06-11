# Maintain a claude.md standing-context file to prevent context drift across sessions

> Back to [[experiments-index]]

Source: **[Stop Picking Between Claude Code and Codex | Do This Instead](https://www.youtube.com/watch?v=R2-Y1Hjwx2U)** · nb · 2026-06-11

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we maintain a claude.md file that records project structure, commands, rules, and session history, then Claude Code sessions will produce more consistent and higher-quality outputs because the agent always has authoritative project context rather than reconstructing it from scratch.

## What they did

Speaker described how serious Claude Code users keep a claude.md file as a standing note containing how the project works, available commands, and rules. This file is used across sessions so context does not need to be re-established each time, and it anchors plan mode before edits begin.

## Relevance to YOLO loop

A claude.md (or equivalent AGENTS.md / YOLO.md) is a foundational artifact in our loop. This experiment validates maintaining it actively and measuring whether session coherence and fewer correction loops result.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-06-11-claude-md-context-file` |
| Channel | nb |
| Video | [Stop Picking Between Claude Code and Codex | Do This Instead](https://www.youtube.com/watch?v=R2-Y1Hjwx2U) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
