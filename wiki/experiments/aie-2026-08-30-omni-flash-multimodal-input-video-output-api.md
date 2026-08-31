# Prototype an automated video post-production pipeline using Gemini Omni Flash API (multimodal-in, video-out)

> Back to [[experiments-index]]

Source: **[SOTA Generative Media Panel — Dumitru Erhan, Shane Gu & Nicole Brichtova, Google DeepMind](https://www.youtube.com/watch?v=KLDdXOw6jIc)** · aie · 2026-08-30

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we pipe storyboard images plus a reference audio track into the newly released Gemini Omni Flash API, then we can automate short-form video assembly end-to-end at Gemini 1.5 Flash pricing, because the API now accepts arbitrary multimodal inputs and returns video output, removing the previous manual editing step.

## What they did

The DeepMind panel (Erhan, Gu, Brichtova) announced the public API launch of Gemini Omni Flash—pre-announced at Google IO—priced equivalently to Gemini 1.5 Flash. The model accepts any combination of images, audio, and text as input and returns video. Demonstrated workhorse use cases include: feeding a storyboard image set plus a reference voice audio to produce a short film segment; try-on applications where product images are composited onto reference subjects; brand-language-consistent ad generation from a corpus of brand assets (images + PDFs). They also launched NanoBanana 2 Light, a faster/cheaper image generation and editing model (~3-second latency) that approaches frontier quality and can produce production-ready outputs. The panelists emphasized that real-world failure modes (pattern tiling across custom rug sizes, earring scale relative to head, brand color precision) are surfaced by talking directly to domain users, not by internal benchmarks.

## Relevance to YOLO loop

Opens a new media-generation node in our dev loop: any pipeline step that currently requires a human to assemble video from script + assets can be prototyped with Omni Flash API calls. NanoBanana 2 Light's 3-second latency also makes it viable as an inline image-generation step during agent reasoning rather than an offline batch job. Pricing parity with 1.5 Flash removes cost as a blocking concern for experimentation.

## Notes

Panel confirmed Omni Flash API is live now. NanoBanana 2 Light also available via API. Panelists explicitly invited developers to share real-world failure cases directly with the team to inform upstream model improvements—worth filing issues if we hit edge cases in pattern replication or brand-color fidelity.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-30 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-30-omni-flash-multimodal-input-video-output-api` |
| Channel | aie |
| Video | [SOTA Generative Media Panel — Dumitru Erhan, Shane Gu & Nicole Brichtova, Google DeepMind](https://www.youtube.com/watch?v=KLDdXOw6jIc) |
| Published | 2026-08-30 |
| Ingested upstream | 2026-08-30 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
