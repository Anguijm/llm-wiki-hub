# Build a skill registry with progressive disclosure and embedding-based retrieval to scale agent capabilities past 10 skills

> Back to [[experiments-index]]

Source: **[Skills are new features: Building Skill-Centric Harness — Yogendra Miraje, FactSet](https://www.youtube.com/watch?v=7jjudsEhBtM)** · aie · 2026-07-29

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we store skills in a registry with name/description/path metadata and inject only skill names and descriptions into the system prompt (progressive disclosure), using embedding similarity search to shortlist relevant skills at runtime, then agent performance will degrade less as the skill library grows past 10 entries because the agent's context window is not saturated with full skill bodies it doesn't need.

## What they did

FactSet moved from 'blueprints' to Anthropic-standard skills and built their own agentic harness. The minimum harness requires a skill registry, system prompt, and file-read tool. Progressive disclosure means only skill name+description+path go into the system prompt; the agent reads the full skill body only when it selects that skill. Beyond 10 skills, they recommend embedding-based similarity search to shortlist candidates. At hundreds of skills, a hierarchy with metadata filters and governance (admission, ownership, boundaries, lifecycle, coherence) is needed. They also learned that model upgrades can break skill compliance even without skill changes, so evals must be re-run on every model update.

## Relevance to YOLO loop

Directly applicable if the YOLO loop uses a growing skill/tool library; the progressive disclosure pattern and embedding-based routing are drop-in architectural improvements to prevent context bloat as capabilities expand.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-29 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-29-skill-centric-harness` |
| Channel | aie |
| Video | [Skills are new features: Building Skill-Centric Harness — Yogendra Miraje, FactSet](https://www.youtube.com/watch?v=7jjudsEhBtM) |
| Published | 2026-07-29 |
| Ingested upstream | 2026-07-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
