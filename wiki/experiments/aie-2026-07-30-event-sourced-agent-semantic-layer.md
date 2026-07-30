# Build a projection-fed semantic layer as the context interface between event-sourced domain and AI agents

> Back to [[experiments-index]]

Source: **[Let's integrate AI Agents in Event-Sourced Systems — Divakar Kumar, FlyersSoft](https://www.youtube.com/watch?v=o6U_2vd967Y)** · aie · 2026-07-30

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we create a denormalized semantic layer that aggregates cross-bounded-context projections (transaction counts, device trust scores, account age, payment history) and expose it exclusively via agent tools, then AI agents can make context-rich decisions on gray-zone cases without coupling to internal domain models, because the semantic layer acts as a stable read-optimized interface that decouples agent context needs from event store internals.

## What they did

Divakar described a tiered fraud detection architecture at FlyersSoft. Tier 1 handled clear approve/block cases via existing rule-based and ML engines. Tier 2 added an agentic layer specifically for gray-zone transactions where neither system could reach a confident verdict. Because their domain used strict bounded contexts (transaction, account, device, payment contexts each unaware of the others), agents couldn't directly query cross-domain data. The solution was a semantic layer: each bounded context publishes denormalized projections via CDC (change data capture) — e.g. transaction context emits averages, counts, recent transactions; device context emits trust scores, location history, IP data; account context emits KYC status, account age. Agents access this layer only through tools. Two specialized sub-agents (rule-migration agent and behavior-analysis agent) each produce a verdict, and a third orchestrating agent synthesizes a final consensus verdict emitted as an event back to the message broker, completing the saga.

## Relevance to YOLO loop

Provides a concrete integration pattern for connecting our agents to existing systems without breaking domain boundaries. If our dev loop agents need cross-service context (e.g. combining deployment state, error logs, and ticket history), building a CDC-fed semantic layer with tool-accessible projections is cleaner than direct DB queries and keeps agent coupling minimal.

## Notes

Key architectural insight: do not replace existing rule-based/ML systems — use agents only for the uncertain gray-zone cases. This staged approach de-risks integration and preserves existing investment. The two-agent consensus + orchestrator synthesis pattern is reusable for any multi-signal decision problem.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-30 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-30-event-sourced-agent-semantic-layer` |
| Channel | aie |
| Video | [Let's integrate AI Agents in Event-Sourced Systems — Divakar Kumar, FlyersSoft](https://www.youtube.com/watch?v=o6U_2vd967Y) |
| Published | 2026-07-30 |
| Ingested upstream | 2026-07-30 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
