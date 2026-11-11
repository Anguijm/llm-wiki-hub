# Apply the ComfyUI contiguous-memory patch on Strix Halo ROCm

> Back to [[experiments-index]]

Source: **[NVIDIA, It's Happening Again](https://www.youtube.com/watch?v=k7_K34eY9TM)** · az · 2026-11-10

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we apply the one-line PyTorch contiguous memory fix to ComfyUI's attention handlers on the Strix Halo box and rerun a fixed image or video generation workflow, then render time drops noticeably because the video showed ROCm attention on a sibling AMD unified-memory chip running about 2.5x faster with the same fix.

## What they did

Alex Ziskind ran ComfyUI on native Ubuntu with ROCm on an AMD Ryzen AI Max+ Pro mini PC. A stock 5-second LTX video took 316 seconds. After a one-line contiguous memory patch to the attention handlers, the same render took 126 seconds (about 2.5x faster). He also noted that WSL has no ROCm GPU access, so native Linux was needed.

## Relevance to YOLO loop

none: This is a hardware and inference tuning tip, not an AI development practice.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-11-10 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `az-2026-11-10-comfyui-contiguous-patch-strix-halo` |
| Channel | az |
| Video | [NVIDIA, It's Happening Again](https://www.youtube.com/watch?v=k7_K34eY9TM) |
| Published | 2026-11-10 |
| Ingested upstream | 2026-11-10 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
