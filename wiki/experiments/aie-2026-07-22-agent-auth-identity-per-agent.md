# Assign Per-Agent Scoped Identity and Audit Logs Instead of Passing User Credentials to Agents

> Back to [[experiments-index]]

Source: **[Better Agent Auth — Bereket Habtemeskel & Paola Estefania, Better Auth](https://www.youtube.com/watch?v=JvKO40CFq-s)** · aie · 2026-07-22

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we give each agent its own scoped identity (not the operator's credentials) with per-tool authorization grants and a full audit log tied to that agent identity, then we can trace exactly which agent did what on behalf of which user and limit blast radius from compromised or misbehaving agents, because granular capability grants prevent agents from acting beyond their authorized scope.

## What they did

Paola Estefania presented the Agent Auth Protocol (Better Auth). The core problem: most current agent setups either pass the user's own credentials to the agent or use a shared service token, meaning the agent can do anything the user can do. Proposed solution: three components — (1) Discovery: agents query a directory (analogous to a phone book) to find what tools/capabilities are available rather than having them hardcoded; (2) Authorization: users grant specific per-tool permissions to each agent identity (e.g., Gmail read-only, not send/delete), not blanket access; (3) Identity + Audit: each agent has its own cryptographic identity so every action is logged as 'Agent X did Y on behalf of User Z.' They demoed an MCP proxy/directory that brokers these scoped connections, showing agents discovering Gmail capabilities through the directory and executing only within granted scopes. The SDK handles key generation and assignment to agents; the server side handles verification and grant enforcement.

## Relevance to YOLO loop

The YOLO loop's agents likely run with broad credentials. Implementing per-agent scoped identity would enable precise audit trails of which sub-agent made which changes, support rollback of specific agent actions, and reduce risk when agents have access to production systems or external APIs.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-22 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-22-agent-auth-identity-per-agent` |
| Channel | aie |
| Video | [Better Agent Auth — Bereket Habtemeskel & Paola Estefania, Better Auth](https://www.youtube.com/watch?v=JvKO40CFq-s) |
| Published | 2026-07-22 |
| Ingested upstream | 2026-07-22 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
