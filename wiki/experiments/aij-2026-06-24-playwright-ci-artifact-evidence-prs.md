# Require Agents to Attach Playwright Video Evidence to Every PR

> Back to [[experiments-index]]

Source: **[OpenClaw Creator's new secret project...](https://www.youtube.com/watch?v=1HkqTlXbQmQ)** · aij · 2026-06-24

**Status:** `adopted` · **Verdict:** `adopt` · **Effort:** `medium`

---

## Hypothesis

If agents are required to run Playwright CI and attach video/screenshot artifacts as evidence in their PRs, then human reviewers can merge agent PRs faster and with more confidence because the visual proof reduces the need to re-run tests manually or mentally model what the agent actually tested.

## What they did

Jason described adding a codebase harness where agents use Playwright to do browser-based E2E testing, capturing video recordings and screenshots as artifacts. These are uploaded to S3 or as GitHub release assets and embedded inline in the PR description. He framed this as the first step of a 'codebase harness' that unlocks trust in agent-generated code and is a prerequisite before scaling to more parallel agents.

## Relevance to YOLO loop

The YOLO loop currently merges agent PRs based on static diff review; requiring Playwright video evidence would give the human reviewer a fast signal that the agent actually verified the feature worked end-to-end, reducing revert rate.

## Notes

This is a lower-effort entry point than the full CrabBox setup and can be implemented incrementally on the existing single-agent workflow before scaling to parallel agents.

Backlog triage 2026-06-24 (owner-preference model). Playwright video/screenshot evidence on PRs — proof/verification discipline (never-trust-self-report); Playwright is preinstalled.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-24 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aij-2026-06-24-playwright-ci-artifact-evidence-prs` |
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
