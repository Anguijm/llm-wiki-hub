# Register agents under a DUNA for open-internet identity and trust

> Back to [[experiments-index]]

Source: **[Beyond the Lethal Trifecta: Agentic Commerce on the Open Internet — David Levine, Kiduna Club](https://www.youtube.com/watch?v=tE2z8-hqoLY)** · aie · 2026-09-01

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we register AI agents under a Decentralized Unincorporated Nonprofit Association (DUNA) and issue JWT tokens with agent identity claims, then agents can interact with untrusted open-internet content with reduced prompt-injection risk because counterparties can verify agent provenance against a state-registered legal entity.

## What they did

David Levine announced the formation of Kaduna Club, a DUNA registered with the West Virginia Secretary of State, as a legal wrapper for agent organizations on the open internet. The problem framing was the 'lethal trifecta': agents have private data + access to untrusted internet content + ability to take actions, making prompt injection catastrophic. Enterprise response has been to keep agents inside closed platforms (Slack, Salesforce, Notion) with MCP bridges. The proposed fix is a state-registered agent identity registry using JWT tokens with blockchain addresses and capability claims, analogous to how SMTP became the standard for email identity.

## Relevance to YOLO loop

If YOLO loop agents ever operate on the open internet (browsing, form submission, API calls to third parties), agent identity tokens would let receiving services verify and selectively trust our agents. Worth tracking as an emerging standard even if not immediately implementable.

## Notes

Very early stage — Kaduna Club just registered. The lethal trifecta framing (private data + untrusted content + action capability) is a useful threat model checklist for any agent with web access.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-01 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-01-duna-agentic-identity-registry` |
| Channel | aie |
| Video | [Beyond the Lethal Trifecta: Agentic Commerce on the Open Internet — David Levine, Kiduna Club](https://www.youtube.com/watch?v=tE2z8-hqoLY) |
| Published | 2026-09-01 |
| Ingested upstream | 2026-09-01 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
