# Build a personal wiki ingestion loop to ground agent responses in owner-specific POV

> Back to [[experiments-index]]

Source: **[Loop engineer practice #1: Reddit loop grew 0 to 95 Karma in 7 days](https://www.youtube.com/watch?v=xn72yW9SNdA)** · aij · 2026-07-30

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we feed an agent a continuously updated personal wiki (past writings, bookmarks, videos) and enforce that all responses must cite a position from that wiki, then agent-generated content will be more unique and less likely to be flagged or ignored, because the output reflects a genuine documented perspective rather than generic web research.

## What they did

Jason built a personal wiki aggregating his YouTube videos, Twitter bookmarks, and written content. A daily/weekly ingestion loop (running via an open-source tool called Looping) automatically pulls recent bookmarks and own content into the wiki with weighted priority. The Reddit agent is then constrained by a hard rule: every comment it posts must be grounded in a point of view documented in the wiki. This replaced a prior approach where the agent would research online and generate generic answers, which got banned quickly.

## Relevance to YOLO loop

Directly applicable as a context-grounding primitive for any agent in our dev loop that produces external-facing content. We could build an equivalent wiki from our own docs, ADRs, and Slack threads so agent outputs reflect our actual architectural positions rather than hallucinated best practices.

## Notes

Jason reports growing from -4 to 97 karma in ~1.5 weeks with this approach. Key companion mechanic: a self-reflect/evolve loop runs every few agent cycles to review post performance and propose new subreddits or content strategies automatically.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-30 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aij-2026-07-30-reddit-karma-loop-personal-wiki` |
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
