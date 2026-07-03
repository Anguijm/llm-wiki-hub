# Build a reusable 9-step agent skeleton for high-trust paperwork processing

> Back to [[experiments-index]]

Source: **[Every AI Agent Demo Stops at Email. I Pointed Mine at the Bills That Cost You Money.](https://www.youtube.com/watch?v=U4TmrlWEY4M)** · nb · 2026-07-03

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we implement a single agent skeleton with context-pack, ingest, chunk, normalize, store, retrieve, cite, export, and gate steps, then the same architecture can handle progressively higher-stakes domains (email → insurance appeals → tax prep) with decreasing marginal build effort because the core data-cleaning and gating logic is reusable across domains.

## What they did

The speaker built three agents live against the same underlying skeleton: (1) email/calendar triage, (2) insurance appeal drafting, and (3) tax document organization. Each agent ingests unstructured files, normalizes entities (dates become dates, people become people), chunks by category, stores with citations, and exports a human-reviewable packet. A hard gate prevents the agent from submitting, paying, or signing anything — that step is always reserved for the human. He emphasized that clean normalized data allows cheaper/smaller models to do the heavy lifting, and that each build makes the next cheaper because the skeleton is reused.

## Relevance to YOLO loop

Directly maps to the YOLO loop's need for a reliable context-engineering layer before any agentic action. The gate pattern (agent prepares, human approves) is a core safety primitive we should standardize in our own loop. The normalize-before-inference principle reduces model cost for repeated tasks.

## Notes

Speaker references a Substack post with healthcare appeals and tax prep runbooks plus two open skills. The citation guard (no deduction without a source file pointer) is worth adopting as a pattern in any retrieval agent.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-03 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-07-03-paperwork-agent-skeleton` |
| Channel | nb |
| Video | [Every AI Agent Demo Stops at Email. I Pointed Mine at the Bills That Cost You Money.](https://www.youtube.com/watch?v=U4TmrlWEY4M) |
| Published | 2026-07-03 |
| Ingested upstream | 2026-07-03 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
