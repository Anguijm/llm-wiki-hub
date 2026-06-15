# Design multi-agent workflows using flocking algorithm principles (local separation, distant attraction, alignment)

> Back to [[experiments-index]]

Source: **[MCP, Agents & the $40M Bet on Multiplayer AI](https://www.youtube.com/watch?v=NsLPju6TZVc)** · mlops · 2026-06-15

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we structure multi-agent coordination around the three flocking rules — local separation (trust/no micromanagement), distant attraction (shared written context/visibility), and alignment (clear narrow mission) — then agents and humans can self-organize around tasks without heavy orchestration because this mirrors the emergent coordination observed at Stripe 150-500 person scale.

## What they did

Guest (Dust co-founder, ex-Stripe/OpenAI) described how Stripe's 150-500 person scaling worked via an emergent flocking algorithm: (1) local separation via high trust culture, (2) distant attraction via open mailing-list writing culture that connected people working on similar problems, (3) alignment on a simple clear mission (dev API for payments as a country × payment-method tensor to fill). He then mapped this to multiplayer AI design at Dust, arguing current agents are still single-player (tasks under half a day, messy traces) but the transition to multiplayer requires the same three properties. Also discussed agentic search replacing RAG as context windows grow and agent tool use becomes more human-like.

## Relevance to YOLO loop

Provides a framework for designing the coordination layer when YOLO loop scales to multiple concurrent agents. The three flocking properties are concrete design constraints: how much do agents share state (attraction), how much do they trust each other's outputs (separation), and how narrowly scoped is the shared objective (alignment).

## Notes

Dust raised $40M (per title). Speaker also made a pragmatist argument for agentic search over RAG: as context windows grow, just give agents the same search tools humans use and pay the latency tax for simplicity. MCP/CLI as the convergence point for human+agent tool interfaces.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-06-15-multiplayer-ai-flocking` |
| Channel | mlops |
| Video | [MCP, Agents & the $40M Bet on Multiplayer AI](https://www.youtube.com/watch?v=NsLPju6TZVc) |
| Published | 2026-06-15 |
| Ingested upstream | 2026-06-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
