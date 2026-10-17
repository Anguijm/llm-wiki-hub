# Pin agent efficacy metadata (model + prompt + provider) as a deployable spec

> Back to [[experiments-index]]

Source: **[Bridging the Gap Between AI Builders and Domain Experts](https://www.youtube.com/watch?v=QnrIyf48MvU)** · mlops · 2026-10-15

**Status:** `discarded` · **Verdict:** `discard` · **Effort:** `medium`

---

## Hypothesis

If we attach a versioned spec (exact prompt, model, hosting provider, harness) to each narrowly-scoped agent, then we can share and reproduce identical efficacy across team members because the relationship between prompt, model, and harness is fragile and non-transferable without explicit pinning.

## What they did

Justin argued that domain-specific agents fail to be reusable because there are no standards pinning the exact prompt version, model, and provider together. He described the need for a runtime spec that bundles these into a shareable, reproducible artifact—analogous to a package.json or lockfile—so that sharing an agent guarantees the same performance. He also noted that swapping models without re-validating the full harness silently degrades quality.

## Relevance to YOLO loop

Directly maps to agent reproducibility in our dev loop: any agent we ship should have a pinned spec so CI can verify it runs with identical efficacy on every deploy, preventing silent regressions from model or provider changes.

## Notes

Backlog triage 2026-10-17 round 3 (operator: "I want you to evaluate the yolo cards"). Settled maybe, cut: Assessment: engine.md already records the model used per stage in the run manifest and grounding_ab.py proves a setting still works, so a lockfile adds a name for something he has.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-15 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-10-15-domain-specific-agent-standards` |
| Channel | mlops |
| Video | [Bridging the Gap Between AI Builders and Domain Experts](https://www.youtube.com/watch?v=QnrIyf48MvU) |
| Published | 2026-10-15 |
| Ingested upstream | 2026-10-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
