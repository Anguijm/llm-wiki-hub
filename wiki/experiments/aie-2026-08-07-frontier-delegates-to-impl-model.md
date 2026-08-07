# Route Planning to Frontier Model and Execution to Cheaper Implementation Model

> Back to [[experiments-index]]

Source: **[The State of Model Routing — NVIDIA, Cognition, OpenRouter](https://www.youtube.com/watch?v=QHBjufYK8TA)** · aie · 2026-08-07

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we split agentic tasks so that a frontier model (e.g., Claude Opus / GPT-4-class) handles only planning and hard decision-making while a cheaper or open-source model executes implementation sub-tasks, then we can reduce cost by ~40% while maintaining or exceeding frontier-only quality, because the implementation model can explore each sub-task with greater depth and parallelism than the frontier model would apply if doing everything itself.

## What they did

Cognition's co-founder Walden described their Fusion model router, which keeps a frontier model in the loop for planning and delegates implementation work to cheaper models or open-source alternatives. Rather than routing users away from smart models entirely, the system lets the frontier model plan and orchestrate while sub-agents do ground-level work (e.g., exploring a codebase). He reported 40% cost reduction versus using the frontier model end-to-end, with comprehensiveness sometimes exceeding solo frontier runs because multiple sub-agents can explore in parallel. OpenRouter's Dane added that for in-distribution easy tasks, small models already dominate by spend (e.g., Claude Opus being top for classification on OpenRouter).

## Relevance to YOLO loop

Directly maps to multi-step dev loop tasks: use a frontier model for task decomposition and acceptance criteria, then spin cheaper models for code generation, test writing, or doc drafting sub-tasks. Could significantly cut API costs on long agentic runs without sacrificing planning quality.

## Notes

Transcript heavily truncated (39k chars elided). Key routing architecture details from Cognition Fusion blog post would be needed for full implementation. Caching was also mentioned as a cost lever worth exploring alongside routing.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-07 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-07-frontier-delegates-to-impl-model` |
| Channel | aie |
| Video | [The State of Model Routing — NVIDIA, Cognition, OpenRouter](https://www.youtube.com/watch?v=QHBjufYK8TA) |
| Published | 2026-08-07 |
| Ingested upstream | 2026-08-07 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
