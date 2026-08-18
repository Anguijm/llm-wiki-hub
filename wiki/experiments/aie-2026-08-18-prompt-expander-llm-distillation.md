# Add a small LLM prompt expander before image generation to improve output quality

> Back to [[experiments-index]]

Source: **[Training Krea 2: What matters in generative model training — Sangwu Lee, Krea.ai](https://www.youtube.com/watch?v=-tviRdpmHvs)** · aie · 2026-08-18

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we prepend a small LLM that expands short user prompts into long, detailed prompts before passing them to a diffusion model, then image quality will improve because longer detailed prompts are more in-distribution with the model's training data, which typically consisted of verbose captions.

## What they did

Sangwu Lee described training a small LLM as a 'prompt expander' that takes a short user prompt and outputs a longer, detailed prompt to feed into the image diffusion model. He noted this is necessary because diffusion models are trained on verbose captions, so short user inputs are out-of-distribution. He also described a next step: multi-expert positive distillation, where specialist models (e.g., photography expert, text rendering expert) are trained separately and then merged into a single student model that matches each expert's capability in its domain.

## Relevance to YOLO loop

Highly relevant for any pipeline that calls image generation models. We can implement a lightweight prompt expansion step using an existing small LLM (e.g., a local model or API call) before invoking image generation, potentially improving output quality with minimal architectural change.

## Notes

Speaker drew analogy to DALL-E 2's conditioning pipeline. Multi-expert distillation noted as a future direction worth tracking. Prompt expansion is the immediately actionable piece.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-18 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-18-prompt-expander-llm-distillation` |
| Channel | aie |
| Video | [Training Krea 2: What matters in generative model training — Sangwu Lee, Krea.ai](https://www.youtube.com/watch?v=-tviRdpmHvs) |
| Published | 2026-08-18 |
| Ingested upstream | 2026-08-18 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
