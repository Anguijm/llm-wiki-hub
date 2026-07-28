# Build shared agent primitives from repeated bespoke implementations to reduce per-customer marginal cost

> Back to [[experiments-index]]

Source: **[Forward Deployed Engineering 101 — Kevin Bai, Anthropic, ex Palantir & Rippling Founding FDE](https://www.youtube.com/watch?v=KwhgfwOSToQ)** · aie · 2026-07-28

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we catalog recurring patterns from bespoke agent implementations and extract them into shared configurable primitives, then each subsequent deployment will require less custom engineering, because the same data model shapes, integration patterns, and workflow structures recur across customers and the marginal implementation cost approaches zero for well-covered patterns.

## What they did

Kevin Bai described the Palantir Foundry model where FDEs build bespoke applications on top of a shared platform, and over time the platform absorbs patterns from bespoke work into reusable primitives. He drew the analogy to AWS — rather than buying server racks, you use DynamoDB because the primitive is general enough to serve a broad swath of customers. He argued the right question is 'how atomic should primitives be?' and answered it depends on industry specificity: some use cases support 60% pre-built primitives with 40% customization, while others need extremely granular configuration. He also described anything generalizable from a customer engagement should be absorbed into the platform long-term.

## Relevance to YOLO loop

Maps to our tool and prompt library strategy. Rather than writing new agent tools per task, we should be identifying which tools appear in multiple tasks and promoting them to first-class shared primitives with tests and documentation.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-28 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-28-anthropic-fde-shared-primitives` |
| Channel | aie |
| Video | [Forward Deployed Engineering 101 — Kevin Bai, Anthropic, ex Palantir & Rippling Founding FDE](https://www.youtube.com/watch?v=KwhgfwOSToQ) |
| Published | 2026-07-28 |
| Ingested upstream | 2026-07-28 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
