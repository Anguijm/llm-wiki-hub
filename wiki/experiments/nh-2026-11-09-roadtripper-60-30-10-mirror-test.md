# Constrain Roadtripper's landing page with the mirror test and 60-30-10 palette

> Back to [[experiments-index]]

Source: **[I Studied 10,000 AI Websites… Here’s what I learned](https://www.youtube.com/watch?v=mImbbszCjCI)** · nh · 2026-11-09

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we answer the three mirror-test questions (who it's for, what they get, what to do next) and fix a 60-30-10 palette before prompting an AI redesign of the Roadtripper landing page, then the output will be clearer and higher-contrast than an unconstrained generation, because the video says models default to generic copy and low-contrast palettes unless constrained.

## What they did

Nate Herk distils patterns from 10,000 AI-built sites. First write answers to the three mirror-test questions before prompting. Then limit the palette to 60% background, 30% text and structure, and 10% accent button, using a palette tool such as Coolors. Layer the page as back (mood image), middle (cards) and front (CTA with a soft shadow). Allow one moving element per screen and honour prefers-reduced-motion.

## Relevance to YOLO loop

none: This is web design advice and no new agent practice.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-11-12 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-11-09-roadtripper-60-30-10-mirror-test` |
| Channel | nh |
| Video | [I Studied 10,000 AI Websites… Here’s what I learned](https://www.youtube.com/watch?v=mImbbszCjCI) |
| Published | 2026-11-09 |
| Ingested upstream | 2026-11-12 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
