# Give AI Agents Git-Branching Parity for Database Schema Changes with One-Click Revert

> Back to [[experiments-index]]

Source: **[Move Fast and Don't Break Things: Scaling Databases for the AI Era — PlanetScale](https://www.youtube.com/watch?v=uKUA1a0Kdfc)** · aie · 2026-10-08

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we expose database schema branching (create branch, apply schema changes, merge via deploy request, one-click revert) through CLI and API interfaces that AI agents can call, then agents performing code changes that require schema migrations will do so more safely and with less human intervention because the schema change lifecycle mirrors the code PR lifecycle agents already understand, and revert capability eliminates the irreversibility risk that currently requires heavy human oversight.

## What they did

PlanetScale (Ben) described a philosophy and product built around applying git-like branching semantics to database schema management. Engineers (and now agents) can branch a database schema, make changes in isolation, then submit a 'deploy request' that merges the schema change to production with zero downtime. If a deployed schema change causes issues, a one-click revert returns to the previous schema state without data loss. This workflow is exposed via MCP server and CLI, allowing coding agents to mirror their code branching workflow with a corresponding database schema branch, enabling schema changes to be part of automated PR flows. They also covered isolation (data plane separated from control plane so a bad control plane deploy doesn't affect database access), redundancy (primary + replicas across availability zones), query-level circuit breakers that reject over-budget queries rather than let them take down the whole system.

## Relevance to YOLO loop

When our YOLO loop agents make code changes requiring schema migrations, they currently need a human to handle the DB side. Wiring schema branching into the agent's tool set (via MCP or CLI) would let agents propose and stage schema changes alongside code PRs, with humans reviewing both before merge. The revert primitive is especially relevant for reducing the risk of allowing agents higher automation levels.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-08 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-08-database-isolation-redundancy-agents` |
| Channel | aie |
| Video | [Move Fast and Don't Break Things: Scaling Databases for the AI Era — PlanetScale](https://www.youtube.com/watch?v=uKUA1a0Kdfc) |
| Published | 2026-10-08 |
| Ingested upstream | 2026-10-08 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
