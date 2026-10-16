# Feed GNN neighborhood embeddings into an existing gradient-boosted model rather than replacing it

> Back to [[experiments-index]]

Source: **[Judge a Transaction by the Company It Keeps — Somya Rai & MD Sharique, EXL](https://www.youtube.com/watch?v=SHvwutPSeZg)** · aie · 2026-10-15

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we train a two-layer GNN to produce transaction neighborhood embeddings and feed those embeddings as additional features into an existing XGBoost model (rather than replacing XGBoost), then fraud detection true-positive rate at a fixed alert budget will increase significantly because the GNN captures cross-row signals (shared devices, merchant velocity, linked transaction chains) that row-level feature engineering cannot express.

## What they did

Somya Rai and MD Sharique built a GNN-augmented fraud detection system for card-present and online transaction portfolios. Key decisions: (1) Sampling—downsampling without breaking graph connectivity required soft fraud-rate targets rather than naive row dropping. (2) Graph construction—32 derived graph features built without leakage (timestamps on edges enforced temporal discipline). (3) GNN architecture—two-layer message passing with gather/aggregate/update; aggregation function choice (permutation-invariant) was noted as having outsized impact. (4) Serving at 3ms P99—pre-compute user and merchant embeddings only (not per-transaction), storing in a ring buffer of last 5 transactions per user; this collapsed the embedding store from 60GB to 2-3GB. At inference, only the new transaction's two-layer forward pass runs. Three micro-optimizations: pin math library thread pools to 1 before heavy library load (30ms → 1ms), warm model at startup, single in-memory process with distributed cache interface. Results: 27-33% lift in TPR at fixed alert rate, ~$65M projected annualized incremental fraud capture, 3ms P99. Explainability via subgraph attribution; transaction-to-transaction velocity edges carried 0.94 mean importance in card-present cases.

## Relevance to YOLO loop

The pattern of using a GNN to generate embeddings that augment an existing model (rather than replacing it) is broadly applicable to any YOLO loop step where relational context between items matters. The serving architecture decisions (edge-level prediction, cached user/merchant embeddings, ring buffer) are reusable patterns for latency-constrained agentic tools.

## Notes

Two separate models for card-present vs online due to different base fraud rates (0.05% vs 0.6%) and different signal geometry. Explainability is a hard requirement in regulated contexts—subgraph attribution was the solution. Thread-pool pinning trick is a low-effort latency win worth testing independently.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-15-gnn-graph-fraud-detection` |
| Channel | aie |
| Video | [Judge a Transaction by the Company It Keeps — Somya Rai & MD Sharique, EXL](https://www.youtube.com/watch?v=SHvwutPSeZg) |
| Published | 2026-10-15 |
| Ingested upstream | 2026-10-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
