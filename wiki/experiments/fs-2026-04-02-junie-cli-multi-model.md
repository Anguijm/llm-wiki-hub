# Evaluate Junie CLI multi-model routing for harness-cli council

> Back to [[experiments-index]]

Source: **[He just crawled through hell to fix the browser...](https://www.youtube.com/watch?v=vd14EElCRvs)** · fs · 2026-04-02

**Status:** `done` · **Verdict:** `adopt` · **Effort:** `low`

---

## Hypothesis

If we route different council angles to different models (e.g. Claude for architecture, Gemini for security, GPT-4 for product) like Junie auto-switches models per task, then council quality improves because each model has different strengths.

## What they did

JetBrains Junie CLI automatically switches between GPT-4, Claude Haiku, and Gemini Flash depending on the task — optimizing for speed, cost, and capability per call.

## Relevance to YOLO loop

Directly applicable to harness-cli council. Currently all 3 council angles use the same model. Multi-model routing could improve quality and reduce cost by using cheaper models for simpler angles.

## Outcome

Implemented in harness-cli. Per-angle model_overrides in harness.yml. Backward compatible. Each council angle can use a different LLM.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-03 | `backlog` | Extracted from Fireship video — Junie CLI multi-model pattern |
| 2026-04-03 | `done` | Shipped to harness-cli |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `fs-2026-04-02-junie-cli-multi-model` |
| Channel | fs |
| Video | [He just crawled through hell to fix the browser...](https://www.youtube.com/watch?v=vd14EElCRvs) |
| Published | 2026-04-02 |
| Ingested upstream | 2026-04-03 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
