# Mine local JSONL conversation history with a fan-out workflow to generate personalized model-upgrade guidance

> Back to [[experiments-index]]

Source: **[3 AMAZING Claude Code Dynamic Workflows (Opus 4.8)](https://www.youtube.com/watch?v=9_ExDZFlaNc)** · mk · 2026-06-11

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we run a dynamic fan-out workflow over all local Claude Code JSONL conversation files to analyze personal usage patterns and compare them against new model release notes, then we will receive tailored migration advice specific to our actual workflows rather than generic tutorials, because agents can cross-reference observed prompting patterns with documented model capability changes.

## What they did

Mark built a three-use-case showcase of dynamic workflows with Opus 4.8. Use case 1 (model migration): A fan-out workflow reads all JSONL conversation files stored locally, mines token usage patterns and prompting behaviors across sessions, invokes a Claude Code guide sub-agent to pull latest Anthropic release notes, then synthesizes a personalized report and auto-generates a 2-minute tutorial video using the Hyperframes open-source library. Use case 2 (adversarial fact-checking): A workflow fans out agents to verify claims in a document, with adversarial agents refuting each finding before returning only confirmed items — ran ~200 agents, checked 170 claims in 20 minutes. Use case 3 (agentic OS audit): A workflow audits the .claude folder (skills, rules, hooks, commands) to identify stale, duplicate, or contradictory assets, reporting low/medium/high severity issues.

## Relevance to YOLO loop

The JSONL mining pattern is directly applicable for auditing our own YOLO loop session history to identify inefficiencies, repeated failure patterns, or underused skills. The adversarial verification pattern is valuable for any code-review or spec-validation step in the loop.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mk-2026-06-11-dynamic-workflow-personal-model-migration` |
| Channel | mk |
| Video | [3 AMAZING Claude Code Dynamic Workflows (Opus 4.8)](https://www.youtube.com/watch?v=9_ExDZFlaNc) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
