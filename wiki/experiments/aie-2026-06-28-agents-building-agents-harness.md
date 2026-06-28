# Build a Golden Dataset + Eval Loop to Drive Agent Improvements

> Back to [[experiments-index]]

Source: **[Agents Building Agents - Alfonso Graziano, Nearform](https://www.youtube.com/watch?v=aHhB3sjGjkI)** · aie · 2026-06-28

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we maintain a golden dataset of input/expected-output pairs and run scored evals against it after each change, then we can catch regressions and systematically improve agent accuracy because we have a quantitative baseline that makes non-deterministic behavior measurable.

## What they did

Alfonso described building a golden dataset (curated with subject-matter experts) that defines expected inputs and outputs—including expected tool calls and call chains—for an agent. They built scorers that run the dataset through the LLM and produce a pass-rate number. Starting from 18% pass rate on a bare Mastra agent, they iteratively added tools, improved system prompts, and re-ran evals. Failure modes discovered on live data were fed back into the golden dataset so regressions would be caught automatically. A coding agent (e.g., AutoAgent) was given the failure clusters plus access to the test harness so it could propose and validate its own fixes.

## Relevance to YOLO loop

Directly maps to the evaluation and regression-detection phase of the YOLO loop: golden dataset acts as the test suite, scorers act as the CI gate, and the coding agent closing the loop mirrors the automated fix-and-validate step we want in our dev loop.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-28 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-28-agents-building-agents-harness` |
| Channel | aie |
| Video | [Agents Building Agents - Alfonso Graziano, Nearform](https://www.youtube.com/watch?v=aHhB3sjGjkI) |
| Published | 2026-06-28 |
| Ingested upstream | 2026-06-28 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
