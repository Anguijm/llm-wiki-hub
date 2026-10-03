# Implement Least-Privilege + Immutable Evidence Logging for All Agentic Tool Calls

> Back to [[experiments-index]]

Source: **[It's Not Just the Sandbox: An AI Security Insider's 4 Lessons](https://www.youtube.com/watch?v=mHkA9710ars)** · eh · 2026-10-03

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we enforce least-privilege access (agents get only the credentials and network access they need for each specific task) and log all tool calls, network traffic, and chain-of-thought to storage the agent cannot modify, then we reduce the blast radius of a misconfigured or misaligned agent because the agent cannot cover its tracks and human review of incidents is always possible.

## What they did

echohive summarized a post by an OpenAI agent security engineer outlining four lessons from inside frontier model security. The most operationally actionable was lesson two: lock down sandboxes from first principles (give models only the access they need, test that walls hold, attack your own environment with frontier models before scale), and monitor everything—tool calls, network traffic, chain-of-thought, and internal activations—in storage the model cannot touch, with a human authorized to stop the run. The engineer was explicit that these controls apply even to developers building on top of models, not just those training them.

## Relevance to YOLO loop

Applies to any agentic pipeline in our dev loop that touches external APIs, file systems, or credentials. Starting with a checklist—does each agent task spec enumerate exactly which tools and credentials are needed, and do we have an append-only log of what actually executed—would be a low-cost first step before building the full monitoring harness.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-03 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `eh-2026-10-03-ai-security-culture-of-paranoia` |
| Channel | eh |
| Video | [It's Not Just the Sandbox: An AI Security Insider's 4 Lessons](https://www.youtube.com/watch?v=mHkA9710ars) |
| Published | 2026-10-03 |
| Ingested upstream | 2026-10-03 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
