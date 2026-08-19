# Use the Codex/Claude SDK as an API-key-free bridge for internal tool AI calls

> Back to [[experiments-index]]

Source: **[THIS AI Hack Could Save You Thousands](https://www.youtube.com/watch?v=JlXfoZvTwzk)** · mk · 2026-08-19

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we replace API key calls in internal tools with the Codex or Claude SDK (which authenticates via an existing subscription's cached session headlessly), then internal tools can make AI inference calls at zero marginal cost beyond the existing subscription, because the SDK routes requests through the authenticated subscription session rather than a metered API endpoint—valid for personal and internal use within the provider's terms of service.

## What they did

Mark Kashef demonstrated a meeting analyzer app and social media analytics tool where all AI inference calls go through the Codex SDK instead of a paid API key. The SDK finds the cached authorization from the existing Codex subscription automatically when constructed with no arguments, spinning up a headless worker. He showed image generation (via GPT-4o image) also working through this bridge. He shared a mega-prompt template specifying 'all AI calls go through the OpenAI SDK using my cached ChatGPT login—no API key anywhere' as the defining constraint, and noted this also works with the Claude SDK (referencing his earlier 'Claude Claw' setup). He used Tailscale to share local apps with small internal teams. Explicitly flagged that this is terms-of-service compliant only for internal/personal use, not for building and selling a SaaS.

## Relevance to YOLO loop

Relevant to our internal tooling cost structure: any prototype or internal agent tool we build during the YOLO loop can use this pattern to avoid API billing during development and low-volume internal use, reducing the cost of experimentation.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-19 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mk-2026-08-19-sdk-bridge-replace-api-keys` |
| Channel | mk |
| Video | [THIS AI Hack Could Save You Thousands](https://www.youtube.com/watch?v=JlXfoZvTwzk) |
| Published | 2026-08-19 |
| Ingested upstream | 2026-08-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
