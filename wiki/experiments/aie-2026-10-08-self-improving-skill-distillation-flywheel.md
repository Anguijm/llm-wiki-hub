# Auto-Distill Successful Agent Runs Into Reusable Skills to Create a Self-Improving Org Flywheel

> Back to [[experiments-index]]

Source: **[From 36% to 100%: How Self-Improving Agents Write Their Own Skills — Rafal Wilinski, Runlayer](https://www.youtube.com/watch?v=u-o0sW9nwmk)** · aie · 2026-10-08

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we automatically distill successful agent run trajectories into skill playbooks (with PII/injection scanning) and serve them via MCP to all future agent sessions, then task success rates will improve over time without model upgrades, because agents guided by retrieved institutional knowledge avoid repeating failed approaches and narrow their search space on hard problems.

## What they did

Rafal Wilinski from Runlayer presented a self-improving organizational flywheel: (1) agents complete tasks, (2) successful runs are grouped by similarity and distilled into skill playbooks using the frontier model, (3) skills are scanned for prompt injection and PII, (4) approved skills land in a central library served via MCP gateway to all agents company-wide, (5) future agents with similar tasks retrieve relevant skills via progressive disclosure (summary first, full content on demand). He showed a benchmark improvement from 36% to 100% task completion rate on a specific task type after skill distillation. He argued this creates a moat competitors cannot copy (internal culture/procedures) and provides resilience against model deprecation (skills encode the knowledge independently of which model discovered it). Key problems with current skill ecosystems: they are developer-centric (non-technical staff can't contribute), discovery is poor (agents don't know when to use which skill), and quality is unverified (some npm skill packages contain prompt injections).

## Relevance to YOLO loop

This is a direct architectural upgrade for our YOLO loop: instead of re-discovering solutions each run, we can accumulate a growing library of verified solution patterns that continuously raise the floor of agent performance on recurring task types.

## Notes

Runlayer scans thousands of skills daily and finds prompt injections in the wild — must implement scanning pipeline before adding any external skills. Progressive disclosure pattern: agent sees only skill summary in initial context, fetches full content when it determines relevance. Start with a small high-frequency task type to validate flywheel before org-wide rollout.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-08 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-08-self-improving-skill-distillation-flywheel` |
| Channel | aie |
| Video | [From 36% to 100%: How Self-Improving Agents Write Their Own Skills — Rafal Wilinski, Runlayer](https://www.youtube.com/watch?v=u-o0sW9nwmk) |
| Published | 2026-10-08 |
| Ingested upstream | 2026-10-08 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
