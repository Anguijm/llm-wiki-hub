# Swap current agent framework for Hermes Agent and benchmark task completion

> Back to [[experiments-index]]

Source: **[Everyone is switching to Hermes Agent… you should too.](https://www.youtube.com/watch?v=1nDiiXfMUK4)** · DavidOndrej · 2026-05-03

**Status:** `discarded` · **Verdict:** `discard` · **Effort:** `medium`

---

## Hypothesis

If we replace our existing agent orchestration layer with Hermes Agent, then we will see improved reliability and tool-use accuracy because Hermes Agent is purpose-built for agentic loops with tighter function-calling adherence.

## What they did

Speaker advocated switching to Hermes Agent, describing its advantages over other agent frameworks, likely demonstrating setup and a comparison of outputs or reliability in agentic tasks.

## Relevance to YOLO loop

Could replace or augment the orchestration layer in our YOLO loop; worth benchmarking against current Claude Code / LangChain setup on our standard task suite.

## Notes

[2026-05-06T19:43:19Z] DISCARD: Vague reactor card — 'switch frameworks' without concrete migration spec or comparable benchmarks.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-05-03 | `backlog` | Extracted from YouTube RSS |
|  | `` | Triage 2026-05-05: Vague reactor card — 'switch frameworks' without concrete migration spec or comparable benchmarks. |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-05-03-hermes-agent-switch` |
| Channel | DavidOndrej |
| Video | [Everyone is switching to Hermes Agent… you should too.](https://www.youtube.com/watch?v=1nDiiXfMUK4) |
| Published | 2026-05-03 |
| Ingested upstream | 2026-05-03 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
