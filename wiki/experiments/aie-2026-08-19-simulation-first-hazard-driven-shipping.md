# Ship AI Agents via Staged Simulation-to-Production Pipeline Anchored to an Explicit Hazard Registry

> Back to [[experiments-index]]

Source: **[Shipping AI to a Million Patients Without an A/B Test — Jared Joselowitz, Ufonia](https://www.youtube.com/watch?v=McknwOzbmyg)** · aie · 2026-08-19

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we enumerate all potential harms as a formal hazard registry and require each hazard to be addressed by a specific simulated test case before any real-user exposure, then we can ship safely without A/B testing on real users, because the evidence base is built proactively rather than reactively and every shipped prompt version traces to the hazards it covers.

## What they did

Ufonia built the MATRIX framework for their voice clinical agent Dora (200,000 real UK clinical calls, contracted to 1M). Because they cannot A/B test on patients, cannot roll back a call, and cannot cite benchmark scores as a safety defense, they adopted a simulation-first approach modeled on self-driving car development. They: (1) enumerate all patient hazards (missed red flags, hallucinated medical answers, ignored distress, etc.); (2) manufacture rare but dangerous cases synthetically rather than waiting for them naturally; (3) run thousands of simulated patient interactions through the agent; (4) use an LLM-judge optimization loop to improve the system; (5) stage real-world exposure through voice actors → supervised clinical evaluation with clinicians in loop → monitored deployment, with autonomy expanding as evidence accumulates. Every prompt version, dataset, and judge verdict traces back to the specific hazard it addresses. They treat voice as a new module in the same safety framework (adding hazards like back-channeling mid-safety-advice) rather than a separate system.

## Relevance to YOLO loop

The hazard-registry-to-test-case mapping is the most rigorous formalization of eval-driven development we've seen and is generalizable beyond healthcare. For our loop, maintaining a living hazard registry and requiring coverage before shipping would raise our safety floor significantly.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-19 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-19-simulation-first-hazard-driven-shipping` |
| Channel | aie |
| Video | [Shipping AI to a Million Patients Without an A/B Test — Jared Joselowitz, Ufonia](https://www.youtube.com/watch?v=McknwOzbmyg) |
| Published | 2026-08-19 |
| Ingested upstream | 2026-08-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
