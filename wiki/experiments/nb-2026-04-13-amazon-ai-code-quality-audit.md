# Audit AI-generated code for systemic failure patterns

> Back to [[experiments-index]]

Source: **[I Looked At Amazon After They Fired 16,000 Engineers. Their AI Broke Everything.](https://www.youtube.com/watch?v=E1idsrv79tI)** · nb · 2026-04-13

**Status:** `adopted` · **Verdict:** `adopt` · **Effort:** `medium`

---

## Hypothesis

If we run a structured audit pass over AI-generated code in our repo, then we will surface recurring failure patterns (e.g. hallucinated dependencies, shallow error handling, integration gaps) because large-scale AI code generation introduces consistent blind spots that accumulate silently.

## What they did

Speaker analyzed Amazon's post-layoff codebase and engineering output, arguing that replacing 16,000 engineers with AI tooling introduced systemic quality degradation — broken integrations, missing context, and compounding technical debt that AI could not self-correct.

## Relevance to YOLO loop

Directly relevant to the review and validation gate in the YOLO loop. If AI is generating code autonomously, we need a recurring audit step that checks for the failure modes Nate identifies — not just unit test pass rates but structural and integration health.

## Notes

See tick_queue_approved entry 'infra-ai-code-audit-lenses' in session_state.json.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-13 | `backlog` | Extracted from YouTube RSS |
| 2026-04-22 | `adopted` | Promoted to tick queue as infra-ai-code-audit-lenses. |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-04-13-amazon-ai-code-quality-audit` |
| Channel | nb |
| Video | [I Looked At Amazon After They Fired 16,000 Engineers. Their AI Broke Everything.](https://www.youtube.com/watch?v=E1idsrv79tI) |
| Published | 2026-04-13 |
| Ingested upstream | 2026-04-13 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
