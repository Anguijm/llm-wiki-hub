# Run overnight synthetic-audio tests against Push to Talk

> Back to [[experiments-index]]

Source: **[Claude Fable 5.2 Can Do So Much More Than Build Apps](https://www.youtube.com/watch?v=5cZontQjBH4)** · mk · 2026-11-13

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we play 30+ synthetic spoken prompts from a laptop speaker into the phone running Push to Talk and log transcripts with timing, then we will find latency and misrecognition regressions without manual dictation because the loop is fully automated and repeatable.

## What they did

Kashef had Claude play synthetic audio from Mac speakers to the robot to simulate over 30 conversations overnight. The run logged second-by-second screenshots and tool traces, which surfaced latency, missed wake words and tool-calling misfires.

## Relevance to YOLO loop

medium: Automated end-to-end testing with synthetic input is good practice but is close to existing verification gates.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-11-14 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mk-2026-11-13-synthetic-audio-ptt-test` |
| Channel | mk |
| Video | [Claude Fable 5.2 Can Do So Much More Than Build Apps](https://www.youtube.com/watch?v=5cZontQjBH4) |
| Published | 2026-11-13 |
| Ingested upstream | 2026-11-14 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
