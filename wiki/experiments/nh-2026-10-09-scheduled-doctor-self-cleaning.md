# Schedule a monthly self-cleaning agent audit that proposes CLAUDE.md changes for human approval

> Back to [[experiments-index]]

Source: **[Anthropic Engineers Just 10x'd Everyone's Claude Code](https://www.youtube.com/watch?v=oz2CwrPV2Rg)** · nh · 2026-10-09

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we automate a monthly /doctor + audit-prompt run that outputs a diff of recommended instruction changes for human review, then our AI operating system will stay current with model upgrades without manual drift because human consistency (forgetting to update rules) is the primary failure mode in long-lived agent setups.

## What they did

Nate described scheduling local tasks that run /doctor and workflow audits on a cadence, waking up to approve or deny recommendations. He framed this as a self-improving, self-cleaning AI OS where the agent helps maintain its own instruction files. He noted that on every new model release, a fresh audit is warranted because each model interprets settings differently. He also discussed scaling this pattern to teams to prevent duplicated work across individual AI operating systems.

## Relevance to YOLO loop

Closes the maintenance loop in YOLO: automate the audit step so instruction debt doesn't accumulate between model upgrades.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-09 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-10-09-scheduled-doctor-self-cleaning` |
| Channel | nh |
| Video | [Anthropic Engineers Just 10x'd Everyone's Claude Code](https://www.youtube.com/watch?v=oz2CwrPV2Rg) |
| Published | 2026-10-09 |
| Ingested upstream | 2026-10-09 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
