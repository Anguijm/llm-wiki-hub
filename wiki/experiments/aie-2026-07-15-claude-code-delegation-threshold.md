# Calibrate Agent Delegation Threshold by Tracking Permission-Prompt Acceptance Rate Over Model Generations

> Back to [[experiments-index]]

Source: **[Simon Willison in conversation with Cat Wu & Thariq Shihipar, Anthropic](https://www.youtube.com/watch?v=uU5Gv2h8-9g)** · aie · 2026-07-15

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we track how often we override or deny agent actions across model generations and use that rate as a delegation-threshold metric, then we can systematically increase autonomy grants as the rate drops, because decreasing intervention frequency is a measurable proxy for trust that avoids arbitrary autonomy decisions.

## What they did

Cat Wu described the evolution of Claude Code usage at Anthropic: initially users read every permission prompt carefully and frequently said no, closely monitoring each action. With each model generation, the team stepped back and delegated more implementation work. With Fable, many features can be one-shotted. Thariq noted that rewrites — previously considered the worst possible engineering decision — are now actively good practice because the model can execute them reliably given a good test suite, and the rewrite forces the team to ensure the test suite is solid. The conversation framed this as a shift in required human skills: product taste and business sense now matter more than execution speed.

## Relevance to YOLO loop

In our dev loop we should instrument how often we manually intervene, rollback, or override agent outputs. Plotting this rate over time gives us a data-driven signal for when to expand the agent's autonomous scope rather than relying on intuition. Also validates investing in test suite quality as a prerequisite for broader delegation.

## Notes

Secondary finding from transcript: Claude Code memory in Claude.ai is currently per-channel markdown files, with session contributions back to main memory. Rewrites are now considered a forcing function for test suite quality rather than a risk. Simon Willison noted software engineering is harder now because ambition level has risen with capability.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-15-claude-code-delegation-threshold` |
| Channel | aie |
| Video | [Simon Willison in conversation with Cat Wu & Thariq Shihipar, Anthropic](https://www.youtube.com/watch?v=uU5Gv2h8-9g) |
| Published | 2026-07-15 |
| Ingested upstream | 2026-07-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
