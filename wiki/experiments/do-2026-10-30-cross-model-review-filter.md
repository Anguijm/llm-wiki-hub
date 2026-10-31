# Add cross-model PR review with primary-model false-positive filter

> Back to [[experiments-index]]

Source: **[High-Level Agentic Engineering with David Ondrej](https://www.youtube.com/watch?v=F8rc-ULd4_4)** · do · 2026-10-30

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we have a second frontier model score each PR's issues by severity and likelihood and then send the findings back to the primary model to filter out overthinking, then fewer real bugs will reach production without a flood of false positives because the two models have different blind spots and the filter pass removes hallucinated issues.

## What they did

David Ondrej runs a 'GPT review' where an alternate frontier model audits changes and scores issues on a 1-to-10 severity and likelihood matrix. The findings go back to the primary model (Opus 5.5) to drop overthinking and false-positive bugs before pushing to production. He warns that repeated adversarial review makes models hallucinate non-existent bugs.

## Relevance to YOLO loop

high: Adds a cross-model review and filter stage to Claude Code verification loops and councils.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-30 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-10-30-cross-model-review-filter` |
| Channel | do |
| Video | [High-Level Agentic Engineering with David Ondrej](https://www.youtube.com/watch?v=F8rc-ULd4_4) |
| Published | 2026-10-30 |
| Ingested upstream | 2026-10-30 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
