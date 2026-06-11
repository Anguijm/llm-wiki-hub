# Write spec files that are legible enough for AI security review

> Back to [[experiments-index]]

Source: **[271 Vulnerabilities: What Mozilla's AI Found Changes Everything](https://www.youtube.com/watch?v=W79FW7iUkro)** · nb · 2026-05-09

**Status:** `deferred` · **Effort:** `medium`

---

## Hypothesis

If we write code specifications with explicit intent, clear verb-per-module contracts, and well-defined boundaries, then AI-assisted security and quality review will surface more real issues because models like Mythos can only find gaps between intent and implementation when intent is machine-readable.

## What they did

Speaker analyzed Mozilla's use of Anthropic's Claude Mythos preview on Firefox, which surfaced 271 vulnerabilities in one release cycle versus 22 from a prior run. He argued the key takeaway is not that AI beats humans but that human authorship is no longer a sufficient trust anchor. He recommended engineers focus on writing better specs with clear intent so that AI verification pipelines can defend the code, and framed specificity as the enemy of technical and security debt.

## Relevance to YOLO loop

Directly relevant: improving SPECS.md and task-level intent documents in our repo makes our codebase more defensible by automated review tools and improves Claude Code task scoping.

## Notes

Deferred 2026-05-10: spec-legibility research spike; valuable but lower priority than the deterministic-script-verification tick we're promoting from the same batch.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-05-09 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-05-09-mozilla-mythos-spec-legibility` |
| Channel | nb |
| Video | [271 Vulnerabilities: What Mozilla's AI Found Changes Everything](https://www.youtube.com/watch?v=W79FW7iUkro) |
| Published | 2026-05-09 |
| Ingested upstream | 2026-05-09 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
