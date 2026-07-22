# Replace Session Logs with an Immutable Event-Sourced Graph as Agent Ground Truth

> Back to [[experiments-index]]

Source: **[Active Graph Agent Runtime (BabyAGI 4) — Yohei Nakajima, Untapped Capital](https://www.youtube.com/watch?v=khVX_BUnEwU)** · aie · 2026-07-22

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we build agents around an immutable append-only event log that projects a typed graph state (rather than around the LLM response stream), then we gain native replay, rollback, and fork capabilities plus a shared state that multiple LLM behaviors can read without direct LLM-to-LLM communication, because all changes are serialized through the log and policies gate what mutations are accepted.

## What they did

Yohei presented ActiveGraph, an event-sourced graph runtime where the log is the agent (arxiv paper: 'The Log Is the Agent'). Key primitives: typed immutable events, behaviors that listen to graph changes and emit new events (can be deterministic or LLM-based), policies that gate whether a change is accepted (e.g., human-in-the-loop for prompt edits, contradiction checks for facts), and a shared graph state all behaviors communicate through instead of calling each other. He validated it by running 80 self-improvement passes on a Pokémon game agent: each pass proposed a change, ran 200 simulated games against reference agents, checked win-rate delta with Wilson score, and accepted ~20-30 of 80. The agent accumulated knowledge of what didn't work (a property YOLO-style agents lack). Debugging shifted naturally from session logs to querying the ActiveGraph DB because everything was already typed and logged.

## Relevance to YOLO loop

Directly addresses the YOLO loop's lack of persistent experiment memory. Replacing ad-hoc logs with an ActiveGraph runtime would give the loop native rollback (undo a bad prompt change), fork (try two variants in parallel), and cross-run learning (the agent knows which hypotheses already failed). The policy layer maps to the loop's human-approval gates.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-22 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-22-active-graph-log-centric-agent-runtime` |
| Channel | aie |
| Video | [Active Graph Agent Runtime (BabyAGI 4) — Yohei Nakajima, Untapped Capital](https://www.youtube.com/watch?v=khVX_BUnEwU) |
| Published | 2026-07-22 |
| Ingested upstream | 2026-07-22 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
