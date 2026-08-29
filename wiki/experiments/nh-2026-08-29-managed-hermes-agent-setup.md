# Deploy a managed Hermes agent via Hostinger and connect it to Telegram for persistent pocket-agent access

> Back to [[experiments-index]]

Source: **[Set Up a Personal Hermes in 14 Mins (no VPS or mac mini)](https://www.youtube.com/watch?v=gQef3d3erOs)** · nh · 2026-08-29

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we deploy a managed Hermes agent (no VPS, no Docker, no SSH) through a hosting platform and wire it to a Telegram bot powered by a ChatGPT subscription, then we will have a persistent, always-on coding/research agent accessible from any device in under 15 minutes, because managed app platforms abstract away server maintenance while Telegram provides a universal chat interface.

## What they did

Nate walks through spinning up a Hermes agent on Hostinger's managed AI Agents panel (~$6/month), connecting it to a ChatGPT subscription (for cheaper inference than direct API), linking it to Telegram, adding Tavily for web search, and installing a 'grill me' onboarding skill that interviews the user to build persistent memory context. He contrasts this with the VPS approach (more flexible but requires Docker/SSH/ENV config) and recommends the managed path for 98% of users. The agent stores project memory across sessions and surfaces chain-of-thought reasoning in Telegram.

## Relevance to YOLO loop

Adds a lightweight always-on agent layer outside the main dev environment: useful for async task delegation, research queries, and context hydration that can feed back into the YOLO loop without requiring a full local environment to be running.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-29 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-08-29-managed-hermes-agent-setup` |
| Channel | nh |
| Video | [Set Up a Personal Hermes in 14 Mins (no VPS or mac mini)](https://www.youtube.com/watch?v=gQef3d3erOs) |
| Published | 2026-08-29 |
| Ingested upstream | 2026-08-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
