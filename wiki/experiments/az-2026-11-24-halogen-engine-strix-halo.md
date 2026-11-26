# Compare the Halogen engine with llama.cpp Vulkan on the Strix Halo box

> Back to [[experiments-index]]

Source: **[128GB AI Desktops… HUGE Price difference (ACTUALLY Tested)](https://www.youtube.com/watch?v=dkITChVXii0)** · az · 2026-11-24

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we run Qwen 3.8 Flash Next (94 GB 4-bit) through the Halogen engine on the Strix Halo box and compare it with the current llama.cpp Vulkan baseline, then decode and long-prompt prefill will speed up noticeably, because the video measured Halogen at 51 tok/s with a 71 s prefill on a 133k-token prompt, against 26.6 tok/s and 8 min for llama.cpp on the same Ryzen AI Max+ 395 class hardware.

## What they did

Alex Ziskind ran baseline llama.cpp on four 128 GB machines, including an AMD Ryzen AI Halo (Ryzen AI Max+ 395). He then re-tested with hardware-specific engines. On the Halo he used Halogen with speculative decoding. Flash Next decode went from 26.6 to 51 tok/s, and the 133k-token prefill dropped from 8 min to 71 s. He had to raise the OS GPU memory limit so the 94 GB model would load. He also ran 1–8 concurrent users, plus power and temperature logging. Halogen only supports Strix Halo and specific Qwen models.

## Relevance to YOLO loop

none: This is a hardware and inference-engine benchmark, not a development-practice technique.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-11-25 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `az-2026-11-24-halogen-engine-strix-halo` |
| Channel | az |
| Video | [128GB AI Desktops… HUGE Price difference (ACTUALLY Tested)](https://www.youtube.com/watch?v=dkITChVXii0) |
| Published | 2026-11-24 |
| Ingested upstream | 2026-11-25 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
