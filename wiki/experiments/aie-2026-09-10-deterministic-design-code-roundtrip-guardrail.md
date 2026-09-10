# Add Deterministic Drift-Detection Guardrails to Catch Design-Code Divergence Before Merge

> Back to [[experiments-index]]

Source: **[The Design-Code Roundtrip That Isn't — Jonathan Gordon, ReWeaver AI](https://www.youtube.com/watch?v=NW-jwOVr32w)** · aie · 2026-09-10

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we instrument a deterministic reconciliation layer that scans AI-generated code for drift from design system specifications and either auto-fixes known violations or blocks unknowns with a human prompt, then we will prevent the accumulation of 'drift debt' that compounds over time in vibe-coded codebases, because LLM code generation is nondeterministic and will introduce divergence on every run.

## What they did

Jonathan Gordon described his investigation into whether true bidirectional design-code roundtrips (Figma ↔ code with no fidelity loss) exist today, concluding they do not despite vendor claims. He then described ReWeaver AI: a local-first tool (no extra token cost) that applies nine dimensions of deterministic guardrails to AI-generated code—design consistency, accessibility, AI code governance, and others. It does not generate code itself; it scans code written by any agent, applies known fixes automatically, and surfaces unknown issues for human review with accept/reject controls. He framed 'drift over time' as the new technical debt in AI-assisted codebases. A public playground at reweaver.ai/playground lets users test their code and get a 'production drift ratio' score.

## Relevance to YOLO loop

Highly relevant post-generation quality gate: adding a drift-scan step after any agentic code generation before commit/merge would catch design-system violations early. The accept/refuse pattern preserves human control without blocking the loop. Test the playground against our own agent-generated code to establish a baseline PDR score.

## Notes

ReWeaver beta launching ~mid-July per speaker. Playground available now at reweaver.ai/playground. Challenge: get AI to produce code scoring below 30 PDR for a beta seat.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-10 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-10-deterministic-design-code-roundtrip-guardrails` |
| Channel | aie |
| Video | [The Design-Code Roundtrip That Isn't — Jonathan Gordon, ReWeaver AI](https://www.youtube.com/watch?v=NW-jwOVr32w) |
| Published | 2026-09-10 |
| Ingested upstream | 2026-09-10 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
