# Add an ontology-based validator after each agent tool call to catch semantically invalid outputs before they propagate

> Back to [[experiments-index]]

Source: **[Why Agentic Systems Need Ontologies — Frank Coyle, UC Berkeley](https://www.youtube.com/watch?v=Sir59K8ZDPU)** · aie · 2026-07-23

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we run tool call outputs through a domain ontology reasoner (OWL/RDFS constraints) before passing them back to the agent, then we catch a class of semantic errors (duplicate refunds, wrong recipient types, invalid status values) that Pydantic type checks miss, because ontologies can express relational and disjoint constraints that pure type systems cannot.

## What they did

Frank Coyle (Berkeley) presented a pattern for grounding LLM agents with ontologies at tool-call boundaries. His architecture: Pydantic validates types at the input gate, the tool executes, and an ontology reasoner validates the output before returning to the agent. He gave concrete examples of errors ontologies catch that code alone misses: a second refund on the same order (functional property violation), a payout sent to a support rep instead of a buyer (disjoint class violation), an invalid status value like 'probably shipped' (enumerated value constraint). He positioned neuro-symbolic AI (LLM + ontology reasoner) as guardrails that keep probabilistic agents honest by checking whether their outputs are consistent with a formal domain specification.

## Relevance to YOLO loop

Our yolo loop likely validates tool outputs only via Pydantic or not at all. A lightweight OWL/RDFS ontology for our core domain (even a small one covering 5-10 key entity constraints) placed at the tool-call return boundary would catch a category of agent mistakes — particularly in multi-step loops where an invalid intermediate output silently corrupts downstream reasoning.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-23 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-23-ontology-validator-for-agent-tool-outputs` |
| Channel | aie |
| Video | [Why Agentic Systems Need Ontologies — Frank Coyle, UC Berkeley](https://www.youtube.com/watch?v=Sir59K8ZDPU) |
| Published | 2026-07-23 |
| Ingested upstream | 2026-07-23 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
