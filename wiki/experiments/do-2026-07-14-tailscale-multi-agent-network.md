# Connect All Agent Machines via Tailscale with Zero Open Ports

> Back to [[experiments-index]]

Source: **[Tailscale, Clearly Explained (Beginner's Guide)](https://www.youtube.com/watch?v=eNn2tT-lrz4)** · do · 2026-07-14

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we put all VPS and local machines running AI agents onto a Tailscale network, then we can orchestrate and update remote agents programmatically without manual SSH key management or exposed ports, because Tailscale creates a WireGuard-encrypted peer-to-peer tunnel accessible by machine name from anywhere.

## What they did

David set up Tailscale on a local MacBook and a Hostinger VPS, then used a local Codex/Hermes agent to SSH into the remote VPS over the Tailscale network, install a new Hermes agent, configure it to use Aperture for secure API key storage, and remotely update the default model (from GLM 5.2 to GPT 5.6) — all without manual intervention. He closed all open ports on the VPS and relied entirely on the Tailscale tunnel for access. He also described using ACLs to restrict which agents can reach which machines.

## Relevance to YOLO loop

Directly relevant: our dev loop likely involves agents running on multiple machines. Putting them all on Tailscale means a loop-runner agent can SSH into any node to restart crashed agents, swap models, or push config changes without human involvement, tightening the autonomous repair cycle.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-14 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-07-14-tailscale-multi-agent-network` |
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
