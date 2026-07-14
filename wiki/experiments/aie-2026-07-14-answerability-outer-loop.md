# Enforce an 'Explain It or Don't Ship It' Rule at the Outer Loop Boundary

> Back to [[experiments-index]]

Source: **[Don't Build Agents You Can't Answer For — Addy Osmani](https://www.youtube.com/watch?v=n97BCfyFIvw)** · aie · 2026-07-14

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we require every agent-generated PR or change to include a rationale trace (diffs, test results, logs, and a human-readable explanation) before it can be merged, then we will maintain answerability as agent output volume scales, because the bottleneck shifts from generation capacity to evidence-backed human judgment rather than rubber-stamp review.

## What they did

Addy Osmani (Google) argued that as AI-generated code becomes normal, answerability becomes an engineering requirement not a philosophical one. He framed the inner loop (agents investigate, implement, test, report) as capability and the outer loop (humans decide, verify, approve, own) as agency. He cited Sonar research showing 96% of engineers are skeptical of AI code but only ~50% always verify before committing, creating 'distrust without bandwidth.' He proposed clean code as a forcing function (clean repos use fewer tokens and cause fewer agent revisits) and an 'owners file' model where every part of the codebase has a named human accountable for agent-generated changes in that area. His operational rule: 'Explain it or don't ship it.'

## Relevance to YOLO loop

Directly applicable: our loop's merge gate should require the agent to attach evidence (test output, rationale) to every PR. This is the governance layer that keeps the YOLO loop from becoming a liability as it scales.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-14 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-14-answerability-outer-loop` |
| Channel | aie |
| Video | [Don't Build Agents You Can't Answer For — Addy Osmani](https://www.youtube.com/watch?v=n97BCfyFIvw) |
| Published | 2026-07-14 |
| Ingested upstream | 2026-07-14 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
