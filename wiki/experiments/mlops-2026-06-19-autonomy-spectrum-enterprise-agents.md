# Gate agent autonomy by reversibility and blast radius using a three-tier classification

> Back to [[experiments-index]]

Source: **[Autonomous Agents at Work: From OpenClaw Hype to Enterprise Reality](https://www.youtube.com/watch?v=_p_xjaf7XFw)** · mlops · 2026-06-19

**Status:** `adopted` · **Verdict:** `adopt` · **Effort:** `medium`

---

## Hypothesis

If we classify agent tasks into reversible, sensitive, and consequential tiers before execution and apply matching approval gates, then we will reduce catastrophic agent mistakes in production because the gate friction is proportional to the actual risk of the action.

## What they did

Pramod (PwC) described a framework for enterprise agent deployment. He classified agent work into three categories: (1) reversible work (ticket enrichment, summarization, RCA—can be autonomous), (2) sensitive work (production changes affecting system stability—needs tighter controls and testing), (3) consequential work (customer-facing, policy/legal docs—highest blast radius, strictest gatekeeping). He layered this with an autonomy progression: assistant mode → recommend mode (agent suggests but doesn't act) → gated action mode (agent acts but checks in at each step). He also described a control plane including agent-owned credentials with proper expiration/authorization as a foundational guardrail.

## Relevance to YOLO loop

The three-tier classification and autonomy progression model can be applied to YOLO loop task routing: low-risk tasks run fully autonomous, medium-risk tasks surface recommendations for human confirmation, high-risk tasks require explicit approval before tool calls execute.

## Notes

Speaker also emphasized that humans must own system architecture even when agents own code blocks. Relevant to YOLO loop design reviews.

Backlog triage 2026-06-24 (owner-preference model). Gate autonomy by reversibility/blast-radius — mirrors the harness's hard-to-reverse-confirm doctrine + escalation.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-19 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-06-19-autonomy-spectrum-enterprise-agents` |
| Channel | mlops |
| Video | [Autonomous Agents at Work: From OpenClaw Hype to Enterprise Reality](https://www.youtube.com/watch?v=_p_xjaf7XFw) |
| Published | 2026-06-19 |
| Ingested upstream | 2026-06-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
