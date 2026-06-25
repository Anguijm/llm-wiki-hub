# Implement a Creator Trust Stack metadata layer for AI-assisted outputs

> Back to [[experiments-index]]

Source: **[You Can't Tell If I'm Real Anymore. And That's Now YouTube's Problem Too.](https://www.youtube.com/watch?v=lWbtvC0Hn18)** · nb · 2026-06-20

**Status:** `discarded` · **Verdict:** `discard` · **Effort:** `medium`

---

## Hypothesis

If we tag each AI-assisted output with structured provenance metadata covering voice, face, script, idea, and human-approval layers, then reviewers and end-users can make informed trust decisions because the five-layer trust stack separates distinct types of AI involvement that are currently collapsed into a single ambiguous 'AI-assisted' label.

## What they did

Nate proposed a five-layer 'creator trust stack' framework: (1) Disclosure — what was synthetic (voice, face, script, edit); (2) Provenance — where source material came from and whether it was consented to; (3) Control — who had authority to approve or reject the output; (4) implied accountability layer — whether a responsible human stands behind the final output. He demonstrated a labeled voice clone in the video itself as a concrete disclosure practice, and argued that the binary 'AI or no AI' question is too blunt and should be replaced with 'where in the stack did AI operate and where did human judgment take over.'

## Relevance to YOLO loop

In our dev loop, every generated artifact (code, docs, summaries, voice output) could carry a trust-stack metadata block logged alongside the output. This maps directly to our logging and provenance concerns: we can annotate which loop steps were fully automated vs. human-reviewed, making audit and accountability explicit rather than implicit.

## Notes

Nate explicitly ran a live voice clone demo labeled on-screen as synthetic, modeling the disclosure practice he advocates. The five questions he enumerates (voice synthetic? face synthetic? script synthetic? idea synthetic? human approved?) could map directly to a metadata schema field per artifact in our pipeline.

Backlog triage 2026-06-24 (owner-preference model). AI-media provenance disclosure — the loop ships code, not published media; off-domain.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-20 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `nb-2026-06-20-creator-trust-stack-disclosure` |
| Channel | nb |
| Video | [You Can't Tell If I'm Real Anymore. And That's Now YouTube's Problem Too.](https://www.youtube.com/watch?v=lWbtvC0Hn18) |
| Published | 2026-06-20 |
| Ingested upstream | 2026-06-20 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
