# Add a mandatory accessibility skill to UI-generating agents

> Back to [[experiments-index]]

Source: **[The Cost of Accessibility in AI — Jemima Abu, CAIS](https://www.youtube.com/watch?v=ZccJsdOE54M)** · aie · 2026-10-15

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we provide an explicit accessibility skill (semantic HTML, ARIA guidance, keyboard operability, labeling rules) to an agent generating UI from Figma, then token cost and time-to-completion will decrease because the agent spends less time backtracking from inaccessible implementations.

## What they did

Jemima Abu ran a coding agent twice against the same Figma-to-code prompt: once with no accessibility guidance and once with a purpose-built accessibility skill. The version with the skill finished in roughly one-third of the time and at 58% lower cost. She attributed the gap to the agent avoiding dead-end paths caused by inaccessible defaults absorbed from the existing codebase. She also recommends a lightweight skill baseline: semantic HTML first, ARIA only when HTML is insufficient, keyboard operability for every interactive element, proper labeling, and a pre-commit accessibility audit step.

## Relevance to YOLO loop

Any step in the YOLO loop that uses an agent to scaffold or generate UI components can attach this skill document. Low effort to add a system-prompt or skill file; directly reduces agent token spend and rework on accessibility retrofits.

## Notes

One-off experiment, not controlled; treat the 58% cost reduction as directional signal only. Pair with automated accessibility audit tool (e.g., axe) as a post-generation gate to verify quality.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-10-15-accessibility-skill-reduces-agent-cost` |
| Channel | aie |
| Video | [The Cost of Accessibility in AI — Jemima Abu, CAIS](https://www.youtube.com/watch?v=ZccJsdOE54M) |
| Published | 2026-10-15 |
| Ingested upstream | 2026-10-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
