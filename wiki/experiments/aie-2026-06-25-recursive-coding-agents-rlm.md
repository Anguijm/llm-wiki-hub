# Apply Recursive Language Model (RLM) patterns to coding agents for reliable, large-scale refactors

> Back to [[experiments-index]]

Source: **[Recursive Coding Agents - Raymond Weitekamp, OpenProse](https://www.youtube.com/watch?v=3hXJI2q0Jz8)** · aie · 2026-06-25

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we structure coding agent workflows as recursive language models — where the full prompt/codebase is a variable explored symbolically via a REPL and sub-agents handle subtasks in parallel — then agents can reliably complete repo-scale tasks that exceed a single context window because reasoning is unified with code execution and sub-agents decompose the problem rather than the root agent holding the entire thread.

## What they did

Raymond presented RLMs (from the DSPy/MIT paper) as the next paradigm of test-time compute. He showed a 5.9B Qwen model outperforming frontier models on long-reasoning benchmarks when used as an RLM. He then described OpenProse, a declarative language for specifying Prose contracts (typed, verifiable agent workflows) that can be used with Claude Code or Codex. Use cases demoed: parallel repo-scale migrations with merge, adversarial red-team sub-agents, and capturing a 'golden session' to auto-generate a reusable Prose workflow that reproduces that performance reliably.

## Relevance to YOLO loop

High relevance for our most complex tasks: large refactors, multi-file feature builds, and audit sweeps. The golden-session-to-reusable-workflow feature is especially useful for codifying successful YOLO loop runs into repeatable processes.

## Notes

Interactive slides at recursivecodingagents.com. OpenProse is the implementation vehicle.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-25 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-25-recursive-coding-agents-rlm` |
| Channel | aie |
| Video | [Recursive Coding Agents - Raymond Weitekamp, OpenProse](https://www.youtube.com/watch?v=3hXJI2q0Jz8) |
| Published | 2026-06-25 |
| Ingested upstream | 2026-06-25 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
