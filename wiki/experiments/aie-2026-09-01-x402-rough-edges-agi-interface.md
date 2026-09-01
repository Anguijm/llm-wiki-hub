# Expose paid tool APIs via an agent-readable markdown interface (AGI endpoint) instead of versioned REST APIs

> Back to [[experiments-index]]

Source: **[x402 isn't good (yet) — Jan Curn, Apify](https://www.youtube.com/watch?v=h6mi88VrPtQ)** · aie · 2026-09-01

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we publish a simple markdown document at an agent-readable endpoint (e.g., agi.service.com) describing how agents can authenticate and purchase access to tools, then we can iterate on payment protocol support without breaking existing human-facing API contracts because agents are flexible and can pick up new instructions without backwards-compatibility constraints.

## What they did

Jan described Apify's solution to the problem of supporting multiple competing agentic payment standards (x402, MPP, etc.) without breaking their existing API used by tens of thousands of customers. They created agi.apify.com — a single markdown document not designed for humans — that instructs agents how to buy a prepaid Apify token via x402 or MPP, then use that token through the normal MCP/API. This decouples the payment negotiation layer from the stable API layer. Jan also noted x402 ecosystem maturity issues: even basic tooling like local wallets with QR codes doesn't exist yet, live demo failed due to ecosystem immaturity.

## Relevance to YOLO loop

If any YOLO loop service needs to be monetized or needs to call paid external services, the AGI endpoint pattern — a machine-readable markdown file describing capabilities and payment instructions — is a lightweight way to make it agent-discoverable without rebuilding the entire API.

## Notes

Jan's honest assessment: x402 transaction volume is ~$1M/month (tiny), ecosystem tooling is immature, but the long-term trajectory is strong once token subsidies end and build-vs-buy economics favor purchasing external agent tools. Apify added 20,000 tools to the x402 market in this launch, 10x-ing its size.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-01 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-01-x402-rough-edges-agi-interface` |
| Channel | aie |
| Video | [x402 isn't good (yet) — Jan Curn, Apify](https://www.youtube.com/watch?v=h6mi88VrPtQ) |
| Published | 2026-09-01 |
| Ingested upstream | 2026-09-01 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
