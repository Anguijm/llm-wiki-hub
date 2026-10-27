# Pick from a 100-image option grid before generating 3D

> Back to [[experiments-index]]

Source: **[Ask AI for Options, Not Adjectives: 3 Trades](https://www.youtube.com/watch?v=zAyEj9ien2A)** · eh · 2026-10-26

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we generate a grid of about 100 image variations and choose candidates before running text/image-to-3D, then we get usable miniature models faster because human selection replaces adjective-driven prompt iteration.

## What they did

Echo showed that stacking subjective adjectives like 'impressive' or 'unique' makes models swing between cliche and nonsense. He replaced adjectives with three trades: a physical shape (e.g. crescent), a process (brainstorm 50 possibilities, pick 5 at random, build from those), or an option grid (100 stills to choose from before expensive video or 3D). Using a 100-image spaceship grid, he picked 35 designs and made 35 3D models in 30 minutes, after hours of failed adjective prompting. Costs: higher up-front compute and human curation time.

## Relevance to YOLO loop

medium: The generate-many-then-select pattern could be reused in agent prompting, but it is not specific to dev agents.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-26 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `eh-2026-10-26-option-grid-before-3d` |
| Channel | eh |
| Video | [Ask AI for Options, Not Adjectives: 3 Trades](https://www.youtube.com/watch?v=zAyEj9ien2A) |
| Published | 2026-10-26 |
| Ingested upstream | 2026-10-26 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
