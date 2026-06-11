# Integrate Flux Context for sub-second in-loop image editing instead of generation-only models

> Back to [[experiments-index]]

Source: **[FLUX, Open Research, and the Future of Visual AI — Stephen Batifol, Black Forest Labs](https://www.youtube.com/watch?v=x8Yb4RidLgM)** · aie · 2026-05-10

**Status:** `deferred` · **Effort:** `low`

---

## Hypothesis

If we use Flux Context (or the faster Client variant) for iterative image editing in an agent loop instead of a text-to-image-only model, then the loop can perform character/product-consistent visual modifications in under 1 second per step, because Flux Context combines editing and generation in one model and the Client variant achieves ~0.5s latency vs ~15s for comparable open-source alternatives.

## What they did

Stephen Batifol described Black Forest Labs' model progression: Flux 1 (open-source text-to-image), Flux Context (first open-source combined text-to-image + image editing model with character consistency, ~7-8s vs GPT Image's 40-50s), Flux 2 (best quality, accepts up to 10 simultaneous input images), and Client (near-real-time editing at ~0.5s for 4B and 9B variants vs Qwen's ~15-20s). He demonstrated storyboarding, product photography, outfit generation from reference images, and local editing use cases. He also previewed world models and physical AI/robotics directions.

## Relevance to YOLO loop

An agent loop that generates visual artifacts (mockups, UI screenshots, diagrams) currently waits on slow image generation. Swapping to Flux Context/Client enables rapid iterative visual refinement within the loop at near-real-time speed, making visual output a practical loop-native operation rather than an expensive async step.

## Notes

Deferred 2026-05-10: image-editing cluster. Park with the other image-tooling defers.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-05-10 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-05-10-flux-context-realtime-image-editing` |
| Channel | aie |
| Video | [FLUX, Open Research, and the Future of Visual AI — Stephen Batifol, Black Forest Labs](https://www.youtube.com/watch?v=x8Yb4RidLgM) |
| Published | 2026-05-10 |
| Ingested upstream | 2026-05-10 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
