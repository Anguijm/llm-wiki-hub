# Evaluate each tool/action in your agent for semantic meaning, not just access

> Back to [[experiments-index]]

Source: **[The Work Primitive: What Every AI Product Leader Gets Wrong](https://www.youtube.com/watch?v=b1fxYGPbHeo)** · nb · 2026-05-09

**Status:** `deferred` · **Effort:** `medium`

---

## Hypothesis

If we evaluate agent tools by whether they expose semantic meaning (intent, permissions, reversibility, context) and not just technical access, then we will build more robust and trustworthy agentic systems because agents fail most often in the gap between what an action looks like and what it actually means.

## What they did

Speaker introduced the concept of the 'semantic work primitive' as a layer beneath computer use access. Using examples like moving a calendar invite or clicking 'buy', he argued that computer use gives agents hands but semantic primitives tell agents what they are touching and why it matters. He described three layers: access (computer use/MCP), meaning (semantic work primitives), and authority (permissions/governance). He criticized products that only provide access without meaning, using Salesforce vs SAP as a case study in semantic openness.

## Relevance to YOLO loop

Applicable to tool design in our loop: when we add new MCP tools or Claude Code actions, we should document not just what the tool does mechanically but its semantic contract, reversibility, and permission implications.

## Notes

Deferred 2026-05-10: 'semantic work primitive' framing; needs a concrete product test before we build. Revisit when we can attach it to a tock.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-05-09 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-05-09-semantic-work-primitive-product-test` |
| Channel | nb |
| Video | [The Work Primitive: What Every AI Product Leader Gets Wrong](https://www.youtube.com/watch?v=b1fxYGPbHeo) |
| Published | 2026-05-09 |
| Ingested upstream | 2026-05-09 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
