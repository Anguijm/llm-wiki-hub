# Add cold multi-persona review and dual extraction to the council

> Back to [[experiments-index]]

Source: **[I Believe Everything My Agents Tell Me: Three Levels of Review — Corey Gallon, Rexmore](https://www.youtube.com/watch?v=dYh7TQkuYFE)** · aie · 2026-10-13

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we add a self-audit stage, then cold reviewers with no conversation history (for example a skeptical auditor), then a fresh final verification, and use dual independent extraction with a reconciling third agent for source-data tasks, then more errors will be caught than by self-review because the reviewers do not share the drafter's context or blind spots.

## What they did

Corey Gallon described Level 2, where two agents extract the same source data independently and a third reconciles discrepancies against the primary source. He also described Level 3, an agent self-audit classifying claims, then multi-persona cold review without history or prior drafts, then fresh final verification. He reported that dual extraction on a year of scanned financial statements caught 56 discrepancies and balanced to the penny in 20 minutes for 7.5 million tokens. Two Level 3 reviews of memory leak pull requests took about 15 minutes and 6 million tokens. A cold review of a legal demand letter caught an active 3-year auto-renewal clause in 15 minutes for 13 million tokens. He cautioned that drafting agents routinely confirm their own errors during self-review.

## Relevance to YOLO loop

high: It extends the council and verification-loop pattern with cold, history-free reviewers and independent reconciliation, which can be tried on yolo outputs.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-19 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-13-cold-persona-adversarial-review` |
| Channel | aie |
| Video | [I Believe Everything My Agents Tell Me: Three Levels of Review — Corey Gallon, Rexmore](https://www.youtube.com/watch?v=dYh7TQkuYFE) |
| Published | 2026-10-13 |
| Ingested upstream | 2026-10-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
