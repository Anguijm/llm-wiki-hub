# Pilot Kylon as a shared team workspace where human members and Claude Code subscriptions collaborate on the same agent channel

> Back to [[experiments-index]]

Source: **[AI Agents Just Became Multiplayer. Here's How to Build Them.](https://www.youtube.com/watch?v=KZiF2J83zaY)** · nh · 2026-10-15

**Status:** `discarded` · **Verdict:** `discard` · **Effort:** `low`

---

## Hypothesis

If we use Kylon to create shared agent channels where multiple humans and multiple Claude Code/Codex subscriptions can all interact with the same persistent agent, then team coordination overhead drops and agent-to-agent collaboration becomes possible without custom polling infrastructure, because Kylon provides the Slack-like workspace layer that single-player AIOS setups currently lack.

## What they did

The speaker demonstrated Kylon, a Slack-style multiplayer AI workspace where multiple humans (himself, Cody, Aiden) and multiple coding agent subscriptions (his Claude Code, Aiden's Codex, etc.) share channels. Each channel can have apps built by agents, automations, files, and knowledge. Agents proactively communicate with each other (Claude Code subscription messaged his Herk agent to collaborate on a dashboard redesign without human initiation). Each user and agent gets a profile with responsibilities, goals, and work context. Agent subscriptions show model, reasoning effort, and weekly token usage. He contrasted this with his previous workaround of building custom ClickUp-based agent integrations, noting Kylon eliminates the GitHub/deployment/versioning overhead. He framed it as moving from single-player AIOS to team AIOS.

## Relevance to YOLO loop

high: Kylon is a harness layer that extends Claude Code into a multiplayer, persistent, multi-client workspace — directly relevant to agent workflow and harness architecture.

## Notes

Sponsored video — Kylon approached the creator. Pricing was a stated concern initially. Worth evaluating free tier before committing.

Backlog triage 2026-10-16 round 2 (operator: discard cards that are only someone selling a product). Sales only: FACT: the card says the video was sponsored by Kylon; Assessment: a product pilot for a solo operator.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-15 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-10-15-multiplayer-ai-kylon` |
| Channel | nh |
| Video | [AI Agents Just Became Multiplayer. Here's How to Build Them.](https://www.youtube.com/watch?v=KZiF2J83zaY) |
| Published | 2026-10-15 |
| Ingested upstream | 2026-10-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
