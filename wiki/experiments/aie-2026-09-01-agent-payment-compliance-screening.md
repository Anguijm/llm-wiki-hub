# Gate agent payment execution behind wallet-address compliance screening

> Back to [[experiments-index]]

Source: **[Agent Spending Without Controls — Rodrigo Coelho & Pranav Maheshwari, Edge & Node](https://www.youtube.com/watch?v=ZyGMqdIpPoE)** · aie · 2026-09-01

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we integrate a sanctions/AML screening layer (e.g., TRM) that checks counterparty wallet addresses before any agent-initiated transaction is authorized, then enterprise adoption of agentic payments will become feasible because chief legal officers can demonstrate that agents cannot transact with sanctioned or blacklisted entities.

## What they did

Pranav demoed Ampersand's compliance layer where a 'good Claude' and a 'bad Claude' (with a simulated sanctioned wallet address) both attempted microtransactions against a scraping service. With compliance screening disabled, both transacted successfully. After enabling TRM-based wallet screening, the bad Claude's transactions were blocked and rejected with a blacklist reason, while the good Claude continued normally. The demo showed real-time block/reject status in the dashboard. Rodrigo framed the broader argument: traditional payment controls were built for humans with human-in-the-loop approval; agents transact at machine speed and need policy enforcement at the infrastructure layer.

## Relevance to YOLO loop

Any YOLO loop agent authorized to make payments or call paid APIs should have a compliance/policy gate before execution. The pattern — check counterparty identity against a policy store before authorizing spend — is implementable as a middleware wrapper around any payment tool call.

## Notes

Ampersand is built on top of the Graph Protocol / Edge & Node team. x402 protocol used for micropayments. The paid MCP trend (most MCPs currently free, won't stay that way) is a useful forcing function for building payment infrastructure now.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-01 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-01-agent-payment-compliance-screening` |
| Channel | aie |
| Video | [Agent Spending Without Controls — Rodrigo Coelho & Pranav Maheshwari, Edge & Node](https://www.youtube.com/watch?v=ZyGMqdIpPoE) |
| Published | 2026-09-01 |
| Ingested upstream | 2026-09-01 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
