# Offload all reasoning to scaffolding code and use the smallest model that fits the latency budget

> Back to [[experiments-index]]

Source: **[Your Voice Agent Doesn't Need a Frontier Model - Joel Allou & Ornella Bahidika, Microsoft](https://www.youtube.com/watch?v=fnLBmfsI_Fg)** · aie · 2026-07-20

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we extract all reasoning, state tracking, and decision logic from the LLM into deterministic scaffolding code and feed the model only the pre-computed action it needs to execute, then a small model (e.g., Haiku 4.5) will match frontier model quality at ~900ms response time versus 2+ seconds, because model latency is dominated by reasoning tokens that the scaffolding already eliminated.

## What they did

Joel and Ornella demonstrated side-by-side latency comparisons: Claude Opus 4.7 with no scaffolding took several seconds to answer a simple lesson question; Haiku 4.5 wrapped in their state machine scaffolding answered the same question in ~900ms. They extracted lesson logic, student mastery tracking, next-step decisions, and whiteboard display instructions entirely into code. The model receives a pre-computed summary each turn and only produces speech output. They acknowledged the trade-off: small models drift on long unstructured tasks, so strict scaffolding rules must be written once in code rather than re-paid on every inference call.

## Relevance to YOLO loop

For any real-time or high-volume step in the YOLO loop (e.g., inline code review, quick lint checks, fast feedback cycles), replacing a frontier model call with a small model plus pre-computed context could cut per-step latency by 2-3x and reduce API costs significantly.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-20 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-20-small-model-voice-latency` |
| Channel | aie |
| Video | [Your Voice Agent Doesn't Need a Frontier Model - Joel Allou & Ornella Bahidika, Microsoft](https://www.youtube.com/watch?v=fnLBmfsI_Fg) |
| Published | 2026-07-20 |
| Ingested upstream | 2026-07-20 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
