# Implement a three-zone hill-climbing eval loop: fix obvious harness bugs, apply model-family-specific prompt tuning, then stop before overfitting

> Back to [[experiments-index]]

Source: **[Evals Are Broken, Use Them Anyway — Ara Khan, Cline](https://www.youtube.com/watch?v=QuuIywMG4s8)** · aie · 2026-06-11

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we structure our eval improvement process into three explicit zones—(1) fix clear harness bugs, (2) apply nuanced model-family-specific prompt engineering, (3) halt before score-gaming overfitting—then our agents will improve on both benchmark score and real-world vibe-check quality, because conflating these zones leads either to ignoring legitimate signal or to benchmark-maxing that doesn't transfer to production.

## What they did

Ara Khan from Cline gave a critique-and-guidance talk on eval methodology. He identified two failure modes: over-reliance on objective benchmark numbers (which can be gamed and don't reflect real-world quality) and pure vibes/taste (which can't be systematized). His practical framework: use existing public evals as a starting signal but don't trust model-provider numbers uncritically; wait a few weeks after model release before switching to let the dust settle; seek new, precise, narrow evals over old standardized ones. For improving agents via evals, he outlined three zones: Zone 1 (obvious bugs—crashes, rate limits—fix immediately), Zone 2 (nuanced improvements—prompt engineering specific to Anthropic vs. Gemini vs. other model families, prompt size tuning), Zone 3 (danger zone—overfitting to benchmark, don't do it). He shared that Cline discovered they were strong on Anthropic model families but weak on Gemini and Kimi, and hill-climbing on those gaps opened new user segments.

## Relevance to YOLO loop

Directly applicable to our eval loop. The three-zone framework gives us a concrete decision process for triaging eval score changes and avoiding both under-reaction (ignoring real bugs) and over-reaction (overfitting prompts to a specific benchmark).

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-11-evals-hill-climbing-zones` |
| Channel | aie |
| Video | [Evals Are Broken, Use Them Anyway — Ara Khan, Cline](https://www.youtube.com/watch?v=QuuIywMG4s8) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
