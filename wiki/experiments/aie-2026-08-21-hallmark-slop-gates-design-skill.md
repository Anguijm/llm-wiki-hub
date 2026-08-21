# Encode an anti-slop design ruleset and curated visual references into agents.md to improve AI-generated UI quality

> Back to [[experiments-index]]

Source: **[The Missing Layer: Design Taste in AI Agents — Hassan El Mghari, Together AI](https://www.youtube.com/watch?v=7GMKdpLsxwU)** · aie · 2026-08-21

**Status:** `backlog` · **Effort:** `low`

---

## Hypothesis

If we add an explicit list of anti-patterns to avoid (purple gradients, italic headers, emoji overuse, pill components with all-caps letter-spaced text, 'scroll to explore' banners) plus a curated set of reference screenshot themes into our agent instruction files, then AI-generated UIs will be meaningfully more distinct and professional, because models given negative constraints and positive visual references produce outputs that deviate from the statistical center of vibe-coded defaults.

## What they did

Speaker built a design skill called Hallmark that codifies common AI-generated UI slop patterns as explicit prohibitions ('slop gates') and pairs them with a library of curated design themes fed as context. He reported 10,000+ users tried it within six weeks of launch. He also advocated for: pasting reference screenshots into every new app prompt ('inspiration vault'), writing 2-3 paragraph voice-note-style prompts instead of one-liners, breaking feature builds into sequential prompts rather than one-shotting, iterating with faster open-source models for UI polish loops, and maintaining a growing agents.md with accumulated design constraints discovered through iteration.

## Relevance to YOLO loop

We generate UI components and agent output renderers in our loop. Adding a Hallmark-style anti-pattern block and a small reference image set to our CLAUDE.md / agents.md is a low-effort change that could immediately raise the baseline quality of any frontend work produced by our agents without changing the core loop architecture.

## Notes

Hallmark is open and available to test directly. Speaker's 'inspiration vault' habit (saving screenshots of admired UIs and pasting them into prompts) is immediately actionable as a personal workflow change independent of any tooling build.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-08-21 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-08-21-hallmark-slop-gates-design-skill` |
| Channel | aie |
| Video | [The Missing Layer: Design Taste in AI Agents — Hassan El Mghari, Together AI](https://www.youtube.com/watch?v=7GMKdpLsxwU) |
| Published | 2026-08-21 |
| Ingested upstream | 2026-08-21 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
