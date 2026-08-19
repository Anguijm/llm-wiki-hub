# Build dual-era MCP servers that serve both stateless and stateful clients from a single endpoint during transition

> Back to [[experiments-index]]

Source: **[MCP 728: What Changes, What Breaks, and What You Need to Do About It](https://www.youtube.com/watch?v=rKqg5JtP5KI)** · mlops · 2026-08-19

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we implement dual-era MCP servers that detect whether an incoming client uses the modern stateless meta-field handshake or the legacy initialize-session pattern and route accordingly, then we can serve both old and new clients without running separate server instances during the 12-month transition period, because the spec defines a clear detection mechanism (presence of meta field vs. initialize request) that allows a single endpoint to branch behavior.

## What they did

Mateo (Margie) explained the three migration paths for MCP server operators: go fully modern (stateless, simplest), stay legacy (works now but clients will eventually drop support), or implement dual-era servers that detect client version from the first message and serve both. He showed a simulation of stateless vs. stateful load balancing, explained why sticky sessions create fragility at deploy time, and described how dual-era is the 'best citizen' approach but carries maintenance cost (two authorization models, two test suites, error-detection callbacks for each). He recommended using a gateway to abstract the complexity. Also noted MCP Inspector and MCP Jam already support both protocol versions for testing.

## Relevance to YOLO loop

Practical migration guidance for any MCP server we operate: during the transition window our servers will receive both legacy and modern clients, and failing to handle both will break agent sessions mid-loop.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-19 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-08-19-mcp-dual-era-server-migration` |
| Channel | mlops |
| Video | [MCP 728: What Changes, What Breaks, and What You Need to Do About It](https://www.youtube.com/watch?v=rKqg5JtP5KI) |
| Published | 2026-08-19 |
| Ingested upstream | 2026-08-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
