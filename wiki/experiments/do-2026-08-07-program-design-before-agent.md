# Add Explicit Program Design Phase Before Letting Agent Execute

> Back to [[experiments-index]]

Source: **[Ex-NASA dev reveals his Agentic Engineering Workflow](https://www.youtube.com/watch?v=xgkjtF89-44)** · do · 2026-08-07

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we require a structured program design step (defining measurable outputs, architectural decisions, and constraints) before an agent begins coding, then review burden and rework will decrease because the agent's degrees of freedom are constrained to choices the human has already approved, reducing the chance of unmaintainable or surprising implementations.

## What they did

Dex (Dexter Horthy, who coined 'context engineering') described how the software factory loop—issue tracker → build → PR → CI/CD → prod—accelerates dramatically when agents replace the build step, but the review step becomes the new bottleneck since tens of thousands of lines cannot be manually reviewed. His solution is a pre-execution program design phase where the human specifies measurable outputs and key architectural decisions before the agent starts. He also described routing incidents and user feature requests directly into the agent factory (wake up to a PR not an alert), using two separate models (Codex and Opus) to cross-review agent output, and using KL divergence-style trust signals rather than pure accuracy benchmarks. He emphasized that if you give the agent a measurable output it will 'move mountains' and that skipping design leads to unmaintainable code even if it runs.

## Relevance to YOLO loop

The YOLO loop currently risks agents making unconstrained implementation choices. Inserting a lightweight program design artifact (measurable output definition + key constraints) before each agent run would reduce review surface area and make the loop's output more predictable and auditable.

## Notes

Dex's dual-model cross-review pattern (run two different models on the same PR and require both to sign off) is a concrete low-overhead trust-building mechanism worth piloting on high-risk agent outputs.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-07 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-08-07-program-design-before-agent` |
| Channel | do |
| Video | [Ex-NASA dev reveals his Agentic Engineering Workflow](https://www.youtube.com/watch?v=xgkjtF89-44) |
| Published | 2026-08-07 |
| Ingested upstream | 2026-08-07 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
