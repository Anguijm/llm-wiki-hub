# Add a cross-repo session memory graph (Polygraph pattern) so agents reference past decisions without human re-explanation

> Back to [[experiments-index]]

Source: **[A Genius With Amnesia - Victor Savkin, Nx](https://www.youtube.com/watch?v=jVjt-2g8NMY)** · aie · 2026-06-26

**Status:** `adopted` · **Verdict:** `adopt` · **Effort:** `high`

---

## Hypothesis

If we maintain a graph of all agent sessions and their relationships to repos — and surface relevant past sessions at the start of each new session — then the number of times a developer must re-explain prior context drops from O(N handoffs) to O(1) because the agent can query what was done, why, and by whom across the entire codebase history.

## What they did

Victor Savkin (Nx) quantified the re-explanation tax: a single UI change propagated across 4 repos with one production bug required 7 separate explanations to 7 agent sessions. He built Polygraph, an agent-agnostic meta-harness that wraps Claude, Codex, or any agent and provides: (1) a repository graph — metadata about how all repos (owned + open source) relate to each other, enabling cross-repo context without manual selection; (2) episodic session memory — every agent session is stored and indexed, searchable by content, repo relationship, and recency; (3) automatic session suggestion — when starting work in a repo, Polygraph surfaces past sessions relevant to that repo or task; (4) cross-developer memory — sessions from all engineers contribute to one shared graph, so any agent can draw on any engineer's prior work. Demo showed: bug fix that required only 'this happened, there is a bug' with zero additional context because Polygraph loaded the original session automatically. Also showed natural language repo discovery ('find every repo depending on version X and update it') and session-informed best practice replication.

## Relevance to YOLO loop

The YOLO loop re-explains the same project context every session. Polygraph's session graph pattern — even implemented minimally as a JSON log of session summaries indexed by file paths touched — would let the loop bootstrap with relevant prior decisions. The 'sessions relate to repos, repos relate to sessions' bidirectional index is the key data structure to prototype first.

## Notes

Available at try.polygraph.com. Works as a CLI wrapper around existing agents — low adoption friction. The cross-developer shared memory aspect is most novel for team YOLO loop usage. Conceptually overlaps with Paul Iusztin's AI Research OS but focused on code sessions not notes. Both point to the same unsolved problem.

Backlog triage 2026-06-27 (owner-preference model). Cross-session/repo memory graph surfacing relevant past sessions — compounding-memory/hot-cache family; strong fit.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-26 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-26-polygraph-cross-repo-agent-memory` |
| Channel | aie |
| Video | [A Genius With Amnesia - Victor Savkin, Nx](https://www.youtube.com/watch?v=jVjt-2g8NMY) |
| Published | 2026-06-26 |
| Ingested upstream | 2026-06-26 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
