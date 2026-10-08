# Measure Software Factory Outcomes With Signal-to-Production Time and Cost-per-PR Instead of Token Usage

> Back to [[experiments-index]]

Source: **[The Software Factory: From Bug Report to Production Code — Davis Palmie, Factory](https://www.youtube.com/watch?v=exiwa9QbQXI)** · aie · 2026-10-08

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we replace token-usage KPIs with outcome-based metrics (signal-to-production time, human intervention count, median time to repair, code shelf life, cost per PR), then we will avoid Goodhart's Law token-maximization behavior and get a true picture of agent leverage in our dev loop, because token count is gameable and not correlated with user-facing value.

## What they did

Davis Palmie from Factory described a 'software factory' model where agents handle the full SDLC (triage, planning, coding, review, testing, deployment, monitoring). He emphasized starting narrow (e.g. incident triage only, posting Sentry alerts to Slack for human review) and expanding trust incrementally per pillar. He argued coding was never the bottleneck — median PR review time, time to reproduce bugs, doc staleness, and deploy pipeline duration dwarf the actual coding time. He proposed measuring: signal-to-production time, human intervention count, median time to repair (MTTR), shelf life of code, and cost per PR. He explicitly warned against token leaderboards as Goodhart's Law in real time. Factory's agent-readiness framework has 8 pillars: validation (linters), build system docs, feedback loops (tests), docs (READMEs, agents.md), reproducible dev environments, modular code, observability, and security scanning.

## Relevance to YOLO loop

We should instrument our YOLO loop with these five outcome metrics immediately. The agent-readiness 8-pillar checklist is also a direct audit we can run against our repo today.

## Notes

Factory's 8 agent-readiness pillars: validation, build system, feedback loops, docs, reproducible environments, modularity, observability, security scanning. Start with incident triage as the first narrow pillar before enabling full pipeline loop.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-08 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-08-software-factory-incremental-agent-trust` |
| Channel | aie |
| Video | [The Software Factory: From Bug Report to Production Code — Davis Palmie, Factory](https://www.youtube.com/watch?v=exiwa9QbQXI) |
| Published | 2026-10-08 |
| Ingested upstream | 2026-10-08 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
