# Replace Single-Shot Prompts with Stateful REPL Loops for Long-Horizon Coding Tasks

> Back to [[experiments-index]]

Source: **[Reading Group July 2026 - Loop Engineering](https://www.youtube.com/watch?v=-DrnzIBASbg)** · mlops · 2026-08-17

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we architect coding agent workflows as persistent loops that carry state across turns (rather than stateless prompt-response pairs), then long-horizon tasks will complete more reliably because the agent retains planning context, can re-enter failed steps, and avoids re-deriving intent from scratch each iteration.

## What they did

The reading group traced an evolution from prompt engineering → context engineering → harness engineering → loop engineering. Practitioners shared that tools like Claude Code work well for individual turns but break down on multi-step autonomous tasks because state is not persisted between loop iterations. The group discussed using slash-goal and agents.md patterns to encode loop state, and referenced LangGraph/CrewAI as prior art for agentic loops. Key insight: a REPL loop with externalized state is the primitive that makes software factories possible.

## Relevance to YOLO loop

The YOLO loop is itself a loop engineering problem. This session provides vocabulary and architectural patterns (state file, loop condition, re-entry point) that we can apply directly to make our agent retry cycles more robust and observable.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-17 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-08-17-loop-engineering-eval-harness` |
| Channel | mlops |
| Video | [Reading Group July 2026 - Loop Engineering](https://www.youtube.com/watch?v=-DrnzIBASbg) |
| Published | 2026-08-17 |
| Ingested upstream | 2026-08-17 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
