# Build a config-driven eval harness with hard launch gates, simulated multi-turn conversations, and online regression monitoring

> Back to [[experiments-index]]

Source: **[Build Evals That Actually Matter - Nick Ung, Lyft](https://www.youtube.com/watch?v=3z2uT5aDx_Y)** · aie · 2026-07-19

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we implement a YAML-config-driven eval harness with (a) LLM-simulated multi-turn conversations against synthetic production-representative datasets, (b) LLM-as-judge graders tied to hard launch gates, and (c) online production graders with human-in-the-loop error analysis, then agent regression will be caught before it reaches live users and eval results will be trusted and acted upon, because floating scores with no gate are ignored while gated scores force decision accountability.

## What they did

Lyft's customer support AI team described their end-to-end eval pipeline built over ~2 years. Offline eval: synthetic dataset representative of production traffic, LLM user simulator plays out complete multi-turn conversations, LLM-as-judge grades interaction quality, hard launch gate blocks production deploy if criteria not met. Online eval: production trace capture, online LLM grader, human-in-the-loop error analysis feeding back to dev team. Three failure modes they identified: (1) grader scores not tied to a meaningful gate so nobody acts on them; (2) LLM judges that are too generic/noisy to be trusted; (3) no clear regression ownership when production degrades. Eval harness is YAML config-driven so analysts and data scientists (not just engineers) can contribute evals; runs locally during dev, at pre-commit hooks, and in CI/CD. Future work: systematizing scattered notebook scripts into the harness, and fine-tuning sub-agent models with real user signal + reinforcement learning.

## Relevance to YOLO loop

Core infrastructure for the YOLO loop's quality gate. The harness pattern (YAML configs, parallelized runs, pre-commit hooks, CI/CD integration) should be adopted for any agentic workflow in the loop. The three failure modes are a direct checklist: ensure every grader is gated, every judge is task-specific, and every regression has a named owner.

## Notes

Eval harness primitives defined: task, dataset, persona, LM adapter, evaluator. Key insight: 'we don't want to use live users as test data for our agents.' Multi-turn simulation is the distinguishing requirement vs. single-turn evals. Post-training roadmap: reward modeling for RL on real user signals.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-19 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-19-eval-pipeline-customer-support` |
| Channel | aie |
| Video | [Build Evals That Actually Matter - Nick Ung, Lyft](https://www.youtube.com/watch?v=3z2uT5aDx_Y) |
| Published | 2026-07-19 |
| Ingested upstream | 2026-07-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
