# Route All Agent Egress Through a Protocol-Aware Firewall with Human Approval Rules

> Back to [[experiments-index]]

Source: **[Security Firewall for Agents — Ryan Dahl, Deno](https://www.youtube.com/watch?v=MkRYPFIMCSA)** · aie · 2026-08-17

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we place a protocol-aware proxy (like Claw Patrol) between the agent VM and all external systems, then we can enforce fine-grained allow/deny rules at the network layer without modifying agent code, because all destructive actions ultimately manifest as bytes over the wire and can be intercepted regardless of how the agent spawns them (HTTP, psql subprocess, kubeconfig, etc.).

## What they did

Ryan Dahl described Deno's production incident-response agents that have full read/write access to Postgres, Kubernetes, ClickHouse, AWS, GitHub, and Slack. Rather than trusting model alignment alone, they treat the agent as untrusted software and route all egress through Claw Patrol—an outbound proxy that understands HTTP, Postgres wire protocol, ClickHouse, AWS SigV4, and OAuth. Rules can block, log, or route requests to a Slack approval channel or an LLM judge. The system runs over Tailscale and holds credentials centrally, injecting them per-request so the agent never stores them directly.

## Relevance to YOLO loop

As the YOLO loop agents gain write access to deployment targets, databases, and external APIs, a network-layer firewall is the correct backstop. This pattern is immediately applicable: stand up Claw Patrol (or equivalent) in front of any agent that touches production resources, define SQL/Kubernetes deny rules, and wire Slack approval for destructive actions.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-17 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-17-agent-network-firewall` |
| Channel | aie |
| Video | [Security Firewall for Agents — Ryan Dahl, Deno](https://www.youtube.com/watch?v=MkRYPFIMCSA) |
| Published | 2026-08-17 |
| Ingested upstream | 2026-08-17 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
