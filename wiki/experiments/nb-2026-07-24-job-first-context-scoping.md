# Gate context selection on the job, not the file

> Back to [[experiments-index]]

Source: **[How to Use AI on Files You're Not Allowed to Upload](https://www.youtube.com/watch?v=EuVvLwWZ5wc)** · nb · 2026-07-24

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we force explicit statement of the task/question before deciding which file contents to include, then context sent to the model will be smaller and more relevant because the same data element (e.g., a price) is essential for one task and irrelevant for another, and anchoring on intent surfaces that distinction.

## What they did

Demonstrated that an unreleased price was irrelevant when the task was 'identify assumptions that could break this plan' but would be essential if the task were 'evaluate the pricing itself.' Used this to argue that the workflow must start with the job definition, not the file, to determine minimum viable context. Applied this principle throughout the Airlock UI: users state the task first, then review each candidate data element against that task.

## Relevance to YOLO loop

Skills and agent prompts in the YOLO loop often pass entire files or large context blobs. Inserting a job-definition step at skill entry points would allow the skill itself to filter or summarize input context to only what's needed, reducing token cost and hallucination surface.

## Notes

Low-effort to experiment with as a prompt pattern: prepend every file-ingesting skill with a structured 'task statement' block and instruct the model to explicitly list which sections it needs before proceeding.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-24 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-07-24-job-first-context-scoping` |
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
