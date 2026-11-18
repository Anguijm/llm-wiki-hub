# Split a miniature concept into parts before TRELLIS generation

> Back to [[experiments-index]]

Source: **[New Best 3D AI Workflow for Game-Ready Characters](https://www.youtube.com/watch?v=Janlg9BOt1A)** · pa · 2026-11-15

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we split one character concept image into isolated body parts (body, head, arms, legs, cloth) with an image-edit model and generate each part as its own TRELLIS mesh, then face, hand and prop detail will beat single-pass generation because each part gets the full mesh and texture budget.

## What they did

Philipp split a 2D orc concept into isolated parts on white backgrounds using Qwen Image 2.1 Edit in ComfyUI (25 steps, pre-cropped bounding boxes). He generated each part with a Trellis 2 low-poly, watertight and UltraTex workflow (12k faces used, 20k-30k recommended for characters), then assembled the GLB parts in Blender. Neck and hand alignment needed manual cleanup, and UltraTex produced a broken loincloth texture that required falling back to Trellis 2's default texture.

## Relevance to YOLO loop

none: This is a 3D asset pipeline, not an AI development practice.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-11-17 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `pa-2026-11-15-split-part-3d-generation` |
| Channel | pa |
| Video | [New Best 3D AI Workflow for Game-Ready Characters](https://www.youtube.com/watch?v=Janlg9BOt1A) |
| Published | 2026-11-15 |
| Ingested upstream | 2026-11-17 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
