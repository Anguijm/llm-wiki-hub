# Add episodic and semantic memory to agent classification tasks to reduce flip-flop inconsistency on boundary cases

> Back to [[experiments-index]]

Source: **[Why Your Agent Disagrees With Itself (And What To Do About It) - Diane Lin, Datadog](https://www.youtube.com/watch?v=wEc9aG7cRQc)** · aie · 2026-07-20

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we augment an agent's classification or triage decisions with (1) semantic memory containing distilled domain policy for edge cases and (2) episodic memory of past similar cases and their human-verified verdicts, then flip-flop inconsistency on boundary-zone inputs will decrease significantly (from ~25% to ~10% in observed data) and remaining inconsistencies will be routed to human review for policy clarification, because boundary cases are ambiguous by definition and memory provides the consistent policy anchor the model lacks.

## What they did

Diane Lin (Datadog, formerly Chromite) presented data from 93 real cybersecurity alerts run through an LLM triage agent three times: ~25% flip-flopped between benign and suspicious. She showed that flip-flopping concentrates near the decision boundary where even human experts disagree, so the root cause is missing policy (what should we do in this ambiguous case) not model failure. Her solution: semantic memory stores distilled domain knowledge and company policy for recurring ambiguous patterns; episodic memory stores past similar cases with their human-verified labels. The agent consults both before deciding. Cases that still flip after memory lookup get routed to human review which then enriches the semantic memory. Result: 15% of flip-floppers resolved automatically by episodic memory, remaining 10% sent to human review. She also recommended treating each model disagreement as a training signal via active learning rather than a bug.

## Relevance to YOLO loop

Applicable to any YOLO loop step where an agent makes repeated classification decisions (PR review, test failure triage, security alert routing): adding a simple episodic store (e.g. a JSON file of past decisions with outcomes) and prompting the agent to check it before deciding would reduce inconsistency with minimal engineering.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-20 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-20-episodic-semantic-memory-agent-consistency` |
| Channel | aie |
| Video | [Why Your Agent Disagrees With Itself (And What To Do About It) - Diane Lin, Datadog](https://www.youtube.com/watch?v=wEc9aG7cRQc) |
| Published | 2026-07-20 |
| Ingested upstream | 2026-07-20 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
