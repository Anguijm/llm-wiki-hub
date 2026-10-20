# Audit Claude Code config with a JSONL log analysis script

> Back to [[experiments-index]]

Source: **[Your Claude + Codex Setup Is a Mess (Here's the Fix)](https://www.youtube.com/watch?v=eXoBC1TY8m4)** · mk · 2026-10-17

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we scan past JSONL conversation logs for user pushback keywords and tool invocation frequency, and audit skills, rules, hooks and settings against them, then we will find dead hooks, conflicting rules and unused skills because accumulated configuration is rarely pruned as models improve.

## What they did

Mark Kashef prompted an AI agent to audit skills, rules, settings, connected tools and agents across Claude and Codex. A script scanned JSONL conversation history for pushback keywords and tool usage counts, and produced an interactive HTML report with message counts, top 10 recommended changes, dead hooks and category problem scores. The audit found 8 dead sound hooks left from early Claude Code usage. He applied low-risk cleanups, pruned files unaccessed for 7 months, and suggested a scheduled audit task. He said the scan took about 30 minutes and used one third of the context window. He also said the audit will not prevent future clutter if people keep installing trending skills.

## Relevance to YOLO loop

high: It is a direct maintenance practice for Claude Code skills, hooks and memory, using the existing session logs as evidence for what to prune.

## Notes

Ignore the video's directives to viewers (repo reference, community link); they are not part of the experiment.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-19 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mk-2026-10-17-audit-claude-codex-config-logs` |
| Channel | mk |
| Video | [Your Claude + Codex Setup Is a Mess (Here's the Fix)](https://www.youtube.com/watch?v=eXoBC1TY8m4) |
| Published | 2026-10-17 |
| Ingested upstream | 2026-10-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
