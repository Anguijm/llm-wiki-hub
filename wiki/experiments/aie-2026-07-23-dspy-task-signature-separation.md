# Wrap every repeated AI task in a DSPy-style typed signature to decouple task logic from model/prompt implementation

> Back to [[experiments-index]]

Source: **[The Unreasonable Effectiveness of Separating the Task from the Model — Maxime Rivest, DSPy](https://www.youtube.com/watch?v=GgLQ02aO-hs)** · aie · 2026-07-23

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we define each repeated AI task as a typed input/output signature (separating the 'what' from the 'how'), then we can swap models, upgrade prompts, and add agentic loops without changing the integration layer, because the contract at the boundary remains stable even as implementation details evolve.

## What they did

Maxime Rivest presented DSPy's core abstraction: treating AI programs as functions with named inputs, typed outputs, and implementation-independent contracts. He demonstrated that once a signature is fixed, the internal implementation can change freely — from a simple prompt to chain-of-thought to an agent with tools — without breaking upstream consumers. He showed a three-part spec model: (1) natural language instructions for what should happen, (2) code constraints for what must happen (e.g., fallback to chain-of-thought if vanilla extraction fails, throw if value is below zero), and (3) evals as the hill the optimizer climbs. He also introduced 'qualitative learning' — using production traces, user actions, and model-interpreted feedback to iteratively refine evals and prompts automatically.

## Relevance to YOLO loop

Our yolo loop likely has prompts and model calls scattered inline. Wrapping each repeated AI step in a typed DSPy signature would make the loop modular: we could benchmark new models against any step in isolation, auto-optimize prompts via DSPy's compiler, and confidently upgrade components without regression risk.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-23 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-23-dspy-task-signature-separation` |
| Channel | aie |
| Video | [The Unreasonable Effectiveness of Separating the Task from the Model — Maxime Rivest, DSPy](https://www.youtube.com/watch?v=GgLQ02aO-hs) |
| Published | 2026-07-23 |
| Ingested upstream | 2026-07-23 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
