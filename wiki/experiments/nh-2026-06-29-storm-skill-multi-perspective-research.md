# Implement Stanford STORM skill with five specialist personas and a verification pass

> Back to [[experiments-index]]

Source: **[Stanford's Method Turns Claude Into a PHD Level Research Team](https://www.youtube.com/watch?v=Tj3018n5MVg)** · nh · 2026-06-29

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we run research tasks through a Claude skill that instantiates five distinct expert personas (practitioner, academic, skeptic, economist, historian) in parallel and then runs a second-pass verification agent to confirm/demote/correct sources, then research output will be more organized, better-sourced, and more actionable than a single deep-research prompt, because multi-perspective conflict surfaces blind spots and the verification pass filters hallucinated citations.

## What they did

Nate encoded Stanford's STORM research methodology into a Claude Code skill. The skill spins up five persona sub-agents in parallel, converges their outputs, identifies contradictions, then runs six verification agents to confirm or demote each citation. The result is a structured HTML briefing with reliability scores per finding, sourced footnotes, and a 60-second summary. He benchmarked it against Claude Code's native deep-research (103 agents) and found the STORM skill faster, 100% cheaper, and rated superior by Codex on six quality dimensions.

## Relevance to YOLO loop

Replaces ad-hoc single-prompt research in our loop with a repeatable, structured skill. Can be tailored with business context so every research run is domain-relevant. The verification pass directly reduces hallucination risk in specs and planning docs fed into the coding loop.

## Notes

Skill is freely available from Nate's repo. Runs on Opus 4.8 sub-agents by default but can be downgraded to Haiku/Sonnet to cut cost. Adding a sixth lens (e.g. end-user or content-creator perspective) is explicitly recommended. Compare output on a known domain first to calibrate quality.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-29 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-06-29-storm-skill-multi-perspective-research` |
| Channel | nh |
| Video | [Stanford's Method Turns Claude Into a PHD Level Research Team](https://www.youtube.com/watch?v=Tj3018n5MVg) |
| Published | 2026-06-29 |
| Ingested upstream | 2026-06-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
