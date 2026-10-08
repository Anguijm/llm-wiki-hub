# Replace Manual Agent Message Routing With a Stateful Agent Communication Layer

> Back to [[experiments-index]]

Source: **[Why AI Agents Can't Talk to Each Other (Yet) — Vlad Luzin, BAND](https://www.youtube.com/watch?v=toq-jyGLZDk)** · aie · 2026-10-08

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we use a dedicated agent communication platform (instead of manually passing messages between Claude/Codex sessions or chaining MCP REST calls), then agents can maintain persistent stateful conversations with each other, discover peers, and delegate tasks bidirectionally without developer-as-router overhead, because MCP is stateless and A2A is unidirectional client-server by default.

## What they did

Vlad Luzin from BAND demoed a platform where agents onboard with an identity/card in seconds, discover each other in a shared registry, and enter persistent conversational spaces. A Claude Code terminal session and a Codex SDK agent were spun up, registered, and then invited into a shared workspace where they collaboratively built a website — one planning, one reviewing — with the human able to join or observe any conversation. He contrasted this with current approaches: (1) human-as-router between sessions, (2) Python/TypeScript loop orchestration scripts, (3) MCP (stateless, no callback), (4) A2A (unidirectional unless you implement both client and server sides). Key pain point: connecting an agent to Slack requires 8 steps, WhatsApp 11 steps, and still only enables agent-to-human not agent-to-agent.

## Relevance to YOLO loop

Our YOLO loop currently requires manual context passing between agent sessions. A stateful agent communication layer would let planner, coder, and reviewer agents collaborate persistently with human-in-the-loop visibility, reducing the orchestration glue code we maintain.

## Notes

BAND platform booth at LG17. Bilateral consent model for agent introductions — neither agent can be connected without both parties accepting. Full conversation visibility for human owners. Try at bend.ai or similar — check description for QR.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-08 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-08-agent-to-agent-stateful-communication` |
| Channel | aie |
| Video | [Why AI Agents Can't Talk to Each Other (Yet) — Vlad Luzin, BAND](https://www.youtube.com/watch?v=toq-jyGLZDk) |
| Published | 2026-10-08 |
| Ingested upstream | 2026-10-08 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
