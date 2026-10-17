# Replace pre-built schemas with just-in-time ontologies generated at decision time by cheap models

> Back to [[experiments-index]]

Source: **[Just-in-Time Ontologies: What Cheap Intelligence Means for Data — Hrishi Olickel, Southbridge AI](https://www.youtube.com/watch?v=Fa3hQVIKShw)** · aie · 2026-10-13

**Status:** `discarded` · **Verdict:** `discard` · **Effort:** `medium`

---

## Hypothesis

If we defer schema/ontology construction until the specific decision is known and use cheap LLM calls to generate and apply that schema on-demand, then transformation costs will drop dramatically while accuracy stays high, because Southbridge reduced an Ohio campaign finance entity-resolution job from a projected $10,000 to under $800 by swapping models iteratively against a fixed failure surface.

## What they did

Hrishi Olickel argued that universal schemas always fail because there are four simultaneous schemas (source, storage, decision, prior) that are only all known at decision time. His team builds 'just-in-time ontologies': split the problem into typed sub-questions, define a failure surface on a small manually-checked slice, run minimal bounded pilots to find a working architecture, move checks into reusable codons, then iteratively swap in faster/cheaper models and tighten success criteria ('burrito surfing'). Ontologies built this way are stored with their receipts and reused for similar future jobs.

## Relevance to YOLO loop

We often pre-define data structures before running agent tasks. Generating schemas at query time using a cheap model, validated against a small ground-truth slice, could cut cost and improve task-specific accuracy.

## Notes

The 'burrito surfing' technique: fix a baseline result, swap cheaper model, compare against known intermediates, tighten requirements, repeat. Key prerequisite: a well-defined failure surface before any optimization starts.

Backlog triage 2026-10-17 round 3 (operator: "I want you to evaluate the yolo cards"). Settled maybe, cut: Assessment: same move as grounding_ab.py (fix a gold slice, swap cheaper models), which exists, with grounding-gold in 90_meta.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-13 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-13-just-in-time-ontology-burrito-surfing` |
| Channel | aie |
| Video | [Just-in-Time Ontologies: What Cheap Intelligence Means for Data — Hrishi Olickel, Southbridge AI](https://www.youtube.com/watch?v=Fa3hQVIKShw) |
| Published | 2026-10-13 |
| Ingested upstream | 2026-10-13 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
