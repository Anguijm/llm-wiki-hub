# Run a frontier model over the codebase to find vulnerability classes before adversaries do

> Back to [[experiments-index]]

Source: **[The AI bugpocalypse is here. Now what? - Jack Cable, Corridor](https://www.youtube.com/watch?v=7JgIS42mz7U)** · aie · 2026-07-12

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we use a frontier model (e.g. Claude with Fable-level safeguards) to proactively scan our own codebase for known vulnerability classes, then we can patch them before AI-assisted adversaries exploit them, because vulnerability classes are not novel even when the specific instance is new, giving defenders a structural advantage if they act first.

## What they did

Jack Cable (CEO, Corridor; ex-CISA) argued that AI coding tools are expanding attack surfaces at the same rate that frontier models are improving at finding and exploiting vulnerabilities. His 'secure by design' framework—originally from a 2023 CISA paper—recommends: (1) preventing vulnerabilities in new AI-generated code going forward, (2) hardening the open-source foundation via systematic rewrites (not one-off patches) to eliminate entire vulnerability classes, and (3) using the same AI models to defend as adversaries use to attack. He testified to Congress that defenders must get frontier model capabilities quickly, and that open-weight models are essential for fine-tuning and remaining competitive.

## Relevance to YOLO loop

As we generate more code with Claude Code and other agents, our attack surface grows proportionally. Inserting a model-driven security scan step into the CI/CD loop (or as a periodic agent task) is a direct application of this 'use AI to defend what AI builds' principle.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-12 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-12-ai-bugpocalypse-secure-by-design` |
| Channel | aie |
| Video | [The AI bugpocalypse is here. Now what? - Jack Cable, Corridor](https://www.youtube.com/watch?v=7JgIS42mz7U) |
| Published | 2026-07-12 |
| Ingested upstream | 2026-07-12 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
