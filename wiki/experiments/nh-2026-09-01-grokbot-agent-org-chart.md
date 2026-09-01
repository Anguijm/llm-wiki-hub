# Implement an org-chart agent hierarchy with executive routing bots

> Back to [[experiments-index]]

Source: **[Every Grok Bot Concept Explained for Normal People](https://www.youtube.com/watch?v=NyfYxpXiw_0)** · nh · 2026-09-01

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we structure a multi-agent system as an org chart where a small set of executive bots delegate to specialist bots based on descriptions, then task routing accuracy and maintainability will improve because descriptions act as capability contracts that scale without the user needing to track every specialist directly.

## What they did

Nate demonstrated his Grokbot ecosystem where each bot has a name, job title, and description that defines its specialty. Rather than the user talking to all bots directly (hub-and-spoke), he structured it as an org chart where executive bots know which specialists are on their teams and delegate accordingly. Key mechanics covered: bot descriptions as routing contracts, global vs. per-bot memory layers, shareable bot templates via link, scheduled routines, agent logging to external databases (ClickUp/Google Sheets), and phone notifications for async agent completion.

## Relevance to YOLO loop

Directly maps to YOLO loop multi-agent orchestration design. The description-as-capability-contract pattern and the agent logging recommendation (log every agent action to a structured store) are immediately implementable. The global vs. per-bot memory distinction informs context management architecture.

## Notes

Nate also covers: duplicate-bot pattern for resetting conversation history without losing skills/routines, hiding vs. deleting bots, and per-bot notification controls. The agent logging point — store every agent action in a structured DB — is an evergreen governance recommendation.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-01 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-09-01-grokbot-agent-org-chart` |
| Channel | nh |
| Video | [Every Grok Bot Concept Explained for Normal People](https://www.youtube.com/watch?v=NyfYxpXiw_0) |
| Published | 2026-09-01 |
| Ingested upstream | 2026-09-01 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
