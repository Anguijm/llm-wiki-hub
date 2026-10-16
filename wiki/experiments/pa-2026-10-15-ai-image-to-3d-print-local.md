# Run a fully local ComfyUI pipeline from text prompt through Trellis 2 to watertight 3D print STL

> Back to [[experiments-index]]

Source: **[Turn AI Images Into Real 3D Prints – 100% Free & Local](https://www.youtube.com/watch?v=CSiNa_ZCwwA)** · pa · 2026-10-15

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we chain Qwen Image 2.1 (text-to-image) → Trellis 2 (image-to-3D) → watertight mesh nodes → Blender cleanup → slicer in a single ComfyUI workflow running entirely locally, then we can produce printable watertight STL files up to 2K resolution without any cloud services, because Trellis 2 and the watertight nodes compiled for CUDA 12.8 + PyTorch 2.8 + Python 3.12 handle mesh sealing that raw Trellis output lacks.

## What they did

Pixel Artistry demonstrated a fully local pipeline: text prompt → Qwen Image 2.1 in ComfyUI → Trellis 2 for 3D mesh → custom watertight mesh nodes (by MostAtt tech, CUDA 12.8/PyTorch 2.8/Python 3.12) → Blender loose-part cleanup → Chitubox slicer → resin printer. Three print resolution workflows provided (1K, 1.5K, 2K) plus a multi-view workflow. All workflows, an installer bat, prompt templates, and examples are free on their GitHub (pixel artistry image-to-3D-print repo). Printed result was a dragon gear miniature in ~4 hours on a resin printer.

## Relevance to YOLO loop

none: this is a 3D printing pipeline, not an AI dev loop pattern.

## Notes

Critical dependency: watertight nodes require CUDA 12.8 + PyTorch 2.8 + Python 3.12 exactly—install via Trellis 2 bat file first. AMD version of Trellis 2 in progress (linked in video). Blender cleanup step: import GLB, edit mode, P → by loose parts, delete tiny floating meshes, export STL with 'selection only' + scale 1. Slicer scale trick: model imports tiny, change scale from 100 to 10000. GitHub repo: pixel artistry image-to-3D-print. Three resolution tiers: 1K, 1.5K, 2K.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `pa-2026-10-15-ai-image-to-3d-print-local` |
| Channel | pa |
| Video | [Turn AI Images Into Real 3D Prints – 100% Free & Local](https://www.youtube.com/watch?v=CSiNa_ZCwwA) |
| Published | 2026-10-15 |
| Ingested upstream | 2026-10-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
