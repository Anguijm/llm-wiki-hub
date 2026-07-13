# Implement RLM pattern to externalize large-codebase context into a programmable REPL environment

> Back to [[experiments-index]]

Source: **[RLM: Recursive Language Models for Large Codebases - Shashi, Superagentic AI](https://www.youtube.com/watch?v=8oyalrfwgjw)** · aie · 2026-07-13

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we give a coding agent a sandboxed REPL environment to programmatically inspect, slice, and compute relevant chunks from a large codebase rather than loading it all into context, then context window degradation on monorepos is eliminated and agent performance on root-cause analysis and onboarding tasks improves, because the model only pulls bounded observations into main context and can recursively query sub-models for specialized knowledge.

## What they did

Shashi (Superagentic AI) presented the RLM (Recursive Language Models) pattern from an MIT paper and their open-source reference implementation RLM-Code. The pattern: treat the entire repository as external data; give the agent a REPL (programmable execution environment) to write code that inspects, slices, and extracts relevant snippets; feed only the bounded observations into the main context window. Recursive element: when the agent needs deeper knowledge, it issues an LLM query to a sub-model (another specialist), gets a response, and continues the loop. The loop terminates when a final result is reached. The JSONL trajectory (plan → REPL code → observations → LLM queries → output) is exportable to any observability platform. He also notes that Codex's harness, Claude managed agents, and Gemini managed agents all use RLM-like patterns under the hood, and Anthropic engineers have confirmed RLM concept use in Claude Code on X.

## Relevance to YOLO loop

Directly applicable to any YOLO loop step that involves large codebases: instead of stuffing repo context into the prompt, wrap the agent with an RLM harness. The recursive sub-model query pattern also maps to our orchestrator→worker model. JSONL trajectory export enables loop observability.

## Notes

Open source: RLM-Code on GitHub (Superagentic AI). Also see: original MIT RLM paper, DSPy RLM implementation by Omar (also DSPy author), official RLM and RLM-minimal repos. Live demo used Gemini model via CLI.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-13 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-13-rlm-recursive-context-management` |
| Channel | aie |
| Video | [RLM: Recursive Language Models for Large Codebases - Shashi, Superagentic AI](https://www.youtube.com/watch?v=8oyalrfwgjw) |
| Published | 2026-07-13 |
| Ingested upstream | 2026-07-13 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
