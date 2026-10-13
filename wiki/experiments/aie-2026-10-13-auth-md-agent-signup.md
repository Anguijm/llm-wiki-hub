# Implement auth.md (OMD) so agents can autonomously register for and access external services

> Back to [[experiments-index]]

Source: **[Auth for Agents: Let AI Sign Up for Your Product with auth.md — Michael Grinich, WorkOS](https://www.youtube.com/watch?v=nSkmXakJ6eo)** · aie · 2026-10-13

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we add an auth.md / OMD endpoint to our dev loop's tool-access layer, then agents can self-provision accounts on external APIs without human-in-the-loop credential setup, because OMD provides a machine-readable registration spec that bypasses traditional sign-up UX.

## What they did

Michael Grinich (WorkOS) described auth.md (also called OMD — Open Machine-readable Docs), an open spec that lets AI agents autonomously discover, sign up for, and authenticate with web services. The spec is hosted on a public GitHub repo, is vendor-neutral, and WorkOS offers a one-click hosted version. The core idea: instead of forcing an agent to navigate sign-up forms or requiring a human to pre-provision credentials, a service exposes an auth.md file that the agent can read and use to self-register and obtain tokens. Grinich compared this to PLG (product-led growth) for agents — services that adopt the spec open their growth funnel to the entire agent ecosystem.

## Relevance to YOLO loop

In the YOLO loop, agents frequently hit walls when they need to call external APIs that require accounts or OAuth flows. Implementing OMD-compatible auth discovery would let the loop's tool-use layer autonomously acquire credentials for new services mid-run, removing a major human-intervention bottleneck.

## Notes

Open spec repo referenced in talk; WorkOS hosts a reference implementation. Worth checking github for auth.md / OMD spec directly. Pairs well with MCP tool registration patterns.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-13 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-13-auth-md-agent-signup` |
| Channel | aie |
| Video | [Auth for Agents: Let AI Sign Up for Your Product with auth.md — Michael Grinich, WorkOS](https://www.youtube.com/watch?v=nSkmXakJ6eo) |
| Published | 2026-10-13 |
| Ingested upstream | 2026-10-13 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
