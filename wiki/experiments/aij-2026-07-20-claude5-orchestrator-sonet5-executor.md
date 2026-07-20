# Use Claude 4 Opus as orchestrator and Sonnet 5 as persistent executor sub-agent to cut costs 35%

> Back to [[experiments-index]]

Source: **[Tmux + Fable = Cut 35% less token](https://www.youtube.com/watch?v=wCSPgHpcxdc)** · aij · 2026-07-20

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we configure Claude Code with a delegation rules section in CLAUDE.md that routes planning/architecture to Opus and hands execution to a persistent Sonnet 5 sub-agent session (sidekick model), then we will reduce token spend by ~35% with equivalent output quality, because cached context tokens for the persistent sub-agent cost ~10% of new input tokens and Sonnet 5 performs near Opus 4 levels on execution tasks.

## What they did

Jason walked through Devon's 'fusion harness' finding that Claude 4 Opus as orchestrator spinning up persistent Sonnet 5 worker sessions outperforms the alternative (Sonnet 5 main agent calling Opus as advisor) because the advisor pattern forces the expensive model to read the full conversation history each time. The key implementation is a CLAUDE.md delegation rules section specifying what stays with the coordinator (design, architecture, tiny edits, review) and what gets delegated to executor sub-agents. The sub-agents are started as persistent sessions using Claude Code's send-message tool so follow-up feedback reuses cached context. He also demonstrated a tmux-based open-agent-team script for multi-CLI-agent orchestration when not using Claude Code exclusively.

## Relevance to YOLO loop

High relevance: adding a delegation rules section to our CLAUDE.md is a one-time low-effort change that could immediately reduce Opus quota burn on the YOLO loop while keeping planning quality high.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-20 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aij-2026-07-20-claude5-orchestrator-sonet5-executor` |
| Channel | aij |
| Video | [Tmux + Fable = Cut 35% less token](https://www.youtube.com/watch?v=wCSPgHpcxdc) |
| Published | 2026-07-20 |
| Ingested upstream | 2026-07-20 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
