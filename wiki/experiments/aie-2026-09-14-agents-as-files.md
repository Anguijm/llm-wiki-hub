# Replace Python Agent Orchestration with Markdown Skill Files

> Back to [[experiments-index]]

Source: **[Agents Without Code: Skills, YAML, and Filesystems Replaced Python — Philipp Schmid, Google DeepMind](https://www.youtube.com/watch?v=fjF8EKnxKCU)** · aie · 2026-09-14

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we replace hand-written Python agent loops and JSON tool schemas with markdown skill files and YAML configuration, then we can extend agent capabilities without changing code and reduce maintenance burden, because modern frontier models are capable enough to reason over plain-language skill definitions and discover the right execution path without explicit orchestration.

## What they did

Philipp Schmid demonstrated building the same GitHub PR review agent three ways, each with less code. Starting from a raw Python loop with explicit JSON schemas and tool routing, he moved to an ADK framework that auto-generates schemas from function signatures, then finally to an 'anti-gravity harness' where agents are defined entirely as files — markdown system prompts, skill .md files, and YAML config. Adding a new capability (e.g., security scanning) required only dropping a new skills.md file into the environment, not changing any Python. He cited Cursor replacing ~12,000 lines of TypeScript with ~200 lines of agent files, and noted a general trend: as models improve, orchestration code should shrink.

## Relevance to YOLO loop

Our YOLO loop currently uses Python harnesses for tool routing and agent orchestration. This experiment suggests we could externalize capability definitions into markdown skill files, letting the model handle routing, which would make adding new tools to the loop a file-drop operation rather than a code change.

## Notes

Google's Interactions API (formerly Gemini API) provides the unified interface shown. The anti-gravity harness demo is available via QR code to AI Studio. Key heuristic: if your harness gets more complex as the model improves, you are overengineering.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-14 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-14-agents-as-files` |
| Channel | aie |
| Video | [Agents Without Code: Skills, YAML, and Filesystems Replaced Python — Philipp Schmid, Google DeepMind](https://www.youtube.com/watch?v=fjF8EKnxKCU) |
| Published | 2026-09-14 |
| Ingested upstream | 2026-09-14 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
