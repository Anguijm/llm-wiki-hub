# Audit shared-GPU deployments for timing side-channel leakage of model identity and workload type

> Back to [[experiments-index]]

Source: **[Your GPU Neighbor Can Hear Your Model — Branislav Brzak, Stealthium](https://www.youtube.com/watch?v=SacJfmp33vM)** · aie · 2026-10-13

**Status:** `discarded` · **Verdict:** `discard` · **Effort:** `medium`

---

## Hypothesis

If we measure memory-barrier timing variance on our shared GPU infrastructure, then we will detect whether a co-tenant can fingerprint our model architecture (layer count), decode speed, and workload category, because Stealthium demonstrated 97% model-identification accuracy and 99.3% decode-speed accuracy on real H100s using only timing—no special permissions required.

## What they did

Branislav Brzak demonstrated a timing side-channel attack on MIG-partitioned H100 GPUs. An attacker on one MIG slice polls its own memory read latency every 5µs; GPU-wide memory barriers leak timing that correlates with the victim's token generation pattern. From this signal alone the attacker can identify: model architecture/layer count (97% accuracy via peak-counting), decode speed (99.3%), busy periods, token count, and answer length. Workload category (code vs. prose vs. JSON) is also recoverable with speculative decoding enabled. The attack requires no root, no exploit, just timing of shared hardware. Stealthium's monitoring product detected it in under 600ms by flagging a kernel re-run 3,000 times against the same 40KB of memory.

## Relevance to YOLO loop

If we run proprietary models on shared cloud GPU infrastructure, our model identity and usage patterns are potentially visible to co-tenants. We should audit our deployment topology and add kernel-behavior monitoring.

## Notes

Mitigations: (1) don't place untrusted MIG slices adjacent to sensitive models; (2) prefer NVLink tensor-parallel setups which leak only timing (not layer counts); (3) monitor GPU kernel behavior for repeated small-range memory access patterns. Attack surface is wider with speculative decoding enabled (VLLM non-default option).

Backlog triage 2026-10-17 round 3 (operator: "I want you to evaluate the yolo cards"). Settled maybe, cut: Assessment: an attack on shared NVIDIA H100 slices; he is single-tenant on AMD.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-13 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-13-gpu-timing-side-channel-shared-tenancy` |
| Channel | aie |
| Video | [Your GPU Neighbor Can Hear Your Model — Branislav Brzak, Stealthium](https://www.youtube.com/watch?v=SacJfmp33vM) |
| Published | 2026-10-13 |
| Ingested upstream | 2026-10-13 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
