# Use CrabBox to Give Each Parallel Agent Its Own Cloud Dev Sandbox

> Back to [[experiments-index]]

Source: **[OpenClaw Creator's new secret project...](https://www.youtube.com/watch?v=1HkqTlXbQmQ)** · aij · 2026-06-24

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If each parallel coding agent is given an isolated cloud sandbox (via CrabBox) with its own database and dev server, then agents can run end-to-end tests without conflicting with each other or the local environment, because shared ports, Docker daemons, and DB instances are the bottleneck that breaks multi-agent parallelism at scale.

## What they did

AIJason described the scaling problem when running 10-15+ parallel Claude/agent sessions: shared local ports, a single Docker daemon, and one local DB instance cause agents' test environments to collide. He then walked through CrabBox (by Peter Steinberg, author of OpenClaw), which provides `crabbox warmup`, `crabbox run`, and `crabbox stopbox` commands. Each agent warms up a cloud box, syncs uncommitted dirty diffs from the local worktree (no commit required), runs commands (install deps, start dev server, Playwright E2E tests) in the isolated cloud environment, then tears it down. Evidence (screenshots, videos) is uploaded to S3 or GitHub release assets and included in PRs. He also shared a `cbx.sh` wrapper script and a CrabBox setup skill for Claude Code/Codex.

## Relevance to YOLO loop

Directly solves the YOLO loop's parallelism bottleneck: when multiple agents are spawned per issue/PR, they currently share a local dev environment. CrabBox would let each agent branch get a fully isolated sandbox for testing before merge, eliminating false-failure noise and environment collisions.

## Notes

CrabBox is open source. Jason also mentions a 'crabbox setup skill' and 'set up codebase harness skill' available in his builder club. Daytona is mentioned as one supported provider with a 60-second default timeout requiring background process workaround.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-24 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aij-2026-06-24-crabbox-isolated-sandbox-testing` |
| Channel | aij |
| Video | [OpenClaw Creator's new secret project...](https://www.youtube.com/watch?v=1HkqTlXbQmQ) |
| Published | 2026-06-24 |
| Ingested upstream | 2026-06-24 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
