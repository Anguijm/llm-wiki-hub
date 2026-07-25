# Build a Private Agent Benchmark from Production Traces for Repeatable Offline Evaluation

> Back to [[experiments-index]]

Source: **[From Agent Traces to Agent Simulations — Rustem Feyzkhanov, Snorkel AI](https://www.youtube.com/watch?v=Ib5t2RLtxvM)** · aie · 2026-07-25

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we convert production agent traces into a private simulation benchmark with deterministic environments, then we can compare agent configurations (model, prompt, tool set) on cost, latency, and success rate in a repeatable apples-to-apples way because offline simulation removes the non-determinism of live tool state and database versions.

## What they did

Rustem described Snorkel AI's approach to agent evaluation. They run millions of agent simulations per month. The workflow: capture production traces (input prompt, actions taken, output), construct benchmark tasks from those traces with mocked environments that replicate real tools, APIs, policies, and DB state, then run the agent under different configurations offline. Verifiers (LLM-based and human SMEs) score outputs on pass rate, cost, latency, and retries. The benchmark serves three purposes: initial release gate, regression test on every config change, and training data for fine-tuning a smaller model to match a larger one. He recommended an 80/20 train/validation split, coverage of both happy-path and edge cases, and connecting the observability and experimentation systems so traces continuously repopulate the benchmark dataset.

## Relevance to YOLO loop

Core infrastructure for our loop: we need exactly this to confidently swap models, change prompts, or modify tool sets without regressions. The trace-to-task pipeline is the missing piece between our current ad-hoc testing and a reliable release gate. Start small: instrument one loop, capture 20-30 traces, hand-craft 5 simulation tasks, add one LLM verifier.

## Notes

Rustem noted SME review should focus on disagreement cases between agent and verifier, not blanket review of everything. Fine-tuning a small planner model using simulation-generated traces was mentioned as a concrete outcome; link to Snorkel website example shared in talk.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-25 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-25-agent-simulation-benchmark-from-traces` |
| Channel | aie |
| Video | [From Agent Traces to Agent Simulations — Rustem Feyzkhanov, Snorkel AI](https://www.youtube.com/watch?v=Ib5t2RLtxvM) |
| Published | 2026-07-25 |
| Ingested upstream | 2026-07-25 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
