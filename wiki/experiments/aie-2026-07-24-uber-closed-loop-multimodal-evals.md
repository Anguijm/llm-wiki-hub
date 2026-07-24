# Implement a Swiss-cheese QA gate architecture with redundant eval layers before production publish

> Back to [[experiments-index]]

Source: **[Building Closed-Loop Evals for a Multimodal Agent at Scale — Soumya Gupta & Jai Chopra, Uber](https://www.youtube.com/watch?v=31GUkCBD-Uc)** · aie · 2026-07-24

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we add a final holistic QA gate after all per-stage eval checks in an agentic pipeline, then the rate of bad outputs reaching production decreases because redundant checks at different granularities catch failures that upstream stage-specific evals miss, similar to the Swiss cheese model where no single layer is perfect but overlapping layers block most failures.

## What they did

Described Uber Eats' multimodal food photo enhancement pipeline: (1) image understanding + routing agent (LLM describes photo, structured output, router decides enhance/skip); (2) image editing agent running in a self-correction loop with QA agent feedback; (3) final post-processing + publish-ready QA gate. The final QA is explicitly redundant—it rechecks policy and quality items already checked upstream. Justified redundancy via Swiss cheese model: each layer has holes, overlapping layers block failures. Also described a 'diagnoser' abstraction that ingests feedback from multiple loops (model drift, dog-fooding thumbs down, merchant feedback, design team flags) and routes optimization signals to the specific agent in the pipeline that needs tuning, rather than retraining the whole system. All agent outputs logged in a flat JSON structure accessible to technical and non-technical team members.

## Relevance to YOLO loop

Our agentic skills currently have single-pass QA at best. Adding a final holistic gate before any externally-visible output (client deliverable, PR, email) and a diagnoser that routes production feedback signals back to the specific skill that caused the failure would significantly reduce escaped defects.

## Notes

Flat JSON logging structure is a low-effort win to adopt immediately—single unified log per pipeline run accessible to all stakeholders. Diagnoser pattern is the more ambitious architectural piece. Multimodal specifics (food photo) are domain-specific but the eval loop architecture generalizes.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-24 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-24-uber-closed-loop-multimodal-evals` |
| Channel | aie |
| Video | [Building Closed-Loop Evals for a Multimodal Agent at Scale — Soumya Gupta & Jai Chopra, Uber](https://www.youtube.com/watch?v=31GUkCBD-Uc) |
| Published | 2026-07-24 |
| Ingested upstream | 2026-07-24 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
