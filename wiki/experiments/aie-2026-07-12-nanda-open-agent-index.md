# Register an agent on the NANDA open index and test cross-organization agent discovery

> Back to [[experiments-index]]

Source: **[The Agentic Web and the Bazaar Era of AI - Ramesh Raskar, MIT Media Lab](https://www.youtube.com/watch?v=sum9DgexFRQ)** · aie · 2026-07-12

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we publish one of our agents to the NANDA index (host39.org) with a signed agent-facts record, then we can validate whether open cross-vendor agent discovery is practically usable today, because NANDA provides the DNS-equivalent layer (identity, capability advertisement, message-box routing) that is currently missing from walled-garden agent platforms.

## What they did

Ramesh Raskar (MIT Media Lab) and Maria presented Project NANDA—an open-source infrastructure for an internet of AI agents analogous to the open web vs AOL. The stack includes: (1) a NANDA Index (discovery layer at host39.org) where agents publish signed 'agent-facts records' describing capabilities, tools, access rules, and endpoints; (2) adaptive resolution routing messages through a message-box that filters spam and holds messages until the agent is ready; (3) Open Clo, a self-hosted agent gateway; (4) Maritime, a sleep/wake cloud hosting platform for cost-effective multi-agent deployment; and (5) NANDA Town, an open-source discrete-event simulator for testing agent coordination protocols (discovery, identity, payments, consensus) at scale before deploying to production.

## Relevance to YOLO loop

If our agents need to call external specialist agents (e.g. a research agent, a code-review agent from another team), the NANDA index is a concrete open alternative to building proprietary inter-agent APIs. Low effort to register and test; high strategic value if the standard gains adoption.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-12 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-12-nanda-open-agent-index` |
| Channel | aie |
| Video | [The Agentic Web and the Bazaar Era of AI - Ramesh Raskar, MIT Media Lab](https://www.youtube.com/watch?v=sum9DgexFRQ) |
| Published | 2026-07-12 |
| Ingested upstream | 2026-07-12 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
