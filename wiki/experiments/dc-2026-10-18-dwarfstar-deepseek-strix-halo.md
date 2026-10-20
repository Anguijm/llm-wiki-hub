# Benchmark DwarfStar with DeepSeek V4.1 Flash Q2 on Strix Halo

> Back to [[experiments-index]]

Source: **[DeepSeek V4.1 Flash 1017 Update: 44% Fewer Tokens, Running on Strix / Gorgon Halo with DwarfStar](https://www.youtube.com/watch?v=A1vscZzkUg4)** · dc · 2026-10-18

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we run the DeepSeek V4.1 Flash 1017 Q2 weights on DwarfStar on our Strix Halo box with SWA bounded reply and speculative decoding enabled, then prefill should exceed about 400 tokens/s and generation should reach about 17-18 tokens/s, because the video reports those figures on a single Gorgon Halo machine.

## What they did

The speaker quantized the updated weights to Q2 using an established calibration dataset, then installed DwarfStar via pipx through the AI Toolbox Cockpit. He enabled SWA bounded reply, which approximates by processing only half the model during prefill, and speculative decoding with a draft model (spark). He also clustered two Strix Halo machines over TCP, reaching nearly 500 tokens/s prefill and about 17 tokens/s generation. He reported baseline prefill of 230-380 tokens/s and baseline generation of 14-15 tokens/s on one Gorgon Halo.

## Relevance to YOLO loop

medium: A fast local model could serve as a cheap backend for agent loops, though this is not a Claude Code practice itself.

## Notes

Caveat from the video: the Q2 quant was made independently by the presenter, not the upstream maintainer, so verify provenance before use. SWA bounded reply is an approximation, so check quality as well as speed. Two-node TCP speculative decoding is unoptimized.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-19 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `dc-2026-10-18-dwarfstar-deepseek-strix-halo` |
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
