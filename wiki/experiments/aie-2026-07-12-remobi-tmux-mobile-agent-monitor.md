# Add Remobi + tmux to the agent-monitoring stack for mobile steering of running agents

> Back to [[experiments-index]]

Source: **[remobi.app: Don't change your terminal workflow for mobile](https://www.youtube.com/watch?v=5192csoTkVo)** · aie · 2026-07-12

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we run coding agents inside named tmux sessions on a remote dev machine and expose them via Remobi (PWA + Tailscale), then we can steer and monitor multiple concurrent agents from a phone without changing our existing terminal workflow, because Remobi mirrors the live tmux session directly over a secure tunnel with touch-friendly pane navigation.

## What they did

Connor Adams presented Remobi, an open-source progressive web app that streams an existing tmux session to a mobile browser via a Tailscale (or Cloudflare/ngrok) tunnel. Setup: install the NPM package, run the skill installer (which configures tmux key bindings for touch), and connect via the PWA. Features shown: multi-pane view of 4 concurrent Claude Code agents, shift-tab to toggle plan mode, lazy-git diff view, port-kill workflow, double-tap zoom per pane, and scrollable pane content. No relay server; traffic goes peer-to-peer through Tailscale. Compared alternatives: Claude mobile app (Claude Code only, relay server), manual handoff mode (requires manual transfer, single agent), SSH terminal apps (key management friction, no tmux gesture support).

## Relevance to YOLO loop

We already run agents in terminal sessions; adding tmux + Remobi is a low-effort way to get mobile visibility into long-running agent tasks without switching to a managed platform. Particularly useful for overnight or background agent runs where human steering may be needed.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-12 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-12-remobi-tmux-mobile-agent-monitor` |
| Channel | aie |
| Video | [remobi.app: Don't change your terminal workflow for mobile](https://www.youtube.com/watch?v=5192csoTkVo) |
| Published | 2026-07-12 |
| Ingested upstream | 2026-07-12 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
