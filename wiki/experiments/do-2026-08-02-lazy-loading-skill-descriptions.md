# Rewrite skill descriptions as precise trigger conditions to exploit lazy-loading behavior

> Back to [[experiments-index]]

Source: **[I open-sourced my Agent Skills repo (it went viral)](https://www.youtube.com/watch?v=clrUbBtD2j4)** · do · 2026-08-02

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we rewrite each skill's name and description to be a precise, unambiguous trigger condition (rather than a broad capability label), then agents will invoke the right skill at the right time and avoid context-window pollution from irrelevant skills loading, because agents load only name+description first and pull full skill content only on match.

## What they did

David explained (corroborating Nate Jones's video) that Codex and Claude Code load skills lazily: name and description are always in context, but the full skill markdown is only loaded when the task matches the description. This means a vague description causes either missed invocations or false positives that bloat the context window. He showed that his 42 skills are each written with AI for AI consumption — long, detailed, agent-optimized — but with tight descriptions so they only activate in the right context. He used a Deep API skill as an example: it loads only when the agent needs deep research or scraping, not on every turn.

## Relevance to YOLO loop

YOLO loop skill/instruction files suffer from the same lazy-loading dynamics. Auditing and tightening trigger descriptions in existing CLAUDE.md skills is a quick win that reduces context waste and improves task-skill matching.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-02 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-08-02-lazy-loading-skill-descriptions` |
| Channel | do |
| Video | [I open-sourced my Agent Skills repo (it went viral)](https://www.youtube.com/watch?v=clrUbBtD2j4) |
| Published | 2026-08-02 |
| Ingested upstream | 2026-08-02 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
