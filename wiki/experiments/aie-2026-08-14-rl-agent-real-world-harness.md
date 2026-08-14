# Add Risk-Aware Execution Guards and Graceful Human-Handoff to Agent Action Loop

> Back to [[experiments-index]]

Source: **[From RL to IRL — Gaurav Mishra, Amazon AGI Lab](https://www.youtube.com/watch?v=Cc0_nyxROBA)** · aie · 2026-08-14

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we wrap an agent's action loop with a harness that detects credential expiry, sponsored/deceptive UI elements, and irreversible-action risk before execution, then real-world task success rates improve because the agent avoids common failure modes (account lockout, wrong-button clicks, adversarial content) that RL training alone does not eliminate.

## What they did

Researchers at Amazon AGI Lab showed that coding agents trained with RL break in predictable ways when deployed on real websites: they guess passwords (causing lockouts), click sponsored buttons that look like real submit buttons, and loop unproductively. Their harness mitigations included: (1) an action risk classifier that flags irreversible actions before execution, (2) credential guardrails that detect session expiry and trigger human handoff instead of guessing, (3) an execution monitor that breaks loops and repeated-click patterns, (4) audit logs of all actions and effects, and (5) calibrated confidence thresholds that force handoff when the model is uncertain. With these in place, agents correctly identified sponsored buttons and handed off credential re-entry to the user.

## Relevance to YOLO loop

The YOLO loop's execution stage runs agent actions that can be irreversible (file writes, API calls, deploys). Adding a thin harness layer that classifies action risk and pauses for confirmation on high-risk actions before executing would prevent costly mistakes without requiring the human to supervise every step.

## Notes

Key design principle from the talk: 'early on the harness is strong and catches all gaps; over time the model improves and the harness becomes thinner.' Start with conservative guardrails and relax them as the agent demonstrates reliable behavior on audit logs.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-14 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-14-rl-agent-real-world-harness` |
| Channel | aie |
| Video | [From RL to IRL — Gaurav Mishra, Amazon AGI Lab](https://www.youtube.com/watch?v=Cc0_nyxROBA) |
| Published | 2026-08-14 |
| Ingested upstream | 2026-08-14 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
