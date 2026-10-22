# Add a PR comprehension quiz CI gate

> Back to [[experiments-index]]

Source: **[How this skill helps me to understand AI code](https://www.youtube.com/watch?v=5sz5YywkMcE)** · pl · 2026-10-21

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we add a Claude skill that appends a multiple-choice quiz to AI-authored PR descriptions and a GitHub Actions check that blocks merge until the answers match, then reviewers will engage with architectural changes instead of skimming because merge is gated on demonstrated comprehension.

## What they did

Philipp Lackner built a custom Claude coding skill that summarizes a diff and appends a 7-question multiple-choice quiz to the PR description. The answer key is stored as Base64-encoded JSON in a hidden PR comment. A GitHub Actions workflow triggered on PR open, edit, synchronize and comment events runs an embedded JavaScript script that compares the reviewer's checked boxes to the decoded key and passes or fails the status check. New commits uncheck recorded answers. He demonstrated question 7 answered B failing the check and A passing it. He noted the check can be bypassed by pasting the quiz and diff into an external LLM, and that new commits do not regenerate questions unless the skill is re-run.

## Relevance to YOLO loop

high: This is a skill plus CI verification loop that enforces human accountability for agent-written code, which is core Claude Code workflow practice.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-21 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `pl-2026-10-21-pr-comprehension-quiz-gate` |
| Channel | pl |
| Video | [How this skill helps me to understand AI code](https://www.youtube.com/watch?v=5sz5YywkMcE) |
| Published | 2026-10-21 |
| Ingested upstream | 2026-10-21 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
