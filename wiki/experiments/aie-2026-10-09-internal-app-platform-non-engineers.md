# Build a CLI + catalog platform so non-engineers can deploy authenticated internal apps without engineer help

> Back to [[experiments-index]]

Source: **[Let Anyone at Your Company Ship Internal Apps with AI — Garrett Galow, WorkOS](https://www.youtube.com/watch?v=HTzgC3FoYsI)** · aie · 2026-10-09

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we provide non-technical staff a CLI that handles git setup, auth, secrets management, and deployment automatically, plus a discoverable catalog with default internal SSO access, then the share of internal tools built and maintained without engineering involvement will exceed 30% because the deployment and security barriers—not the building barriers—are what block non-engineers today.

## What they did

Garrett Galow (WorkOS) described the origin problem: an AE built a useful GPT-powered chatbot on Lovable but their CEO couldn't access it without a Lovable account, requiring engineers to re-implement it. Building is now cheap (Claude Code, Codex), but shipping internally remains hard—auth, secrets, deployment, and discovery are unsolved for non-engineers. WorkOS built: (1) 'Wow' CLI—scaffolds a repo, sets up Git, clones example app, generates code via Claude, and deploys with secrets managed via Doppler; (2) 'Atlas' internal platform—authenticates via company SSO, hosts apps, provides a discoverable catalog where all deployed apps are accessible by default to all employees, and supports API access for agent-to-agent calls. They run company-wide 'Claude Days' hackathons where non-engineers are on keyboard with engineers as consultants. Result: 60 actively used apps, 37% built entirely without engineer commits, 3M+ requests/week.

## Relevance to YOLO loop

Relevant to YOLO loop tooling distribution: the CLI+catalog pattern is a concrete template for making agent-built internal tools accessible to the whole org without per-app engineering overhead.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-09 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-09-internal-app-platform-non-engineers` |
| Channel | aie |
| Video | [Let Anyone at Your Company Ship Internal Apps with AI — Garrett Galow, WorkOS](https://www.youtube.com/watch?v=HTzgC3FoYsI) |
| Published | 2026-10-09 |
| Ingested upstream | 2026-10-09 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
