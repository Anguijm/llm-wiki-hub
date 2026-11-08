# Expose the Markdown vault as a queryable MCP endpoint

> Back to [[experiments-index]]

Source: **[Behind Latent Space: Kill My SaaS, Jev & AI in 2026 | AIEi Shanghai](https://www.youtube.com/watch?v=QmDLDy3ZSNE)** · ls · 2026-11-04

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we package the Markdown knowledge vault as a read-only MCP server, then the agents that write the newsletters can query past notes on demand because structured context is cheaper than pasting notes into prompts.

## What they did

Swyx described transcribing and deep-researching all AI Engineer conference presentations and speaker profiles. The resulting dataset is published as a downloadable file and an MCP endpoint at aiengineer.com/data, so agents can query the whole archive as context.

## Relevance to YOLO loop

medium: Serving an archive to agents over MCP is a common pattern, and it overlaps with the existing on-demand loading of tools and skills.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-11-07 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `ls-2026-11-04-vault-mcp-endpoint` |
| Channel | ls |
| Video | [Behind Latent Space: Kill My SaaS, Jev & AI in 2026 | AIEi Shanghai](https://www.youtube.com/watch?v=QmDLDy3ZSNE) |
| Published | 2026-11-04 |
| Ingested upstream | 2026-11-07 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
