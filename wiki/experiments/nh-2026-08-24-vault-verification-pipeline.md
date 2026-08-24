# Add a pre-flight verification prompt that cites sources and flags low-confidence claims

> Back to [[experiments-index]]

Source: **[Everything Goldman Sachs Taught Me About AI (In 10 minutes)](https://www.youtube.com/watch?v=ZzHsJW10iq4)** · nh · 2026-08-24

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we append a verification instruction to high-stakes LLM prompts asking the model to recheck every number, cite each factual claim, and flag uncertain outputs before returning a final answer, then we will catch more hallucinations before they reach downstream steps because the model is forced to run an internal audit pass rather than confidently presenting a first-draft answer.

## What they did

Herk described baking verification directly into prompts using language like 'before you give me the final answer, recheck every number and factual claim, cite the source for each one, and flag anything you are not fully confident about.' He also recommended using a separate AI reviewer agent that checks the first output before the human sees anything, and noted that for reports only the two or three numbers that could actually change a decision need manual spot-checking.

## Relevance to YOLO loop

Directly applies to any LLM call in the YOLO loop that produces factual output, code review summaries, or data reports; the verification prompt can be injected as a system-level wrapper around existing generation steps.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-24 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-08-24-vault-verification-pipeline` |
| Channel | nh |
| Video | [Everything Goldman Sachs Taught Me About AI (In 10 minutes)](https://www.youtube.com/watch?v=ZzHsJW10iq4) |
| Published | 2026-08-24 |
| Ingested upstream | 2026-08-24 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
