# Build a multi-agent hive-mind with shared memory database and Telegram interface over Claude Code

> Back to [[experiments-index]]

Source: **[This Claude Code Setup Runs My Entire Business](https://www.youtube.com/watch?v=7aQbN543Mec)** · mk · 2026-05-03

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we layer a shared memory state (graph + table DB), role-specific specialized agents, and a messaging interface (Telegram) on top of Claude Code's existing CLI integrations, then we can orchestrate a full business operating system because each agent inherits all existing tool integrations and can report status, complete tasks, and hand off work through a unified standup/command protocol.

## What they did

Speaker built an 'AI operating system' on Claude Code consisting of: (1) a shared hive-mind memory database visualized as a graph (Obsidian-style) and table showing every agent's completed tasks; (2) specialized agents (research, comms/content, meta-ads, etc.) each with their own instruction sets and scoped skills; (3) a 'war room' chat interface supporting slash commands like /standup to poll all agents simultaneously; (4) a Telegram bridge via Anthropic SDK so he can dispatch tasks and receive reports on mobile. He connected agents to external service CLIs (e.g., Meta Ads CLI) so agents can query live business data. He emphasized hygiene—deciding which skills are global vs. project-scoped—as the foundation before adding memory and scheduling layers.

## Relevance to YOLO loop

Represents the most complete implementation of a persistent agentic dev+ops loop seen in the batch; the standup protocol and shared memory graph are directly applicable to coordinating multiple specialized agents within our own loop and auditing their activity across sessions.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-05-03 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mk-2026-05-03-hive-mind-multi-agent-os` |
| Channel | mk |
| Video | [This Claude Code Setup Runs My Entire Business](https://www.youtube.com/watch?v=7aQbN543Mec) |
| Published | 2026-05-03 |
| Ingested upstream | 2026-05-03 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
