# Build a cron-driven agent that reads a markdown task file and generates a prioritized daily plan

> Back to [[experiments-index]]

Source: **[What do we build now? — Theo Browne, @t3dotgg](https://www.youtube.com/watch?v=xUnRQ9vLXxo)** · aie · 2026-07-08

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we run an agent on a daily cron that reads a personal markdown task file, synthesizes it with calendar and project context, and publishes an HTML work plan to S3, then we get a low-maintenance daily prioritization loop because the entire state is a plain markdown file and the compute cost per run is trivial.

## What they did

Theo described a personal system where a markdown file containing his tasks and notes is read by an agent every morning at 9am via cron. The agent synthesizes the content, helps prioritize, updates a static HTML file, uploads it to S3, and sends back a URL. By 9:15-9:20am he has his day planned. He emphasized this required no custom tooling beyond a markdown file on a cron.

## Relevance to YOLO loop

A minimal agentic harness pattern: persistent state in a flat file, scheduled trigger, output pushed to a URL. Directly applicable as a lightweight task-management layer around our dev loop.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-08 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-08-markdown-cron-daily-planner-agent` |
| Channel | aie |
| Video | [What do we build now? — Theo Browne, @t3dotgg](https://www.youtube.com/watch?v=xUnRQ9vLXxo) |
| Published | 2026-07-08 |
| Ingested upstream | 2026-07-08 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
