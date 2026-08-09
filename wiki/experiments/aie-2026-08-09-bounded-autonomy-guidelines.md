# Define Bounded Autonomy Guidelines Specifying What Agents Can and Cannot Touch

> Back to [[experiments-index]]

Source: **[Guide, Verify, Solve — Anirban Chatterjee, Sonar](https://www.youtube.com/watch?v=03l29gJXpCE)** · aie · 2026-08-09

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If teams establish explicit bounded autonomy rules for AI agents (what files, systems, and decisions are off-limits), then agents will be safer to run autonomously and human oversight can focus on the highest-risk decision points rather than reviewing everything.

## What they did

Chatterjee recommended establishing bounded autonomy guidelines as a governance primitive: give agents freedom to generate code but enforce centralized verification constraints. He framed the ACDC pattern—give agents context up front, verify with independent metrics, and use agents to fix their own mistakes. He also emphasized standardizing on a single multi-layered verification platform across all teams and tools to eliminate blind spots from siloed tooling.

## Relevance to YOLO loop

Maps directly to defining the permission boundary in the YOLO loop—documenting which paths, services, and architectural decisions require human approval before the agent proceeds, and which it can execute autonomously.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-09 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-09-bounded-autonomy-guidelines` |
| Channel | aie |
| Video | [Guide, Verify, Solve — Anirban Chatterjee, Sonar](https://www.youtube.com/watch?v=03l29gJXpCE) |
| Published | 2026-08-09 |
| Ingested upstream | 2026-08-09 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
