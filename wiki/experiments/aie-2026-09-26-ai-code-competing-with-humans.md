# Measure AI vs. Human Code Quality on Production Codebases Using Greptile-Style Evaluation

> Back to [[experiments-index]]

Source: **[AI-Generated Code Is Already Competing With Human Code — Daksh Gupta, Greptile](https://www.youtube.com/watch?v=474j-n1Ltxc)** · aie · 2026-09-26

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we evaluate AI-generated code against human-written code on real production metrics (correctness, maintainability, review pass rate) rather than toy benchmarks, then AI code will score competitively in well-scoped tasks because frontier models have crossed a quality threshold sufficient for production use on bounded problems.

## What they did

Daksh Gupta from Greptile presents data from evaluating AI-generated code against human-written code on real codebases, using Greptile's codebase understanding layer to provide context. He shares metrics on where AI code matches human quality, where it falls short, and what patterns distinguish high-quality AI code generation.

## Relevance to YOLO loop

Informs the YOLO loop's code generation step — understanding where AI code is production-ready vs. requires human review helps calibrate how much autonomy to grant the agent in the loop.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-26 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-26-ai-code-competing-with-humans` |
| Channel | aie |
| Video | [AI-Generated Code Is Already Competing With Human Code — Daksh Gupta, Greptile](https://www.youtube.com/watch?v=474j-n1Ltxc) |
| Published | 2026-09-26 |
| Ingested upstream | 2026-09-26 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
