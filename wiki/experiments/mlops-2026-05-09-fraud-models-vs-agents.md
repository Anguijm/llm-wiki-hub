# Keep specialized ML models for high-stakes decisions; use agents only for orchestration

> Back to [[experiments-index]]

Source: **[Why AI Agents Shouldn't Replace Your Fraud Models](https://www.youtube.com/watch?v=HaWk8kAD8ZU)** · MLOps · 2026-05-09

**Status:** `deferred` · **Effort:** `low`

---

## Hypothesis

If we keep purpose-built ML models (e.g. fraud detection) in their domain and use agents only to orchestrate around them, then system reliability and accuracy will be higher than fully replacing these models with general-purpose agents because specialized models have calibrated uncertainty and auditability that LLM agents lack.

## What they did

Inferred from title: the video argues that AI agents are not suitable replacements for specialized fraud detection models, likely covering differences in latency, explainability, calibration, and regulatory requirements.

## Relevance to YOLO loop

Relevant to architecture decisions: when our loop needs to call domain-specific models (classifiers, rankers), we should wire agents to invoke them rather than prompting a general LLM to replicate their behavior.

## Notes

Deferred 2026-05-10: ML-training topic, not our scope (we don't train models). Park.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-05-09 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-05-09-fraud-models-vs-agents` |
| Channel | MLOps |
| Video | [Why AI Agents Shouldn't Replace Your Fraud Models](https://www.youtube.com/watch?v=HaWk8kAD8ZU) |
| Published | 2026-05-09 |
| Ingested upstream | 2026-05-09 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
