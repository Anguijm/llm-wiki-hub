# Architect agent systems around a Know-Decide-Act-Learn loop with humans and agents on the same substrate

> Back to [[experiments-index]]

Source: **[AI in GTM at Notion — Flora Liu](https://www.youtube.com/watch?v=L4I7WgiEquo)** · aie · 2026-08-27

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we structure our agent system as four explicit layers — Know (trusted context), Decide (single next best action), Act (concrete execution), Learn (feedback into decisioning) — with humans and agents reading from the same context layer, then we will avoid the drift problem of parallel human and agent systems and achieve higher decision consistency, because Notion's early results show 63% lift in users taking the next recommended step when context-aware recommendations are served.

## What they did

Speaker (Notion GTM engineer) described rebuilding Notion's fragmented GTM stack into a unified decisioning system spanning self-serve and sales-assist motions. Architecture has four layers: Know (context layer in Notion markdown, synced from Salesforce/Gong/Snowflake/meeting docs), Decide (single next best action selection), Act (lifecycle email, in-app nudge, or rep task), Learn (outcome feeds back into decisioning). Key design principle: agents and humans operate on the same substrate so they don't drift apart. Agents handle repetitive context-gathering and drafting; humans provide judgment and relationship ownership.

## Relevance to YOLO loop

The Know-Decide-Act-Learn loop is a clean architectural pattern for our YOLO loop. We can implement it as: Know = project state file, Decide = task selection agent, Act = specialist agents, Learn = outcome logging. The 'same substrate' principle means our context file must be readable by both humans reviewing work and agents planning next steps.

## Notes

Build vs. buy insight: own the context layer (your edge), rent orchestration/email/CRM. The context layer must be debuggable and not outsourced.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-27 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-27-notion-know-decide-act-learn-loop` |
| Channel | aie |
| Video | [AI in GTM at Notion — Flora Liu](https://www.youtube.com/watch?v=L4I7WgiEquo) |
| Published | 2026-08-27 |
| Ingested upstream | 2026-08-27 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
