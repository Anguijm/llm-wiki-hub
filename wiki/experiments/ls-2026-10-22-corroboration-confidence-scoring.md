# Add multi-source corroboration confidence scores to vault verify step

> Back to [[experiments-index]]

Source: **[The Recommendation Engine for Commodity Traders — Anekha Sokhal, Moshi](https://www.youtube.com/watch?v=DWHyPWnzGAI)** · ls · 2026-10-22

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we score each captured claim in the Markdown vault's verify stage by how many independent sources corroborate or contradict it, and surface only low-confidence items for human review, then newsletter errors will fall and review time will shrink because noisy single-source claims get flagged automatically instead of being read by hand.

## What they did

Sokhal described Moshi ingesting many noisy sources (news, podcasts, X posts, PDFs). It calculates confidence scores for diverging reports across outlets before pushing updates to traders. Public social streams are noisy and open to deliberate manipulation, so the system requires multi-source corroboration. It maps the data into a knowledge graph of second- and third-order dependencies and pushes proactive recommendation cards into the user's workflow rather than relying on a chat interface.

## Relevance to YOLO loop

medium: Corroboration scoring and proactive push of non-obvious findings could inform verification loops in agent workflows, but the video gives no concrete harness or Claude Code technique.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-24 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `ls-2026-10-22-corroboration-confidence-scoring` |
| Channel | ls |
| Video | [The Recommendation Engine for Commodity Traders — Anekha Sokhal, Moshi](https://www.youtube.com/watch?v=DWHyPWnzGAI) |
| Published | 2026-10-22 |
| Ingested upstream | 2026-10-24 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
