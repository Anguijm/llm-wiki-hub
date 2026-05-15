# Replace cloud TTS with on-device CPU model to eliminate API costs

> Back to [[experiments-index]]

Source: **[Voice AI: when is the "Her" moment? — Neil Zeghidour, Gradium AI](https://www.youtube.com/watch?v=P_RI1kCkRbo)** · aiDotEngineer · 2026-05-10

**Status:** `deferred` · **Effort:** `medium`

---

## Hypothesis

If we swap a cloud TTS provider for an on-device model (e.g., Gradion Phonon, <100M params running on smartphone CPU), then per-user voice API costs drop to near zero, because the inference runs locally without any network call or billed API token.

## What they did

Neil Zeghidour described how voice apps routinely burn fundraising budgets on TTS API bills before achieving user-base growth. His team built Gradion Phonon, a sub-100M parameter TTS model that runs on a smartphone CPU with voice cloning, outperforming existing on-device models like Kokoro which lack cloning. They opened a private beta to let developers build consumer voice apps that scale without per-call API fees.

## Relevance to YOLO loop

Any YOLO-loop feature that speaks output (status narration, agent voice feedback) currently incurs TTS API cost per run. Swapping to an on-device model removes that cost ceiling and enables offline/private operation.

## Notes

Deferred 2026-05-10: TTS-cluster; same reasoning as tts-models-like-llms. Park together.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-05-10 | `backlog` | Extracted from YouTube RSS |
|  | `` |  |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-05-10-on-device-tts-cost-reduction` |
| Channel | aiDotEngineer |
| Video | [Voice AI: when is the "Her" moment? — Neil Zeghidour, Gradium AI](https://www.youtube.com/watch?v=P_RI1kCkRbo) |
| Published | 2026-05-10 |
| Ingested upstream | 2026-05-10 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
