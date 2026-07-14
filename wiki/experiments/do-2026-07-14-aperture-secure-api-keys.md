# Store Agent API Keys in Aperture Instead of on the VPS

> Back to [[experiments-index]]

Source: **[Tailscale, Clearly Explained (Beginner's Guide)](https://www.youtube.com/watch?v=eNn2tT-lrz4)** · do · 2026-07-14

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we use Aperture as a secrets manager for agent API keys rather than storing them directly on VPS machines, then API keys will not be exposed even if a VPS is compromised, because keys are held centrally and injected at runtime rather than persisted in plaintext on the remote host.

## What they did

David configured a newly provisioned Hermes agent on a VPS to retrieve its OpenRouter API key from Aperture, confirming via OpenRouter logs that the model call succeeded with the key never stored on the VPS itself. The Codex agent handled the entire setup via CLI over the Tailscale tunnel.

## Relevance to YOLO loop

Any agent in our loop that makes external API calls (LLM providers, search, etc.) should not have keys baked into its environment. This pattern lets us rotate or revoke keys centrally without touching individual machines.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-14 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-07-14-aperture-secure-api-keys` |
| Channel | do |
| Video | [Tailscale, Clearly Explained (Beginner's Guide)](https://www.youtube.com/watch?v=eNn2tT-lrz4) |
| Published | 2026-07-14 |
| Ingested upstream | 2026-07-14 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
