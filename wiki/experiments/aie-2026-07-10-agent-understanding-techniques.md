# Have agents generate explainer docs, quizzes, and micro-world simulations after each large PR

> Back to [[experiments-index]]

Source: **[Understanding is the new bottleneck — Geoffrey Litt, Notion](https://www.youtube.com/watch?v=WkBPX-oDMnA)** · aie · 2026-07-10

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we instruct agents to produce an explainer document, a short comprehension quiz, and an interactive micro-world simulation alongside each large code change, then we will reduce cognitive debt accumulation in the YOLO loop because these artifacts force the agent to surface its own reasoning in forms a human can rapidly internalize and verify.

## What they did

Geoffrey Litt described three concrete techniques he uses at Notion to maintain understanding of agent-written code: (1) having agents write explainer docs that teach him how the new code works, (2) having agents generate quizzes he takes to verify his own comprehension, and (3) having agents build interactive micro-world simulations — small runnable environments that let him develop intuitive understanding of system behavior beyond what written docs convey. He framed this as fighting 'cognitive debt' and argued understanding is necessary not just for correctness-checking but for remaining a creative participant who can generate the next idea.

## Relevance to YOLO loop

After each YOLO loop iteration that produces a large diff, adding a post-run prompt asking Claude Code to output (a) a plain-language explainer, (b) three quiz questions with answers, and (c) a minimal runnable demo of the core logic would let us stay orientated without reading every line, directly addressing the cognitive debt risk in fast agentic loops.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-10 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-10-agent-understanding-techniques` |
| Channel | aie |
| Video | [Understanding is the new bottleneck — Geoffrey Litt, Notion](https://www.youtube.com/watch?v=WkBPX-oDMnA) |
| Published | 2026-07-10 |
| Ingested upstream | 2026-07-10 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
