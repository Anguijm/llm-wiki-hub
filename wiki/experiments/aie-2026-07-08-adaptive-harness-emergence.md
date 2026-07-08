# Allow agent harness roles and tooling to emerge mid-run rather than being fully pre-defined

> Back to [[experiments-index]]

Source: **[Beyond the Harness: A Journey Towards Adaptative Engineering - Rajiv Chandegra, Annicha Labs](https://www.youtube.com/watch?v=qdZzND79mcg)** · aie · 2026-07-08

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we design a minimal constraint set at the start of an agentic engineering run and allow agent roles, tool assignments, and sequencing to self-organize mid-runtime in response to the problem, then overall task performance on dynamic or real-world problems will improve compared to a fully pre-defined harness, because fixed harnesses become brittle when the problem space changes unexpectedly during execution.

## What they did

Rajiv Chandegra proposed a design philosophy called 'adaptive engineering' contrasted with the current 'fixed harness' paradigm. In the fixed paradigm, all agent roles, tools, sequencing, and memory protocols are defined ahead of runtime (e.g., Claude Code, Cursor, LangChain). In the adaptive paradigm, the engineer instead defines only high-level constraints ('rules of play') and allows the harness structure—agent specializations, orchestration topology, tool availability—to emerge, stabilize, shift, and eventually dissolve during the engineering runtime itself. He argued this is necessary as AI engineering moves into real-world multi-agent, multi-human, cross-institutional scenarios where no pre-defined structure can anticipate all contingencies.

## Relevance to YOLO loop

Directly challenges the static system-prompt and role definition approach used in our dev loop. An experiment would involve starting a YOLO loop session with only a goal and minimal guardrails, then observing whether agents self-organize more effective sub-roles and tool usage patterns than our hand-crafted harness produces.

## Notes

Rajiv noted key failure modes to watch: false attractors (stable but suboptimal structures), lack of genuine selection pressure leading to drift, monoculture risk among agents, and collapse of legibility/auditability. Any experiment should instrument heavily to detect these failure modes.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-08 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-08-adaptive-harness-emergence` |
| Channel | aie |
| Video | [Beyond the Harness: A Journey Towards Adaptative Engineering - Rajiv Chandegra, Annicha Labs](https://www.youtube.com/watch?v=qdZzND79mcg) |
| Published | 2026-07-08 |
| Ingested upstream | 2026-07-08 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
