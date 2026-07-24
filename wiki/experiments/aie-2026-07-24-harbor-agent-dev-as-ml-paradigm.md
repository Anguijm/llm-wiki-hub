# Treat agent skills as ML model weights and use rollout-based evals to optimize them

> Back to [[experiments-index]]

Source: **[Everything Is a Rollout — Alex Shaw + Ryan Marten, Terminal-Bench, Harbor, Laude Institute](https://www.youtube.com/watch?v=jRCpXUjz4CI)** · aie · 2026-07-24

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we reframe skill/prompt development as an ML training loop (environment=eval task, weights=skills+prompts+model choice, loss=environment reward, optimizer=context-based hill-climbing), then we can systematically improve agent performance using empirical evaluation rather than intuition-driven prompt tweaking because agent outputs are non-deterministic blackbox artifacts just like ML model outputs.

## What they did

Presented Harbor, an agent evaluation and RL environment framework. Argued that agent development is more analogous to ML training than traditional software engineering: you cannot predict agent behavior from reading the code, just as you cannot predict a neural network's output from its weights. Drew explicit ML-to-agent analogies: training data→environments, val set→eval environments, model weights→skills+prompts+tools+model selection, loss function→environment rewards, backprop→context-based optimization (JEPA or coding-agent-in-a-loop), gradient step→PR into repo, overfitting→reward hacking. Demonstrated Harbor Exec: map-reduce over coding agent sessions (cursor CLI for map, Fable 5 for reduce) to extract recurring mistake patterns from past sessions, generating a feedback file that informs the next round of Harbor eval tasks. Showed ecosystem: Frontier Suite, BankerToolBench, RuneBench (Runescape), Scale Atlas Suite, Poolside model training, auto-agent self-optimization loop.

## Relevance to YOLO loop

The YOLO loop's skills are currently iterated by feel. Adopting Harbor's map-reduce pattern to analyze past session transcripts for recurring failure categories would give us data-driven skill improvement. Even without full Harbor integration, the map-reduce prompt pattern (cursor CLI for individual session analysis, stronger model for pattern synthesis) is immediately usable.

## Notes

Harbor is open source. The map-reduce session analysis demo is the most immediately actionable piece: collect last N Claude Code sessions, run per-session mistake extraction with a cheap/fast model, synthesize recurring failure categories with a stronger model, use output to update skill prompts. This is essentially automated skill debugging.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-24 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-24-harbor-agent-dev-as-ml-paradigm` |
| Channel | aie |
| Video | [Everything Is a Rollout — Alex Shaw + Ryan Marten, Terminal-Bench, Harbor, Laude Institute](https://www.youtube.com/watch?v=jRCpXUjz4CI) |
| Published | 2026-07-24 |
| Ingested upstream | 2026-07-24 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
