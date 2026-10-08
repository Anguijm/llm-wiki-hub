# Build a Multi-Agent Investigation Harness That Reasons Across Code, Infra, Observability, and Knowledge Bases

> Back to [[experiments-index]]

Source: **[The 6 Pillars of an Agentic Harness for Production — Varun Krovvidi, Resolve AI](https://www.youtube.com/watch?v=eXA2tjRZIbY)** · aie · 2026-10-08

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we design a production incident agent that explicitly reasons across four data source domains (code, infrastructure, observability, and knowledge bases) and maintains a causal chain of evidence rather than agreeing with user-suggested theories, then root cause identification will be more accurate and resistant to confirmation bias because grounding conclusions in a traceable evidence chain prevents the model from hallucinating plausible but incorrect causes.

## What they did

Resolve AI built an agentic harness for on-call and incident response that spins up two categories of agents: investigators and responders. Investigators gather metrics, traces, logs, change events, and deployment history, then correlate across code, infrastructure, knowledge bases, and observability platforms to produce a root cause with ruled-out alternative theories explicitly listed. The system is designed to reject user-pushed theories unless they fit the causal chain of evidence. Results are surfaced in a collaborative 'virtual war room' UI integrated with Slack, enabling multiplayer incident response where teammates can interrogate specific hypotheses inline.

## Relevance to YOLO loop

Directly maps to the 'run and fix' axis of our dev loop. The four-domain reasoning pattern (code + infra + observability + knowledge base) and the ruled-out-theories output format are immediately applicable to how we structure agent context during debugging sessions. The anti-sycophancy design (agent refuses to agree unless evidence supports it) is a concrete prompt/architecture pattern we can experiment with in our own agents.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-08 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-08-six-pillars-agentic-harness` |
| Channel | aie |
| Video | [The 6 Pillars of an Agentic Harness for Production — Varun Krovvidi, Resolve AI](https://www.youtube.com/watch?v=eXA2tjRZIbY) |
| Published | 2026-10-08 |
| Ingested upstream | 2026-10-08 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
