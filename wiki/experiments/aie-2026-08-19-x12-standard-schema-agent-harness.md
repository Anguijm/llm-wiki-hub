# Ground Agent Memory and Transactions in a Domain-Standard Schema to Constrain Action Space

> Back to [[experiments-index]]

Source: **[Healthcare's Agent Bytecode: X12 as the Harness for AI Agents — Vasant Kearney, Onlay](https://www.youtube.com/watch?v=UyyOoJmuATU)** · aie · 2026-08-19

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we ground agent internal state and outputs in an established domain-standard schema (like X12 for healthcare claims), then agent actions become interpretable, auditable, and bounded without requiring custom schema design, because the standard schema provides a shared vocabulary that new engineers can look up and that constrains the agent to valid transaction types.

## What they did

Kearney described using the X12 EDI standard as the 'bytecode' for healthcare insurance AI agents. Rather than letting agents invent their own internal representations, all agent transactions — eligibility checks, claim submissions, status updates, EOBs — are normalized to X12 format internally even when the source is a web portal, phone call, or FHIR feed. This gives agents a standard action space, makes memory storable in a well-understood format, and allows new engineers to look up any transaction type. He also described a skeptical, cost-aware approach: use small cheap models for high-frequency routine steps and reserve larger models only where cheaper ones fail.

## Relevance to YOLO loop

Generalizable principle: for any vertical domain, grounding agent state in an existing standard schema reduces the design surface and improves auditability. For our loop, we should evaluate whether a standard schema exists for our domain and whether normalizing agent outputs to it simplifies debugging.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-19 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-19-x12-standard-schema-agent-harness` |
| Channel | aie |
| Video | [Healthcare's Agent Bytecode: X12 as the Harness for AI Agents — Vasant Kearney, Onlay](https://www.youtube.com/watch?v=UyyOoJmuATU) |
| Published | 2026-08-19 |
| Ingested upstream | 2026-08-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
