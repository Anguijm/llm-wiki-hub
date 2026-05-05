# Build custom evals that measure real YOLO build quality beyond synthetic benchmarks

> Back to [[experiments-index]]

Source: **[Beyond SWE-Bench Pro - Where do Agents go from Here?]()** · @MLOps · 2026-04-02

**Status:** `adopted` · **Verdict:** `adopt` · **Effort:** `medium`

---

## Hypothesis

If we design custom evaluation metrics tailored to YOLO project requirements (user experience quality, feature completeness, maintainability) rather than relying on generic benchmarks, then we get a more accurate picture of agent capability because SWE-Bench style metrics don't capture what matters for our use case.

## What they did

MLOps discussed the limitations of SWE-Bench Pro as a coding agent benchmark and explored what comes next — real-world evals that measure agent performance on actual engineering tasks beyond isolated bug fixes.

## Actionable steps

- Define 5 custom eval dimensions for YOLO builds: test pass rate, UI quality, feature completeness, code maintainability, build time
- Create a scoring rubric for each dimension (1-5 scale with examples)
- Run the rubric on the last 10 YOLO builds to establish a baseline
- Use the baseline to measure improvement as the build pipeline evolves

## Success metric

Custom eval rubric established and baseline measured across 10 projects.

## Relevance to YOLO loop

Related to mlops-2026-04-01-coding-agent-evals but focuses on going beyond generic benchmarks to YOLO-specific quality metrics.

## Target projects

- [[yolo-projects]] (`yolo-loop-infrastructure`)

## Notes

Adopted 2026-04-07: extends current test_project.py + eval_bugs.py + security_scan.py with YOLO-specific lenses. Low effort, real value. Next step: write 2-3 new lens scripts (e.g., ux-completeness.py, mobile-usability.py, cult-status.py).

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-03 | `backlog` | Ingested from Phase 4 YouTube pipeline — title-only inference |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-04-03-beyond-swebench-evals` |
| Channel | @MLOps |
| Published | 2026-04-02 |
| Ingested upstream | 2026-04-03 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
