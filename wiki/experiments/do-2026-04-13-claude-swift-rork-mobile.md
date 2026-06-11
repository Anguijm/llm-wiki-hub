# Use Rork as a Claude-powered mobile prototyping layer

> Back to [[experiments-index]]

Source: **[Claude + Swift + Rork = insane mobile apps](https://www.youtube.com/watch?v=rQY-yB-Gob4)** · do · 2026-04-13

**Status:** `deferred` · **Effort:** `low`

---

## Hypothesis

If we route mobile app prototyping through Rork with Claude as the backend model and Swift as the output target, then we can collapse the design-to-native-prototype cycle from days to hours because Rork handles the Swift scaffolding while Claude maintains coherent feature logic across iterations.

## What they did

Speaker demonstrated building functional iOS apps by combining Claude (for logic and code generation), Swift (as the native target language), and Rork (as the AI-native mobile IDE/platform). The workflow produced working mobile prototypes rapidly with minimal manual coding.

## Relevance to YOLO loop

Maps to the scaffolding and rapid-prototype phase of the YOLO loop. If we ever need a mobile surface or want to test AI-assisted native app generation, this stack is a low-friction entry point. Also useful as a reference architecture for how a domain-specific IDE (Rork) can wrap a general model (Claude) effectively.

## Notes

Mobile not in current portfolio scope; Rork is external service. Revisit if mobile enters scope.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-04-13 | `backlog` | Extracted from YouTube RSS |
| 2026-04-22 | `deferred` | Mobile not in current portfolio scope; Rork is external service. Revisit if mobile enters scope. |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `do-2026-04-13-claude-swift-rork-mobile` |
| Channel | do |
| Video | [Claude + Swift + Rork = insane mobile apps](https://www.youtube.com/watch?v=rQY-yB-Gob4) |
| Published | 2026-04-13 |
| Ingested upstream | 2026-04-13 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
