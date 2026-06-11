# Stack DeepSpeed Ulysses + gradient checkpointing + U-Pipe chunked-head recompute for long-context fine-tuning

> Back to [[experiments-index]]

Source: **[Road to 5 Million Tokens: Breaking Barriers in Long Context Training — Max Ryabinin, Together AI](https://www.youtube.com/watch?v=TUnPNY4E2fw)** · aie · 2026-06-11

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we combine DeepSpeed Ulysses context parallelism, activation recomputation, and U-Pipe chunked-head attention recompute on a single 8×H100 node, then we can fine-tune a Llama 3B/8B model at 3–5M token context lengths without OOM, because each technique addresses a distinct memory bottleneck (parameter sharding, attention activation size, and buffer reuse respectively).

## What they did

Max Ryabinin from Together AI described their 'Road to 5M sequence length' research. Starting from a standard Llama 3B on 8×H100, they layered: (1) FSDP to shard parameters, (2) DeepSpeed Ulysses context parallelism to distribute multi-head attention across GPUs so each GPU handles only a subset of heads over the full sequence, (3) gradient checkpointing to recompute activations on the backward pass, and (4) their novel U-Pipe technique which further chunks attention head groups within a GPU, reusing allocated buffers across iterations to cut activation memory without significant throughput loss. At 8B and 32B scale they matched memory-optimized baselines while reaching 5M token contexts.

## Relevance to YOLO loop

Directly relevant if we need to fine-tune models on long-context agent trajectories or multi-turn histories. Establishes a concrete layered recipe for pushing context limits during training without buying more hardware.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-11-long-context-ulysses-upipe` |
| Channel | aie |
| Video | [Road to 5 Million Tokens: Breaking Barriers in Long Context Training — Max Ryabinin, Together AI](https://www.youtube.com/watch?v=TUnPNY4E2fw) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
