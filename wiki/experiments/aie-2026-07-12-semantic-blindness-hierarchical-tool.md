# Replace large-context entity lookup with a deterministic hierarchical resolver tool handed to the LLM

> Back to [[experiments-index]]

Source: **[Semantic Blindness: 500,000 Sensors Confused an LLM - Raahul Singh & Vanč Levstik, Phaidra](https://www.youtube.com/watch?v=EUsPvBeIx70)** · aie · 2026-07-12

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we model structured entity namespaces (sensors, resources, files) as a traversable hierarchy and expose a deterministic path-resolver as an LLM tool instead of stuffing all names into context, then recall accuracy will be near-perfect and token cost will be O(tree depth) rather than O(entity count), because LLMs fail on near-identical token sequences at scale but excel at navigating structured trees step by step.

## What they did

Phaidra engineers described 'semantic blindness': at 1 GW data-center scale with 400k+ GPUs and supporting equipment, neither naive LLM context stuffing nor RAG vector search worked—vector search failed on near-identical names (Chiller 6 vs Chiller 7), and LLMs hallucinated phantom equipment or silently dropped real ones. Their solution: (1) model the facility as a hierarchy (data center → data hall → aisle → row → rack → GPU), (2) give the LLM a linearized path summary (small finite list) so it can navigate root-to-leaf, (3) implement exact set logic, counting, and dedup as deterministic Software 1.0 code tools, and (4) let the LLM handle only ambiguous query parsing and final answer synthesis. Result: zero failures on 66 test cases across 6 production systems, token cost flat at ~9k tokens regardless of whether the system had 64 or 460k GPUs (vs 116M tokens for the old approach).

## Relevance to YOLO loop

Directly applicable whenever our agents must resolve entities from large, similarly-named namespaces (files, PRs, API endpoints, config keys). The pattern—start 3.0 (prompt everything), identify what has structure, migrate that to 1.0 deterministic tools—is a reusable design heuristic for any agent that degrades at scale.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-12 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-12-semantic-blindness-hierarchical-tool` |
| Channel | aie |
| Video | [Semantic Blindness: 500,000 Sensors Confused an LLM - Raahul Singh & Vanč Levstik, Phaidra](https://www.youtube.com/watch?v=EUsPvBeIx70) |
| Published | 2026-07-12 |
| Ingested upstream | 2026-07-12 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
