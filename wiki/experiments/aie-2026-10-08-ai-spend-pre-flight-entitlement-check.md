# Implement Pre-Flight Entitlement Checks and Budget Reservation Before Agent Inference Calls

> Back to [[experiments-index]]

Source: **[Every AI Company Is Accidentally Building a Bank — Dor Sasson, Stigg](https://www.youtube.com/watch?v=cf2IhzqeQH4)** · aie · 2026-10-08

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we check user/agent entitlements and reserve a budget before each inference call (rather than reconciling spend post-invoice), then we prevent runaway agent spend and over-quota usage in real time, because post-hoc settlement (the current industry default) allows unbounded consumption until the invoice arrives — as demonstrated by Anthropic, Replit, and Uber incidents.

## What they did

Dor Sasson from Stigg argued that AI companies are accidentally building banks because they manage token budgets, credit pools, and usage entitlements — financial infrastructure problems. He cited April 2025 pricing emergencies: Anthropic subsidizing third-party agent usage at $150-750/user while charging cents, Replit allowing 3 users to drain an entire org's credit pool, Uber burning its annual AI budget in weeks. Root cause: entitlement checks happen after inference, not before. His proposed architecture: (1) pre-flight entitlement check before inference, (2) budget reservation (escrow) for the estimated cost of the agent task, (3) async reconciliation after the task completes. For agentic workloads where final cost is unknown upfront, agents should check balance at each step and reserve incrementally. He also described how OpenAI's April change (same model, same price per token, but faster token burn rate) was effectively a pricing change that required infrastructure support to handle correctly.

## Relevance to YOLO loop

Our YOLO loop agents can spin up sub-agents unpredictably. Adding pre-flight balance checks and per-agent budget reservations would prevent a single runaway session from exhausting our API budget and provide per-task cost attribution.

## Notes

Stigg product is the infrastructure layer for this. Key pattern for agents: reserve budget at task start → check remaining balance at each tool call → reconcile actual vs reserved at task end. CFO/CIO visibility into AI spend by model, feature, and product is becoming table stakes for enterprise sales. Stigg booth at conference.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-08 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-08-ai-spend-pre-flight-entitlement-check` |
| Channel | aie |
| Video | [Every AI Company Is Accidentally Building a Bank — Dor Sasson, Stigg](https://www.youtube.com/watch?v=cf2IhzqeQH4) |
| Published | 2026-10-08 |
| Ingested upstream | 2026-10-08 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
