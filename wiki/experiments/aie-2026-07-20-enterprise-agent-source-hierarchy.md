# Structure agent knowledge sources as a ranked hierarchy from curated to flexible

> Back to [[experiments-index]]

Source: **[Enterprise Agents Have a Structure Problem - Ishita Daga, Tesla](https://www.youtube.com/watch?v=B8l81jhvHbI)** · aie · 2026-07-20

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we rank agent knowledge sources from most curated (semantic layer with KPI definitions) to most flexible (raw database graph) and instruct the agent to resolve queries by starting at the cleanest tier, then ambiguity errors will decrease because the agent always has an unambiguous authoritative source to consult before falling back to less structured data.

## What they did

Ishita identified three root causes of enterprise data agent failures: ambiguity (which knowledge base to use), staleness (context goes stale as processes change), and preference (different teams calculate the same metric differently). For ambiguity, she proposed a three-tier source-of-truth hierarchy: (1) semantic layer with curated KPI definitions and business logic, (2) canonical parametric queries with flexible filter selection, (3) a full database graph for maximum flexibility but high maintenance cost. She recommended enterprises implement tiers 1 and 2 first as they solve ~80% of cases. For staleness, she proposed a context lifecycle with live-updating data sources (GitHub, CRM, DBT/Tableau semantic layers) plus an event-driven feedback loop that logs incorrect answers and triggers context updates with automated evaluation. Preference remains an open problem she acknowledged has no clean solution yet.

## Relevance to YOLO loop

The YOLO loop's agent needs to resolve which codebase context, documentation, or API reference to use for a given task. Implementing a ranked context hierarchy (pinned project docs > repo README > general web knowledge) would reduce the agent choosing stale or wrong references.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-20 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-20-enterprise-agent-source-hierarchy` |
| Channel | aie |
| Video | [Enterprise Agents Have a Structure Problem - Ishita Daga, Tesla](https://www.youtube.com/watch?v=B8l81jhvHbI) |
| Published | 2026-07-20 |
| Ingested upstream | 2026-07-20 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
