# Create a centralized skills registry with governance and static evaluation against framework best practices to standardize agent behavior across teams

> Back to [[experiments-index]]

Source: **[AI-Native Organisations Run on Skills: How to Structure and Scale Them — Imad Touil, QuantumBlack](https://www.youtube.com/watch?v=M05vON8i0aI)** · aie · 2026-08-29

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we maintain a centralized skills registry where agents can discover and reuse existing skills rather than reinventing them, and evaluate each skill statically against framework best practices (e.g., Anthropic's skill invocation guidelines), then we will see quality and productivity converge upward across teams because the agent's harness will automatically pull the governed skill instead of generating a lower-quality ad-hoc version.

## What they did

Imad from QuantumBlack described the full agentic software stack and argued that ungoverned skills (reusable instruction+tool units) are the primary source of quality and cost variance across engineering teams. Teams without shared skills burn more tokens (agent must rediscover approaches), produce inconsistent quality, and have higher security risk. When a centralized skill is published, the next agent encountering that task class automatically pulls the governed version. He showed heat-map productivity data comparing teams with and without skill governance. Near-term roadmap: skills registry (internal developer portals are starting to include this), skills eval (static evaluation against Anthropic best practices as a proxy for invocation quality), and auto-evolving skills (closed-loop skill improvement with guardrails). He also described the full SDLC workflow decomposed into skills: product strategy, market research, discovery, data product delivery, product increment, platform engineering ops—each as a distinct skill domain.

## Relevance to YOLO loop

A skills registry is the instruction-management backbone for the YOLO loop at team scale: rather than each developer maintaining their own prompt library, a shared governed registry ensures the loop uses the best-known approach for each task class and improves it centrally.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-29 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-29-skills-registry-governance` |
| Channel | aie |
| Video | [AI-Native Organisations Run on Skills: How to Structure and Scale Them — Imad Touil, QuantumBlack](https://www.youtube.com/watch?v=M05vON8i0aI) |
| Published | 2026-08-29 |
| Ingested upstream | 2026-08-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
