# Use RunPod Flash SDK decorator to deploy GPU inference functions from local dev environment without Docker build cycles

> Back to [[experiments-index]]

Source: **[GPU Cloud Deployment Without Leaving Your IDE — Audry Hsu, RunPod](https://www.youtube.com/watch?v=zDGHt0LB-dA)** · aie · 2026-06-11

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we use the RunPod Flash Python SDK's @endpoint decorator on async inference functions, then we can iterate on GPU-dependent model code from a local IDE with hot-reload rather than enduring commit→Docker build→registry push→deploy cycles, reducing per-iteration feedback time from minutes to seconds because only the decorated function is packaged and deployed to cloud GPU while surrounding orchestration code runs locally.

## What they did

Audrey Hsu from RunPod presented Flash, their Python SDK for GPU cloud development. Core mechanic: add a @flash_endpoint decorator to any async Python function; Flash packages everything inside that function and deploys it to a RunPod GPU worker while the rest of the application (orchestration, helper functions, main loop) runs on the local machine. Hot file reload means any change to the function triggers immediate repackaging and redeployment. She demonstrated a multi-model image generation pipeline: Qwen 3 generates prompts → DreamShaper generates images → NanoBanana 2 (Google model) composites them. All model calls used RunPod-hosted endpoints invoked via the Flash decorator. Pricing: charged per second of actual GPU usage at ~$0.00116/sec for H100. She contrasted serverless (auto-scaling, slight premium, best for variable load) vs. pods (reserved GPU, no scaling, better for experimentation).

## Relevance to YOLO loop

Relevant if our YOLO loop includes GPU-dependent steps (model inference, fine-tuning, embedding generation). Flash's decorator pattern could dramatically speed up iteration on those steps by eliminating infrastructure boilerplate and enabling local-first development with cloud GPU execution.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-11-runpod-flash-sdk-local-gpu-iteration` |
| Channel | aie |
| Video | [GPU Cloud Deployment Without Leaving Your IDE — Audry Hsu, RunPod](https://www.youtube.com/watch?v=zDGHt0LB-dA) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
