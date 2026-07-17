# Use Code as the Reasoning Medium for Multi-Step Agent Tasks Instead of Natural Language Chains

> Back to [[experiments-index]]

Source: **[Research to Reality: Benoit Schillings, Google DeepMind, VP Research (Thinking, Reasoning, Coding)](https://www.youtube.com/watch?v=1P1hJ36rxM0)** · aie · 2026-07-17

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we structure agent reasoning as executable code (chain-of-code) rather than natural language chain-of-thought, then the agent will produce more verifiable, reliable, and composable multi-step results because code is executable, testable, and not subject to the ambiguity and hallucination risk of prose reasoning steps.

## What they did

Benoit Schillings (VP Research, Google DeepMind) described DeepMind's research trajectory from Project Pitchfork (2018, ML for code editing) to current frontier capabilities. He articulated a key insight from their research: 'thinking and reasoning today is chain of code' rather than chain of tokens—models that reason by writing and executing code outperform those reasoning in natural language prose. He noted the current bottleneck in agentic software engineering is not syntax generation (which is now superhuman) but multi-step codebase navigation and specification clarity. He also raised the open research question of whether models should reason in new languages designed for machines rather than human-readable ones, noting that 'strongly typed' or proof-oriented languages could put the burden of correctness on the model. He pointed to chemistry, biology, and 'the gold we cannot see' (solutions humans are cognitively biased against perceiving) as the highest-value frontiers for ML-assisted discovery.

## Relevance to YOLO loop

Directly informs how we structure agent reasoning steps in the loop: prefer code-executable reasoning traces over prose. Any multi-step planning task should be expressed as runnable code where possible so intermediate steps can be validated. Also validates our interest in strongly-typed interfaces between agents.

## Notes

Schillings' framing of software eras is useful context: (1) machine-limited era → assembly, (2) human-brain-limited era → modular design patterns, (3) AI-frontier era → specification and verification are the bottlenecks, not code writing. The implication for our loop: invest in eval/spec quality, not code generation quality. He also noted Gemini's multimodal-from-day-one choice as strategically important for spatial/dynamic reasoning tasks.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-17 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-17-deepmind-chain-of-code-reasoning` |
| Channel | aie |
| Video | [Research to Reality: Benoit Schillings, Google DeepMind, VP Research (Thinking, Reasoning, Coding)](https://www.youtube.com/watch?v=1P1hJ36rxM0) |
| Published | 2026-07-17 |
| Ingested upstream | 2026-07-17 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
