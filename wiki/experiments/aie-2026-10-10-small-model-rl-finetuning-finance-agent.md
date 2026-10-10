# Fine-tune a 4B parameter model with RL on domain-specific tool-use data to outperform large generalist models

> Back to [[experiments-index]]

Source: **[Small Models, Big Results: Training a Finance Agent for Under $500 — Charles Dickens, Snorkel AI](https://www.youtube.com/watch?v=TyPpSRXGhbc)** · aie · 2026-10-10

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we apply RL fine-tuning to a small (4B parameter) model using high-quality, expert-verified domain data with a simple binary reward signal, then it can match or exceed a 235B generalist model on specialized tasks, because the bottleneck in specialized workflows is reliable tool use rather than raw reasoning depth, and quality domain data with a clean reward signal is sufficient to close the gap.

## What they did

Snorkel AI and UC Berkeley Sky Lab built the RLLM-FinQA-4B model: a Qwen 4B trained with RL on ~4,000 expert-verified financial Q&A pairs derived from 10-K SEC filings. The pipeline used Qwen-3-30B to generate SQL tables from 10-K reports, produced one Q&A pair per table with financial expert taxonomy guidance, then applied a three-layer verification (programmatic checks, independent agent review, expert manual review). RL training used a single binary reward signal (correct/incorrect final answer). The 4B model achieved ~60% pass@1 vs. 51% for the 235B variant. Ablation showed training on simpler single-table data outperformed multi-table curriculum. General tool-use benchmarks (BFCL) were not degraded. Total training cost was under $500.

## Relevance to YOLO loop

Directly applicable if our loop has a recurring specialized agent task (e.g., code review scoring, bug triage, specific API tool use). Rather than routing every call to a frontier model, we could fine-tune a small model cheaply for that task, reducing per-call cost and latency while maintaining quality.

## Notes

Open-source training scripts, synthetic data, and model available on Snorkel AI GitHub.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-10 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-10-small-model-rl-finetuning-finance-agent` |
| Channel | aie |
| Video | [Small Models, Big Results: Training a Finance Agent for Under $500 — Charles Dickens, Snorkel AI](https://www.youtube.com/watch?v=TyPpSRXGhbc) |
| Published | 2026-10-10 |
| Ingested upstream | 2026-10-10 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
