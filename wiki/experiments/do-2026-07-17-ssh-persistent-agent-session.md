# Run Agent Sessions in a Persistent Multiplexed Terminal Accessible via SSH from Any Device

> Back to [[experiments-index]]

Source: **[L8 Principal's Agentic Engineering Setup (just copy him)](https://www.youtube.com/watch?v=8ZgpAXe5V5w)** · do · 2026-07-17

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we host long-running agent sessions in a Zellij (or tmux) session on a always-on machine and connect via SSH from laptop or phone, then we can monitor and steer agents continuously without being tied to a single workstation, because the session state persists independently of the client connection.

## What they did

Kun runs his entire agentic workflow from a Mac Mini using Wezterm (highly customizable frameless terminal) with Zellij sessions. He can SSH into the exact same terminal session from his phone, maintaining full context of all running agent processes. Zellij was chosen over tmux (which he used for 10+ years) because it has a more modern UX and natively understands the concept of multiple agent sessions. This setup means agents can run overnight or during commutes while remaining inspectable at any time from any device.

## Relevance to YOLO loop

Infrastructure primitive for the YOLO loop: long-running agent jobs should not depend on a laptop staying open. This pattern enables truly async agent execution with human-in-the-loop review from wherever the engineer happens to be.

## Notes

Stack: Mac Mini + Wezterm + Zellij + SSH. Zellij replaces tmux with a more modern session management model. Low effort to adopt if already comfortable with terminal; there is an initial learning curve for non-terminal users that Kun acknowledged.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-17 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-07-17-ssh-persistent-agent-session` |
| Channel | do |
| Video | [L8 Principal's Agentic Engineering Setup (just copy him)](https://www.youtube.com/watch?v=8ZgpAXe5V5w) |
| Published | 2026-07-17 |
| Ingested upstream | 2026-07-17 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
