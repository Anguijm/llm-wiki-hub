# Test cross-session failure micro-skills with injection guard

> Back to [[experiments-index]]

Source: **[This Is Microsoft's New Plan To Fix Claude's Usage Limits](https://www.youtube.com/watch?v=1kQ_1_QL5Es)** · ail · 2026-10-28

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we synthesize repeated command failures into project micro-skills every few sessions and seed them from existing session history, then repeat failures and stuck loops will decrease because the agent keeps cross-session failure memory.

## What they did

The speaker enabled micro-skills synthesis, where an LLM reviews recent session logs every three sessions and extracts repeated failures. They modified the plugin startup script to ingest past sessions from the .claude folder to avoid a cold start. They also enabled stuck-loop detection, which prompts the model to try alternatives before advising manual termination. They noted that untrusted command output could inject malicious instructions into the micro-skills.

## Relevance to YOLO loop

high: Cross-session memory and loop detection are core harness and verification-loop concerns, and the prompt-injection risk needs a mitigation check.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-28 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `ail-2026-10-28-micro-skills-failure-memory` |
| Channel | ail |
| Video | [This Is Microsoft's New Plan To Fix Claude's Usage Limits](https://www.youtube.com/watch?v=1kQ_1_QL5Es) |
| Published | 2026-10-28 |
| Ingested upstream | 2026-10-28 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
