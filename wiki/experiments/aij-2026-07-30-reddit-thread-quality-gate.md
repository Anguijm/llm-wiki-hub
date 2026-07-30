# Implement a three-rule thread quality gate before any agent post action

> Back to [[experiments-index]]

Source: **[Loop engineer practice #1: Reddit loop grew 0 to 95 Karma in 7 days](https://www.youtube.com/watch?v=xn72yW9SNdA)** · aij · 2026-07-30

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we gate agent posting decisions behind strict thread-filtering rules (under 48 hours old, low comment temperature, answerable from a documented position in the wiki), then the agent will spend its limited daily posting slots on high-value opportunities, because fresh low-competition threads with a concrete available answer yield better engagement than old high-karma noise from sitewide search.

## What they did

Rather than using Reddit's global sitewide search, Jason defined a curated list of target subreddits and fetched only fresh threads. The agent then applied three filtering rules before deciding to post: (1) thread must be under 48 hours old, (2) thread must have low comment volume/temperature, (3) the agent must be able to produce a concrete answer grounded in the personal wiki. Threads failing any rule are dropped. Combined with injected randomness in posting schedule (3-5 posts spread across the day rather than a fixed cron time) to avoid bot-like patterns.

## Relevance to YOLO loop

Maps directly to any agent action-gating pattern in our loop. We can apply the same quality-gate idiom before our agents take external actions (posting, commenting, opening PRs) — define explicit pre-conditions that must all pass before the action fires, and skip rather than force when conditions aren't met.

## Notes

Jason also notes using OpenCRI (browser-based Reddit tool) over the closed Reddit API, and adds a workflow-based trigger with randomness to avoid posting at exactly the same time each day. The evolve/self-reflect loop reviews past post performance weekly and updates subreddit strategy automatically.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-30 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aij-2026-07-30-reddit-thread-quality-gate` |
| Channel | aij |
| Video | [Loop engineer practice #1: Reddit loop grew 0 to 95 Karma in 7 days](https://www.youtube.com/watch?v=xn72yW9SNdA) |
| Published | 2026-07-30 |
| Ingested upstream | 2026-07-30 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
