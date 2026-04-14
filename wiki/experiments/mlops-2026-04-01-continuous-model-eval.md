# Build a golden-prompt eval suite to detect model regression after upgrades

> Back to [[experiments-index]]

Source: **[Choosing the Right Model is Hard. Maintaining Accuracy is Harder.](https://www.youtube.com/watch?v=HVqyWXa1SJ4)** · @MLOps · 2026-04-01

**Status:** `done` · **Verdict:** `adopt` · **Effort:** `medium`

---

## Hypothesis

If we maintain a set of 5-10 representative YOLO build prompts as a regression suite and run it after any model upgrade, then we catch model behavioral changes before they affect production builds because we have a measurable baseline to compare against.

## What they did

Ash Lewis (Fastino) argued at the Coding Agents Conference that model selection is not one-time — models update, drift, or get replaced, and production accuracy degrades silently. Her team uses agents to continuously test, swap, and tune model choices in production rather than hardcoding a single model.

## Relevance to YOLO loop

The YOLO loop uses claude-sonnet-4-6 throughout. When Claude updates (new versions, behavioral changes), there is currently no mechanism to detect regression. A golden prompt suite would catch these before they silently break build quality.

## Outcome

Built model-eval/ with 8 golden prompts (dev tool, productivity, creative, doc gen, reference, game, converter, data viz), runner with --compare for regression detection, JSON reports. Pairs with model-upgrade-audit.md — audit tells you what to check, eval suite tests whether quality held.

## Notes

Complements mlops-2026-04-01-coding-agent-evals which focuses on past bugs as evals; this card focuses on model regression detection.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-03 | `done` | 8 golden prompts + runner + comparison built |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-04-01-continuous-model-eval` |
| Channel | @MLOps |
| Video | [Choosing the Right Model is Hard. Maintaining Accuracy is Harder.](https://www.youtube.com/watch?v=HVqyWXa1SJ4) |
| Published | 2026-04-01 |
| Ingested upstream | 2026-04-02 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
