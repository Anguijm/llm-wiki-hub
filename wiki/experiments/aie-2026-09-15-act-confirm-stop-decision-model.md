# Add a confidence-threshold decision layer (Act / Confirm / Stop) to agent actions to reduce user ouch without changing model accuracy

> Back to [[experiments-index]]

Source: **[Act, Confirm, or Stop? Smarter behavior for AI assistants, wearables & robots — Amit Desai, Roku](https://www.youtube.com/watch?v=Zd5b40Jbp_k)** · aie · 2026-09-15

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we add a multi-tier behavioral decision model to our AI agent actions—acting when confidence is high, confirming when medium, and stopping/rejecting when low—then we improve user satisfaction metrics significantly without any changes to underlying model accuracy, because the cost of wrong actions is asymmetric and a naive confidence threshold (e.g. 65%) performs worse than an optimized two-threshold model derived from annotated outcome data.

## What they did

Amit Desai (voice AI expert, Roku/Alexa/startups) presented a framework for improving voice AI user satisfaction via a second knob orthogonal to accuracy: system decision behavior under uncertainty. Using a smart speaker example with 1000 annotated requests (79% correct, 21% wrong), he showed that adding a Stop behavior with an AI-optimized confidence threshold (41%) reduced user dissatisfaction score from 2.1 to 1.27. Adding a three-tier system (Act/Confirm/Stop) with a two-threshold model (T1=41%, T2=49%) further reduced it to 1.26. He emphasized that the relative cost weights of wrong-act vs. confirm-friction vs. stop-rejection must be tuned per surface (TV, wearable, robot) because modality changes the cost of each outcome. The approach is claimed to scale across all voice AI surfaces.

## Relevance to YOLO loop

Directly applicable to any agentic step in our loop where the agent takes consequential actions (file writes, API calls, sends). Adding a confidence-gated confirm step before irreversible actions could significantly reduce costly errors without model changes—we could implement this as a lightweight wrapper around our existing tool-call layer.

## Notes

The cost-weight matrix (wrong act vs. confirm vs. stop) needs to be defined per action type in our system before thresholds can be optimized. Start with a simple two-tier (Act/Stop) before adding Confirm.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-15-act-confirm-stop-decision-model` |
| Channel | aie |
| Video | [Act, Confirm, or Stop? Smarter behavior for AI assistants, wearables & robots — Amit Desai, Roku](https://www.youtube.com/watch?v=Zd5b40Jbp_k) |
| Published | 2026-09-15 |
| Ingested upstream | 2026-09-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
