# Build a dual-display ESP32 terminal as a dedicated offline AI interaction device

> Back to [[experiments-index]]

Source: **[OpenClaw in Your Hand: Building a Physical AI Terminal - Lech Kalinowski, Callstack](https://www.youtube.com/watch?v=akk6KRlcwW4)** · aie · 2026-06-28

**Status:** `backlog` · **Effort:** `high`

---

## Hypothesis

If we build a microcontroller-based terminal with a dynamic OLED display and a bistable e-paper display connected to a backend that routes LLM calls through an OpenAI-compatible proxy, then we get a distraction-free, energy-efficient AI interface that works even when primary devices fail, because separating the display medium from the compute layer allows each to be optimised independently.

## What they did

Lech built a handheld terminal using an ESP32 dual-core MCU, a small OLED (live/dynamic surface) and an e-paper display (rendered output), a keyboard, and an encoder. The device runs an internal shell for system control, an AI assistant mode, and an RPG world-generation mode. A full backend handles agentic work via OpenClaw and proxies LLM calls through a TensorRT-served open-source 120B model exposed as an OpenAI-style API. He used fixed static buffers and pre-allocated 1-bit image pages on the MCU (no markdown engine, no malloc on device) to keep firmware tiny and fast. A shared index means context persists across sessions. The device is power-managed from a single LiPo cell and proved resilient — e-paper works if OLED fails, encoder works if keyboard fails.

## Relevance to YOLO loop

Mostly exploratory hardware project — low direct relevance to the YOLO loop. However, the backend architecture (OpenAI-compatible proxy over a locally-served open-source model, OpenClaw integration) is a reusable pattern for self-hosted model routing in the loop.

## Notes

High effort for hardware build. Backend proxy pattern (TensorRT + OpenAI-style API over local model) is the extractable experiment worth revisiting independently of the physical device.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-06-28 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aie-2026-06-28-openclaw-physical-ai-terminal` |
| Channel | aie |
| Video | [OpenClaw in Your Hand: Building a Physical AI Terminal - Lech Kalinowski, Callstack](https://www.youtube.com/watch?v=akk6KRlcwW4) |
| Published | 2026-06-28 |
| Ingested upstream | 2026-06-28 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
