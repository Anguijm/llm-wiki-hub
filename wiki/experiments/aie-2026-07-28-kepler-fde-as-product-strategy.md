# Treat every agent deployment as a product research session — detect the real problem before building

> Back to [[experiments-index]]

Source: **[How Forward Deployed Engineering is done at Kepler — Vinoo Ganesh](https://www.youtube.com/watch?v=1OMHGsUZiqA)** · aie · 2026-07-28

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we require agents and FDEs to validate the actual user behavior before implementing a requested solution, then we will avoid building over-engineered solutions that miss the real need, because stated requirements (e.g., a 47-page BI dashboard spec) routinely collapse to trivial solutions (e.g., a Slack alert) when the actual Monday-morning workflow is observed.

## What they did

Vinoo Ganesh told a story from Palantir where a dispatching company submitted a 47-page requirements document for a custom BI tool estimated at 3 months of work. After 4 months of scoping, an engineer happened to visit on-site and asked what the dispatcher actually does first on Monday morning. The answer was: check if trucks are late, then call to reroute. The entire requirement collapsed to a trivial Slack alert built in 4 hours. He codified this as 'detect the real problem, ship the real thing' and described a checklist FDEs should run before shipping: will I be on a support call about this in 6 months? Am I solving this customer's pain in a way that has negative compounding effects on the product?

## Relevance to YOLO loop

Directly applicable to our agent task intake. Before spinning up an agent to build something, we should require a minimum viable problem statement validated against actual usage patterns, not stated requirements. This is a process gate, not a technical build.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-28 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-28-kepler-fde-as-product-strategy` |
| Channel | aie |
| Video | [How Forward Deployed Engineering is done at Kepler — Vinoo Ganesh](https://www.youtube.com/watch?v=1OMHGsUZiqA) |
| Published | 2026-07-28 |
| Ingested upstream | 2026-07-28 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
