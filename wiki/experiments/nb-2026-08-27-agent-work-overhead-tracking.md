# Track human overhead per agent run to quantify management tax

> Back to [[experiments-index]]

Source: **[Agents Aren't Taking Your Jobs. They're Creating More Work Instead.](https://www.youtube.com/watch?v=IpEaSa7tgfc)** · nb · 2026-08-27

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we instrument our agent runs to log human-touch events (start, interrupt, check, takeover) alongside token usage, then we will be able to quantify the actual human overhead per agent task and identify which task types generate the most management work, because the Anthropic Claude Code study found humans made 70% of planning decisions and experienced users interrupted agents on ~9% of turns.

## What they did

Speaker cited Anthropic's study of 400,000 Claude Code sessions showing humans handle ~70% of planning decisions while agents handle execution, and that experienced users interrupt agents on ~9% of conversational turns. He also cited OpenAI data showing heaviest Codex users generate 60+ hours of agent activity daily, arguing this creates more human oversight work via the Jevons effect — more efficient agents enable more agent usage, not less human work.

## Relevance to YOLO loop

Directly relevant to understanding the true cost of our dev loop. If we add lightweight logging of human interventions per agent session we can measure whether our loop is generating net leverage or net overhead, and identify which subtasks to constrain or automate further.

## Notes

Jevons effect framing is useful for justifying continued investment in agent management tooling even as individual agents improve.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-27 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-08-27-agent-work-overhead-tracking` |
| Channel | nb |
| Video | [Agents Aren't Taking Your Jobs. They're Creating More Work Instead.](https://www.youtube.com/watch?v=IpEaSa7tgfc) |
| Published | 2026-08-27 |
| Ingested upstream | 2026-08-27 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
