# Build a supervised procedural memory update pipeline that promotes trace-derived rule changes to human review before committing

> Back to [[experiments-index]]

Source: **[Giving AI Agents Memory That Learns — Jake Broekhuizen, LangChain](https://www.youtube.com/watch?v=KGFyOtl5ktI)** · aie · 2026-10-09

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we route agent trace analysis through a pipeline that identifies tone/behavior violations, proposes procedural memory updates (instruction changes), surfaces them for human approval, and only then commits them to the agent's live context, then agent behavior will improve across runs without regressions because unreviewed automatic instruction updates risk silently degrading the 75% of behavior that procedural memory governs.

## What they did

Jake Broekhuizen (LangChain Labs) described a financial services budgeting agent whose tone slipped from advisory to directive in some sessions. Manual trace review to fix tone doesn't scale. His team built an adaptive memory system: (1) classify agent memory into semantic (facts/preferences), episodic (learned patterns/examples), and procedural (instructions/skills/rules—governs ~75% of visible behavior); (2) observe traces to detect violations; (3) use an LLM to analyze the trace, identify the procedural memory gap, and propose a markdown file update to Context Hub; (4) surface the proposed update for human review before committing; (5) on next agent run, verify tone correction. Key design principles: not every trace should become a memory update; cache invalidation matters for long-running agents (memory updates must be available in hot path); procedural memory changes especially need human-in-the-loop given their outsized behavioral impact.

## Relevance to YOLO loop

Maps directly to YOLO loop instruction maintenance: automate detection of behavioral drift from traces, generate proposed CLAUDE.md/skill updates, require human approval before committing—closing the loop between observation and instruction.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-09 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-09-procedural-memory-update-loop` |
| Channel | aie |
| Video | [Giving AI Agents Memory That Learns — Jake Broekhuizen, LangChain](https://www.youtube.com/watch?v=KGFyOtl5ktI) |
| Published | 2026-10-09 |
| Ingested upstream | 2026-10-09 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
