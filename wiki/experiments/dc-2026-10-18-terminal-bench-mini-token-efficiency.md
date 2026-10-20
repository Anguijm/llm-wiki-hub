# Compare token use of local model on Terminal Bench Mini

> Back to [[experiments-index]]

Source: **[DeepSeek V4.1 Flash 1017 Update: 44% Fewer Tokens, Running on Strix / Gorgon Halo with DwarfStar](https://www.youtube.com/watch?v=A1vscZzkUg4)** · dc · 2026-10-18

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we run Terminal Bench Mini against the 1017 refresh and the previous weights on our Strix Halo box, then we should see roughly 44% fewer generated tokens and about 42% shorter completion time, because the video attributes this to more concise reasoning in the refreshed model.

## What they did

The speaker ran Terminal Bench Mini live, completing 9 of 9 command-line coding tasks. He reported 44% fewer generated tokens and a 42% drop in average completion time on the first eight tasks. The server was launched through the AI Toolbox Cockpit UI in DwarfStar server mode with SWA bounded reply.

## Relevance to YOLO loop

medium: Terminal Bench Mini is a small repeatable benchmark that could act as a verification loop for comparing local agent backends.

## Notes

The completion-time result covers only the first eight tasks and the sample is small, so treat the percentages as indicative.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-19 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `dc-2026-10-18-terminal-bench-mini-token-efficiency` |
| Channel | dc |
| Video | [DeepSeek V4.1 Flash 1017 Update: 44% Fewer Tokens, Running on Strix / Gorgon Halo with DwarfStar](https://www.youtube.com/watch?v=A1vscZzkUg4) |
| Published | 2026-10-18 |
| Ingested upstream | 2026-10-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
