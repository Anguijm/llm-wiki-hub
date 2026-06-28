# Apply a four-phase design framework (requirements → architecture → evaluation → optimisation) before writing any AI system code

> Back to [[experiments-index]]

Source: **[AI System Design: From Idea to Production - Apoorva Joshi, MongoDB](https://www.youtube.com/watch?v=T0HhO4YtTfE)** · aie · 2026-06-28

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we define business constraints, performance requirements, and evaluation criteria before generating any code, then we ship higher-quality AI systems with fewer expensive rearchitecting cycles, because each architectural decision downstream is constrained and validated by explicit upfront requirements rather than discovered through production failures.

## What they did

Apoorva presented a repeatable four-phase framework for AI system design using a health insurance claims review system as the worked example. Phase 1 (Product Requirements): write a user-specific, measurable, solution-agnostic business problem statement; enumerate regulatory/data/procurement/performance constraints; classify AI's role (critical vs complementary, reactive vs proactive, augmentation vs automation). Phase 2 (System Design): choose data sources and architecture patterns that satisfy constraints; decide where human-in-the-loop is mandatory (e.g. denial decisions). Phase 3 (Evaluation & Monitoring): define offline eval metrics before building; instrument production to track implicit quality signals (e.g. human override rate, review latency). Phase 4 (Optimisation): apply prompt engineering, reranking, semantic caching, batch processing, and structured outputs only after baseline accuracy is established. She emphasised designing the simplest system that meets requirements and iterating from there.

## Relevance to YOLO loop

The framework provides the planning scaffold that should precede any YOLO loop setup for a new project. Particularly the constraint enumeration (latency budget, cost ceiling, data residency) and the eval-before-build requirement directly inform what the loop's acceptance criteria should be.

## Notes

MongoDB + Voyage AI stack used in examples but framework is stack-agnostic. GenAI cookbook linked in talk for retrieval technique and agentic pattern examples.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-28 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-28-ai-system-design-framework` |
| Channel | aie |
| Video | [AI System Design: From Idea to Production - Apoorva Joshi, MongoDB](https://www.youtube.com/watch?v=T0HhO4YtTfE) |
| Published | 2026-06-28 |
| Ingested upstream | 2026-06-28 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
