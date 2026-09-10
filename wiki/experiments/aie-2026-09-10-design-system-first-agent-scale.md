# Establish a Locked Design System Foundation Before Delegating Deliverables to Agents

> Back to [[experiments-index]]

Source: **[One Designer + AI. Hundreds of Deliverables. — Vincent Wendy, AI Engineer](https://www.youtube.com/watch?v=O1FN4awNEtM)** · aie · 2026-09-10

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we define typography, color tokens, spacing, and component constraints explicitly before prompting agents to generate any deliverable, then agents will produce on-brand, consistent outputs at scale without per-deliverable correction, because agents default to arbitrary design choices when constraints are absent.

## What they did

Vinson Weng (sole designer for AI Engineer conference: 7,000 attendees, 140+ sponsors, 300+ speakers, 600+ sessions) described a five-part framework for scaling one designer's output using Devin and Figma: (1) Foundation first—lock design system (typography, colors, components, tagline) before any generation; (2) Reusable designs—atomic design approach so other teams can generate emails, flyers, docs from the same system; (3) Automated workflows—Devin pulls live schedule data and exports PNGs directly to screens, replacing manual Figma updates; (4) Validated output—Devin performs visual QA on sponsor logo banners (100% accuracy in tests) and speaker photo matching using visual detection; (5) Remove friction—designer thinks as attendee to anticipate wayfinding needs. He also used Devin to add an edit button to a deployed schedule when a last-minute change was needed.

## Relevance to YOLO loop

Maps directly to our code generation quality problem: establishing a locked constraint set (analogous to a design system) before agentic code generation should reduce drift and stylistic inconsistency across outputs. The automated QA validation pattern (agent checks agent output against a source-of-truth list) is immediately applicable to our test generation and asset verification steps.

## Notes

Visual logo QA demo showed 100% accuracy for presence/absence checks against a known list—worth testing as a pattern for completeness verification in generated artifacts.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-09-10 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-09-10-design-system-first-agent-scale` |
| Channel | aie |
| Video | [One Designer + AI. Hundreds of Deliverables. — Vincent Wendy, AI Engineer](https://www.youtube.com/watch?v=O1FN4awNEtM) |
| Published | 2026-09-10 |
| Ingested upstream | 2026-09-10 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
