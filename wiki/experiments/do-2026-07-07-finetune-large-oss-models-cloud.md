# Fine-tune a 1T-parameter OSS model via cloud GPU rental and deploy via API

> Back to [[experiments-index]]

Source: **[Fine-Tune the biggest open-source models (even with a bad PC)](https://www.youtube.com/watch?v=kxstlfc8Lw4)** · do · 2026-07-07

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we fine-tune a large open-source model (e.g., Kimi K2.7) on a curated domain-specific dataset using rented cloud GPUs instead of local hardware, then we can produce a custom model that outperforms the base model on that domain at a fraction of the cost of proprietary APIs, because supervised fine-tuning on high-quality examples shifts model behavior without requiring ownership of expensive hardware.

## What they did

David walked through the full pipeline for fine-tuning Kimi K2.7 (a ~1T parameter open-source model) on a custom dataset. He explained that local hardware is cost-prohibitive (~$300k+ for Blackwell server racks), so he used a cloud GPU rental platform. He prepared a dataset using a reusable skill/script that reformats HuggingFace datasets into the correct fine-tuning format. He performed supervised fine-tuning (not RL), deployed the fine-tuned model via the Kimi API, and then ran a live comparison UI showing the fine-tuned model (trained on a 'Fable' reasoning dataset with thinking traces) versus the base Kimi model across productivity and health questions, observing differences in verbosity, reasoning visibility, and formatting.

## Relevance to YOLO loop

Directly applicable for creating specialized model variants for specific loop tasks (e.g., code review, planning, summarization). The cloud GPU approach removes the hardware barrier, and the dataset formatting script reduces prep friction. The comparison UI pattern is a useful eval harness idea.

## Notes

Video is sponsored by Kimi; treat platform-specific claims with mild skepticism. Core methodology (cloud GPU fine-tuning of OSS models + supervised FT on curated data) is platform-agnostic and reproducible on other providers (Together AI, Modal, RunPod, etc.).

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-07 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-07-07-finetune-large-oss-models-cloud` |
| Channel | do |
| Video | [Fine-Tune the biggest open-source models (even with a bad PC)](https://www.youtube.com/watch?v=kxstlfc8Lw4) |
| Published | 2026-07-07 |
| Ingested upstream | 2026-07-07 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
