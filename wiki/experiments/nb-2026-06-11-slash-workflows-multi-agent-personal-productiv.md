# Use /workflows (slash-workflows) to spawn multi-agent sub-task decomposition for complex research

> Back to [[experiments-index]]

Source: **[My Codex Ran 800 Million Tokens in A Day. The Real Story Isn't Cost.](https://www.youtube.com/watch?v=l8BloTSLK6M)** · nb · 2026-06-11

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we invoke /workflows inside Codex (ported from Claude Code's Opus 4.8 release) for complex multi-part tasks, then task completion quality will improve because multiple specialized sub-agents tackle the problem from different angles simultaneously rather than a single agent handling it sequentially.

## What they did

Speaker grabbed an open-source /workflows skill originally released with Opus 4.8 for Claude Code, ported it to Codex, and used it to research schools for his children. The command caused Codex to dynamically create an orchestration plan, spin up three to four sub-agents, and produce a comprehensive comparative report with no significant extra effort. He observed the token chart spike corresponding to the multi-agent run and noted that more agents increased the probability of solving the problem correctly by attacking it from multiple angles.

## Relevance to YOLO loop

Directly applicable to our loop for any task that benefits from parallel research or multi-perspective analysis. Port the /workflows skill and measure quality delta vs single-agent runs on equivalent tasks.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-06-11-slash-workflows-multi-agent-personal-productivity` |
| Channel | nb |
| Video | [My Codex Ran 800 Million Tokens in A Day. The Real Story Isn't Cost.](https://www.youtube.com/watch?v=l8BloTSLK6M) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
