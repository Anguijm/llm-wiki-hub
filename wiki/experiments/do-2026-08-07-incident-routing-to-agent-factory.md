# Route Uptime Incidents Directly Into Agent for Triage and PR Generation

> Back to [[experiments-index]]

Source: **[Ex-NASA dev reveals his Agentic Engineering Workflow](https://www.youtube.com/watch?v=xgkjtF89-44)** · do · 2026-08-07

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we pipe monitoring alerts directly into an agent that produces an incident triage report and optionally a fix PR, then on-call toil will decrease because the agent handles initial diagnosis and response drafting, leaving humans to approve rather than investigate from scratch.

## What they did

Dex described routing production incidents straight into the software factory so that instead of waking up to a raw alert at 3am, the engineer wakes up to a pull request. David Ondrej confirmed he is implementing this: he uses GLM 5.2 to review every uptime incident automatically, producing a structured report (e.g., 'this is a provider outage, no action needed' vs. 'here is the bug'). This closes the monitoring → fix loop without requiring human triage as the first step.

## Relevance to YOLO loop

Extends the YOLO loop backwards into the operational feedback cycle. If incidents auto-generate PRs, the loop becomes self-healing and the human role shifts to PR approval, which is a much lower-friction intervention point than raw log triage.

## Notes

Start small: route a single low-stakes alert type (e.g., uptime checks) to an agent that produces a plain-language summary. Measure time-to-triage before and after.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-07 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-08-07-incident-routing-to-agent-factory` |
| Channel | do |
| Video | [Ex-NASA dev reveals his Agentic Engineering Workflow](https://www.youtube.com/watch?v=xgkjtF89-44) |
| Published | 2026-08-07 |
| Ingested upstream | 2026-08-07 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
