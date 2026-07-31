# Use domain data analysis pipelines as verifiable RL substrates in non-code domains

> Back to [[experiments-index]]

Source: **[Verifiable Environments for AI in Biology — Kenny Workman, LatchBio](https://www.youtube.com/watch?v=3ZMUiFaQ3qg)** · aie · 2026-07-31

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we frame domain-specific data analysis tasks (e.g., bioinformatics pipelines) as verifiable environments analogous to code execution, then we can apply RL and benchmarking techniques from software engineering to domains previously considered unverifiable, because data analysis produces executable, checkable outputs.

## What they did

LatchBio built benchmarks for biological data analysis (spatial genomics, single-cell, epigenomics) by treating analysis pipelines as executable substrates. Just as code can be run and verified, data analysis scripts produce checkable outputs. They identified invariant 'choke points' in analysis trees—intermediate results that all valid solution paths must pass through—and used these to build rubrics for RL and benchmarking. Their benchmarks were organically adopted by Anthropic and others and now appear in model cards.

## Relevance to YOLO loop

The pattern of identifying invariant choke points in complex task trees to construct partial verifiers is generalizable. For any domain where full end-to-end verification is hard, mapping the solution space and finding intermediate verifiable nodes is a tractable path to RL reward design.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-31 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-31-biology-data-analysis-verifiable-substrate` |
| Channel | aie |
| Video | [Verifiable Environments for AI in Biology — Kenny Workman, LatchBio](https://www.youtube.com/watch?v=3ZMUiFaQ3qg) |
| Published | 2026-07-31 |
| Ingested upstream | 2026-07-31 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
