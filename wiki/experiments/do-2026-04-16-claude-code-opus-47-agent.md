# Run Claude Code with Opus 4.7 as Primary Coding Agent and Benchmark Against Sonnet

> Back to [[experiments-index]]

Source: **[Claude Code + Opus 4.7 = Ultimate Coding Agent](https://www.youtube.com/watch?v=Tv3lIkbdAGc)** · DavidOndrej · 2026-04-16

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we configure Claude Code to use Opus 4.7 as the primary model for agentic coding tasks, then we will see higher task completion rates on complex multi-file refactors compared to Sonnet-class models, because Opus 4.7 has improved long-context reasoning that reduces mid-task derailment.

## What they did

Speaker configures Claude Code CLI to target Opus 4.7, walks through a multi-file coding task end-to-end, and compares output quality and self-correction behavior versus prior model versions. Highlights specific prompt patterns and CLAUDE.md configurations that maximize Opus 4.7's agentic capabilities.

## Relevance to YOLO loop

Direct swap-in experiment for the YOLO loop's model selection layer — we can A/B test Opus 4.7 vs Sonnet 3.7 on our standard task suite to measure quality vs cost tradeoff.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-16 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-04-16-claude-code-opus-47-agent` |
| Channel | DavidOndrej |
| Video | [Claude Code + Opus 4.7 = Ultimate Coding Agent](https://www.youtube.com/watch?v=Tv3lIkbdAGc) |
| Published | 2026-04-16 |
| Ingested upstream | 2026-04-16 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
