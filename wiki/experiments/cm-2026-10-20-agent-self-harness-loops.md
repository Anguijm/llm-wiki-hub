# Add escalation and trace-driven instruction-diff loops to an agent harness

> Back to [[experiments-index]]

Source: **[Let Your AI Agent Do ITS OWN Harness Engineering (Here's How)](https://www.youtube.com/watch?v=TVhhmhvCovg)** · cm · 2026-10-20

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we have agents escalate low-confidence cases to a human, record corrections into categorized memory case files, and propose concise instruction diffs from failed traces for human approval, then benchmark accuracy will rise because lessons accumulate without bloating the main instructions file.

## What they did

Structured a production agent with markdown files (instructions.md, skills/, memory/) in a ~30-line Python definition, built an uncertainty escalation inbox, wrote supervisor corrections into shared and user-specific memory, and used LangSmith traces to propose instruction diffs approved by humans. Benchmark went from 4/14 to 13/14 correct on a small support-question set.

## Relevance to YOLO loop

high: Escalation, persistent memory and human-approved harness diffs map directly onto Claude Code memory and verification loops.

## Notes

Benchmark of 14 questions is small; the video itself cautions that small eval sets can mask regressions.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-22 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `cm-2026-10-20-agent-self-harness-loops` |
| Channel | cm |
| Video | [Let Your AI Agent Do ITS OWN Harness Engineering (Here's How)](https://www.youtube.com/watch?v=TVhhmhvCovg) |
| Published | 2026-10-20 |
| Ingested upstream | 2026-10-22 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
