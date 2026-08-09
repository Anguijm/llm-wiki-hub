# Deploy a Persistent On-Call Agent That Triages Alerts and Performs Root Cause Analysis

> Back to [[experiments-index]]

Source: **[Always-on agents run production without the on-call tax — Justin Smith, Resolve AI](https://www.youtube.com/watch?v=vSx5IULvBns)** · aie · 2026-08-09

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If an always-on AI agent automatically triages every production alert, performs root cause investigation, and surfaces findings in Slack before any human is paged, then on-call engineer burden will decrease because engineers receive pre-diagnosed incidents rather than raw alerts requiring full context reconstruction.

## What they did

Justin Smith from Resolve AI described their on-call agent that runs for every incoming alert: it performs triage, root cause investigation, and posts findings to Slack. The agent understands the organization's environment via a knowledge system built from runbooks, past incidents, and system topology. It also handles cross-team incident coordination, keeping all stakeholders aligned on impact and status. A passive background variant watches Slack channels and responds to questions only when it judges it has relevant answers—without requiring explicit @mention.

## Relevance to YOLO loop

Relevant to post-deploy monitoring in the YOLO loop—an always-on agent that watches production and flags regressions introduced by AI-generated code closes the feedback loop from deploy back to the next loop iteration with actionable diagnostics rather than raw alerts.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-09 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-09-always-on-oncall-agent` |
| Channel | aie |
| Video | [Always-on agents run production without the on-call tax — Justin Smith, Resolve AI](https://www.youtube.com/watch?v=vSx5IULvBns) |
| Published | 2026-08-09 |
| Ingested upstream | 2026-08-09 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
