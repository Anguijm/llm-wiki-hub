# Build a /benchmark slash command that runs your real tasks against new models and scores them against your personal rubric

> Back to [[experiments-index]]

Source: **[Stop Guessing Which Model to Use. Build THIS Instead.](https://www.youtube.com/watch?v=3ICM9ZdflZA)** · mk · 2026-07-26

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we build a slash command that mines our own chat history for recurring task types and runs those exact tasks against any new model at configurable effort levels, then we can make model-switching decisions in under an hour rather than relying on generic benchmarks because the eval is grounded in our actual work.

## What they did

Mark built a Claude Code slash command (/benchmark) that: (1) scans the user's full conversation history (he has ~2GB / 1000+ conversations stored as JSONL) to mine recurring task types and their execution patterns; (2) lets the user specify two models and effort levels (e.g., Opus 4.8 low vs Opus 5 low) and a task domain (copywriting, email triage, etc.); (3) spawns a live web artifact showing a benchmark table; (4) runs 3 trials per task, scoring each against a user-defined rubric covering quality (1-10), instruction fidelity, token efficiency, speed, and number of tool calls/turns; (5) produces a post-mortem report per trial with verdict (e.g., 'skip the pricier Opus high, Fable low quietly wins'). The rubric is fully customizable. He showed three completed runs: Opus 5 vs Fable 5 on email triage, Opus low vs high vs Fable low vs high, and a generic dealer's-choice run. He is releasing the skill/command free via a link in the description.

## Relevance to YOLO loop

Directly addresses model selection in the YOLO loop: instead of guessing which model to use for a dev loop task, we can run our own task corpus through this benchmark and pick the most cost-efficient option that meets our quality bar. Token efficiency and turns-per-task metrics are especially useful for loop cost control.

## Notes

Rubric dimensions to adopt: quality score, instruction fidelity, token efficiency, speed, number of turns (proxy for context bloat). The JSONL conversation history as benchmark seed is a clever reuse of existing artifacts—worth checking if our own session logs are accessible in a similar format.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-26 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mk-2026-07-26-personal-benchmark-slash-command` |
| Channel | mk |
| Video | [Stop Guessing Which Model to Use. Build THIS Instead.](https://www.youtube.com/watch?v=3ICM9ZdflZA) |
| Published | 2026-07-26 |
| Ingested upstream | 2026-07-26 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
