# Evaluate agent reasoning quality using dynamic state-inference tasks where causal chains are opaque

> Back to [[experiments-index]]

Source: **[Training Frontier Models to Out-Think Hackers — Uri Rolls, Arithmetic & Thom Wolf, Hugging Face](https://www.youtube.com/watch?v=O-CBZ3JtRvo)** · aie · 2026-07-24

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we test agents on tasks requiring them to build and update an internal world model from indirect observations (actions at one location cause effects elsewhere, zero prior information about system topology), then we get a more accurate measure of genuine reasoning capability than standard benchmarks because current frontier models have 1-2% success rates on such tasks despite high scores on static knowledge benchmarks.

## What they did

Described a cybersecurity benchmark developed by Arithmetic where agents must compromise systems with zero prior information: no knowledge of authentication mechanisms, network topology, or microservice structure—only a known zero-day entry point. Agent must infer the dynamic state of the environment from its own actions and their effects, similar to ARC-AGI 3. Current frontier models score 1-2% on the generic version. Argued this reveals a fundamental gap: models can read code and find known vulnerability patterns (mythos-style) but cannot build dynamic causal world models on the fly. Proposed that post-training on this benchmark data would create specialized defensive models that respond faster than attackers, since defenders need to understand the full attack surface while attackers only need one crack.

## Relevance to YOLO loop

Less directly applicable to the YOLO loop's current scope, but the dynamic world-model evaluation pattern is relevant for any skill that requires agents to diagnose opaque systems (production outages, data pipeline failures) where the causal structure is unknown. The 1-2% benchmark result is a useful calibration anchor for setting expectations on diagnostic agent tasks.

## Notes

Primarily relevant as a safety/capability research signal rather than an immediate YOLO loop experiment. The open-source vs closed-source framing for defensive AI is worth tracking. Hugging Face's Thomas Wolf involvement suggests potential for open post-training data release.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-24 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-24-cyber-benchmark-dynamic-world-model` |
| Channel | aie |
| Video | [Training Frontier Models to Out-Think Hackers — Uri Rolls, Arithmetic & Thom Wolf, Hugging Face](https://www.youtube.com/watch?v=O-CBZ3JtRvo) |
| Published | 2026-07-24 |
| Ingested upstream | 2026-07-24 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
