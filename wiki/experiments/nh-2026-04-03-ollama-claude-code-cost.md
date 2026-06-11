# Use Ollama local models for Claude Code's routine sub-tasks to cut costs

> Back to [[experiments-index]]

Source: **[Ollama + Claude Code = 99% CHEAPER]()** · nh · 2026-04-02

**Status:** `discarded` · **Verdict:** `discard` · **Effort:** `medium`

---

## Hypothesis

If we route Claude Code's routine sub-tasks (file reading, simple edits, boilerplate generation) through a local Ollama model while keeping complex reasoning on Claude, then we reduce API costs by up to 90% because most token spend goes to simple operations that don't need frontier intelligence.

## What they did

NateHerk demonstrated a setup combining Ollama (local inference) with Claude Code to achieve dramatically lower costs — implying a hybrid routing approach where local models handle the bulk of simple work.

## Actionable steps

- Identify which Claude Code operations consume the most tokens (likely file reads, simple completions)
- Set up Ollama with a capable model (Gemma 4, Qwen, or similar) for sub-task routing
- Configure Claude Code to use local model for specified task types
- Measure cost reduction over 10 build sessions vs pure Claude API

## Success metric

50%+ reduction in Claude API costs per build session with no quality degradation.

## Relevance to YOLO loop

The YOLO loop is token-intensive. Reducing per-session costs means more builds per budget, directly increasing throughput.

## Target projects

- [[yolo-projects]] (`yolo-loop-infrastructure`)

## Notes

Discarded 2026-04-07: same local-model policy decision as #42. NO on local routing — Anthropic spend is not currently a problem, and the operational complexity does not earn its slot.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-03 | `backlog` | Ingested from Phase 4 YouTube pipeline — title-only inference |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-04-03-ollama-claude-code-cost` |
| Channel | nh |
| Published | 2026-04-02 |
| Ingested upstream | 2026-04-03 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
