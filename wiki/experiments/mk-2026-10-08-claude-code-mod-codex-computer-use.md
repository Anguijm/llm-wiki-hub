# Build a Claude Code Mod That Delegates Computer-Use Actions to Codex via MCP Bridge

> Back to [[experiments-index]]

Source: **[These Mods Take Claude Code to Another Level](https://www.youtube.com/watch?v=UcvD53jqHRU)** · mk · 2026-10-08

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we create a Claude Code mod that bridges to Codex's computer-use MCP server via a persistent local helper, then Claude can orchestrate GUI actions (clicking, typing in native apps) without taking over the user's mouse, because Codex exposes its computer-use tools as an MCP endpoint that any LLM can call once a bridge maintains the session and auto-approves permissions.

## What they did

Mark built a Claude Code mod using a multi-phase prompt: (1) Claude listens to a running Codex session to reverse-engineer which MCP tools it exposes, (2) a launcher script connects to that MCP server, (3) a persistent helper bridge maintains the Codex session and auto-approves permission prompts, (4) Claude acts as the reasoning brain sending actions to Codex's computer-use limbs. Demonstrated by having Claude open the Calculator app, perform arithmetic, and write findings to a formatted text document — all without the user's mouse being taken over. Also built a parallel-sessions mod using slash-goal to spin up Opus for planning, Sonnet for execution, and Haiku for final review, with remote control of sub-threads.

## Relevance to YOLO loop

Directly extends our YOLO loop's action space: Claude agents could perform GUI-based tasks (browser navigation, desktop app interaction) by delegating to Codex computer-use, enabling automation of workflows that lack APIs.

## Notes

Key prompt engineering insight: when Claude refuses to attempt a 'hacky' connection, have it run the target app and observe the tools being invoked live — it usually discovers the connection is possible. Use slash-goal to force battle-testing of the mod. Resources linked in video description.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-08 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mk-2026-10-08-claude-code-mod-codex-computer-use` |
| Channel | mk |
| Video | [These Mods Take Claude Code to Another Level](https://www.youtube.com/watch?v=UcvD53jqHRU) |
| Published | 2026-10-08 |
| Ingested upstream | 2026-10-08 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
