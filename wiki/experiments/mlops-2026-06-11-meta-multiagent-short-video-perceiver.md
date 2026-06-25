# Decompose content-understanding pipelines into specialized perceiver + attribution + decision agents with caching between stages

> Back to [[experiments-index]]

Source: **[Whats Special About Meta's Multi-Agent Systems](https://www.youtube.com/watch?v=psC2-iEvXCg)** · mlops · 2026-06-11

**Status:** `discarded` · **Verdict:** `discard` · **Effort:** `high`

---

## Hypothesis

If we decompose a complex content-understanding pipeline into a perceiver agent (granular multimodal understanding), a context/attribution agent (comparison against corpus), and a decision agent, then accuracy and cost-efficiency will both improve because each agent is scoped to a domain where it excels and expensive inference is only triggered when earlier cheaper stages flag a case as needing deeper analysis.

## What they did

Meta AI architect described a multi-agent system for short-form video policy enforcement at 100M–1B reads scale. A perceiver agent does granular video understanding across all modalities. A separate agent handles originality attribution by comparing against indexed content corpus using RAG and embeddings. A unified architecture handles both within-modality intrusion detection and original attribution because the problems share structure. Key optimizations: caching, skip-processing logic, smart token-length management, and right-sizing agent granularity (not too coarse to create contradictions, not too fine to over-complicate). Standalone LLMs were ruled out due to modality bias, context limitations, and prohibitive inference cost at scale.

## Relevance to YOLO loop

The perceiver-then-decide decomposition pattern and the skip-processing optimization are applicable to any multi-stage AI pipeline in our loop where we want to gate expensive model calls behind cheaper early-stage filters.

## Notes

Backlog triage 2026-06-24 (owner-preference model). Enterprise multimodal content pipeline — off-domain, high effort.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-06-11-meta-multiagent-short-video-perceiver` |
| Channel | mlops |
| Video | [Whats Special About Meta's Multi-Agent Systems](https://www.youtube.com/watch?v=psC2-iEvXCg) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
