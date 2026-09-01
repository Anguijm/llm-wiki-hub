# Encode UX layout rules as a slot hierarchy for AI-generated interfaces

> Back to [[experiments-index]]

Source: **[The End of the Static Screen: Architecting Intent-Driven UX — Gus Iwanaga, commercetools](https://www.youtube.com/watch?v=QrMcNe2jjt8)** · aie · 2026-09-01

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we codify UX knowledge as a component catalog with a page→layout→slot→sub-slot→component hierarchy and feed it to an orchestrator agent, then the AI can generate contextually appropriate UI layouts from natural language queries because the hierarchy constrains valid component placement without hardcoding every screen.

## What they did

Gus described commercetools' generative UX system where an orchestrator agent retrieves eligible components from a catalog and an LLM arranges them according to a codified slot hierarchy (page > layout > slots > sub-slots > component categories). The catalog acts as the contract between the agent and the UI — every property matters. The team inverted the hierarchy for assembly: components map to sub-slots, sub-slots to slots, slots to templates. Key challenges: curating the catalog/schema is extremely labor-intensive, the design team no longer designs pixels but instead curates schemas and synthetic data, and continuous evals are needed at every step. They tested protocols including ATUI, JSON Render, and Open UI.

## Relevance to YOLO loop

If the YOLO loop ever generates UI or dashboards dynamically, the slot-hierarchy pattern is a concrete architecture for constraining LLM layout decisions. More immediately, the catalog-as-contract pattern applies to any domain where structured output must conform to a schema — agent tool definitions, report templates, etc.

## Notes

Gus emphasized that the people/process shift is as hard as the technical shift — UX designers now write schemas and synthetic data queries instead of designing screens. Three Ps framing: people, product, process.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-01 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-01-intent-driven-ux-component-hierarchy` |
| Channel | aie |
| Video | [The End of the Static Screen: Architecting Intent-Driven UX — Gus Iwanaga, commercetools](https://www.youtube.com/watch?v=QrMcNe2jjt8) |
| Published | 2026-09-01 |
| Ingested upstream | 2026-09-01 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
