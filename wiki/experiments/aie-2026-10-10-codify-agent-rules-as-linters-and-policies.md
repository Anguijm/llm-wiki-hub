# Replace repeated agent re-prompting with custom linters and policy agents to enforce code quality deterministically

> Back to [[experiments-index]]

Source: **[Stop Prompting — Greg Pstrucha, Sentry](https://www.youtube.com/watch?v=E3KbFLAGD6A)** · aie · 2026-10-10

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we analyze past agent transcripts and code review feedback to extract recurring quality issues and encode them as custom linters (for deterministic rules) and policy sub-agents (for qualitative rules), then agents will stop repeating the same elementary mistakes across context window resets, because linters provide persistent, context-independent enforcement that doesn't depend on the agent's memory.

## What they did

Greg Pstrucha (Sentry) described the failure mode: agents make the same mistakes repeatedly after context compaction, requiring constant re-prompting. His solution: (1) ask the agent to analyze past transcripts and GitHub review comments to generate custom lint rules for recurring issues (e.g., ban console.log, enforce design system components, no overly-defensive try/catch everywhere); (2) create a 'grumpy engineer' policy agent (internally called Garfield) that runs sub-agents against qualitative policies (e.g., no too many tests, no overly defensive code, prefer type-system constraints over runtime guards) and loops until all sub-agents stand down before the human reviews. He warned against quantitative proxies like cyclomatic complexity and test coverage because agents optimize the metric rather than the underlying quality.

## Relevance to YOLO loop

Directly applicable: our YOLO loop likely has recurring agent output quality issues we re-prompt for. Encoding these as linters (run in CI) and policy agents (run pre-merge) would raise the floor of generated code quality without human intervention, freeing review time for genuinely novel decisions.

## Notes

Starting point: ask agent to review past session transcripts and GitHub PR comments, then generate candidate lint rules ranked by frequency.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-10 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-10-codify-agent-rules-as-linters-and-policies` |
| Channel | aie |
| Video | [Stop Prompting — Greg Pstrucha, Sentry](https://www.youtube.com/watch?v=E3KbFLAGD6A) |
| Published | 2026-10-10 |
| Ingested upstream | 2026-10-10 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
