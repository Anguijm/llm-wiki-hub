# Add a Shared Database-Backed Memory Broker to Multi-Agent or Multi-Developer Workflows

> Back to [[experiments-index]]

Source: **[No Memory, No Harness: Why the Database Is the Last Line of Defense — Kay Malcolm, Oracle](https://www.youtube.com/watch?v=jA_x7F8caHI)** · aie · 2026-09-14

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we persist agent memory (procedural, episodic, semantic, long-term) to a shared database rather than relying on per-session context windows or file-system memory, then teams of agents or developers can share context across sessions and forks without losing intent, because git records code but not human/agent intent, and file-system memory fails to scale past a single agent instance.

## What they did

Kay Malcolm described the problem her Oracle team faced: AI made individual developers faster but not the team more productive, because Codex context was not shared across time zones — the US team got code commits without the context that generated them. She built 'Py', a memory broker agent backed by Oracle Autonomous Database using the Oracle Agent Memory SDK (pip install oracle-agent-memory). Py categorizes memory into five types (short-term, long-term, episodic, procedural, semantic), stores live conversations and facts, determines what is worth keeping, and makes it retrievable across sessions and git forks. The result: developers shared not just code but context; diverging repositories were resolved; team productivity increased. She cited an OpenAI paper on their in-house data agent confirming memory was crucial for correct filtering, and Harrison Chase's quote: 'Your harness, your memory. If you don't own your harness, you don't own your memory.'

## Relevance to YOLO loop

Our YOLO loop loses context between runs and across contributors. Adding a lightweight memory broker — even a simpler key-value store with session tagging — that persists agent reasoning, decisions made, and rationale would directly address context loss between loop iterations and across team members.

## Notes

Oracle Agent Memory SDK: pip install oracle-agent-memory. Requires Oracle Autonomous DB or OCI (always-free tier available). The five memory type taxonomy (short-term, long-term, episodic, procedural, semantic) is a useful classification framework for designing any agent memory system regardless of storage backend.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-14 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-14-oracle-agent-memory` |
| Channel | aie |
| Video | [No Memory, No Harness: Why the Database Is the Last Line of Defense — Kay Malcolm, Oracle](https://www.youtube.com/watch?v=jA_x7F8caHI) |
| Published | 2026-09-14 |
| Ingested upstream | 2026-09-14 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
