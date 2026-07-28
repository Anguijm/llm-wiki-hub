# Deploy a multi-turn scoping agent to front-load requirements gathering before engineering work begins

> Back to [[experiments-index]]

Source: **[How Forward Deployed Engineering is done at Ramp — Leo Mehr](https://www.youtube.com/watch?v=ITMXwI6QL6A)** · aie · 2026-07-28

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we insert an agent that conducts iterative back-and-forth questioning with request submitters before a spec is created, then we will reduce wasted engineering effort by at least 20%, because most requests contain under-specified assumptions that cause rework when discovered late (e.g., building Android when the customer only uses iOS).

## What they did

Leo Mehr described a Ramp internal tool — illustrated with a penguin mascot for approachability — that intercepts feature/integration requests from account managers and conducts multiple rounds of clarifying questions until it judges the request is ready to generate a spec. This replaced asynchronous human back-and-forth (hours or days of latency) with seconds-latency automated scoping. He reported it saves approximately 20% of time previously spent on manual scoping and serves as the first stage of a larger agentic pipeline from intake to shipped feature.

## Relevance to YOLO loop

Maps to the front of the YOLO loop. A scoping agent that clarifies intent before code generation begins would reduce iteration cycles caused by ambiguous initial prompts, improving first-pass quality.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-28 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-28-ramp-scoping-agent-intake` |
| Channel | aie |
| Video | [How Forward Deployed Engineering is done at Ramp — Leo Mehr](https://www.youtube.com/watch?v=ITMXwI6QL6A) |
| Published | 2026-07-28 |
| Ingested upstream | 2026-07-28 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
