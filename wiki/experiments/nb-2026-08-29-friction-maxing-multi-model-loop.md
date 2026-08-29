# Route every AI output through at least two competing models before accepting it

> Back to [[experiments-index]]

Source: **[How I Fight AI Brain Rot. Friction Maxxing With Codex, Grok And Claude.](https://www.youtube.com/watch?v=CSCwaqVqHGE)** · nb · 2026-08-29

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we deliberately pass each AI-generated answer through at least one additional model and one human reviewer before accepting it, then we will surface more disagreements and produce higher-quality outputs because surviving multi-round argument filters out model-consensus blind spots.

## What they did

Nate describes a daily workflow where he cycles between Codex, Grok, and Claude plus ~10 trusted human contacts. He never accepts the first answer; instead he asks whether to accept, challenge, compare against another model, ask a person, or discard. He frames every disagreement as a 'rep for his brain' and argues the work that survives 4-10 rounds of argument is categorically better than the initial output. He also caught a concrete agent failure (wrong spreadsheet attachment) and used it to learn about agent environment disclosure patterns rather than just labeling the agent bad.

## Relevance to YOLO loop

Directly maps to the review/validation gate in the YOLO loop: instead of auto-accepting agent output, insert a structured multi-model challenge step and a human spot-check before merging.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-29 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-08-29-friction-maxing-multi-model-loop` |
| Channel | nb |
| Video | [How I Fight AI Brain Rot. Friction Maxxing With Codex, Grok And Claude.](https://www.youtube.com/watch?v=CSCwaqVqHGE) |
| Published | 2026-08-29 |
| Ingested upstream | 2026-08-29 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
