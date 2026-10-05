# Audit every piece of knowledge in your agent system against a prompt/memory/weights decision matrix and fix misplaced artifacts

> Back to [[experiments-index]]

Source: **[Stop Fine-Tuning to Fix Retrieval Problems — Anant Srivastava](https://www.youtube.com/watch?v=qflLT3SoVbw)** · aie · 2026-10-05

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we explicitly audit each knowledge artifact in our agent system against the three-way decision matrix (prompt=stable behavior/tone, memory=current/large/citable facts, weights=reflexive reasoning patterns) and relocate misplaced artifacts, then agent accuracy will improve and we will eliminate silent failures caused by stale facts baked into fine-tuned weights, because the speaker demonstrated that a real support assistant accumulated a product catalog in fine-tuned weights by accident, causing it to hallucinate discontinued product names after a catalog update.

## What they did

Anant Srivastava described how enterprise AI teams make knowledge routing decisions by accident through incremental product work rather than explicit architecture. He gave a concrete failure example: a support assistant had its product catalog accidentally baked into fine-tuned weights (via support tickets that referenced products), so when the catalog updated, the model hallucinated old product names. He proposed a diagnostic matrix: prompt for small/stable/behavioral knowledge, memory (RAG + agent memory) for current/large/citable facts, and fine-tuning only for reflexive reasoning patterns that have stabilized and won't change. He also described the circulation loop: prompt→memory (durable signals), memory→weights (stable retrieval patterns), weights→memory (once fine-tuned, stop retrieving those examples).

## Relevance to YOLO loop

Immediately applicable: we can audit the YOLO loop's current knowledge distribution across system prompts, RAG indexes, and any fine-tuned models against this matrix. The circulation loop architecture (prompt↔memory↔weights) is a useful mental model for how the YOLO loop's knowledge should evolve as the system matures.

## Notes

Key diagnostic questions from the talk: (1) Is this knowledge small, stable, and about behavior? → prompt. (2) Is this current, large, and needs citation? → memory. (3) Has this pattern stabilized, humans converged, and is the motivation cost reduction not capability? → fine-tune. The 'lost in the middle' problem is cited as the failure mode for over-stuffed prompts.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-05 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-05-prompt-memory-weights-routing` |
| Channel | aie |
| Video | [Stop Fine-Tuning to Fix Retrieval Problems — Anant Srivastava](https://www.youtube.com/watch?v=qflLT3SoVbw) |
| Published | 2026-10-05 |
| Ingested upstream | 2026-10-05 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
