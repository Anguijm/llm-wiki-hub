# Build an internal NL-to-SQL agent with persistent widget output for business queries

> Back to [[experiments-index]]

Source: **[Why Can't Anyone Answer Questions About the Business? — Garrett Galow, WorkOS](https://www.youtube.com/watch?v=iUWwcG-C8OU)** · aie · 2026-06-11

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we build a LangGraph agent that translates natural language questions into Snowflake/DB queries guided by a schema context layer, and renders results as declarative code widgets rather than live LLM calls, then non-technical teammates can self-serve data questions reliably because widgets execute deterministically after initial generation.

## What they did

WorkOS built an internal tool called Studio using LangGraph with Claude Opus, connected to Snowflake, Linear, and Notion via an integration proxy. A guidance layer provides schema context and join rules so the agent avoids common SQL mistakes. Query results are rendered as JavaScript widgets that make direct API calls on refresh, removing the LLM from the hot path after initial widget creation. The tool is accessible via a dashboard or a Slack bot.

## Relevance to YOLO loop

Pattern for making our dev loop's data layer queryable by agents: separating LLM-generated code from LLM-at-runtime is a reliability pattern we can apply when agents need repeatable data access in the loop.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-11-studio-nl-business-queries` |
| Channel | aie |
| Video | [Why Can't Anyone Answer Questions About the Business? — Garrett Galow, WorkOS](https://www.youtube.com/watch?v=iUWwcG-C8OU) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
