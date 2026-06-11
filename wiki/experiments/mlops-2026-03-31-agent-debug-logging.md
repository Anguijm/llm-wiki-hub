# Add structured debug logging at agent decision points to speed up failure diagnosis

> Back to [[experiments-index]]

Source: **[Decomposing the Agent Orchestration System: Lessons Learned](https://www.youtube.com/watch?v=H9fsxdK-NeQ)** · mlops · 2026-03-31

**Status:** `done` · **Verdict:** `adopt` · **Effort:** `low`

---

## Hypothesis

If we emit structured log events at each major agent decision (tool call initiated, response evaluated, branch taken, test outcome), then diagnosing build failures takes minutes instead of hours because we have a complete audit trail of what the agent decided and why.

## What they did

Niels Bantilan (Union.ai) at the Coding Agents Conference argued that production agent failures are almost always infrastructure and debuggability failures — not model failures. Durable, self-healing, debuggable systems beat flashy model features. Key lesson: invest in observability before capability.

## Relevance to YOLO loop

YOLO build sessions currently fail silently — if a test fails or Gemini review reveals issues, there's no structured log of what decisions led there. Adding event logging (even to a simple JSONL file) would make post-mortems faster and identify patterns across failures.

## Outcome

Built build_log.py — structured JSON logging per project. Events: idea_selected, plan_created, gemini_critique, build_complete, test_result, eval_bugs, council_review, fixes, shipped. CLI and Python API. --show for audit trail, --recent for dashboard.

## Notes

Concept reinforced by mlops-2026-03-17-durable-execution-agents (done/adopt). This card focuses on the observability/logging angle specifically.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-03 | `done` | build_log.py created with CLI and Python API |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-03-31-agent-debug-logging` |
| Channel | mlops |
| Video | [Decomposing the Agent Orchestration System: Lessons Learned](https://www.youtube.com/watch?v=H9fsxdK-NeQ) |
| Published | 2026-03-31 |
| Ingested upstream | 2026-04-02 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
