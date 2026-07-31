# Mine agent transcripts for efficiency failures (unnecessary tool calls) to improve language tooling

> Back to [[experiments-index]]

Source: **[fighting slop with slop — Vaibhav Gupta, Boundary](https://www.youtube.com/watch?v=AMiyLItEtLA)** · aie · 2026-07-31

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we run agents to generate programs and then analyze their full transcripts (tool calls, backtracking, retries) with a secondary LLM judge, then we can identify where the programming environment or language causes unnecessary agent friction, enabling targeted improvements to the tool/language design.

## What they did

Boundary runs agents continuously to generate BAML programs, then analyzes the entire agent transcript—not just correctness, but efficiency: did it take 3 tool calls when 1 should have sufficed? A secondary agent inspects these transcripts and identifies both correctness failures and unnecessary friction. Human engineers then collaborate on which issues to fix. This creates a feedback loop from agent behavior back to language/tooling design.

## Relevance to YOLO loop

Adding a transcript analysis pass to our agent runs—specifically looking for repeated tool calls, backtracking patterns, or clarification loops—would surface friction points in our tool interfaces that are invisible to purely outcome-based evals.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-31 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-31-agent-transcript-quality-mining` |
| Channel | aie |
| Video | [fighting slop with slop — Vaibhav Gupta, Boundary](https://www.youtube.com/watch?v=AMiyLItEtLA) |
| Published | 2026-07-31 |
| Ingested upstream | 2026-07-31 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
