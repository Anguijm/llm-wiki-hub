# Structure AI Dev Effort Across Scientist, Architect, and Coach Roles

> Back to [[experiments-index]]

Source: **[The Chief AI Officer: Scientist, Architect, Coach — Rania Khalaf, WSO2](https://www.youtube.com/watch?v=9cJrbj23fOA)** · aie · 2026-10-03

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we explicitly allocate team effort across three modes — Scientist (explore/experiment), Architect (product strategy and integration), and Coach (evangelism, documentation, trusted-advisor outputs) — then AI development will be more focused and less overwhelming because each mode has distinct goals and success metrics rather than competing for the same attention.

## What they did

Rania Khalaf, Chief AI Officer at WSO2, described how she breaks the sprawling CAIO role into three focus areas: Scientist (experimenting with new models and approaches, including a small research group publishing papers with undergrads), Architect (extending WSO2's existing API, integration, and identity platforms with AI-specific capabilities like an AI gateway, agent identity, and an agent builder), and Coach (over-communicating internally, educating customers as a trusted advisor, and reporting to the board). She emphasized that the mix of these three varies by company type and AI maturity, and that the Coach dimension surprised her most — requiring heavy evangelism even for someone with 20 years of AI research experience.

## Relevance to YOLO loop

Our dev loop conflates exploration (trying new models/tools), integration (wiring them into the system), and communication (writing up what we learned) into undifferentiated work. Adopting explicit Scientist/Architect/Coach time-boxing could help us ship experiments faster by separating 'try it' sprints from 'wire it in' sprints and ensuring findings are documented and communicated rather than lost.

## Notes

Khalaf notes WSO2 added agent identity (for non-human agents) and an AI gateway to their existing API management platform — a concrete Architect pattern worth examining. She also warns that measurement drives optimization, so choose metrics carefully when moving from experimentation to production. The Coach dimension is often underestimated and may map to our internal retros and external blog/demo outputs.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-03 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-03-caio-scientist-architect-coach-framework` |
| Channel | aie |
| Video | [The Chief AI Officer: Scientist, Architect, Coach — Rania Khalaf, WSO2](https://www.youtube.com/watch?v=9cJrbj23fOA) |
| Published | 2026-10-03 |
| Ingested upstream | 2026-10-03 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
