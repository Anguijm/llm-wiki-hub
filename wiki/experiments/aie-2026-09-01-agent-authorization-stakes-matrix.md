# Apply a stakes-and-evidence matrix to classify agent actions and required authorization proof

> Back to [[experiments-index]]

Source: **[Your Agent Just Authorized What?! — Jay Mok & Ben Coumes, Paypal](https://www.youtube.com/watch?v=vGn6N4-bxBY)** · aie · 2026-09-01

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we classify every agent action by stakes (low/medium/high) and ecosystem openness (closed/open counterparty), then we can apply the right authorization mechanism at each tier — from system logs for low stakes to cryptographic verifiable credentials for high-stakes open-internet transactions — because the cost of proof should scale with the cost of reversal.

## What they did

Jay and Ben presented a three-tier stakes-and-evidence matrix for agent authorization. Low stakes / closed ecosystem (e.g., Claude Code with GitHub): granular tool permissions, system logs sufficient for audit, actions reversible. Medium stakes / closed ecosystem (e.g., shared vault OAuth for merchant payments): third-party payment mandate enforces policy, both parties trust a common authority. High stakes / open ecosystem (e.g., autonomous agent transacting with unknown merchant): requires cryptographic verifiable intent — a signed JSON payload with amount, expiry, and merchant binding that only the payment provider can issue. PayPal is shipping an 'approval token' primitive for this tier. They argued this mental model applies beyond payments to any hard-to-reverse agent action: medical orders, e-signatures, securities trading.

## Relevance to YOLO loop

The stakes matrix is immediately usable as a design checklist when adding new tool calls to YOLO loop agents. Any action that is hard to reverse (file deletion, external API calls, database writes, payments) should be classified and gated accordingly. The verifiable-intent pattern for high-stakes actions maps to human-in-the-loop confirmation flows.

## Notes

Three key questions from the talk: (1) Did the human authorize this? (2) Is this allowed right now in this scope? (3) Can we prove it later? These map cleanly to authentication, policy enforcement, and audit logging — three gaps to check in any agent system.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-01 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-01-agent-authorization-stakes-matrix` |
| Channel | aie |
| Video | [Your Agent Just Authorized What?! — Jay Mok & Ben Coumes, Paypal](https://www.youtube.com/watch?v=vGn6N4-bxBY) |
| Published | 2026-09-01 |
| Ingested upstream | 2026-09-01 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
