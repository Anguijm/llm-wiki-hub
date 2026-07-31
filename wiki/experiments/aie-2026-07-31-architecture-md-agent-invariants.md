# Maintain a minimal architecture.md file as the single source of invariants for all AI coding agents

> Back to [[experiments-index]]

Source: **[fighting slop with slop — Vaibhav Gupta, Boundary](https://www.youtube.com/watch?v=AMiyLItEtLA)** · aie · 2026-07-31

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we maintain a small, rarely-changing architecture.md file (layer structure, major invariants only) that every agent reads as context, then different engineers using different AI tools will produce code that respects architectural boundaries, because the invariants are enforced at the context level rather than through code review.

## What they did

Boundary (builder of the BAML language) operates with no code reviews and no AI tool standardization. To prevent architectural drift, they built a minimal architecture.md file describing compiler layers and core invariants—nothing that changes more often than monthly. Every agent is instructed to reference this file. For architectural boundary violations, they built CI/CD tooling that visualizes the dependency graph and fails builds when layering invariants are broken. They've kept the same architecture for 3-4 months this way.

## Relevance to YOLO loop

In our dev loop, creating a minimal architecture.md with only the most stable invariants (module boundaries, data flow direction, key interfaces) and referencing it in agent context could prevent architectural drift without adding review overhead.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-31 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-31-architecture-md-agent-invariants` |
| Channel | aie |
| Video | [fighting slop with slop — Vaibhav Gupta, Boundary](https://www.youtube.com/watch?v=AMiyLItEtLA) |
| Published | 2026-07-31 |
| Ingested upstream | 2026-07-31 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
