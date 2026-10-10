# Add an agentic PR validation layer that auto-reviews, auto-fixes CI failures, and progressively unlocks auto-merge as trust is established

> Back to [[experiments-index]]

Source: **[AI Writes More PRs. Who Validates Them? — Ali-Reza Adl-Tabatabai, Sonar](https://www.youtube.com/watch?v=uuwDWRbxoYo)** · aie · 2026-10-10

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we insert an agentic validation agent into our PR pipeline that reviews code, posts inline issues, analyzes CI failures (including flaky test detection), and optionally auto-fixes and auto-merges green PRs, then we can absorb the increased PR volume from AI-generated code without requiring proportionally more human review time, because the agent handles the repetitive validation triage that would otherwise block the pipeline.

## What they did

Ali-Reza Adl-Tabatabai (Sonar/Guitar.ai) described Guitar: an agentic PR validation system with a control plane (PR workflow orchestration), a custom agent harness (multi-agent execution, context management, tool calling), and an LLM proxy (model routing + failover). The agent reviews every PR, posts noise-minimized inline comments, detects and auto-retries flaky tests, can auto-fix code review issues or CI failures, and can auto-approve and merge PRs based on configurable rules. Users adopt it progressively: first reviews → trust → blocking PRs → autofix → auto-merge. The system also surfaces analytics: CI failure categorization by type (flakiness vs. infrastructure) and PR categorization (feature vs. bug fix vs. chore) for leadership visibility. Now integrated with Sonar's static analysis (taint analysis, data flow, SCA) for combined agent + algorithmic precision.

## Relevance to YOLO loop

Our YOLO loop will generate increasing PR volume. Rather than routing all PRs to human review, a tiered agentic validation layer (start with review-only, build trust, enable auto-merge for low-risk PRs) directly removes the review bottleneck that would otherwise throttle loop throughput.

## Notes

Guitar.ai acquired by Sonar; now available as part of Sonar product. Booth P7 at conference. Key insight: progressive trust unlocking is the adoption pattern — don't start with auto-merge.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-10 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-10-automated-pr-validation-agent-with-autofix-and-automerge` |
| Channel | aie |
| Video | [AI Writes More PRs. Who Validates Them? — Ali-Reza Adl-Tabatabai, Sonar](https://www.youtube.com/watch?v=uuwDWRbxoYo) |
| Published | 2026-10-10 |
| Ingested upstream | 2026-10-10 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
