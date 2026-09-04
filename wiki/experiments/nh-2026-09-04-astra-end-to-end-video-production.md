# Prompt GPT-6 Astra to autonomously produce a finished YouTube video end-to-end from a single open-ended brief

> Back to [[experiments-index]]

Source: **[GPT-6 Astra Made This Entire Video](https://www.youtube.com/watch?v=dT5-x3u5nCg)** · nh · 2026-09-04

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we give GPT-6 Astra a single open-ended prompt requesting a finished YouTube video (with voice clone and avatar specified), then it can autonomously handle research, B-roll capture via computer use, scripting, audio segmentation, avatar rendering, and editing in Hyperframes, because Astra's computer-use and long-horizon task capabilities allow it to orchestrate multiple tools without manual intervention.

## What they did

Speaker gave Astra one prompt asking for a finished YouTube video about GPT-6 Astra's release, specifying use of his 11Labs voice clone and HeyGen Avatar V5. Astra used computer use to open creator posts, capture screenshots, locate avatar and voice clone setups in the workspace, split narration into segments, send audio to the avatar service, build a Hyperframes edit with music/SFX, render, and self-verify by transcribing the finished audio against the script. Total runtime ~50 minutes; estimated API cost ~$60 on fast mode.

## Relevance to YOLO loop

Extreme end-to-end agentic pipeline — maps to a YOLO loop where the model owns the entire production workflow, uses computer use to gather assets, and self-verifies output before delivery. Tests whether a single prompt can close a creative loop without human handoffs.

## Notes

Speaker notes the prompt was intentionally open-ended; Astra self-directed tool selection. Cost ~$60 at API fast-mode pricing. Speaker used 2 full resets of their usage limit and was at 50% on a third. Access is limited rollout (Daybreak program) at time of recording.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-04 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-09-04-astra-end-to-end-video-production` |
| Channel | nh |
| Video | [GPT-6 Astra Made This Entire Video](https://www.youtube.com/watch?v=dT5-x3u5nCg) |
| Published | 2026-09-04 |
| Ingested upstream | 2026-09-04 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
