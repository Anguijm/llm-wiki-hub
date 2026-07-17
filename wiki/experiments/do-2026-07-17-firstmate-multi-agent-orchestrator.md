# Replace Tab-Juggling with a Single Orchestrator Agent (First Mate Pattern)

> Back to [[experiments-index]]

Source: **[L8 Principal's Agentic Engineering Setup (just copy him)](https://www.youtube.com/watch?v=8ZgpAXe5V5w)** · do · 2026-07-17

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we route all agent work through a single orchestrator agent (First Mate) running inside a persistent terminal multiplexer session rather than manually managing 20–30 parallel agent tabs, then we will reduce cognitive overhead and increase throughput because the orchestrator tracks state across sub-agents and surfaces only what needs human attention, keeping the engineer in flow.

## What they did

Kun (L8 principal engineer, formerly Meta/Microsoft/Atlassian) shared his terminal-first agentic setup: a frameless terminal window running Wezterm with a Zellij session (modern tmux alternative) on a Mac Mini accessible via SSH from any device including phone. He found that spinning up 20–30 parallel agent sessions became cognitively unmanageable—too much state to hold in his head. He built 'First Mate,' an orchestrator agent that he talks to almost exclusively; it in turn manages and delegates to sub-agent sessions. He noted the inflection point that enabled this was Claude Sonnet 3.5 v2, which was the first model capable of taking a task and returning a complete result autonomously. His prior role at Atlassian was specifically developing coding agents, giving him deep model comparison experience from GPT-3.5 through current frontier models.

## Relevance to YOLO loop

Directly models the YOLO loop's orchestration layer: instead of a human switching between agent contexts, a meta-agent owns the dispatch table. First Mate is an open-source reference implementation worth studying for our own orchestration design. The Zellij + SSH persistence pattern also means the loop can be monitored from mobile.

## Notes

Kun's GitHub has First Mate and related tooling open-sourced. He also runs a Discord community. Key design insight: as agents become more capable, they should juggle the parallel sessions—not the human. Terminal muscle memory (20+ years) is the reason for his terminal-first preference, not a technical requirement; GUI-first setups are equally valid.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-17 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-07-17-firstmate-multi-agent-orchestrator` |
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
