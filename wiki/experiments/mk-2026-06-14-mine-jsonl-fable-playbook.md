# Mine Claude Code JSONL sessions to generate a model behavior playbook

> Back to [[experiments-index]]

Source: **[Make ANY Model Think Like Fable in Minutes](https://www.youtube.com/watch?v=B95cu7seTm8)** · mk · 2026-06-14

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we parse Claude Code JSONL session files to extract Fable 5 vs Opus behavioral patterns and distill them into an injected playbook, then weaker models will exhibit more deliberate planning and tool-call cadence because they are given explicit behavioral heuristics derived from the superior model's actual execution traces.

## What they did

Speaker wrote Python scripts (via Claude Code) to strip bloat from JSONL session files, filter turns by model tag (e.g. claude-fable-5 vs claude-opus-4.8), extract tool-call sequences, planning steps, and read/edit/test ratios, then ran a side-by-side behavioral comparison. The resulting delta was distilled into a markdown playbook file that is injected at session start via a Claude Code hook or CLAUDE.md entry, so every new session inherits Fable-like behavioral patterns.

## Relevance to YOLO loop

Directly improves the agent execution layer of our dev loop: injecting a behavior playbook at session start can raise baseline code-agent quality without model upgrades, acting as a persistent prompt-engineering layer above whatever frontier model is currently available.

## Notes

Speaker offers their own synthesized playbook as a download. HuggingFace dataset of open-sourced Fable 5 sessions also cited for teams with little Fable history. Hook injection vs CLAUDE.md are two integration paths to test.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-14 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mk-2026-06-14-mine-jsonl-fable-playbook` |
| Channel | mk |
| Video | [Make ANY Model Think Like Fable in Minutes](https://www.youtube.com/watch?v=B95cu7seTm8) |
| Published | 2026-06-14 |
| Ingested upstream | 2026-06-14 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
