# Build a per-task model routing layer that matches model capability to task complexity to control token costs

> Back to [[experiments-index]]

Source: **[Notion's Token Town — Sarah Sachs, Notion](https://www.youtube.com/watch?v=-I5W5QVAT8E)** · aie · 2026-07-23

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we route each task in our agent pipeline to the cheapest model that meets the quality bar for that task (rather than defaulting every call to a frontier model), then we reduce total token spend significantly because a large fraction of subtasks in a complex pipeline are simple enough for cheaper or smaller models.

## What they did

Notion's AI engineering lead Sarah Sachs described the structural cost problem of building AI-native products: model upgrades silently triple output token counts, new model versions cost 40% more with deprecation deadlines, and companies rarely grow revenue at the same rate. Notion developed conviction about which models are required for which tasks — treating model selection as an ongoing engineering discipline, not a one-time decision. She described building optionality across providers (not committing to a lab, committing to the concept of augmentation), using multi-agent orchestration where different specialized agents (Claude, Codex, Decagon) handle different task types, and measuring ROI at the task level (e.g., 3+ minutes saved per task). She also warned against auto-upgrading models without benchmarking the cost/quality tradeoff first.

## Relevance to YOLO loop

In our yolo loop, every agent call likely uses the same default model. A routing layer — even a simple rule-based one that sends classification/routing tasks to a small model and reserves frontier calls for complex reasoning — could cut costs enough to enable longer autonomous runs or higher iteration frequency.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-23 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-23-notion-token-cost-model-routing` |
| Channel | aie |
| Video | [Notion's Token Town — Sarah Sachs, Notion](https://www.youtube.com/watch?v=-I5W5QVAT8E) |
| Published | 2026-07-23 |
| Ingested upstream | 2026-07-23 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
