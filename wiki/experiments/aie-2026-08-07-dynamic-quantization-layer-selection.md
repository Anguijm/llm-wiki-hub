# Apply Dynamic Per-Layer Quantization to Preserve Accuracy on Local Models

> Back to [[experiments-index]]

Source: **[Compression at the Edge — NVIDIA, Unsloth, HuggingFace, Ollama](https://www.youtube.com/watch?v=J4_jCrTxMkk)** · aie · 2026-08-07

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we quantize a large model using dynamic per-layer precision (critical layers at FP16, most layers at 1-2 bit) rather than uniform quantization, then we can achieve 80%+ size reduction while retaining ~76% of benchmark accuracy because important layers that disproportionately affect output logits are preserved at higher fidelity.

## What they did

Daniel from Unsloth described how they applied dynamic quantization to DeepSeek R1 when it launched: instead of uniform low-bit quantization they selectively kept critical layers at higher precision (up to 16-bit) while compressing most layers to 1-2 bit. This reduced GLM 5.2 (1.5TB) to ~250GB (86% smaller) while recovering 76% of accuracy. They validated using KL divergence between the BF16 baseline and the quantized version over calibration data rather than relying solely on accuracy benchmarks. Marv from NVIDIA described the same principle as 'same cost more intelligence' — the progression from FP32 training to FP4 inference representing 8x compression with minimal degradation. Parth from Ollama noted this is what made large models viable for consumer hardware.

## Relevance to YOLO loop

If the YOLO loop runs local models for cost or privacy reasons, dynamic quantization determines which models are actually usable on available hardware. Evaluating quantized variants with KLD rather than benchmark accuracy gives a faster and more reliable signal for model selection decisions.

## Notes

Reference paper mentioned: 'Accuracy is Not All You Need' for KLD-based quantization evaluation methodology. The KLD approach (compare output logits of BF16 vs quantized over calibration set) is worth adopting as a standard local model evaluation step before committing to a quant variant.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-07 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-07-dynamic-quantization-layer-selection` |
| Channel | aie |
| Video | [Compression at the Edge — NVIDIA, Unsloth, HuggingFace, Ollama](https://www.youtube.com/watch?v=J4_jCrTxMkk) |
| Published | 2026-08-07 |
| Ingested upstream | 2026-08-07 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
