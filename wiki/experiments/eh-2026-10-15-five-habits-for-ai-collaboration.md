# Encode five interaction habits into a team AI usage protocol and test against default prompting

> Back to [[experiments-index]]

Source: **[4 years of talking to AI, distilled into insights you can use today](https://www.youtube.com/watch?v=GC32QW-r5Mg)** · eh · 2026-10-15

**Status:** `discarded` · **Verdict:** `discard` · **Effort:** `low`

---

## Hypothesis

If we adopt five structured interaction habits (raise the bar out loud, react immediately with felt observations, describe what you see not how to fix it, ask the model how confident it is, and protect working code by experimenting in isolated copies), then agent output quality and iteration speed will improve over default prompting because each habit addresses a specific failure mode of model drift toward safe mediocrity.

## What they did

The speaker distilled four years of near-daily AI use into five habits demonstrated through building Instant 3D Models. (1) Raise the bar out loud: first message said 'this will take all your creativity, not just the surface level stuff.' (2) React immediately: sent micro-feedback while Claude was still working rather than writing a spec first. (3) Say what you see: at 2am a mech looked like a toy; instead of prescribing a fix he said 'this is about something else—the shape' and Claude found real proportions. (4) Ask how sure it is: when a turntable stuttered he asked 'are you confidently able to identify why?' and Claude found 3 causes; one fix ran 40x faster. (5) Protect what works: the main app stayed untouched; every experiment got its own copy and server so a bad idea could never break it.

## Relevance to YOLO loop

Directly codifiable as a team prompting protocol for our YOLO loop: each habit addresses a known failure mode (model conservatism, late feedback, over-prescription, overconfidence, state pollution) and can be embedded in our agent interaction guidelines.

## Notes

Backlog triage 2026-10-17 round 3 (operator: "I want you to evaluate the yolo cards"). Settled maybe, cut: Assessment: he already pushes on confidence and isolates experiments; the new piece is one prompt question, are you confidently able to identify why.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-15 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `eh-2026-10-15-five-habits-for-ai-collaboration` |
| Channel | eh |
| Video | [4 years of talking to AI, distilled into insights you can use today](https://www.youtube.com/watch?v=GC32QW-r5Mg) |
| Published | 2026-10-15 |
| Ingested upstream | 2026-10-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
