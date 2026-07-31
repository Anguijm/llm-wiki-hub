# Audit existing benchmark tasks against five quality principles before using them for eval or training

> Back to [[experiments-index]]

Source: **[Benchmarks: The Good, the Bad, and the Ugly — Ali Khial, G2i](https://www.youtube.com/watch?v=jWq-aZIU0kM)** · aie · 2026-07-31

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we filter or rewrite benchmark tasks to satisfy human-authored instructions, holistic graders, production-grade value, contamination-free novelty, and informative leaderboard metadata, then our evals will better predict real-world agent utility and reduce reward hacking, because current benchmarks systematically fail on leaky prompts and weak verifiers.

## What they did

G2i's AI director analyzed SWEBench Pro and found: average instruction length of 481 words (unrealistic for real engineers), leaky prompts that expose test file paths or full interfaces, weak verifiers that reject correct implementations (24% false negative rate per DeepSweep analysis) or accept wrong ones (8.5%), and increasing reward hacking as models get smarter. They proposed five principles: human-authored instructions expressing desired behavior not implementation details; holistic graders with behavioral + precision tests; production-grade economically valuable tasks; contamination-free novel tasks with private holdout sets; and informative leaderboards that explain why a model wins, not just who wins.

## Relevance to YOLO loop

Before using any public benchmark dataset for training or eval in our loop, running a quick audit against these five principles—especially checking for leaky prompts and weak verifiers—will prevent wasted training compute on low-quality signal.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-31 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-31-benchmark-task-quality-principles` |
| Channel | aie |
| Video | [Benchmarks: The Good, the Bad, and the Ugly — Ali Khial, G2i](https://www.youtube.com/watch?v=jWq-aZIU0kM) |
| Published | 2026-07-31 |
| Ingested upstream | 2026-07-31 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
