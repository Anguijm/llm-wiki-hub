# Apply world-model visual chain-of-thought (predict future state before acting) to verification loops in agent harnesses

> Back to [[experiments-index]]

Source: **[Robots That Predict the Future: Dyna-2 & Physical AI — Jason Ma, Dyna Robotics](https://www.youtube.com/watch?v=BHiYomkfoGQ)** · ls · 2026-10-16

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we add a 'predict the expected output state' step before an agent executes a destructive or hard-to-reverse action, then the agent will catch intent mismatches earlier because explicitly imagining the post-action world state surfaces assumptions the way Dyna-2's future-video generation surfaces robot planning errors before physical execution.

## What they did

Jason Ma described Dyna-2, a world action model that generates predicted future video frames as an intermediate reasoning step before outputting robot actions—analogous to chain-of-thought but in the visual/physics space. This made robots more dextrous and robust to unseen scenarios. A two-model architecture was used: a high-level reasoning model for planning and a low-level action model for dextrous execution.

## Relevance to YOLO loop

medium: the 'predict expected state before acting' pattern translates to adding a pre-execution prediction step in Claude Code hooks for destructive operations (file deletions, schema migrations, etc.).

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-16 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `ls-2026-10-16-world-action-model-visual-chain-of-thought` |
| Channel | ls |
| Video | [Robots That Predict the Future: Dyna-2 & Physical AI — Jason Ma, Dyna Robotics](https://www.youtube.com/watch?v=BHiYomkfoGQ) |
| Published | 2026-10-16 |
| Ingested upstream | 2026-10-16 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
