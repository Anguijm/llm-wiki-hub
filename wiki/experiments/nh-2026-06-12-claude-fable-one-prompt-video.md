# Drive a Multi-Tool Media Pipeline From a Single /goal Prompt Using Claude Code

> Back to [[experiments-index]]

Source: **[Claude Fable 5 Made This Entire Video By Itself.](https://www.youtube.com/watch?v=ONmaDdOBGig)** · nh · 2026-06-12

**Status:** `discarded` · **Verdict:** `discard` · **Effort:** `high`

---

## Hypothesis

If we specify a complete media artifact goal (script → voice → avatar → edit → verify) as a single /goal prompt in Claude Code with explicit quality criteria and a dynamic verification workflow, then the agent will orchestrate all external API calls and produce a finished artifact without human intervention because long-horizon focus and tool-use chaining can substitute for manual pipeline management.

## What they did

Nate issued one /goal prompt to Claude Code (Fable 5 model on Max plan) that described building a finished YouTube video: Claude read Anthropic's announcement, fact-checked claims, wrote a script in Nate's voice using a voice playbook, chunked the script into sub-minute segments to avoid voice drift, sent each chunk to ElevenLabs for voice cloning, rendered each chunk on HeyGen Avatar 5 via API (with a prior Playwright browser-driving workaround noted), stitched clips with ffmpeg, ran Whisper transcription, built motion graphics as animated HTML/CSS inside Hyperframes timed to speech, visually reviewed rendered frames, and re-rendered anything that failed quality checks. The entire session ran in ~1 hour consuming ~380k tokens (~40% of his $200/month Max plan). He gave the agent explicit stakes context ('this goes to my channel, it will damage my reputation if it looks bad') and instructed it to spin up a dynamic multi-agent verification workflow before declaring done.

## Relevance to YOLO loop

This is a stress test of the YOLO loop's maximum autonomy mode. The chunked-audio-to-avoid-drift pattern, the Playwright browser-driving fallback, the frame-sampling visual QA step, and the dynamic sub-agent verification workflow are all individually extractable techniques applicable to any long-running artifact generation task in our loop.

## Notes

Nate notes the workflow is now skill-encodable and likely replicable with Sonnet after the first successful run. The 40% plan consumption in 1 hour is a meaningful cost signal for budgeting autonomous runs. Verification via screenshot frame-sampling is the most immediately reusable sub-pattern.

Backlog triage 2026-06-24 (owner-preference model). Media-generation pipeline — off-domain, high effort.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-12 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nh-2026-06-12-claude-fable-one-prompt-video` |
| Channel | nh |
| Video | [Claude Fable 5 Made This Entire Video By Itself.](https://www.youtube.com/watch?v=ONmaDdOBGig) |
| Published | 2026-06-12 |
| Ingested upstream | 2026-06-12 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
