# Add a TTS normalization layer between LLM output and speech synthesis to prevent production pronunciation failures

> Back to [[experiments-index]]

Source: **[5 Voice Agent Failure Modes You'll Hit in Week One — Venky B, Plivo](https://www.youtube.com/watch?v=vblnYHzBgS4)** · aie · 2026-09-15

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we insert an explicit normalization layer between LLM output and TTS that strips markdown/emojis, applies custom pronunciation dictionaries for brand names/acronyms/proper nouns, normalizes emails/phone numbers/dates/currency into speakable form, and applies speed control for complex entities, then we eliminate the most common class of TTS production failures without relying on the TTS engine's built-in normalization, because TTS engines vary in their handling of edge cases and switching providers breaks native normalization assumptions.

## What they did

Venky B (founder/CEO, Plivo, 14 years, 1B+ calls/month) enumerated five voice agent failure modes observed at production scale: (1) Latency—most teams target <550ms TTFA but land at 750ms-1.2s; balance cost/intelligence/latency tradeoffs per use case. (2) STT failures—use custom vocabulary, retry logic, and confidence thresholds. (3) LLM output quality—hallucination and context window issues. (4) TTS normalization—the most actionable: strip emojis/markdown, add custom dictionaries for proper nouns/brands/acronyms, normalize emails/currencies/dates explicitly in-house rather than relying on TTS engines, apply speed reduction (0.7-0.8x) for spelled-out entities. (5) Turn detection and barge-in/backchanneling. He recommended testing TTS pronunciation with your own name and company name as a minimum viability check.

## Relevance to YOLO loop

Immediately applicable: if our loop uses TTS at any point, adding a normalization pre-processing step is a low-effort, high-reliability improvement. The custom dictionary approach is especially relevant for our domain-specific terminology. Also useful as a pre-deployment checklist item.

## Notes

Venky's personal test: if TTS can't pronounce your name and your company name correctly out of the box, it will fail on domain-specific terms. Use this as a go/no-go gate when evaluating TTS providers.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-15-voice-agent-failure-modes-production` |
| Channel | aie |
| Video | [5 Voice Agent Failure Modes You'll Hit in Week One — Venky B, Plivo](https://www.youtube.com/watch?v=vblnYHzBgS4) |
| Published | 2026-09-15 |
| Ingested upstream | 2026-09-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
