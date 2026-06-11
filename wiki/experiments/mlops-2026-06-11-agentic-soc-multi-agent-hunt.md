# Build a human-in-the-loop multi-agent pipeline using existing SOAR integrations rather than replacing them

> Back to [[experiments-index]]

Source: **[Architecting Modern AI Systems: Platforms, Agents, and Integration](https://www.youtube.com/watch?v=kDAlW3vRQzI)** · mlops · 2026-06-11

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we wrap existing SOAR/orchestration infrastructure with agent reasoning layers instead of replacing it, then we can deploy production-ready agentic workflows faster and with less risk because the 257 existing Python integrations provide proven tool coverage while agents add reasoning and planning on top.

## What they did

Salesforce security team described their agentic SOC built on top of an existing SOAR with 257 Python integrations. Rather than rebuilding, they taught agents to speak to the existing SOAR. The pipeline includes a normalizer agent (extract IoCs from threat intel reports), a hunt planning agent (propose a search plan), a human-approval step in Slack, parallel hunt execution agents, containment agents, and detection deployment agents. All agent actions are logged for audit. The entire config was written by Claude with no hand-written code from the builders.

## Relevance to YOLO loop

Pattern of wrapping existing tooling rather than replacing it is directly applicable: we can wrap our existing CI/CD, test runners, and deployment scripts with agent reasoning layers rather than rebuilding pipelines from scratch.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-06-11-agentic-soc-multi-agent-hunt` |
| Channel | mlops |
| Video | [Architecting Modern AI Systems: Platforms, Agents, and Integration](https://www.youtube.com/watch?v=kDAlW3vRQzI) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
