# Build a pre-LLM PII scrubber that rebuilds a clean doc before upload

> Back to [[experiments-index]]

Source: **[How to Use AI on Files You're Not Allowed to Upload](https://www.youtube.com/watch?v=EuVvLwWZ5wc)** · nb · 2026-07-24

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we intercept files before they reach a frontier model and rebuild only the semantically necessary content into a new document (rather than redacting in place), then we reduce accidental PII/credential leakage while preserving task utility because bundled sensitive data is stripped at the file-construction stage rather than relying on user memory.

## What they did

Built 'Airlock': user defines protected terms plus auto-detected PII patterns, tool surfaces every candidate item with a default-hide stance, user explicitly opts in to keep only task-relevant facts, then the tool rebuilds a brand-new Word document containing only approved content. The original file never leaves the local machine. Demonstrated on a synthetic pricing/ops plan: stripped home address, email, medical note, API key, and unreleased price; kept warehouse migration schedule, ERP readiness assumption, and training-shift constraint. Passed the clean doc to a frontier model to identify load-bearing assumptions.

## Relevance to YOLO loop

Any skill or agent in the YOLO loop that ingests user-provided files (contracts, specs, PRDs) risks uploading bundled credentials or PII. Adding an Airlock-style pre-processing step before the file hits Claude/Codex enforces least-privilege context and reduces compliance risk in production pipelines.

## Notes

Key insight from transcript: redaction is easy if you don't care whether the model can still help; the hard part is meaning-making—which facts make the task solvable vs. which just came along for the ride. Rebuild approach (new file) preferred over black-rectangle redaction because Word containers leak metadata in track changes, author names, and external relationships.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-24 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-07-24-airlock-pii-scrub-before-llm` |
| Channel | nb |
| Video | [How to Use AI on Files You're Not Allowed to Upload](https://www.youtube.com/watch?v=EuVvLwWZ5wc) |
| Published | 2026-07-24 |
| Ingested upstream | 2026-07-24 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
