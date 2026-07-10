# Route tasks between GPT-5.6 Soul and Claude Fable 5 based on creative vs. execution workload

> Back to [[experiments-index]]

Source: **[I Tested GPT 5.6 Sol vs Fable 5. What You Need To Know.](https://www.youtube.com/watch?v=EthxaDswUFo)** · nh · 2026-07-10

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we route creative, reasoning, and advisory tasks to Claude Fable 5 and shipping/execution/debugging tasks to GPT-5.6 Soul, then we will get higher output quality per dollar because Fable 5 produces richer creative output despite costing ~3x more per run, while Soul executes instructions efficiently at lower token cost.

## What they did

Nate ran identical prompts side-by-side in Claude (Fable 5 via Codex) and GPT-5.6 Soul across three task types: building a browser-based open-world bike game, building an interactive scroll-stopping website, and day-to-day coding/debugging work. He measured wall-clock time, cost, and output token count for each pair. Fable 5 cost ~$14 and produced ~90k output tokens; Soul cost ~$4.50 and produced ~31k tokens. Fable won on creative tasks (better 3D game, richer website); Soul won on systematic debugging due to extensive self-verification and computer use. He concluded Fable = reasoning/judging/creativity, Soul = shipping/executing.

## Relevance to YOLO loop

The YOLO loop uses a single model for all steps. A two-model routing layer — Fable for planning/architecture/review, Soul for implementation/test-fix cycles — could cut costs on execution-heavy phases while preserving quality on design decisions.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-10 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-07-10-soul-vs-fable-routing` |
| Channel | nh |
| Video | [I Tested GPT 5.6 Sol vs Fable 5. What You Need To Know.](https://www.youtube.com/watch?v=EthxaDswUFo) |
| Published | 2026-07-10 |
| Ingested upstream | 2026-07-10 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
