# Replace LLM-as-judge quality-control checks with Jev binary/multi-choice classifiers to eliminate hallucinated verdicts and compounding judge errors

> Back to [[experiments-index]]

Source: **[Jev Fully Explained: 10 Practical Ways to Use It](https://www.youtube.com/watch?v=zZNm4zP_lEE)** · mk · 2026-09-19

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we substitute LLM judge calls (used to verify that an upstream LLM response fits a predefined category) with Jev classifiers that enforce a fixed solution space, then we eliminate hallucinated judge verdicts and compounding multi-judge errors because Jev can only select from the predefined options and outputs a transparent confidence score rather than generating free-form tokens.

## What they did

Mark explained Jev's architecture as a generalized classifier that accepts a question plus a predefined solution space and returns a choice plus confidence score with no output token generation. He identified a specific high-value use case: replacing LLM-as-judge in commercial pipelines (contract review, proposal generation, intelligence analysis) where a judge LLM verifying another LLM's output can itself hallucinate, creating compounding errors across chains. With Jev, the judge step becomes a structured classification: e.g., 'is this contract ready for review / final QA / send to client?' with confidence scores. He also outlined browser-use acceleration (Jev answers 'is there a downloads button? yes/no' instead of an LLM taking a screenshot and reasoning over the whole page), healthcare triage (classify whether a patient conversation item warrants attention), and finance alert routing (ignore/review/watchlist). He provided cost math: 10k input tokens per request = $0.0042; 100k requests = $42.

## Relevance to YOLO loop

High relevance: any YOLO loop node that currently uses an LLM to validate/route the output of another LLM is a candidate for Jev replacement — faster, cheaper, no hallucinated verdicts, transparent confidence scores enable threshold-based branching logic.

## Notes

Mark is sharing a live demo site with $7 of credits (first-come-first-served) plus an API guide in the video description. Three question types: binary (null), multiple-choice (choice), scored rubric (score). Output tokens are free.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-19 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mk-2026-09-19-jev-llm-judge-replacement` |
| Channel | mk |
| Video | [Jev Fully Explained: 10 Practical Ways to Use It](https://www.youtube.com/watch?v=zZNm4zP_lEE) |
| Published | 2026-09-19 |
| Ingested upstream | 2026-09-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
