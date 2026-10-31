# Gate task completion on pre-written evals via a hook

> Back to [[experiments-index]]

Source: **[Anthropic Just Released A New System For Using Claude Code](https://www.youtube.com/watch?v=S49gppZl8H0)** · ail · 2026-10-30

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we turn feature specs into eval files and mockups before coding and use a hook that blocks task completion until all evals pass, then fewer regressions will be merged because the agent cannot declare success on its own judgment.

## What they did

The workflow converts feature requirement markdown into explicit eval files and HTML mockups up front. A hook prevents agents from marking tasks complete until the evals pass. The video credits Anthropic's structured verification with a drop of more than 40% in reverted changes.

## Relevance to YOLO loop

high: A hook-enforced eval gate is a core verification-loop pattern for Claude Code harnesses.

## Notes

Anthropic statistics are as relayed by the channel, not independently verified.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-30 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `ail-2026-10-30-evals-first-stop-hook` |
| Channel | ail |
| Video | [Anthropic Just Released A New System For Using Claude Code](https://www.youtube.com/watch?v=S49gppZl8H0) |
| Published | 2026-10-30 |
| Ingested upstream | 2026-10-30 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
