# Attach a provenance ledger to every AI-produced data point tracking its source, derivation, and company-specific transformation

> Back to [[experiments-index]]

Source: **[How Kepler Built Verifiable AI for Financial Services — Vinoo Ganesh](https://www.youtube.com/watch?v=Tt2kX2sgQio)** · aie · 2026-07-29

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we track the full provenance chain for every number or claim an AI agent produces (source document, mathematical derivation, internal policy applied), then AI outputs become auditable and trustworthy enough for downstream decision-making because the work product itself becomes the proof rather than relying on post-hoc citation lists.

## What they did

Kepler built verifiable AI for financial services by recording provenance for every data point: whether it came from extracted filing text, a mathematical ratio calculation, or an internal document. Any time the model triggers an IO operation, that is logged in the provenance chain. This shifts AI from a search/citation tool to one that can produce auditable work product like DCFs, fairness opinions, and investment memos that satisfy SEC/OCC audit requirements.

## Relevance to YOLO loop

Applying provenance tracking to agent tool calls in the YOLO loop would make it possible to audit why the agent made a particular code change or decision, surfacing the exact context and rules it acted on.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-29 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-29-verifiable-provenance-chain` |
| Channel | aie |
| Video | [How Kepler Built Verifiable AI for Financial Services — Vinoo Ganesh](https://www.youtube.com/watch?v=Tt2kX2sgQio) |
| Published | 2026-07-29 |
| Ingested upstream | 2026-07-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
