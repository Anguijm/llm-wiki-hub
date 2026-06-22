# Replace metrics/traces with logs-only observability for agent pipelines

> Back to [[experiments-index]]

Source: **[Logs Are All You Need: Rethinking Observability with AI Agents](https://www.youtube.com/watch?v=RSs0PDsULJM)** · mlops · 2026-06-22

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we instrument AI agent systems using only structured logs (dropping traces and metrics), then we can reduce observability setup friction and still answer all production questions via LLM-powered chat queries, because logs contain sufficient signal and traces/metrics are hard to instrument correctly in agentic workflows.

## What they did

The Sazabi founder argued that the traditional three pillars of observability (metrics, logs, traces) are unnecessary for modern AI-heavy dev teams. His platform strips out traces and metrics entirely, requiring only logs, then surfaces a chat interface and Slackbot so engineers ask natural language questions instead of navigating dashboards. The agent queries the log data and answers questions about uptime, errors, affected customers, and responsible commits. He claimed this dramatically simplifies instrumentation (no Prometheus setup, no span context propagation) while matching or exceeding the value of full-stack observability for teams shipping via agentic coding workflows.

## Relevance to YOLO loop

Our YOLO loop runs agents in production and currently lacks structured observability. Switching to logs-only with an LLM query layer could replace ad-hoc debugging with a chat-driven root cause workflow, directly accelerating the fix cycle after agent failures.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-22 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-06-22-logs-only-observability` |
| Channel | mlops |
| Video | [Logs Are All You Need: Rethinking Observability with AI Agents](https://www.youtube.com/watch?v=RSs0PDsULJM) |
| Published | 2026-06-22 |
| Ingested upstream | 2026-06-22 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
