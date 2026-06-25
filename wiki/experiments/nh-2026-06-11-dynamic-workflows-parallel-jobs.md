# Run a dynamic workflow to audit all skills in parallel with cheap scoring agents feeding one synthesis agent

> Back to [[experiments-index]]

Source: **[Claude Code Dynamic Workflows Clearly Explained](https://www.youtube.com/watch?v=jZgcWCzxh1I)** · nh · 2026-06-11

**Status:** `adopted` · **Verdict:** `adopt` · **Effort:** `medium`

---

## Hypothesis

If we trigger a Claude Code dynamic workflow that spins up N Haiku scoring agents in parallel (one per skill file) feeding results into a single Opus synthesis agent, then we get a comprehensive ranked skill audit with improvement recommendations in a fraction of the time serial execution would take, because parallel sub-agents share no context and Haiku is 20x cheaper than Opus for the scoring pass.

## What they did

Nate ran a dynamic workflow against his 41 skill files: Claude Code generated a JavaScript workflow file, spawned 41 Haiku agents in parallel each scoring one skill, then fed all scores into one Opus synthesis agent that produced a ranked HTML report with patterns, worst-to-best ordering, and fix recommendations. Total cost was ~5M input tokens (mostly cache reads) with low output tokens. He explained the workflow vs sub-agent vs agent-team ladder, showed that workflows save themselves to .claude/workflows/ as JS files for re-use, and warned that 'ultra code' mode (x-high + auto-workflow) bypasses permission prompts and can burn half a $200/month subscription in one prompt. He also noted the trigger word 'workflow' highlights rainbow in terminal and that the explicit phrase 'set up a dynamic workflow to...' is the safest invocation.

## Relevance to YOLO loop

Provides a repeatable, cheap way to self-audit the skill library that powers the YOLO loop; the JS workflow file can be re-run after any batch of skill edits to track quality over time.

## Notes

Decision ladder: quick task→ask Claude; repeatable→skill; messy side task→sub-agent; small crew that talks→agent team; objective-criteria loop→/goal; giant parallel job→dynamic workflow. Ultra code = x-high + workflows, very expensive. Store workflows in <project>/.claude/workflows/ not global dir.

Backlog triage 2026-06-24 (owner-preference model). Fan-out scorers -> synthesis — council/parallel-agent + golden-eval family.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-11 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-06-11-dynamic-workflows-parallel-jobs` |
| Channel | nh |
| Video | [Claude Code Dynamic Workflows Clearly Explained](https://www.youtube.com/watch?v=jZgcWCzxh1I) |
| Published | 2026-06-11 |
| Ingested upstream | 2026-06-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
