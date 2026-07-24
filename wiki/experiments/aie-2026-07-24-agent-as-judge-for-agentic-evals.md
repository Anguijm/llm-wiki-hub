# Replace fixed-rubric LLM-as-judge evals with an agent-as-judge for multi-turn agentic outputs

> Back to [[experiments-index]]

Source: **[The Future of Evals: From LLM as a Judge to Agent as a Judge — Aparna Dhinakaran, Arize AI](https://www.youtube.com/watch?v=q2JrUKBMf0w)** · aie · 2026-07-24

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we use a long-running agent to evaluate other agents' trajectories (rather than a fixed-rubric LLM judge), then we catch subtle agentic failure modes that deterministic evals miss—like tool call loops, inefficient trajectories, and context-forgetting—because agent-as-judge can adaptively explore trajectory patterns rather than scoring against a preset checklist.

## What they did

Argued that classical LLM-as-judge evals with fixed rubrics were designed for single-prompt responses and fail on modern agentic systems where every user interaction creates a unique trajectory. Described Arize's 'agent as a judge' approach via their Signal product: a long-running agent that ingests production traces, discovers patterns of issues across trajectories, identifies failures that would never appear in a fixed rubric (e.g., model calling the same tool repeatedly, inefficient path to answer, forgetting context mid-task), and can generate a PR with a fix. Positioned this as a third tier alongside deterministic evals and LLM-as-judge, not a replacement for the first two.

## Relevance to YOLO loop

Our current evals (when they exist) are single-turn checks. As the YOLO loop runs longer agentic sessions (multi-step skills, overnight runs), we need trajectory-level evaluation. Starting with a lightweight agent-as-judge that reviews session transcripts for loop detection and tool redundancy would be a practical first step.

## Notes

Short keynote-style talk. The three-tier eval stack (deterministic + LLM-as-judge + agent-as-judge) is a useful mental model. Minimum viable version: write a post-session review skill that reads the full tool-call log and flags repeated tool calls, stalled loops, and context loss events.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-24 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-24-agent-as-judge-for-agentic-evals` |
| Channel | aie |
| Video | [The Future of Evals: From LLM as a Judge to Agent as a Judge — Aparna Dhinakaran, Arize AI](https://www.youtube.com/watch?v=q2JrUKBMf0w) |
| Published | 2026-07-24 |
| Ingested upstream | 2026-07-24 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
