# Run Multiple Coding Agents in Parallel on a Backlog to Achieve Step-Function Productivity

> Back to [[experiments-index]]

Source: **[From AI-Assisted to AI-Native: Building a Frontier Development Team — Clare Liguori, AWS](https://www.youtube.com/watch?v=pqlWNihgdjI)** · aie · 2026-08-29

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If engineers shift from single-agent synchronous interaction to running multiple coding agents in parallel on a well-scoped task backlog (with minimal intervention, targeting hours-long autonomous runs), then team deployment velocity will increase by 4-10x, because the bottleneck moves from code-writing time to task decomposition and review rather than implementation.

## What they did

Clare Liguori described Amazon's internal 'frontier development' pilots. The Bedrock Mantle team rebuilt an inference data plane with 6 engineers in 76 days (estimated 30 people × 18 months). A Prime Video 10-day sprint with 6 engineers reduced a 90-week project estimate to 24 weeks. Amazon Stores ran a 50-team pilot and found a 4.5x median productivity improvement (deployment velocity) with some teams exceeding 10x. The key differentiator: teams that used agents for hands-off, long-running parallel tasks vs. synchronous pair-programming-style use. Frontier developer behaviors: writing ~1-2% of code themselves, running agents for hours without intervention, running multiple agents in parallel. She also identified new bottlenecks: organizational decision speed, launch approval processes, and reviewing AI output being harder than writing it for junior engineers.

## Relevance to YOLO loop

Core to the YOLO loop architecture: moving from one agent at a time to a parallel multi-agent task queue with overnight runs is the structural change that unlocks step-function gains. Requires investing in task decomposition, well-scoped CLAUDE.md context, and async review workflows.

## Notes

Liguori's warning: must 'slow down to speed up' — teams need 2 months to invest in codebase context and best practices before parallelizing. Also: decision-making speed (not code speed) becomes the new bottleneck once agents handle implementation. Prioritize reversible decisions to keep velocity high.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-29 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-29-amazon-frontier-dev-parallel-agents` |
| Channel | aie |
| Video | [From AI-Assisted to AI-Native: Building a Frontier Development Team — Clare Liguori, AWS](https://www.youtube.com/watch?v=pqlWNihgdjI) |
| Published | 2026-08-29 |
| Ingested upstream | 2026-08-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
