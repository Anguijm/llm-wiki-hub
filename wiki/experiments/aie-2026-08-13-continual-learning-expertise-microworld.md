# Build a Domain-Specific Continual Learning Loop to Accumulate Agent Expertise

> Back to [[experiments-index]]

Source: **[Intelligence + Continual Learning = Expertise — Yu Su, NeoCognition](https://www.youtube.com/watch?v=I6aiEf3aEFQ)** · aie · 2026-08-13

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we implement a continual learning loop that allows an agent to accumulate situated, domain-specific expertise (procedural patterns, local environment affordances, error recovery heuristics) across episodes in a specific microworld rather than treating each episode independently, then the agent will perform more reliably and token-efficiently in that domain because expertise reduces the need to reason from scratch each time.

## What they did

Yu Su argued that current agents exhibit a modern Moravec's paradox — strong at symbolic tasks like coding but brittle in heterogeneous real-world digital environments. He distinguished intelligence (reasoning over unfamiliar problems from context, per-episode) from expertise (accumulated, situated competence enabling reliable, efficient, reproducible performance). He proposed that agents must continually learn on-the-job to acquire specialized expertise for each microworld, combining both parametric and non-parametric learning, and that specialization could feed back generalization via private in-situ data.

## Relevance to YOLO loop

Core to the YOLO loop's long-term goal: rather than each agent run starting cold, a persistent expertise store per project/repo would let the agent accumulate knowledge about codebase conventions, recurring error patterns, and tool quirks, improving reliability over successive runs.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-13 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-13-continual-learning-expertise-microworld` |
| Channel | aie |
| Video | [Intelligence + Continual Learning = Expertise — Yu Su, NeoCognition](https://www.youtube.com/watch?v=I6aiEf3aEFQ) |
| Published | 2026-08-13 |
| Ingested upstream | 2026-08-13 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
