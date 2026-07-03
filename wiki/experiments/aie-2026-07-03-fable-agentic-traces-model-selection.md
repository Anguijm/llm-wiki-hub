# Log agentic traces to real-world benchmark data for evidence-based model selection

> Back to [[experiments-index]]

Source: **[WF2026: Autoresearch & Keynotes ft. Anthropic, Google DeepMind, Amazon AGI, Sonar, Arena, Recursive](https://www.youtube.com/watch?v=4sX_He5c4sI)** · aie · 2026-07-03

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we log all agentic session traces (agent-user interactions, token counts, task outcomes) and mine them against business metrics, then we can select the optimal model per task type based on real cost-performance data rather than list-price benchmarks, because list price obscures actual token consumption differences between models on identical tasks.

## What they did

The Chatbot Arena team (arena.ai) presented real-world agentic benchmarking data comparing Fable, Opus 4, GPT-5, Gemini, and other models on coding agent tasks run against real repositories. Key finding: list price is misleading — GPT-5 uses fewer tokens than Opus on equivalent tasks despite similar list pricing, making it more efficient in practice. Fable ranked highest on performance at ~$10/session. The presenter recommended logging all agentic traces, mining for insights, measuring against business outcome metrics, then using that real-world data (not synthetic benchmarks) to select models. Upcoming Arena work includes richer professional-task categories and rubric-based scoring. Separately, the Anthropic/Tariq Shihipar keynote introduced Fable as a new model class and framed it as working best when the agent receives upstream intent context (not just the task, but why it matters and how to verify it).

## Relevance to YOLO loop

Directly actionable: we should instrument our YOLO loop to log traces per task type, capture token counts and wall-clock time, and tag outcomes. This gives us our own pareto frontier chart (performance vs. cost) to decide when Fable is worth the premium over a cheaper model.

## Notes

Tariq's framing — 'tell the agent why the task matters and how to verify it, not just what to do' — aligns with the upstream intent principle from Day 1 keynotes. The 3x more off-by-pass vulnerability code stat for Claude Code vs. other models is worth tracking as a safety metric in our loop. Transcript truncated at 443K chars; Arena leaderboard data at arena.ai for full model comparison tables.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-03 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-03-fable-agentic-traces-model-selection` |
| Channel | aie |
| Video | [WF2026: Autoresearch & Keynotes ft. Anthropic, Google DeepMind, Amazon AGI, Sonar, Arena, Recursive](https://www.youtube.com/watch?v=4sX_He5c4sI) |
| Published | 2026-07-03 |
| Ingested upstream | 2026-07-03 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
