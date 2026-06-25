# Use CMAX terminal for managing parallel CLI agents with per-pane zoom, workspaces, and jump-to-unread notifications

> Back to [[experiments-index]]

Source: **[This 100% open-source terminal is insane… just watch](https://www.youtube.com/watch?v=8jDXI4_rJOE)** · do · 2026-06-11

**Status:** `discarded` · **Verdict:** `discard` · **Effort:** `low`

---

## Hypothesis

If we switch from tmux or default terminal to CMAX for running parallel Claude Code / Codex / Hermes agent sessions, then developer ergonomics for multi-agent management will improve because CMAX provides independent per-pane zoom, workspace switching, command-D/shift-D split shortcuts, and a jump-to-unread shortcut (cmd+shift+U) that eliminates manual polling of agent status.

## What they did

Speaker demonstrated CMAX, a native macOS Swift terminal built on libGhosty that supports multiple panes (cmd+D horizontal, cmd+shift+D vertical), multiple workspaces, integrated browser sidebar, and per-pane independent zoom. Key features for agent workflows: cmd+shift+U jumps to the latest unread agent output across all panes, panes highlight when active, and agents themselves can be taught to drive CMAX via a CMAX skill file. Speaker used it daily for running Claude Code with Ultra Code (/workflows), Codex, and Hermes in parallel across different projects. He demonstrated a 3D interior design app built in a single Opus 4.8 prompt via Ultra Code running inside CMAX.

## Relevance to YOLO loop

Drop-in replacement for our terminal multiplexer. Low effort to evaluate: install CMAX, port our existing multi-agent grid layout, and measure whether jump-to-unread and per-pane zoom reduce friction in monitoring concurrent agent runs.

## Notes

Backlog triage 2026-06-24 (owner-preference model). Specific terminal product for ergonomics — low value vendor tooling.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-06-11-cmax-terminal-parallel-agents` |
| Channel | do |
| Video | [This 100% open-source terminal is insane… just watch](https://www.youtube.com/watch?v=8jDXI4_rJOE) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
