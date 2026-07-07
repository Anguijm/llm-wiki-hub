# Build an explicit model routing table for dynamic multi-agent workflows

> Back to [[experiments-index]]

Source: **[How I Make Opus Think Like Fable (5 easy steps)](https://www.youtube.com/watch?v=XTBWVVcF3Pk)** · nh · 2026-07-07

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we give the orchestrator agent an explicit routing table listing available models with cost, intelligence, and taste scores, then the orchestrator will make better model-selection decisions for sub-agent tasks, reducing total token spend while maintaining output quality, because structured metadata about trade-offs enables deliberate allocation rather than defaulting to the most expensive model for every subtask.

## What they did

Nate described giving his Claude orchestrator a table of models in the toolkit with three scored dimensions: cost (higher = cheaper), intelligence (code review, comprehension), and taste (creativity, UI/UX, out-of-box thinking). He ran a concrete test where Opus orchestrated Haiku scouts for a multi-agent workflow and achieved ~3x cost reduction with equivalent output quality compared to using Opus workers throughout. He also noted that the same routing logic can include Codex, open-source models, and other providers.

## Relevance to YOLO loop

Direct drop-in enhancement for any multi-agent loop: add a routing table to the orchestrator context. Low implementation effort, measurable cost impact. Especially useful if our loop currently defaults all sub-tasks to a single model tier.

## Notes

Pairs naturally with the Fable-mode system prompt experiment above. Together they form an orchestrator upgrade: better reasoning process + smarter model selection.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-07 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-07-07-model-routing-table-agent-teams` |
| Channel | nh |
| Video | [How I Make Opus Think Like Fable (5 easy steps)](https://www.youtube.com/watch?v=XTBWVVcF3Pk) |
| Published | 2026-07-07 |
| Ingested upstream | 2026-07-07 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
