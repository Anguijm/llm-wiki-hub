# Build a declarative YAML harness so domain teams can ship compliant agents without AI/security expertise

> Back to [[experiments-index]]

Source: **[Agentic DX: Bringing IDP into your IDE](https://www.youtube.com/watch?v=u3ocH-qdyi4)** · mlops · 2026-08-19

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If domain teams can declare an agent's capabilities, tools, and compliance requirements in a YAML file that is packaged as a Helm chart and deployed into a shared agentic platform, then they will ship working agents faster with consistent security posture and without duplicating AI infrastructure work, because the platform harness handles MCP versioning, zero-trust auth, A2A routing, and human-approval gates centrally.

## What they did

Adnan Waraich (Motorola Solutions) described evolving from a 'bring your own agent' strategy (which caused duplicated R&D and fragmented UX) to a composable agent harness. The harness uses a Perception-Decision-Action-Memory loop internally; agents are declared via YAML + Helm chart; the platform enforces zero-trust execution, per-tool-call human approval (HITL), A2A protocol for inter-agent communication, and short-lived OAuth/OIDC tokens. Domain teams only write business logic. The platform handles security reviews, compliance, and MCP spec updates. A master agent composes specialist sub-agents recursively.

## Relevance to YOLO loop

Directly relevant to scaling our agent fleet: if we want multiple specialized agents contributing to the YOLO loop without each team re-solving auth, MCP versioning, and approval workflows, this declarative harness pattern is the architecture to evaluate.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-19 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-08-19-idp-into-ide-declarative-agent-harness` |
| Channel | mlops |
| Video | [Agentic DX: Bringing IDP into your IDE](https://www.youtube.com/watch?v=u3ocH-qdyi4) |
| Published | 2026-08-19 |
| Ingested upstream | 2026-08-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
