# Implement a deterministic review-debt score on every AI-generated PR

> Back to [[experiments-index]]

Source: **[ReviewDebt: a practical framework for scoring every pull request — Sachin Gupta, Ebay](https://www.youtube.com/watch?v=TJPInBjhE4Q)** · aie · 2026-07-12

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we compute a deterministic review-debt score (using five signal families: size/coupling, test-evidence gap, ownership spread, AI-authorship indicators, and rationale gaps) on every PR and post it as a comment, then we will make the compounding gap between AI-generated code and human-understood code visible and actionable before it causes incidents, because the score is traceable to fixed rules rather than LLM judgment, making it defensible in engineering reviews.

## What they did

Sachin Gupta presented data showing that AI adoption has caused PR commits to rise 25% YoY while review comments dropped 27%, median PR review time increased 441.5%, and 31% more PRs are merged with no review. He defined 'review debt' as the compounding gap between code agents produce and code humans have actually reviewed and understood. His framework scores PRs using 10 deterministic checks across five signal families (no LLM-as-judge, to keep scores stable and defensible). Adoption steps: (1) backfill score over last 200 merged PRs, (2) set a threshold (e.g. 50) requiring author comment, (3) post score as PR comment for visibility without blocking, (4) aggregate weekly per team as a leading indicator, (5) discuss the number in retros. He also named anti-patterns: 'approve with comment', 'we'll catch it in QA', 'PRs are smaller now', and LGTM culture.

## Relevance to YOLO loop

As we use Claude Code to generate PRs, this scorer is a direct quality-gate addition to our CI pipeline. The five signal families are implementable as a GitHub Action or pre-merge script, giving us the first quantitative handle on whether AI-generated code is being meaningfully reviewed.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-12 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-12-review-debt-scorer` |
| Channel | aie |
| Video | [ReviewDebt: a practical framework for scoring every pull request — Sachin Gupta, Ebay](https://www.youtube.com/watch?v=TJPInBjhE4Q) |
| Published | 2026-07-12 |
| Ingested upstream | 2026-07-12 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
