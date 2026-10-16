# Apply a three-check diligence card to any AI automation claim before trusting the metric

> Back to [[experiments-index]]

Source: **[What Technical Due Diligence Finds When the Deck Says "70% Automated" — Soukaïna Abelhad](https://www.youtube.com/watch?v=gDRCpTMCqEU)** · aie · 2026-10-15

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we apply three structured checks—arithmetic (workload volume vs. fully loaded human labor), definition (AI-attributed vs. straight-through autonomous rate within a named boundary), and evaluation maturity (expert-validated ground truth, escape rate)—then misleading automation metrics will be caught before influencing build or investment decisions, because each check targets a distinct failure mode where genuine measurements are carried into conclusions they cannot support.

## What they did

Soukaïna Abelhad outlined three diligence checks for AI automation claims: (1) Arithmetic—compare workload volume to fully loaded human labor including operators, reviewers, trainers, and rework staff; if human labor tracks volume, the system is assistance not replacement. (2) Definition—distinguish 'AI attributed' from 'autonomous straight-through processing' within an explicitly named workflow boundary (draft, PR approval, or production deploy). (3) Evaluation maturity—ask who labeled ground truth, whether domain experts agree with automated graders, and what bad output escaped; she cited a Meta study showing a 24-point gap between automated grader and human maintainer merge decisions on 296 AI-generated PRs. She also recommended translating surviving claims into unit economics: cost per accepted autonomous task, subtracting AI cost, human review, escalation, and rework.

## Relevance to YOLO loop

Directly applicable when evaluating whether an agent step in the YOLO loop is genuinely autonomous vs. human-assisted. The straight-through rate definition and cost-per-accepted-task metric can be instrumented as part of loop telemetry.

## Notes

Speaker provides a printable reference card via QR code in the talk. The builder.ai case is used as a warning: automation claims that survive narrative scrutiny still need to survive unit economics before deployment decisions.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-15-ai-automation-due-diligence-checks` |
| Channel | aie |
| Video | [What Technical Due Diligence Finds When the Deck Says "70% Automated" — Soukaïna Abelhad](https://www.youtube.com/watch?v=gDRCpTMCqEU) |
| Published | 2026-10-15 |
| Ingested upstream | 2026-10-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
