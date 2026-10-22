# Track harness shims in a registry and prune stale ones

> Back to [[experiments-index]]

Source: **[Is the Agent Harness Dead? — Jediah Katz, SpaceXAI](https://www.youtube.com/watch?v=7Y4sbZgBdnc)** · aie · 2026-10-19

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we log every deterministic workaround in our Claude Code harness (hooks, prompt rules) in a central registry with firing telemetry and remove those that stop firing, then the harness will stay lean and avoid technical debt because newer models absorb the behaviors the shims patched.

## What they did

Jediah Katz argued that frontier models have absorbed coding guardrails, citing a UC Berkeley study across 7 models in Pi, Codex and Claude Code that found no significant harness effect on SWE-bench Light, and an Apple/EPFL study showing the same on MLE-bench. He described splitting the harness into a runtime layer and a context/orchestration layer, retiring legacy coding prompts, and tracking temporary deterministic shims in a central registry with bot PRs that remove shims when telemetry shows they stop firing. He also described reusable primitives such as event subscriptions and coordinator bots managing worker fleets. He cautioned that long-running multi-agent tasks cannot rely on personal laptops and that unmonitored shims create debt.

## Relevance to YOLO loop

high: Pruning hooks and prompt rules as models improve is a direct maintenance practice for Claude Code harnesses.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-21 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-19-harness-shim-registry` |
| Channel | aie |
| Video | [Is the Agent Harness Dead? — Jediah Katz, SpaceXAI](https://www.youtube.com/watch?v=7Y4sbZgBdnc) |
| Published | 2026-10-19 |
| Ingested upstream | 2026-10-21 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
