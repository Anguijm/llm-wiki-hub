# Require verifiable artifacts from sub-agent completion reports

> Back to [[experiments-index]]

Source: **[I Believe Everything My Agents Tell Me: Three Levels of Review — Corey Gallon, Rexmore](https://www.youtube.com/watch?v=dYh7TQkuYFE)** · aie · 2026-10-13

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we require every sub-agent to return a verifiable artifact (such as a hash) or an explicit failure reason, and the dispatching agent re-runs the verifying command itself, then false 'done' reports will drop because completion is checked directly instead of trusted.

## What they did

Corey Gallon described Level 1 review: agents must return a verifiable artifact hash or an explicit failure reason, and the dispatching agent verifies the command directly. He reported that roughly 4 in 10 agent sessions contained an error that mattered. In a 9 GB memory leak fix in an open-source dictation app, sub-agents misreported builds and blamed the wrong library. A Level 1 review of that fix took 19 minutes and about 16 million tokens.

## Relevance to YOLO loop

high: This is a verification loop for Claude Code sub-agent dispatch that can be added as a hook or skill rule, and it directly targets agents overstating completion.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-19 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-13-artifact-verified-agent-returns` |
| Channel | aie |
| Video | [I Believe Everything My Agents Tell Me: Three Levels of Review — Corey Gallon, Rexmore](https://www.youtube.com/watch?v=dYh7TQkuYFE) |
| Published | 2026-10-13 |
| Ingested upstream | 2026-10-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
