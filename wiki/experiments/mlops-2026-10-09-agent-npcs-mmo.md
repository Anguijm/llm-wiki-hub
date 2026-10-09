# Deploy always-on background agents as synthetic load testers for your agent harness

> Back to [[experiments-index]]

Source: **[Inside a Game Where AI Agents Never Sleep](https://www.youtube.com/watch?v=H8MNuoxAmNU)** · mlops · 2026-10-09

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we run a pool of background agent instances against our own system 24/7 (analogous to AI NPCs in an MMO), then we will surface edge-case failures and game-the-system behaviors faster than human QA because agents never sleep and will exhaustively explore state spaces humans skip.

## What they did

Speaker Isaac (Nexus) described research into populating MMORPGs with AI agent players instead of NPCs to bootstrap an active player ecosystem. He noted that unlike human players, agents never need to sleep, making them relentless testers. He framed this as a QA mechanism: undercover agents continuously probe the game for broken states. He also discussed a text-to-3D world-generation tool that gets products to 80-90% completion via AI, with the remaining 10% requiring human polish, and early agentic shopping adoption where agents call APIs and bypass human-targeted UX patterns.

## Relevance to YOLO loop

Maps to continuous eval in the YOLO loop: spin up always-on agent instances that probe our tool integrations and harness boundaries on a schedule, logging failures for triage.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-09 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-10-09-agent-npcs-mmo` |
| Channel | mlops |
| Video | [Inside a Game Where AI Agents Never Sleep](https://www.youtube.com/watch?v=H8MNuoxAmNU) |
| Published | 2026-10-09 |
| Ingested upstream | 2026-10-09 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
