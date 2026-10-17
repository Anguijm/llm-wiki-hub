# Design new infrastructure tools headless-first with full API/MCP/CLI parity before building any dashboard

> Back to [[experiments-index]]

Source: **[How to build a $10B AI company (Supabase Co-Founder)](https://www.youtube.com/watch?v=2DmP5etgh4U)** · do · 2026-10-16

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we expose every capability through API, MCP server, and CLI before building a UI, then coding agents will be able to use our tools autonomously without human navigation, because agents prefer headless interfaces and dashboards are becoming irrelevant for agent-driven workflows.

## What they did

Supabase co-founder noted that despite years of dashboard investment, users now prefer asking agents to interact with the platform directly; he said if building a new infrastructure company today he would skip the dashboard entirely and provide only agent-accessible interfaces (API, MCP, CLI).

## Relevance to YOLO loop

high: directly informs how we design Claude Code agent harnesses—every capability should be CLI/API accessible so agents can invoke it without human dashboard interaction.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-16 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-10-16-headless-api-first-no-dashboard` |
| Channel | do |
| Video | [How to build a $10B AI company (Supabase Co-Founder)](https://www.youtube.com/watch?v=2DmP5etgh4U) |
| Published | 2026-10-16 |
| Ingested upstream | 2026-10-16 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
