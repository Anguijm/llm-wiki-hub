# Add domain-expert-in-the-loop evaluation to any persona/character agent to detect anachronistic compositing

> Back to [[experiments-index]]

Source: **[The Miranda Hypothesis: How Hamilton Poisoned Persona Evals - Jacob E. Thomas, Results Gen](https://www.youtube.com/watch?v=IJXjTLPzvAU)** · aie · 2026-06-25

**Status:** `discarded` · **Verdict:** `discard` · **Effort:** `high`

---

## Hypothesis

If we include a domain expert (historian, theologian, clinician, etc.) as a required build-time evaluator for persona-based agents rather than relying solely on fluency and personality-consistency benchmarks, then we will detect 'Miranda distortion' — anachronistic compositing where the model blends culturally salient modern representations with historical figures — because standard in-character benchmarks measure how well the output sounds like the persona, not whether it accurately reflects documented primary sources.

## What they did

Jacob presented the Miranda Hypothesis: that dominant persona eval benchmarks (e.g. in-character benchmark reporting 80.7% alignment) cannot detect their own dominant failure mode because they measure fluency and personality consistency, not fidelity to the archival record. He coined 'Miranda distortion' for outputs where Hamilton sounds like he has read his own Broadway musical. He built an open-source prompt framework ('Companion') that grounds persona reasoning in explicit document anchors. He partnered with historian Rick Halpern (U Toronto) and librarian Shawn Martin to create a pre-registered evaluation instrument with sealed historian vignettes and a rubric that measures fidelity to primary sources rather than fluency. He proposed this as a build-time gate (not a runtime cost) that scales with context window.

## Relevance to YOLO loop

Applicable if our loop includes any persona, tutor, or historical simulation feature: use his pre-registered rubric and the principle of document-anchored personas rather than fluency-based evals. The build-time gate pattern (expert review before ship) is broadly transferable.

## Notes

Paper with Rick Halpern and Shawn Martin forthcoming with pre-registered instrument, rubric, and sealed historian vignettes. Demo at Results Gen site.

Backlog triage 2026-06-27 (owner-preference model). Domain-expert-in-loop eval for persona/character agents — off-domain; the loop doesn't build persona agents.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-25 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-25-miranda-hypothesis-persona-eval-humanist-loop` |
| Channel | aie |
| Video | [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals - Jacob E. Thomas, Results Gen](https://www.youtube.com/watch?v=IJXjTLPzvAU) |
| Published | 2026-06-25 |
| Ingested upstream | 2026-06-25 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
