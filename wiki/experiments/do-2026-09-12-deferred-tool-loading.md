# Implement Deferred Tool Loading via Interleaved System Messages

> Back to [[experiments-index]]

Source: **[Pi Agent dev reveals his Agentic Engineering Workflow](https://www.youtube.com/watch?v=SxuQs9GGYbk)** · do · 2026-09-12

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we use interleaved system messages to inject tool definitions only at the point in the conversation where they become relevant rather than front-loading all tools in the initial system prompt, then total token usage per session will decrease and model attention on active tools will improve because unused tool schemas are never present in context.

## What they did

Armen noted that state-of-the-art models now support interleaved system messages within the conversation thread (not just a single opening system prompt). This unlocks 'deferred tool loading' — a pattern where tool definitions are inserted mid-conversation as the agent enters a new phase of work, rather than being declared upfront. He described this as a meaningful architectural change that makes certain patterns possible that were previously not possible, though he acknowledged the overall delta to harness design is modest.

## Relevance to YOLO loop

The YOLO loop currently sends the full tool schema at the start of every run. Deferred loading could shrink the initial prompt and scope the model's tool awareness to whichever phase (plan / edit / test / commit) it is currently executing.

## Notes

Depends on model support for interleaved system messages — verify which providers in our stack support this before scheduling. Pairs naturally with the bash-first harness experiment.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-12 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-09-12-deferred-tool-loading` |
| Channel | do |
| Video | [Pi Agent dev reveals his Agentic Engineering Workflow](https://www.youtube.com/watch?v=SxuQs9GGYbk) |
| Published | 2026-09-12 |
| Ingested upstream | 2026-09-12 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
