# Cap open-ended improvement loops with a plateau stop and human checkpoint

> Back to [[experiments-index]]

Source: **[I Told Claude to "Make it better" 100 Times (It Went Too Far)](https://www.youtube.com/watch?v=DByAR5Su1Yw)** · nh · 2026-10-30

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we limit autonomous 'make it better' loops to about 30 rounds with a milestone log and a human review checkpoint, then we will keep most of the gains and avoid overengineering because the video shows functional gains peaked around round 32 and later rounds added broken fluff.

## What they did

Nate Herk ran Claude Code 100 consecutive clean-room rounds on an ugly coffee shop site with Sonnet 5.5 and Opus 5.5, each round shipping one bold change. He tracked lines of code, tool calls, cost and feature milestones. Major gains peaked near round 32. Opus bloated to over 21,000 lines with broken mini-games and a broken language toggle, and neither model searched the web for inspiration unless told to.

## Relevance to YOLO loop

high: Directly informs iteration caps, plateau detection and human taste checkpoints for autonomous loops.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-30 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-10-30-cap-improvement-loops` |
| Channel | nh |
| Video | [I Told Claude to "Make it better" 100 Times (It Went Too Far)](https://www.youtube.com/watch?v=DByAR5Su1Yw) |
| Published | 2026-10-30 |
| Ingested upstream | 2026-10-30 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
