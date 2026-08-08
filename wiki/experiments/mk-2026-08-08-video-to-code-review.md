# Feed screen-recording MP4 directly to Claude Code for codebase improvement review

> Back to [[experiments-index]]

Source: **[Claude Code and Codex Quietly Learned to Watch Video](https://www.youtube.com/watch?v=0I-J1aoxYQY)** · mk · 2026-08-08

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we drag-and-drop a Loom/screen-recording MP4 of a website walkthrough into Claude Code (no plugins), then it will decompose the video into frames, extract audio, and produce a prioritized improvement list tied to the live codebase because Claude Code now natively processes raw MP4 by converting it to per-frame images married with transcript.

## What they did

Mark recorded a walkthrough of his website using Loom, then fed the raw MP4 (and separately a direct Loom URL) into Claude Code and Codex. Both agents broke the video into second-by-second frames, extracted the audio transcript, and returned a comprehensive list of UI/UX improvements without any additional plugins or skills. He also tested giving a direct URL link to the video and letting the agent download and process it autonomously.

## Relevance to YOLO loop

Directly accelerates the requirements-gathering step of our dev loop: instead of manually writing issue tickets after reviewing a build, a developer can screen-record their review session and hand the MP4 to Claude Code, which then opens PRs or edits files against the live codebase.

## Notes

Resolution matters: author notes that lower-res video is preferable to stay within context limits. Gemini was previously the go-to for this; now Claude Code and Codex handle it natively.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-08 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `mk-2026-08-08-video-to-code-review` |
| Channel | mk |
| Video | [Claude Code and Codex Quietly Learned to Watch Video](https://www.youtube.com/watch?v=0I-J1aoxYQY) |
| Published | 2026-08-08 |
| Ingested upstream | 2026-08-08 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
