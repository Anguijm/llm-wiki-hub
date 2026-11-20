# Refine mini-forge base meshes with HY3D 1.0 and watertight nodes

> Back to [[experiments-index]]

Source: **[Best New Local 3D AI is Here! (Hi3D Open-Source)](https://www.youtube.com/watch?v=Mi2-AFifowU)** · pa · 2026-11-18

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we pass Trellis 2 or Pixel 3D base meshes through the HY3D 1.0 Refiner (1024 resolution plus watertight nodes) in ComfyUI before slicing, then faces and fine details will be sharper and mesh holes will drop sharply, because the refiner rebuilds detail and the video reports holes falling from about 13,000 to 17-26 on a Pixel 3D mesh.

## What they did

The presenters generated base meshes in ComfyUI with Trellis 2 or Pixel 3D and passed them through the HY3D 1.0 Refiner at 512, 1024 and 1536 resolution with watertight nodes. They compared the results side by side on character and dragon models and reported holes dropping from about 13k to 26, or 17 with watertight nodes. They cleaned up the remaining holes with a Blender Python script. The refiner needs 12-16 GB VRAM and is released under the HY3D Open License.

## Relevance to YOLO loop

none: This is a 3D asset-quality tool, not an AI development practice.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-11-19 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `pa-2026-11-18-hy3d-mesh-refiner` |
| Channel | pa |
| Video | [Best New Local 3D AI is Here! (Hi3D Open-Source)](https://www.youtube.com/watch?v=Mi2-AFifowU) |
| Published | 2026-11-18 |
| Ingested upstream | 2026-11-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
