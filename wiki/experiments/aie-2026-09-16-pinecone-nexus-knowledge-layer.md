# Build a Persistent Company Knowledge Layer to Give Agents Tribal Knowledge, Not Just Document Retrieval

> Back to [[experiments-index]]

Source: **[Pinecone 2.0 — Edo Liberty, Pinecone](https://www.youtube.com/watch?v=IN-rb-9WmiY)** · aie · 2026-09-16

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we create a persistent, structured knowledge layer capturing company processes, priorities, and tribal knowledge (beyond individual document RAG), then agents will perform tasks with 20-90% fewer tokens, 20-77% faster, and with substantially higher accuracy because they start with organizational context rather than rediscovering it from scratch each session.

## What they did

Edo Liberty (Pinecone) distinguished three knowledge types: general (in model weights), specific (per-document RAG), and tribal (company-wide process knowledge that seasoned employees have but new hires lack). He argued current agents behave like new hires — brilliant but contextless — and proposed a 'knowledge layer' that is persistent (built once, shared across all agents), domain-specialized (HR agents get HR knowledge, infra agents get infra knowledge), and continuously updated (deprecates stale info). He introduced Pinecone Nexus as their implementation: a 'runtime coding agent' that at query time writes and executes code (like a Jupyter notebook) to retrieve knowledge, rather than issuing static database queries. This reduced prompt size from ~150K tokens to <1K tokens for tool specification, cut token consumption by 77-90%, improved speed by 20-77%, and improved accuracy. Nexus entered public preview the day after the talk.

## Relevance to YOLO loop

High relevance: our dev loop currently reinitializes agent context each session. Building a persistent knowledge layer with team conventions, architecture decisions, and workflow processes would reduce the token overhead of context-setting and improve agent decision quality across all tasks.

## Notes

Pinecone Nexus is in public preview as of talk date. Key innovation: runtime code generation for knowledge retrieval (NoQL) vs static query. Three knowledge categories (general/specific/tribal) is a useful mental model for designing what goes in agent system prompts vs RAG vs knowledge layer. Domain experts should own and maintain their domain's knowledge slice.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-16 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-16-pinecone-nexus-knowledge-layer` |
| Channel | aie |
| Video | [Pinecone 2.0 — Edo Liberty, Pinecone](https://www.youtube.com/watch?v=IN-rb-9WmiY) |
| Published | 2026-09-16 |
| Ingested upstream | 2026-09-16 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
