# Give agents a persistent email identity for two-way async communication with external services

> Back to [[experiments-index]]

Source: **[The Next Trillion Internet Users Still Don't Have an Identity — Adi Singh, AgentMail](https://www.youtube.com/watch?v=mBNVKkyfnE0)** · aie · 2026-10-13

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we provision each agent with a dedicated email address (not shared with a human inbox), then the agent can complete multi-step external workflows that require a contact point for confirmations, receipts, and follow-ups, because AgentMail observed that agents signing up for third-party services naturally became the contact point for billing alerts, support, and account recovery—functions that break when agents lack a persistent identity.

## What they did

Adi Singh described AgentMail, an email inbox API for coding agents (OpenCode, Cursor, Claude Code, etc.). He argued that agent identity is accumulated through existing surfaces rather than issued fresh, using email as the example. A demo showed an agent given a dedicated AgentMail address to sign up for Telnyx; Telnyx then used that address as the canonical contact for low-balance alerts, account suspensions, and support—demonstrating that a persistent inbox becomes part of the agent's operational identity. He noted that agents currently borrowing human inboxes create audit and blast-radius problems.

## Relevance to YOLO loop

Our agents that interact with external services (GitHub, APIs, SaaS tools) currently have no email identity for async callbacks. Adding a dedicated agent inbox would enable workflows that require email verification or async confirmations.

## Notes

Key insight: giving an agent its own email creates a scoped audit trail of what it signed up for, what it did with each resource, and how to reach it—analogous to what OAuth does for API access but for human-facing communication channels.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-13 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-13-agent-email-identity-persistent-inbox` |
| Channel | aie |
| Video | [The Next Trillion Internet Users Still Don't Have an Identity — Adi Singh, AgentMail](https://www.youtube.com/watch?v=mBNVKkyfnE0) |
| Published | 2026-10-13 |
| Ingested upstream | 2026-10-13 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
