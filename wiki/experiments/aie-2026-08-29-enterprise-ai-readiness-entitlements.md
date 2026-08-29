# Audit and fix entitlement models before deploying agents to prevent 100x amplification of permission boundary failures

> Back to [[experiments-index]]

Source: **[Which AI startups actually land enterprise contracts? — Brian Lewis, Millennium](https://www.youtube.com/watch?v=7A65O-0lvKE)** · aie · 2026-08-29

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we audit and repair entitlement models (who can access what, under what conditions) before giving agents access to enterprise systems, then we will prevent agents from inheriting and amplifying existing permission boundary failures, because agents exercise judgment probabilistically across all granted permissions simultaneously rather than following the deterministic decision trees that existing entitlement models were designed for.

## What they did

Brian, from Millennium (a hedge fund with ~8,000 employees and tight compliance requirements), described the enterprise AI adoption gap: only ~5% of demo calls end in signed contracts, with 40% of failures due to efficacy, and significant portions dying in security, reliability, and legal. The most actionable finding for internal AI builders: entitlements need a new paradigm before agents are deployed. In traditional systems, over- and under-entitlement is a nuisance; with agents that can autonomously exercise judgment across all granted permissions, the problem is 100x amplified. He also flagged centralized knowledge (all documentation, support articles, process knowledge in one consumable place) and cross-platform integration as prerequisites. He recommended fixing the 'boring 60%' (entitlements, governance, audit logging) before plugging in AI.

## Relevance to YOLO loop

Before the YOLO loop is given write access to any production system, this is the prerequisite checklist: audit what permissions the agent will inherit, confirm they are scoped to the minimum necessary, and verify audit logging captures all agent actions for review.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-29 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-29-enterprise-ai-readiness-entitlements` |
| Channel | aie |
| Video | [Which AI startups actually land enterprise contracts? — Brian Lewis, Millennium](https://www.youtube.com/watch?v=7A65O-0lvKE) |
| Published | 2026-08-29 |
| Ingested upstream | 2026-08-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
