# Replace static API keys with a Security Token Service issuing task-scoped ephemeral credentials

> Back to [[experiments-index]]

Source: **[Your Agent Is a Lethal Trifecta (And What to Do About It) — Kim Maida, Keycard](https://www.youtube.com/watch?v=ws9XcGGPBDk)** · aie · 2026-10-13

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we route all agent tool calls through a Security Token Service that evaluates policy before issuing short-lived, task-scoped tokens, then we eliminate the blast radius of overprivileged agents without removing their capabilities, because Kim Maida demonstrated that the same on-call triage agent blocked PII exfiltration, prevented a production DB drop, and required human approval for server restarts—all while still renewing TLS certs and scaling pods autonomously.

## What they did

Kim Maida showed a before/after demo of an on-call triage agent with six incident types. Before: agent used static API keys, dropped a production DB, scaled pods to 40 ($420/hr), and sent raw PII to incident tickets. After: every credential request goes through a Security Token Service (STS) with policy evaluation; customer PII blocked from agent context, DB drop blocked (agent + user both lacked the role), server restart required human approval, pod scale approved (user had the role). The STS issues ephemeral task-scoped tokens to MCP servers, which in turn request downstream API access. Built on the OAuth token exchange open standard (RFC 8693), interoperates with existing policy engines and identity providers.

## Relevance to YOLO loop

Our dev loop agents use static keys with broad permissions. Introducing an STS layer—even a lightweight policy engine—would let us define what each task is allowed to do and audit every credential grant.

## Notes

Token exchange is RFC 8693 (open standard). Key properties: agent identity + user identity propagated all the way down the call chain; human-in-the-loop approval is access-controlled (user must have the role the action requires, not just rubber-stamp consent).

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-13 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-13-sts-token-exchange-agent-access-control` |
| Channel | aie |
| Video | [Your Agent Is a Lethal Trifecta (And What to Do About It) — Kim Maida, Keycard](https://www.youtube.com/watch?v=ws9XcGGPBDk) |
| Published | 2026-10-13 |
| Ingested upstream | 2026-10-13 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
