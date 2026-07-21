# Decouple Execution Layer from Context and Compute Layers in Agent Architecture

> Back to [[experiments-index]]

Source: **[Your agent architecture has a half-life of 6 months — Dan Farrelly, CTO, Inngest](https://www.youtube.com/watch?v=X1kp-ABIIxQ)** · aie · 2026-07-21

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we explicitly separate our agent architecture into execution (durability, retries, state), context (models, prompts, tools, memory), and compute (sandboxes, runtimes) layers, then we can swap models and prompts without rewriting orchestration logic, because the execution layer has a much longer half-life than the context layer.

## What they did

Dan Farrelly argued that most agent architectures couple all three layers together, causing model or prompt changes to force full rewrites. He proposed treating execution as the stable, long-lived layer — responsible for resumability, step-level durability, parallel coordination, and observability — while context and compute layers change frequently. He demonstrated this with Inngest's durable execution primitives: resumable steps, event triggers, deferred scoring, and outcome-based evaluation attached to running sessions.

## Relevance to YOLO loop

Core architectural principle for the YOLO loop's orchestration backbone — if we decouple execution from prompt/model choices, we can iterate on models and prompts in the inner loop without destabilizing the outer orchestration layer.

## Notes

Dan's half-life framing is useful for prioritizing refactoring: prompts (weeks) < models (months) < execution (years). Audit current YOLO loop for layer coupling before next major model upgrade.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-21 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-21-execution-layer-decoupling` |
| Channel | aie |
| Video | [Your agent architecture has a half-life of 6 months — Dan Farrelly, CTO, Inngest](https://www.youtube.com/watch?v=X1kp-ABIIxQ) |
| Published | 2026-07-21 |
| Ingested upstream | 2026-07-21 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
