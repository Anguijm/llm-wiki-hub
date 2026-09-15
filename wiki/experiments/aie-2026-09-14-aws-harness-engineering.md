# Deploy a Composable Agent Harness with Managed Memory and Runtime Using Amazon Bedrock Agent Core

> Back to [[experiments-index]]

Source: **[Harness Engineering: Building the Production Cage for Powerful Domain Agents — Mike Chambers, AWS](https://www.youtube.com/watch?v=gxVZ_1tuuq4)** · aie · 2026-09-14

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we use a composable agent infrastructure layer (like Bedrock Agent Core) that separates harness components — memory, runtime, tool connections, observability — into independently adoptable modules, then we can incrementally harden production agents without rewriting existing code, because the harness components can be added to a running agent one at a time rather than requiring an all-or-nothing migration.

## What they did

Mike Chambers defined harness engineering as 'everything in an agent except the model' and demonstrated Amazon Bedrock Agent Core, a composable set of infrastructure primitives for agents built with the Strands agents framework (open source, model-first). He live-coded an agent using the agentcore CLI: scaffolding via 'agentcore init', local development with 'agentcore dev' (spins up a local browser-based chat interface with live reload), and deployment with 'agentcore deploy' (infrastructure-as-code deployment with managed memory, runtime, and tracing). He showed that the harness components (long-term memory, sandboxed execution, tool connections, observability/traces) are individually composable — an existing agent can adopt just the managed memory module without changing its core code. He also showed a minimal harness as pure JSON config (model + system prompt, no Python) that can be deployed directly. AWS is a founding member of the Agentic Foundation (Linux Foundation).

## Relevance to YOLO loop

The composable harness model maps well to our loop's needs: we could adopt Bedrock Agent Core's managed memory module first (lowest effort, highest immediate value for context persistence), then layer in observability and sandboxed execution without rewiring the whole loop.

## Notes

Agent Toolkit for AWS available on GitHub (free). Strands agents framework is open source and model-first. Agent Core is on Amazon Bedrock. MCP Lambda handler by same author: ~35k downloads/month. The 'agents we use vs agents we build' distinction is a useful framing for deciding when token-maxing is acceptable.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-14 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-14-aws-harness-engineering` |
| Channel | aie |
| Video | [Harness Engineering: Building the Production Cage for Powerful Domain Agents — Mike Chambers, AWS](https://www.youtube.com/watch?v=gxVZ_1tuuq4) |
| Published | 2026-09-14 |
| Ingested upstream | 2026-09-14 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
