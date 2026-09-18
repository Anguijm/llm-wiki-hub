# Connect Higgsfield Video/Image API to Codex via .env Skill for Pay-Per-Use Generation

> Back to [[experiments-index]]

Source: **[This ONE GPT-6 Astra Skill Replaces Your Higgsfield Subscription](https://www.youtube.com/watch?v=oWCcN6hSFjA)** · nh · 2026-09-18

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we integrate Higgsfield's pay-per-usage API into a Codex agent via a pre-built skill file and .env key injection, then we can generate images and videos programmatically using natural language without a monthly subscription, because the API allows per-request billing and a skill file encodes all model options and defaults so the agent needs no manual research at runtime.

## What they did

The presenter showed how to create a Higgsfield API account, generate an API key, inject it into a Codex project's .env file via a chat prompt, and then load a pre-built 'Higgsfield API generations' skill file that encodes all available models, settings, and defaults. With the skill active, Codex could accept natural-language requests and dispatch image and video generation jobs to Higgsfield's API (e.g., Seedance 2.5, Klang, Omniflash, Minimax) without the user needing to know API specifics. He also walked through break-even analysis: fewer than ~19 clips/month favors API over the Plus subscription, fewer than ~50 clips/month favors API over Ultra.

## Relevance to YOLO loop

Pattern of injecting a third-party API key + a skill file to extend an AI coding agent's capabilities without code changes is directly reusable in our dev loop for any external media, data, or tool API we want to give an agent access to.

## Notes

Low-effort setup if we already use Codex. The skill-file pattern (encoding API docs and defaults into a reusable context file) is the transferable idea, independent of Higgsfield specifically. Break-even math: API wins below ~19 clips/month on Plus plan.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-18 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-09-18-higgsfield-api-codex-integration` |
| Channel | nh |
| Video | [This ONE GPT-6 Astra Skill Replaces Your Higgsfield Subscription](https://www.youtube.com/watch?v=oWCcN6hSFjA) |
| Published | 2026-09-18 |
| Ingested upstream | 2026-09-18 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
