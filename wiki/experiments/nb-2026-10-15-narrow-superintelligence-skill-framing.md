# Apply the 'narrow superintelligence' lens to decide where to keep vs. remove human judgment in agent workflows

> Back to [[experiments-index]]

Source: **[OpenAI's AI Wrote 700 Math Papers. Engineers Still Won't Trust AI With Their Code.](https://www.youtube.com/watch?v=pTh4IJ-Mi3Y)** · nb · 2026-10-15

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we audit each step of our Claude Code agent workflows by asking whether success criteria are perfectly verifiable (like math proofs or test suites), then we can safely delegate those steps fully to the agent while retaining human judgment for ambiguous business-logic steps, because verifiability is the key variable that determines whether a model's spiky capability translates into reliable production output.

## What they did

The speaker analyzed OpenAI releasing 700+ math papers produced by a single unreleased model (each result in ~3 hours), arguing this represents 'narrow superintelligence' — superhuman in domains with perfectly verifiable success criteria (math, formal logic) but uneven everywhere else. He contrasted this with production coding, where most engineers still maintain zero-trust environments and heavy evals, noting that code verifiability (does it run?) should in theory make LLMs crush codebases, but they don't, because real engineering involves ambiguous business judgment, messy databases, and CRM data that fall outside the narrow capability spike. He argued the skill worth investing in is diagnosing where verifiability exists and structuring work accordingly.

## Relevance to YOLO loop

high: directly informs which agent workflow steps should have human-in-the-loop checkpoints vs. full automation — a core harness design decision.

## Notes

Commentary video; the actionable part is the mental model for structuring agent trust boundaries, not a specific tool.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-10-15-narrow-superintelligence-skill-framing` |
| Channel | nb |
| Video | [OpenAI's AI Wrote 700 Math Papers. Engineers Still Won't Trust AI With Their Code.](https://www.youtube.com/watch?v=pTh4IJ-Mi3Y) |
| Published | 2026-10-15 |
| Ingested upstream | 2026-10-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
