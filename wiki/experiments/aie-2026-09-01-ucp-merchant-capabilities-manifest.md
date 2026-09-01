# Publish a merchant capabilities manifest and structured catalog to make a service agent-commerce ready

> Back to [[experiments-index]]

Source: **[Teaching agents to pay — Anna Spysz, Stripe](https://www.youtube.com/watch?v=A-zeQiYkmXk)** · aie · 2026-09-01

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we add a /.well-known/merchant-capabilities.json manifest and a structured JSON product/policy catalog to any service, then AI agents using UCP can discover, filter, and transact with that service without token-expensive HTML parsing because agents rely on structured signals rather than visual browsing.

## What they did

Anna built a commerce agent using Stripe's Universal Commerce Protocol (UCP) to autonomously buy headphones. She demonstrated the full flow: agent receives natural language requirements, asks clarifying questions, searches UCP-enabled merchants, and completes purchase using a shared payment token (never exposing raw card number to agent or merchant — only to Stripe). She also showed the merchant onboarding path: (1) publish a /.well-known/ merchant capabilities manifest declaring capabilities, payment methods, and API endpoints; (2) convert product catalog and policies to structured JSON; (3) expose agent-readable endpoints. She showed the persona/system-prompt effect: a pushy-agent system prompt produced aggressive upsell behavior; a trust-focused system prompt produced deferential behavior — demonstrating that system prompt design dominates agent commerce UX.

## Relevance to YOLO loop

Two immediate applications: (1) if any YOLO loop service should be agent-discoverable, the /.well-known/ manifest pattern is a one-file addition; (2) the shared payment token architecture (provider enforces limits, agent never sees raw credentials) is the right pattern for any agent authorized to make purchases.

## Notes

Key finding from persona experiment: system prompt choice is the dominant variable in agent commerce UX — agents with different system prompts behave as completely different purchasing personas on identical tasks. Stripe Developers YouTube channel has follow-up videos on UCP.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-01 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-01-ucp-merchant-capabilities-manifest` |
| Channel | aie |
| Video | [Teaching agents to pay — Anna Spysz, Stripe](https://www.youtube.com/watch?v=A-zeQiYkmXk) |
| Published | 2026-09-01 |
| Ingested upstream | 2026-09-01 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
