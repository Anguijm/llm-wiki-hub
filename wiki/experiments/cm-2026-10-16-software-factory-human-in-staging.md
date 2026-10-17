# Replace the fully-autonomous dark factory with a human-gated staging review loop inside an AI software factory

> Back to [[experiments-index]]

Source: **[My AI Dark Factory Dream Is Dead (Here's What Actually Works)](https://www.youtube.com/watch?v=GQatuTWSRqY)** · cm · 2026-10-16

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we insert a mandatory human review step at the staging environment boundary (after agents build a full epic batch but before production merge), then we get most of the autonomy benefits of a dark factory while retaining intent verification and codebase maintainability, because the bottleneck is not build speed but human understanding of what was actually wanted.

## What they did

Cole Medin ran a public dark factory experiment (fully autonomous, no steering wheel) and concluded it fundamentally fails because LLMs cannot read human intent no matter how capable they become. He rebuilt it as an AI software factory: agents handle the full build-validate-merge cycle autonomously, a manager agent alerts on stuck workflows, but humans review each epic batch in staging and file batch-correction issues before promoting to production. He also uses mission.md/engineering.md as immutable context that the factory cannot modify.

## Relevance to YOLO loop

high: directly informs the architecture of our own Claude Code harness—specifically the staging-gate pattern and immutable mission context files.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-16 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `cm-2026-10-16-software-factory-human-in-staging` |
| Channel | cm |
| Video | [My AI Dark Factory Dream Is Dead (Here's What Actually Works)](https://www.youtube.com/watch?v=GQatuTWSRqY) |
| Published | 2026-10-16 |
| Ingested upstream | 2026-10-16 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
