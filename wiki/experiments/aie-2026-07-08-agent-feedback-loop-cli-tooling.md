# Build a custom CLI tool that gives coding agents application-level feedback loops including screenshots, logs, and service restarts

> Back to [[experiments-index]]

Source: **[Your agent is blindfolded — Johan Lajili, Poolside AI](https://www.youtube.com/watch?v=iRcX54EO5g8)** · aie · 2026-07-08

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we build a domain-specific CLI harness that lets an agent take screenshots of the running app, extract logs from backend and frontend services, restart services, and perform high-level navigation commands, then agent task completion rate will improve because the agent can reproduce bugs before attempting fixes and verify its own work without human intervention.

## What they did

Johan at Poolside built an internal CLI tool called Spoolside for their VS Code extension. It exposes: screenshot capture of the app, token-compressed page snapshots, log extraction from multiple services, service restart commands, and high-level navigation commands that can be composed sequentially. This allowed agents to reproduce bugs before fixing them and verify fixes autonomously. He argued this 'putting the mask on the AI first' investment enables overnight unattended agent runs and multiplication of parallel agents safely. He generalized the pattern: implement as CLI, MCP skill, or other interface depending on the domain; the key is building whatever feedback loop your specific product needs.

## Relevance to YOLO loop

Core to our yolo-loop: the loop needs feedback signals beyond just test pass/fail. This pattern of custom domain-specific observability tooling for agents is directly applicable to giving our agents visibility into running services.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-08 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-08-agent-feedback-loop-cli-tooling` |
| Channel | aie |
| Video | [Your agent is blindfolded — Johan Lajili, Poolside AI](https://www.youtube.com/watch?v=iRcX54EO5g8) |
| Published | 2026-07-08 |
| Ingested upstream | 2026-07-08 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
