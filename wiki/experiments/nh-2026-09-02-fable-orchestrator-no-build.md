# Prompt Fable 5.1 as Pure Orchestrator — Spin Sub-Agents, Never Build Directly

> Back to [[experiments-index]]

Source: **[I Analyzed How Anthropic ACTUALLY Prompts Fable 5.1](https://www.youtube.com/watch?v=FBVNS1l5Vb8)** · nh · 2026-09-02

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we instruct Fable 5.1 explicitly not to write code or conduct research itself but only to decompose work, spin up sub-agents, interpret their results, and verify the final output, then we will get dramatically more total work done per session limit because Fable's tokens are spent on high-value reasoning and coordination rather than low-level execution.

## What they did

Nate described prompting Fable 5.1 with explicit instructions: 'I don't want you to build anything, code anything, or research anything — just spin up sub-agents, drive strategy, interpret what they give you, and spin up more sub-agents.' Fable handles orchestration and final verification while cheaper/parallel sub-agents do the execution. He reported this as the single biggest lever for stretching his weekly Fable usage limit.

## Relevance to YOLO loop

Maps directly to the YOLO loop's orchestration layer: using Fable as the planning/verification brain while Claude Code or Codex sub-agents handle implementation would preserve the expensive model's capacity for the decisions that matter most.

## Notes

Nate emphasizes that Fable 5.1 is still accountable for the final output quality even in orchestrator mode — it should spin up verifier sub-agents and do a final pass itself before handing to the human.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-02 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-09-02-fable-orchestrator-no-build` |
| Channel | nh |
| Video | [I Analyzed How Anthropic ACTUALLY Prompts Fable 5.1](https://www.youtube.com/watch?v=FBVNS1l5Vb8) |
| Published | 2026-09-02 |
| Ingested upstream | 2026-09-02 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
