# Map personal pain points from Opus 4.7 to Opus 4.8 effort levels to find the cheapest effective setting

> Back to [[experiments-index]]

Source: **[Opus 4.8 Just Dropped. Here's How To Actually Use It.](https://www.youtube.com/watch?v=q5lg3npxjAc)** · nh · 2026-06-11

**Status:** `adopted` · **Verdict:** `adopt` · **Effort:** `low`

---

## Hypothesis

If we systematically test each effort level (low, medium, high, x-high, max, ultra code) against the specific tasks where Opus 4.7 failed (over-claiming completion, attitude, token sprawl), then we find the minimum effort level that resolves those pain points, saving tokens without sacrificing quality, because Opus 4.8 was explicitly trained to address 4.7's honesty and over-verbosity issues and the effort slider directly controls reasoning depth.

## What they did

Nate reviewed the Opus 4.8 launch blog, highlighted the /effort slider in Claude Code CLI (low→medium→high→x-high→max→ultra code), noted that rate limits (not session limits) were increased for API users, and walked through the honesty improvement benchmarks showing 4.8 at ~half the misaligned-behavior score of 4.7. He listed the main 4.7 complaints (false completion claims, attitude, token waste, lying about push counts) and mapped how 4.8 addresses each. He recommended testing personal workflows rather than trusting global benchmarks, and mentioned a free open-source token dashboard GitHub repo for tracking where tokens actually go.

## Relevance to YOLO loop

Effort level is a key loop parameter; finding the minimum effective effort for each loop step (plan vs execute vs review) directly reduces session-limit burn and cost.

## Notes

Ultra code = x-high + dynamic workflows, most expensive. Opus 4.8 priced same as 4.7. Dynamic workflows are a new separate feature covered in dedicated video. Token dashboard repo available via School community.

Backlog triage 2026-06-24 (owner-preference model). Find cheapest effective effort level — efficiency without leaving Claude; matches Haiku/Sonnet-vs-Opus benchmarking.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-06-11-opus48-effort-levels-token-efficiency` |
| Channel | nh |
| Video | [Opus 4.8 Just Dropped. Here's How To Actually Use It.](https://www.youtube.com/watch?v=q5lg3npxjAc) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
