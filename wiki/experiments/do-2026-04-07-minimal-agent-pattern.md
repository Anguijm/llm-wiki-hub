# Build a Bare-Metal Minimal Agent Loop with No Framework Dependencies

> Back to [[experiments-index]]

Source: **[This 100% minimal AI Agent can do anything… just watch](https://www.youtube.com/watch?v=9KYfx_GzY1o)** · DavidOndrej · 2026-04-07

**Status:** `adopted` · **Verdict:** `adopted` · **Effort:** `low`

---

## Hypothesis

If we implement the smallest possible agent loop (LLM call → tool dispatch → result injection → repeat) using only raw API calls and a dictionary-based tool registry, then we will have a maximally understandable and portable core that can be extended without framework lock-in, because the video demonstrates that a dozen lines of Python are sufficient for a fully functional general agent.

## What they did

Speaker live-coded a minimal AI agent from scratch: a while-loop that sends a prompt to an LLM, parses a structured tool-call response, executes the matched Python function, appends the result to the conversation, and loops until the model signals completion. No LangChain, no AutoGPT. Showed it browsing the web, writing files, and calling APIs.

## Relevance to YOLO loop

This is a candidate replacement or reference implementation for the orchestration layer of the YOLO loop. Testing whether our current loop can be simplified to this pattern would reduce complexity and improve debuggability.

## Notes

Adopted 2026-04-08: run as a bifurcation comparison study. Build the bare-metal 50-line agent loop and run it on one harness-cli project (roadtripper or sportsdata). Measure where harness-cli's overhead is real vs. ceremonial. Result feeds the YOLO/Harness bifurcation memory. ~1 day of work, high signal value about whether harness-cli is actually justified vs. could be replaced by a thin core.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-07 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-04-07-minimal-agent-pattern` |
| Channel | DavidOndrej |
| Video | [This 100% minimal AI Agent can do anything… just watch](https://www.youtube.com/watch?v=9KYfx_GzY1o) |
| Published | 2026-04-07 |
| Ingested upstream | 2026-04-07 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
