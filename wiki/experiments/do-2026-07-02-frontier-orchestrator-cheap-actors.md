# Use frontier model as orchestrator/planner and cheap open-source models as actor agents

> Back to [[experiments-index]]

Source: **[Fable 5 is back… here is my plan](https://www.youtube.com/watch?v=0akM-5lBurA)** · do · 2026-07-02

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we assign a frontier model (Claude Fable/Opus) exclusively to orchestration, planning, and high-stakes decisions while routing all execution steps (code writing, data transforms, UI fixes) to cost-efficient open-source models (Kimi 2.7, GLM 5.2), then we get near-frontier output quality at 5-7x lower cost because planning quality dominates outcome quality while execution steps are well within smaller model capability.

## What they did

Speaker described his personal agent architecture: Fable (Claude) acts as 'CEO/manager/orchestrator' — handling long-term planning, competitor analysis, product decisions, and agent architecture design. Below it, a layer of cheaper open-source actor agents (Kimi 2.7, GLM 5.2, Miniaxe, DeepSeek) execute the actual steps. He argued that most token spend is wasted having expensive models fix front-end buttons and routine code, which smaller models handle equally well at 25x lower cost.

## Relevance to YOLO loop

Directly maps to our yolo loop's agent dispatch layer. We could implement a two-tier dispatch: the loop's planning/routing node calls the frontier model, then spins up cheaper worker agents for subtask execution. Would require instrumenting per-task cost tracking to validate the savings claim.

## Notes

Speaker also mentions a 'Fable safe prompt' skill he built to reduce classifier rejections when using Claude via API vs. web — worth investigating if we hit refusal rate issues in agentic contexts.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-02 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-07-02-frontier-orchestrator-cheap-actors` |
| Channel | do |
| Video | [Fable 5 is back… here is my plan](https://www.youtube.com/watch?v=0akM-5lBurA) |
| Published | 2026-07-02 |
| Ingested upstream | 2026-07-02 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
