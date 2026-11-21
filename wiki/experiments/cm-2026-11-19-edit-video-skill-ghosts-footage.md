# Trial the edit-video skill with local Whisper on one raw clip

> Back to [[experiments-index]]

Source: **[This Skill Turns Claude Code Into an Expert Video Editor (I'm Giving It Away)](https://www.youtube.com/watch?v=a90pZ1DSyls)** · cm · 2026-11-19

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we run Cole Medin's open-source edit-video skill with local Whisper transcription on one raw Ghosts with Guns narration clip, then we get a rough cut with silence and retakes removed that passes a word-by-word transcript diff, because deterministic helper scripts handle the cutting and a validation script re-transcribes the output and compares it to the source.

## What they did

Cole open-sourced an edit-video skill for Claude Code. It routes through a SKILL.md step table: word-timestamp transcription, silence and retake cutting, clip assembly, transitions and SFX from brand.json, and a Python script that re-transcribes the output and diffs it word-by-word against the source. A references/lessons.md file logs recurring agent mistakes. The optional OpenRouter pipeline adds Gemini video review and Fish Audio voice patching. He edited a full video for $2.71 in API cost. He says outputs still need human review.

## Relevance to YOLO loop

medium: A deterministic word-diff gate and a lessons.md log resemble existing hard gates and failure digests, so the technique itself is mostly not new.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-11-20 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `cm-2026-11-19-edit-video-skill-ghosts-footage` |
| Channel | cm |
| Video | [This Skill Turns Claude Code Into an Expert Video Editor (I'm Giving It Away)](https://www.youtube.com/watch?v=a90pZ1DSyls) |
| Published | 2026-11-19 |
| Ingested upstream | 2026-11-20 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
