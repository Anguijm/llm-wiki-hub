# Enable OpenClaw trusted-proxy-auth mode behind an identity-aware proxy to remove token friction

> Back to [[experiments-index]]

Source: **[Claws Out: Securing and Building with OpenClaw - Nick Taylor, Pomerium](https://www.youtube.com/watch?v=xg1zNlzw7Jk)** · aie · 2026-07-12

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we configure OpenClaw in trusted-proxy-auth mode behind Pomerium (or Tailscale + Caddy), then we eliminate per-session token pasting and device pairing while improving security posture, because the identity-aware proxy enforces authentication at the network layer and forwards a signed JWT header that OpenClaw accepts as the sole trust signal.

## What they did

Nick Taylor (dev advocate, Pomerium) described a feature he contributed to OpenClaw (merged February) that adds a 'trusted proxy' auth mode. Prior to this, even with a reverse proxy in front of OpenClaw, users still had to paste a token into the WebSocket UI and manually pair devices. The new config adds: a `trusted_proxies` list (IP addresses of the proxy), a `user_header` field (JWT from the identity-aware proxy), and optional `required_header` / `allowed_users` fields. With this in place, token and device-pairing steps are eliminated. He also demoed building a speaker-search UI for a conference website by issuing natural-language instructions to OpenClaw from Discord, with the result auto-deployed to a publicly accessible site via Pomerium tunnel—illustrating a secure remote-build workflow.

## Relevance to YOLO loop

If we run OpenClaw for our agent development, switching to trusted-proxy-auth mode is a low-effort config change that removes authentication friction from the inner loop and sets up a secure pattern for exposing agent UIs to team members without leaking tokens.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-12 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-12-openclaw-trusted-proxy-auth` |
| Channel | aie |
| Video | [Claws Out: Securing and Building with OpenClaw - Nick Taylor, Pomerium](https://www.youtube.com/watch?v=xg1zNlzw7Jk) |
| Published | 2026-07-12 |
| Ingested upstream | 2026-07-12 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
