# Rebuild evals in parallel with every major agent architecture change and use production data to surface novel failure modes

> Back to [[experiments-index]]

Source: **[Your Agent Evolved. Your Evals Didn't. — Ameya Bhatawdekar, Braintrust](https://www.youtube.com/watch?v=nxokqOq1imY)** · aie · 2026-08-20

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we treat evals as a living system that must be rearchitected alongside each major model or agent architecture upgrade, and we use production data clustering to discover new failure modes we didn't anticipate, then our eval suite will remain effective across generational model changes rather than becoming stale and misleading.

## What they did

Ameya Bhatawdekar (field CTO, Braintrust) traced how eval requirements evolve through agent architecture generations using a notional SRE agent as the example: (1) single prompt → eval on final answer accuracy/hallucination; (2) RAG chain → eval on retrieval quality + answer quality separately; (3) tool-calling agents → eval on tool selection correctness + parameter accuracy + sequence; (4) multi-agent orchestration → eval on sub-agent coordination, task decomposition, and aggregation. Key insight: each architectural upgrade introduces new surface area for failure. Common failure pattern: teams keep old evals when rearchitecting, so they measure the wrong things. Braintrust's 'Topics' feature does cluster analysis on production data to surface new failure categories the team didn't anticipate. The flywheel: define what good looks like → run evals → observe production → harvest new failure cases (known and novel) → update evals → hill climb → repeat. He emphasized that teams often accept the flywheel concept but don't actually run it — evals go static.

## Relevance to YOLO loop

Critical for maintaining quality as we upgrade our agent architecture. Actionable steps: (1) document current eval suite and what architecture generation it was designed for; (2) when adopting a new model family or agent pattern, explicitly update evals to cover new failure modes; (3) instrument production to harvest failure cases; (4) run cluster analysis on production traces periodically to discover unanticipated failure patterns.

## Notes

Braintrust provides: evals, observability, production data harvesting, Topics (cluster analysis for novel failure discovery). The SRE agent example progression: single prompt → RAG → tool-calling → multi-agent orchestration, with each step requiring eval suite expansion. Key failure pattern to avoid: dropping in a new model expecting the old system to work — old system was built around old model limitations and cannot tap new capabilities without rearchitecting. The 'architecture follows model, evals follow architecture' chain is the core discipline.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-20 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-20-braintrust-eval-flywheel-architecture-generations` |
| Channel | aie |
| Video | [Your Agent Evolved. Your Evals Didn't. — Ameya Bhatawdekar, Braintrust](https://www.youtube.com/watch?v=nxokqOq1imY) |
| Published | 2026-08-20 |
| Ingested upstream | 2026-08-20 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
