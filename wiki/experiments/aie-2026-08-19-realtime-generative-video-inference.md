# Serve Distilled Video Generation Models in Streaming Pipelines for Real-Time Interactive Applications

> Back to [[experiments-index]]

Source: **[Generative Video at the Speed of Light — Keegan McCallum, uRun](https://www.youtube.com/watch?v=Xln-On3syJk)** · aie · 2026-08-19

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we serve distilled video generation models (e.g. distills of 14B-class models) through WebRTC-based streaming pipelines with asynchronous generation, then we can deliver continuous real-time generative video at roughly 1/100th the cost of frontier models, because distillation preserves sufficient quality while dramatically reducing compute, and streaming pipelines decouple generation speed from consumption speed.

## What they did

uRun built an inference platform for interactive generative video. They serve Helios (a distill of Wan 2.1 14B) and other efficient video models. Key findings: $10 buys ~3 hours of continuous generated video with current models; $50 gives 15 hours. They observed 40+ models with real-time or long-horizon generation capabilities released in the past year. Their platform handles GPU routing globally, WebRTC/ICE/TURN setup, and multi-model streaming pipeline composition. They offer a React component for video interactivity and a Python runtime for building complex async generation pipelines, plus a CLI/MCP server interface for agent-driven video generation.

## Relevance to YOLO loop

If our dev loop involves any visual or multimodal agent outputs, this represents a rapidly cheapening modality worth evaluating. The MCP server interface for generative video is directly relevant if we want agents to produce or steer video as part of their action space.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-19 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-19-realtime-generative-video-inference` |
| Channel | aie |
| Video | [Generative Video at the Speed of Light — Keegan McCallum, uRun](https://www.youtube.com/watch?v=Xln-On3syJk) |
| Published | 2026-08-19 |
| Ingested upstream | 2026-08-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
