# Embed code verification inside the agentic loop (not just CI) using the guide-verify-solve three-loop pattern

> Back to [[experiments-index]]

Source: **[In the Land of AI Agents, the Verifiers Are King — Tariq Shaukat, Sonar](https://www.youtube.com/watch?v=VrpEyglYgeU)** · aie · 2026-07-20

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we add inline verification (complexity, bug, and security checks) inside the agentic coding loop rather than only at the CI gate, then the compounding degradation of code quality observed after 3 months of AI coding tool adoption will be arrested, because the Carnegie Mellon study shows that velocity gains dissipate when verification is absent and a 92% reduction in issues is achievable when guide-verify-solve is embedded in the inner loop.

## What they did

Tariq Shaukat presented Sonar's benchmarking showing that even state-of-the-art models (GPT-5.5, Claude etc.) produce functionally correct but complexity-high, security-issue-containing code. He cited a Carnegie Mellon study showing AI coding tools produce a 3-5x velocity boost that dissipates to baseline after 3 months due to accumulating bugs and security issues. The fix is a three-loop architecture: (1) agentic inner loop with in-context verification and constraint injection as the agent generates code; (2) CI verification loop with fast automated review and fix suggestion at PR time; (3) code maintenance loop with scheduled quality and security remediation. He showed a bank customer achieving 92% issue reduction by embedding this across the three loops, and noted cleaner codebases also reduce agent token consumption compoundingly.

## Relevance to YOLO loop

Core architecture recommendation for our YOLO loop: we should map our current verification touchpoints to these three loops and identify which loop has no verification today (likely the inner agentic loop) and add at minimum a lightweight complexity/security check there.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-07-20 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-07-20-inloop-verification-three-loop-sdlc` |
| Channel | aie |
| Video | [In the Land of AI Agents, the Verifiers Are King — Tariq Shaukat, Sonar](https://www.youtube.com/watch?v=VrpEyglYgeU) |
| Published | 2026-07-20 |
| Ingested upstream | 2026-07-20 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
