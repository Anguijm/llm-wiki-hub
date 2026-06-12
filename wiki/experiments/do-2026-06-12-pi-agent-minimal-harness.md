# Swap Opinionated Agent Framework for Pi Agent's Minimal Harness

> Back to [[experiments-index]]

Source: **[Forget Claude Code, try Pi Agent instead…](https://www.youtube.com/watch?v=jcUqsNpDDDk)** · do · 2026-06-12

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we replace a full-featured opinionated agent (Claude Code / Codex) with Pi Agent's minimal four-tool harness for a defined set of tasks, then we will reduce per-task token overhead and gain faster customization cycles because the 1,000-token system prompt costs 10-15x fewer baseline tokens and imposes no hidden guardrails.

## What they did

David walked through a complete Pi Agent setup: installing via a one-liner curl command, authenticating against OpenRouter to access any model (he used Opus 4.8 fast), configuring thinking effort via Shift-Tab, and running tasks entirely through a minimal bash+file+search+edit toolset. He contrasted Pi's harness philosophy (you adapt it to your workflow) against Claude Code/Codex as mass-market products with large system prompts and opinionated guardrails. He also covered skills (reusable prompt modules), agents.md context files, session management with /resume, conversation sharing with /share, and a CLI-based alternative to MCP servers.

## Relevance to YOLO loop

We can benchmark Pi Agent as a drop-in alternative execution layer inside the YOLO loop for tasks that currently run through Claude Code. The reduced system-prompt overhead is measurable and the multi-provider support lets us swap the underlying model without changing the harness.

## Notes

Pi's anti-MCP stance (wrapping MCP servers as CLI tools via mcp-bridge or pi-mcp-adapter) is an interesting architectural constraint to evaluate. The /share gist feature is immediately useful for sharing agent sessions with the team.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-12 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-06-12-pi-agent-minimal-harness` |
| Channel | do |
| Video | [Forget Claude Code, try Pi Agent instead…](https://www.youtube.com/watch?v=jcUqsNpDDDk) |
| Published | 2026-06-12 |
| Ingested upstream | 2026-06-12 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
