# Add a self-optimization loop that rewrites agent prompts based on a measurable objective score

> Back to [[experiments-index]]

Source: **[What if the harness mattered more than the model? - Aditya Bhargava, Etsy](https://www.youtube.com/watch?v=2e9ANoOEn28)** · aie · 2026-07-08

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we add a self-optimization step where a meta-agent measures task performance against a defined objective, then iteratively rewrites the system prompt to improve that score, then agent performance will improve more reliably than manual prompt tuning because it replaces guess-and-check iteration with systematic measurement-driven improvement.

## What they did

Aditya Bhargava (Etsy staff engineer) presented a seven-step ladder for progressively improving a coding agent's harness using his new language 'Agency'. The final rung was self-optimization: the harness is given an objective function (e.g., a numeric score baseline of 0.2), runs the agent to establish a baseline, then a meta-optimizer rewrites the system prompt and re-runs the agent iteratively until the objective improves. He contrasted this with manual prompt engineering ('guessing and checking') and framed it as 'systematically measuring and improving.' He also referenced HarnessBench, a 106-task benchmark showing harness changes alone can swing performance by over 20 percentage points (52.4% to 76.2%), with larger gains for weaker models. Earlier rungs on his ladder included: adding tools, adding safety handlers (human-in-the-loop interrupts), partial function application for safe autonomous tool calls, chain-of-thought reasoning steps, and sub-agents for parallelism.

## Relevance to YOLO loop

Directly applicable: our YOLO loop already has iterative runs. Adding an outer optimization loop that scores outputs against a rubric and rewrites the system prompt between runs would formalize what we currently do manually. Agency's serializable pause/resume interrupt system is also relevant for safe human-in-the-loop checkpoints in our loop.

## Notes

HarnessBench paper is worth reading as a prior for evaluating our own harness changes. Agency is available via pip install (agencylang.com). Key safety primitives mentioned: interrupts, handlers, partial function application (PFA), and true pause/resume that works inside nested for loops, tool calls, and sub-agents—serializable across sessions.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-08 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-08-harness-self-optimization` |
| Channel | aie |
| Video | [What if the harness mattered more than the model? - Aditya Bhargava, Etsy](https://www.youtube.com/watch?v=2e9ANoOEn28) |
| Published | 2026-07-08 |
| Ingested upstream | 2026-07-08 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
