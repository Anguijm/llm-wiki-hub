# Configure task-specific model routing rules to cut inference cost 3x without quality loss

> Back to [[experiments-index]]

Source: **[Preferences Over Benchmarks: Model Routing — Archana Kamath & Tyler Gillam, DigitalOcean](https://www.youtube.com/watch?v=FvxY8oPoI8o)** · aie · 2026-08-22

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we route agent sub-tasks to different models based on task type (classification→small open model, code review→frontier, test writing→mid-weight) using natural-language rule descriptions rather than benchmark scores, then we achieve ~3x cost reduction with comparable quality because frontier models are overkill for most subtasks.

## What they did

DigitalOcean's inference router lets users describe workloads in natural language and set cost/latency/quality preferences; a purpose-built routing model (<200ms, open-source) selects the right model per request. Live demo showed a software engineering session costing 8 cents with routing vs 25 cents going straight to Opus, and a full session at 14 cents vs 44 cents — ~3x savings. Router is customizable, evaluatable, and open-sourced via Plamo.

## Relevance to YOLO loop

We could apply the same routing logic to our Claude Code sub-agent calls: cheap models for scaffolding/search/classification, frontier for architecture decisions and security review. Even without DigitalOcean's product, we can implement a simple task-type→model mapping in our harness.

## Notes

DigitalOcean router is free/included with their inference engine. Routing model open-sourced via Plamo. Key principle: no single best model — the right model depends on task, system prompt, cost tolerance, latency needs, and end-user preference.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-22 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-22-model-routing-preferences` |
| Channel | aie |
| Video | [Preferences Over Benchmarks: Model Routing — Archana Kamath & Tyler Gillam, DigitalOcean](https://www.youtube.com/watch?v=FvxY8oPoI8o) |
| Published | 2026-08-22 |
| Ingested upstream | 2026-08-22 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
