# Gate Loop Autonomy Behind Spec-Verified, Test-Covered Slices Rather Than Open-Ended Tasks

> Back to [[experiments-index]]

Source: **[The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](https://www.youtube.com/watch?v=c35YoMdnI78)** · aie · 2026-07-14

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we scope each loop iteration to a well-specified, test-covered slice of work (rather than an open-ended goal), then the loop can autonomously decide whether it succeeded or failed without human review of every output, because a software factory can mechanically verify spec-gated slices but cannot autonomously judge whether it built the right thing at a higher level.

## What they did

In an Oxford-format debate, Team Dex (Dex Horthy + Greg Pstrucha) argued that there is a meaningful gap between loop hype and what works in practice: loops cannot autonomously decide whether they built the right thing, only whether they passed tests against a spec. Team Ian/Jeff (Ian Livingstone + Geoff Huntley) countered that loops are inevitable and already delivering value when combined with proper infra, tests, and discipline. Geoff noted he has not manually written code in 2.5 years and runs loops to autonomously port code across languages. Dex recommended static typing (Rust, Haskell) as a form of verification that makes loops more reliable, and warned that open-source dependencies are a liability — vendor and generate your own dependencies so the agent can modify them. The consensus: loops work well for well-defined slices with strong type systems and test coverage; they break down for open-ended judgement tasks.

## Relevance to YOLO loop

Core design principle for our loop: define each loop task as a verifiable slice with explicit pass/fail criteria rather than a vague goal. Combine with strong typing in generated code to give the loop a mechanical verification layer that doesn't require human review of every PR.

## Notes

Context layer video (@aiDotEngineer WTF Is the Context Layer) had no transcript and was skipped per instructions.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-14 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-14-loops-debate-spec-gated-slices` |
| Channel | aie |
| Video | [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](https://www.youtube.com/watch?v=c35YoMdnI78) |
| Published | 2026-07-14 |
| Ingested upstream | 2026-07-14 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
