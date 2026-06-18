# Use Skills as Context-Efficient Capability Extensions Instead of Inline Prompts

> Back to [[experiments-index]]

Source: **[After spent 30+ hrs building loops...](https://www.youtube.com/watch?v=W6x-hb44C0c)** · aij · 2026-06-18

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we implement agent capabilities as named skills (referenced by pointer in system prompt) rather than inlining full instruction text, then we will extend agent capability without proportionally growing context window consumption, because skills allow prompt caching and selective loading of only the procedures relevant to the current task.

## What they did

Jason described the evolution from simple prompting to skill-based architecture as a response to context window pressure. Even with 1M token windows, effective windows are 128k-200k, so fitting the most relevant information becomes critical. Skills were introduced as a pattern to extend agent capability without blowing up the context window — each skill is a discrete, named procedure that the agent can invoke when needed rather than having all instructions present simultaneously. He also described using compaction strategies for long conversations and keeping system prompts structured to maximize prompt cache hits.

## Relevance to YOLO loop

Our YOLO loop system prompt likely has inline instruction bloat. Refactoring into referenced skill files would reduce baseline context consumption on every invocation and enable more capability within the effective context budget.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-18 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aij-2026-06-18-agent-skill-context-management` |
| Channel | aij |
| Video | [After spent 30+ hrs building loops...](https://www.youtube.com/watch?v=W6x-hb44C0c) |
| Published | 2026-06-18 |
| Ingested upstream | 2026-06-18 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
