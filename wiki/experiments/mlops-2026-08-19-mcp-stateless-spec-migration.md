# Migrate MCP server to stateless mode for horizontal scalability and zero sticky-session headaches

> Back to [[experiments-index]]

Source: **[MCP Release Overview: Stateless and the Big Changes in the New Spec](https://www.youtube.com/watch?v=-uvKf47fbbY)** · mlops · 2026-08-19

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we rebuild our MCP server to the new stateless spec (no session ID, all context carried in each request's meta field, standard OAuth without custom auth server), then we can deploy it behind a standard load balancer with any number of replicas, roll deployments without connection loss, and drop the shared session store, because stateless HTTP allows any replica to answer any request independently.

## What they did

Alex (Block/Goose, MCP steering committee) gave a spec-level overview of the largest MCP protocol change since launch. Key changes: statelessness eliminates per-session server state and sticky-session load balancer requirements; multi-roundtrip requests (MRTR) replace the old server-to-client request model; extensions (like Tasks) are now a formal independently-versioned process; authorization was improved so builders use off-the-shelf OAuth providers instead of custom auth servers; roots, sampling, and logging are deprecated. He recommended all builders use official SDKs (TypeScript, Python, Kotlin, Rust) to absorb protocol changes rather than manually constructing messages.

## Relevance to YOLO loop

Infrastructure-level improvement: stateless MCP servers remove the biggest operational headache in our agent backend—sticky sessions breaking on deploys—making the YOLO loop more resilient to infrastructure events.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-19 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mlops-2026-08-19-mcp-stateless-spec-migration` |
| Channel | mlops |
| Video | [MCP Release Overview: Stateless and the Big Changes in the New Spec](https://www.youtube.com/watch?v=-uvKf47fbbY) |
| Published | 2026-08-19 |
| Ingested upstream | 2026-08-19 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
