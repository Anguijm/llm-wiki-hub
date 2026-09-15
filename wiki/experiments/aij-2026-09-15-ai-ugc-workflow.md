# Build an agent-driven UGC video pipeline using Kling 2.5 + fish audio + Track for $2-3 per clip

> Back to [[experiments-index]]

Source: **[How to run your first AI UGC campaign (step-by-step guide)](https://www.youtube.com/watch?v=GkGufbIVVC8)** · aij · 2026-09-15

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we use a Claude Code or Codex agent equipped with the Track plugin (open-source data/tooling aggregator) to pull trending content, generate a consistent AI character via constrained image prompting, clone a voice via fish audio, and produce talking-head UGC clips via Kling 2.5, then we can generate hyperrealistic UGC content at ~$2.67 per clip versus the $20-50 human creator cost, because modern video generation models with proper character-locking prompts produce output indistinguishable from real UGC at a fraction of the cost.

## What they did

The speaker walked through an end-to-end AI UGC workflow: (1) Use Track (open-source agent plugin) to pull trending TikTok/Instagram videos in a vertical and analyze hooks and characters. (2) Use a constrained prompt technique (credit to friend Harry) with GPT Image 2.5 to generate a realistic AI character that matches a target vibe without the typical AI-slop doll-face artifacts. (3) Clone a voice using fish audio from reference clips. (4) Use a custom Claude Code skill that takes a hook script, generates a Kling 2.5 video with the character and cloned voice, and adds captions—all for $2.67 per clip. (5) Pair one product demo with 5-10 different hooks for A/B testing at scale. He also described a more detailed storyboard flow for complex videos.

## Relevance to YOLO loop

Directly applicable as a content/marketing automation arm of the loop: we could generate demo videos or tutorial UGC for our own tools using this pipeline. The Track plugin pattern (one key, pay-per-use access to 3000+ data/tool endpoints) is also worth evaluating as an agent tooling layer for our own agents.

## Notes

Track is open source and self-hostable. Kling 2.5 accessed via Track API. Character image consistency is the hard part—the constrained-prompt technique is the key unlock.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aij-2026-09-15-ai-ugc-workflow` |
| Channel | aij |
| Video | [How to run your first AI UGC campaign (step-by-step guide)](https://www.youtube.com/watch?v=GkGufbIVVC8) |
| Published | 2026-09-15 |
| Ingested upstream | 2026-09-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
