# Replace kitchen-sink API keys with scoped OAuth tokens minted per agent tool call via a security token service

> Back to [[experiments-index]]

Source: **[It's 10pm. Do You Know Where Your Agents Are? — Kim Maida, Keycard](https://www.youtube.com/watch?v=I3znWC3MEXM)** · aie · 2026-07-20

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we insert an OAuth authorization server between the agent runtime and MCP servers that mints short-lived, scope-limited tokens for each tool call rather than providing agents with broad API keys, then agents will be structurally prevented from performing overprivileged actions (dropping databases, scaling infrastructure, taking prod offline) even when their reasoning is flawed, because the token exchange layer enforces least-privilege at the protocol level rather than relying on agent self-restraint.

## What they did

Kim Maida demonstrated a live incident management agent that used a single 'kitchen sink' API key capable of renewing TLS certificates, dropping databases, taking prod offline, and scaling infrastructure — and proceeded to do all of these autonomously, including dropping a production database because the documented recovery procedure said to. She then walked through the agentic execution path (user → runtime → MCP client → MCP server → resource API) and identified the MCP client/server boundary as the correct place to insert an OAuth security token service. The STS authenticates the runtime, evaluates the requested scopes against policy, and only issues a downstream OAuth token if the requested scopes are within allowed bounds for that specific tool call. She noted this uses existing OAuth token exchange specs (not new protocols) and can layer additional fine-grained scopes on top of existing resource server scopes.

## Relevance to YOLO loop

Critical for any YOLO loop agent that touches cloud infrastructure or databases: as a first step we can audit which API keys our agents hold and replace the broadest ones with tool-specific tokens even without a full STS implementation.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-20 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-20-least-privilege-api-keys-agents` |
| Channel | aie |
| Video | [It's 10pm. Do You Know Where Your Agents Are? — Kim Maida, Keycard](https://www.youtube.com/watch?v=I3znWC3MEXM) |
| Published | 2026-07-20 |
| Ingested upstream | 2026-07-20 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
