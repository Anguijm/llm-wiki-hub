# Use LangSmith's Align Evaluators and full-text trace search to accelerate agent quality assessment

> Back to [[experiments-index]]

Source: **[Vanta and LangSmith: Assessing Compliance Evidence Like an Auditor](https://www.youtube.com/watch?v=_MsL_RIztVc)** · lc · 2026-10-15

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we use LangSmith's Align Evaluators feature to force explicit good/bad ground-truth labeling and use full-text trace search with metadata filters, then agent evaluation workflow speed will increase significantly (reported 10x) because the tooling removes the friction of hunting through traces and makes labeling opinions concrete.

## What they did

A Vanta engineer described building a compliance-evidence assessment agent and using LangSmith for observability. They highlighted two features: flexible full-text trace search with metadata fields (replacing 10-minute manual hunts), and the Align Evaluators feature which forces the developer to label ground truth as good or bad before setting up evaluators, making the eval loop faster.

## Relevance to YOLO loop

high: Align Evaluators and trace search are directly applicable to building verification loops for Claude Code agent workflows—forces explicit ground-truth labeling which is the hardest part of agent evals.

## Notes

Short testimonial video. Key insight: 'it forces you to have an opinion and label your ground truth like good or bad'—a simple but powerful constraint for building eval datasets.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `lc-2026-10-15-vanta-langsmith-compliance` |
| Channel | lc |
| Video | [Vanta and LangSmith: Assessing Compliance Evidence Like an Auditor](https://www.youtube.com/watch?v=_MsL_RIztVc) |
| Published | 2026-10-15 |
| Ingested upstream | 2026-10-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
