# Require a Research Prototype Taxonomy document before any ML prototype enters the production mono-repo

> Back to [[experiments-index]]

Source: **[Research to Reality: Bringing Frontier ML Research to Production - Vaidas Razgaitis, Higharc](https://www.youtube.com/watch?v=OXMMN-XbxwA)** · aie · 2026-06-28

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If every ML research prototype must produce a structured taxonomy document (domain context, business goal, type contracts, persistence layer, system architecture, and decomposition plan) before software engineers begin productionisation, then the handoff velocity increases and rework decreases, because ambiguity about data representations, type boundaries, and deployment topology is resolved before code review rather than discovered during it.

## What they did

Vaidas described Higharc's three-lever system for getting ML research into production: (1) Research Prototype Taxonomy (RPT) document — a TDD variant in Notion capturing domain-specific data representations (for a 'JP Morgan engineer' unfamiliar with architectural domain), business justification, type safety contracts between the core product repo and ML repo, persistence layer design, system architecture, and a PR decomposition plan. (2) Structured ML mono-repo — separate Python-only AI/ML repo with clear module buckets, templates, and patterns so new research concepts have obvious homes. Uses Modal for GPU compute. (3) Decomposition and stacked PR review plan — use Graphite for stacked diffs to slice monolithic prototypes into dependency-ordered PRs, enabling asynchronous parallel review by domain specialists. The RPT document's architectural layers directly inform the decomposition strategy.

## Relevance to YOLO loop

The RPT document pattern is directly applicable to any non-trivial YOLO loop extension (e.g. adding a new retrieval strategy, a new agent tool, or a custom model integration). It provides the planning artefact that makes the loop's own evolution more systematic.

## Notes

Diagnostic questions at end of talk are useful for self-assessment: Is it obvious where new code goes in the repo? Can you consistently estimate delivery timelines for research concepts? Are the right subject-matter experts identifiable for each PR slice?

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-28 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-28-research-to-production-rpt` |
| Channel | aie |
| Video | [Research to Reality: Bringing Frontier ML Research to Production - Vaidas Razgaitis, Higharc](https://www.youtube.com/watch?v=OXMMN-XbxwA) |
| Published | 2026-06-28 |
| Ingested upstream | 2026-06-28 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
