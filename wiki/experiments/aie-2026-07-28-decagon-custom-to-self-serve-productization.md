# Establish a 'custom becomes self-serve' pipeline to systematically productize one-off agent configurations

> Back to [[experiments-index]]

Source: **[How Forward Deployed Engineering is done at Decagon — Sunny Rekhi](https://www.youtube.com/watch?v=7wu2hsRfvV0)** · aie · 2026-07-28

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If every manual or custom agent configuration performed for one customer is immediately evaluated for generalizability and upstreamed into a self-serve product primitive, then the marginal cost of onboarding subsequent customers decreases while agent quality compounds, because patterns that appear unique to one enterprise recur across customers with high regularity.

## What they did

Sunny Rekhi described Decagon's guiding ethos: 'custom becomes self-serve.' Every time an FDE does something manually for a customer — configuring agent behavior, handling an edge case, building a custom integration — the team asks whether it can be upstreamed into the product so the next customer can self-serve it. He also described ingesting historical support data to proactively recommend which automation to build first based on predicted ROI, rather than just executing whatever the customer asked for.

## Relevance to YOLO loop

Maps to the feedback loop in our dev system. Any agent behavior we hand-tune for a specific task should be evaluated for extraction into a reusable eval, tool, or prompt primitive. This is how the YOLO loop compounds over time.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-28 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-28-decagon-custom-to-self-serve-productization` |
| Channel | aie |
| Video | [How Forward Deployed Engineering is done at Decagon — Sunny Rekhi](https://www.youtube.com/watch?v=7wu2hsRfvV0) |
| Published | 2026-07-28 |
| Ingested upstream | 2026-07-28 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
