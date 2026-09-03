# Run agents as the requesting user's identity via per-user Kubernetes namespaces and a sidecar credential injector

> Back to [[experiments-index]]

Source: **[Tethered: Our Agents Are Us — Shu Fang, Two Sigma](https://www.youtube.com/watch?v=wCIYViPd4SU)** · aie · 2026-09-03

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we provision per-user namespaces in our compute cluster where every container mounts the user's own identity via a sidecar credential service, then agents will automatically inherit correct permissions without requiring a separate machine identity to be kept in sync, because the agent is literally running as the user and every downstream system enforces that user's existing ACLs.

## What they did

Shu Fang described how Two Sigma runs agents as the exact user identity (not a machine identity) by leveraging per-user Kubernetes namespaces that already existed for automated jobs and research notebooks. A controller spins up compute, a sidecar pulls down credentials from an identity service, and the container mounts and runs as that user. They add an X-LLM-Agent HTTP header for auditability to distinguish human vs. agent actions in logs without requiring a separate identity.

## Relevance to YOLO loop

If our YOLO loop agents act on behalf of specific developers (e.g., opening PRs, making API calls), running them under the developer's identity rather than a shared service account would eliminate permission-sync overhead and make audit logs automatically attributable. The X-LLM-Agent header pattern is a low-effort quick win we could add immediately.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-03 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-03-twosigma-agent-runs-as-user-identity` |
| Channel | aie |
| Video | [Tethered: Our Agents Are Us — Shu Fang, Two Sigma](https://www.youtube.com/watch?v=wCIYViPd4SU) |
| Published | 2026-09-03 |
| Ingested upstream | 2026-09-03 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
