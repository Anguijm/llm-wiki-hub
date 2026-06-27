# Run private home inference at 374M tokens/month using compressed open-weight models for agentic workloads

> Back to [[experiments-index]]

Source: **["I spent $50,000 self-hosting AI models. You should too." - 0xSero](https://www.youtube.com/watch?v=ImPESBftwr8)** · do · 2026-06-26

**Status:** `discarded` · **Verdict:** `discard` · **Effort:** `high`

---

## Hypothesis

If we self-host compressed open-weight models (e.g., GLM-5.2 at 80% compression, DeepSeek-V4-Flash) on local hardware, then we can sustain frontier-comparable agentic performance at high token volumes for a fixed hardware cost because the per-token marginal cost drops to near zero after the capital expenditure.

## What they did

0xSero demonstrated a home inference setup running GLM-5.2 (custom 80% compression) and DeepSeek-V4-Flash with concurrent sessions, achieving 374 million tokens per month locally. He described GLM as particularly strong for agent work, Docker/DevOps, GPU programming, MLOps, and long reverse-engineering tasks (8+ hour runs). He also visited a German lab (Micro AGI) running Unitree robots + DGX Spark ($4K) + Meta VR headsets for ~$30K total, using Gemma 4 4B for robot control decisions. He emphasized that the cost structure changes fundamentally once you own the hardware and that model compression is the key enabler for running large models on consumer hardware.

## Relevance to YOLO loop

High token volume agentic loops (code review, multi-file editing, long context reasoning) become economically viable at scale if inference is self-hosted. The compression technique (80% reduction while preserving agent capability) is directly applicable to making the YOLO loop cost-sustainable for extended autonomous runs.

## Notes

Guest is @0xSero on Twitter, described as top voice on local/open-source models. Key claim: GLM series is best for agent work specifically. Worth benchmarking GLM-5.2 vs Claude on YOLO loop coding tasks before committing to hardware investment.

Backlog triage 2026-06-27 (owner-preference model). Self-hosted home inference on compressed open weights — consistent local/self-host NO; wrong hardware.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-26 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-06-26-private-inference-374m-tokens` |
| Channel | do |
| Video | ["I spent $50,000 self-hosting AI models. You should too." - 0xSero](https://www.youtube.com/watch?v=ImPESBftwr8) |
| Published | 2026-06-26 |
| Ingested upstream | 2026-06-26 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
