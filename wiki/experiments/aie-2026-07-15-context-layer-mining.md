# Build a Compounding Context Layer by Mining Business System Connections and Reverse-Constructing Semantic Links

> Back to [[experiments-index]]

Source: **[WTF Is the Context Layer? The Missing Infrastructure for Production Agents — Prukalpa Sankar](https://www.youtube.com/watch?v=8G_1-3IO4ZQ)** · aie · 2026-07-15

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we connect heterogeneous business data systems (e.g., CRM, data warehouse, application layer) and use an AI to reverse-construct how entities and metrics relate across those hops, then agent accuracy on business queries will improve substantially because context — the situational knowledge that explains why data means what it means — is currently lost at every system boundary and hardcoding it into prompts does not scale.

## What they did

Prukalpa Sankar argued that model intelligence has 1000x'd in a decade but situated business context has barely moved. She framed performance as a function of intelligence plus context (analogous to IQ vs. on-the-job learning). Her company Atlan built a 'context layer' that: (1) continuously mines knowledge, expertise, and norms from existing business systems; (2) consolidates them into a single company knowledge graph (the 'company brain'); (3) manages this context through skills with versioning, quality, dependency tracking, and approval workflows; (4) harnesses a compounding learning loop where AI reads traces, reverse-constructs what worked, and surfaces approve/reject decisions to maintainers; and (5) exposes retrieved context via MCP, SQL, vector retrieval, and hybrid assembly. She demonstrated the concept through an analyst persona (Maya) who answers 'why is drive-through time up this week?' by knowing metric definitions, seasonal norms, recent product launches, and persona-specific answer formats — all of which must be encoded as machine-usable context for an agent to replicate.

## Relevance to YOLO loop

Our YOLO loop currently hardcodes context into system prompts. This talk argues for externalizing that into a versioned, self-improving context store. Actionable starting point: inventory which facts we currently hardcode, connect two systems (e.g., our issue tracker and codebase), and reverse-construct their semantic relationship as a test of whether mined context improves agent task accuracy versus hardcoded prompts.

## Notes

Key warning from speaker: as we deploy autonomous agents, inconsistent context across systems creates the same problem as asking sales and finance for revenue and getting two different numbers — but now the disagreement is inside autonomous decision-making systems. Context is framed as company IP and competitive differentiator when models are commoditized.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-15-context-layer-mining` |
| Channel | aie |
| Video | [WTF Is the Context Layer? The Missing Infrastructure for Production Agents — Prukalpa Sankar](https://www.youtube.com/watch?v=8G_1-3IO4ZQ) |
| Published | 2026-07-15 |
| Ingested upstream | 2026-07-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
