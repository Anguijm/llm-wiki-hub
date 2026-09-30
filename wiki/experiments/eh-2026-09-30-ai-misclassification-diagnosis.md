# Deliberately Probe Model Misclassification to Expose Reasoning Failure Modes

> Back to [[experiments-index]]

Source: **[Why This AI Called a Car a Horse](https://www.youtube.com/watch?v=ieRgWP3C66Y)** · eh · 2026-09-30

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we systematically feed AI models inputs that produce obvious misclassifications, then we can map the failure modes in their reasoning pipeline because understanding why a model makes a confidently wrong call reveals brittleness in embedding or context-window assumptions that affect our own pipelines.

## What they did

The creator examined a case where an AI model incorrectly identified a car as a horse, then investigated the root cause of that hallucination or misclassification — likely exploring model internals, prompt context, or training data artifacts to explain the failure.

## Relevance to YOLO loop

Maps to the eval and red-teaming phase of our dev loop — building a small adversarial test suite that catches confident wrong answers before they reach production or a user-facing demo.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-30 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `eh-2026-09-30-ai-misclassification-diagnosis` |
| Channel | eh |
| Video | [Why This AI Called a Car a Horse](https://www.youtube.com/watch?v=ieRgWP3C66Y) |
| Published | 2026-09-30 |
| Ingested upstream | 2026-09-30 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
