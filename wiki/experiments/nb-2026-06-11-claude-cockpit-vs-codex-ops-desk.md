# Map tasks to Claude (steering) vs Codex (dispatching) based on fuzziness

> Back to [[experiments-index]]

Source: **[Stop Picking Between Claude Code and Codex | Do This Instead](https://www.youtube.com/watch?v=R2-Y1Hjwx2U)** · nb · 2026-06-11

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we route fuzzy, ambiguous, or design-judgment tasks to Claude Code and parallelizable, well-defined dispatch tasks to Codex, then we will complete complex projects faster with higher quality because each tool's interface trains the cognitive habits best suited to that work mode.

## What they did

Speaker argued that Claude Code feels like a cockpit—close to the model, good for iterative steering through ambiguity, architecture, and writing—while Codex feels like an operations desk—good for dispatching multiple simultaneous parallel agents. Serious Claude users maintain a claude.md standing-context file, use plan mode before edits, add hooks for automated checks, and use MCP servers. Codex users spin up multiple threads (reading, drafting, checking, browsing) concurrently. The recommendation is to use both tools intentionally based on task type rather than picking one.

## Relevance to YOLO loop

Directly affects how we assign tasks in our dev loop: fuzzy spec work and architecture reviews go to Claude Code sessions with a maintained context file, while parallelizable subtasks (linting, doc generation, test runs, research) get dispatched as Codex threads.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-06-11-claude-cockpit-vs-codex-ops-desk` |
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
