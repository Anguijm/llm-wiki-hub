# Audit PAI agent stack against the 12 critical agent architecture pieces

> Back to [[experiments-index]]

Source: **[I Broke Down Anthropic's $2.5 Billion Leak. Your Agent Is Missing 12 Critical Pieces.]()** · nb · 2026-04-02

**Status:** `done` · **Verdict:** `adopt` · **Effort:** `medium`

---

## Hypothesis

If we audit our agent infrastructure against Anthropic's leaked 12-piece agent architecture checklist, then we identify structural gaps (missing guardrails, evaluation layers, memory systems, etc.) because Anthropic's internal architecture reflects what they've learned building production agents at scale.

## What they did

Nate broke down Anthropic's leaked $2.5B internal agent architecture into 12 critical components that production agents need. The implication is most DIY agents are missing key structural pieces.

## Actionable steps

- Enumerate the 12 architectural pieces from the video (watch or find summary)
- Map each piece to existing PAI infrastructure (CLAUDE.md, Algorithm, Council, MCP tools, etc.)
- Identify the 2-3 biggest gaps and prioritize them for the next Tick session
- Document findings in a gap-analysis card for the YOLO loop

## Success metric

At least 2 previously missing architectural pieces identified and addressed.

## Relevance to YOLO loop

PAI is a production agent system. Validating its architecture against Anthropic's internal best practices ensures we aren't missing critical infrastructure layers.

## Target projects

- [[yolo-projects]] (`yolo-loop-infrastructure`)

## Outcome

Full 12-piece audit completed. Result: 5 STRONG, 5 ADEQUATE, 2 WEAK. Weak areas: human escalation path (no explicit trigger when autonomous builds fail) and cost management (no token tracking or spend caps). 262-line audit report saved.

## Notes

Title-only inference. Need to watch video or find summary for the actual 12 pieces.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-03 | `backlog` | Ingested from Phase 4 YouTube pipeline — title-only inference |
| 2026-04-04 | `done` | Implemented and verified |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-04-03-agent-architecture-12-pieces` |
| Channel | nb |
| Published | 2026-04-02 |
| Ingested upstream | 2026-04-03 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
