# Orchestrate Claude as Planner and Codex as Executor in a Two-Agent Dev Pipeline

> Back to [[experiments-index]]

Source: **[You Can Make Claude + Codex Plan Together. Here's How.](https://www.youtube.com/watch?v=RChO5deJ_fE)** · Mark_Kashef · 2026-04-28

**Status:** `in_progress` · **Effort:** `medium`

---

## Hypothesis

If we separate planning and code execution into two distinct agents where Claude owns task decomposition and specification while Codex owns code generation and execution, then the combined pipeline will produce higher-quality code with fewer revision cycles than a single-model approach, because each model is operating within its strongest capability domain.

## What they did

Speaker walked through a concrete integration where Claude is prompted to produce a structured plan and task breakdown, which is then handed off to OpenAI Codex as a precise specification for code generation, with both agents communicating through a shared context or message-passing layer.

## Relevance to YOLO loop

Directly applicable to the planning and implementation phases of the YOLO loop; introduces a specialization pattern that could replace the current single-model code generation step with a planner-executor split.

## Notes

[2026-04-29T08:05:00Z] Implemented at experiments/planner-executor/. Adapters degrade to deterministic stubs without API keys, so the scaffold is runnable end-to-end. Promotion to tick queue is the next step.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-28 | `backlog` | Extracted from YouTube RSS |
|  | `` | Implemented as research-spike scaffold at experiments/planner-executor/. See README.md for design and usage. |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mk-2026-04-28-claude-codex-plan-together` |
| Channel | Mark_Kashef |
| Video | [You Can Make Claude + Codex Plan Together. Here's How.](https://www.youtube.com/watch?v=RChO5deJ_fE) |
| Published | 2026-04-28 |
| Ingested upstream | 2026-04-28 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
