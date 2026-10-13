# Benchmark agent compliance with non-gated MEMORY.md / CLAUDE.md instructions

> Back to [[experiments-index]]

Source: **[AAIF Reading Group: Measuring Agent Policy Compliance](https://www.youtube.com/watch?v=HglV1_EF7tA)** · mlops · 2026-10-13

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we systematically measure how often our agent follows non-gated instructions in configuration files (e.g., MEMORY.md, CLAUDE.md) using a strict pass/fail criterion, then we will surface the true compliance rate and identify which instruction categories fail most often, because the benchmark in this paper found a best-case compliance rate of only 36.2% under strict evaluation.

## What they did

Speakers from Centic and a freelance collaborator presented an AAIF reading group session on a benchmark paper measuring LLM agent compliance with long-context, non-gated policy instructions (SOPs) across five enterprise domains (finance, HR, insurance, logistics, medical billing). Domain experts wrote SOPs, tasks were derived from those SOPs with variations, and verifiers were created per variation. Results showed the highest strict-pass compliance was 36.2%, with logistics performing worst (72-page handbook). The session highlighted that strict compliance matters because a single failure erodes user trust.

## Relevance to YOLO loop

Directly tests whether the agent in our dev loop reliably follows the standing instructions we put in MEMORY.md / CLAUDE.md. A compliance audit would tell us which rules are silently ignored, informing where to add hooks or restructure instructions.

## Notes

Paper evaluated 5 domains; logistics (longest handbook at 72pp) performed worst. Strict vs. lenient pass distinction is important—use strict for trust-critical instructions.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-13 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-10-13-benchmark-agent-policy-compliance` |
| Channel | mlops |
| Video | [AAIF Reading Group: Measuring Agent Policy Compliance](https://www.youtube.com/watch?v=HglV1_EF7tA) |
| Published | 2026-10-13 |
| Ingested upstream | 2026-10-13 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
