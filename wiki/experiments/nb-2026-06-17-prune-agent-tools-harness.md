# Audit and prune agent tool sets to improve reliability

> Back to [[experiments-index]]

Source: **[Don't build more AI agents until you watch this](https://www.youtube.com/watch?v=BOXK2XFLA-E)** · nb · 2026-06-17

**Status:** `adopted` · **Verdict:** `adopt` · **Effort:** `low`

---

## Hypothesis

If we systematically remove underused or redundant tools from an agent's harness rather than adding more, then the agent will produce more reliable and trustworthy outputs because fewer available tools reduces decision ambiguity and confabulation surface area.

## What they did

Nate described how Vercel improved a sales-qualified-lead agent by deleting 80% of its tools. The agent had been built around an observed top-performer workflow covering filtering, qualifying, researching, drafting, and routing. Over time the team discovered that piling on tools degraded performance; removing tools improved it. Nate framed this as a core maintenance principle: the beginner instinct is to add, the mature instinct is to ask what should be removed.

## Relevance to YOLO loop

Directly applicable to any agent in the YOLO loop that has accumulated tools over time. A periodic tool-audit step could be inserted as a harness health check before each sprint or model-version upgrade.

## Notes

Nate also recommends Stewart Brand's 'Maintenance of Everything' (Stripe Press) as a mental model for agent harness upkeep.

Backlog triage 2026-06-24 (owner-preference model). Prune tools for reliability — harness discipline (mirrors tool-deferral); cheap.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-17 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-06-17-prune-agent-tools-harness` |
| Channel | nb |
| Video | [Don't build more AI agents until you watch this](https://www.youtube.com/watch?v=BOXK2XFLA-E) |
| Published | 2026-06-17 |
| Ingested upstream | 2026-06-17 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
