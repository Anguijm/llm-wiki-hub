# Use Competing-Model Debate Pattern for Deep Domain Research

> Back to [[experiments-index]]

Source: **[Omnigent: Composition, Control, and Collaboration for AI Agents](https://www.youtube.com/watch?v=MQqV-v5HqaU)** · mlops · 2026-07-15

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we route a research query through two different LLMs (e.g., GPT-4 vs. Claude Opus) configured to debate each other with shared domain memory and skill files as background context, then the output will surface more nuanced and complete information than a single-model query because adversarial framing forces each model to challenge the other's assumptions and fill gaps.

## What they did

Speaker described using Omnigent's 'Poly Debate' mode where ChatGPT and Claude Opus are instantiated as debating agents sharing pre-loaded agentic memory and skills markdown files as background. He used this to research specific farming regions in Taiwan (Nanto County) for matcha production, identifying which sub-regions had tea oxidation processing infrastructure, which distributors to contact, and what logistical constraints (steaming/drying proximity) existed. The agents debated competing regional options and surfaced details he said he would not have found through single-model or manual research.

## Relevance to YOLO loop

In our dev loop, we could apply this pattern to architectural decision research or library evaluation — spin up two model instances with opposing priors and shared codebase context, let them debate trade-offs, and harvest the synthesis rather than accepting a single model's first answer.

## Notes

Transcript was heavily truncated after the intro conversation. Core pattern extracted from the first third. Omnigent appears to be the framework enabling the debate composition. Stateful agent memory via persistent skills MDs is a prerequisite for meaningful debate grounding.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-07-15-multi-agent-debate-research` |
| Channel | mlops |
| Video | [Omnigent: Composition, Control, and Collaboration for AI Agents](https://www.youtube.com/watch?v=MQqV-v5HqaU) |
| Published | 2026-07-15 |
| Ingested upstream | 2026-07-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
