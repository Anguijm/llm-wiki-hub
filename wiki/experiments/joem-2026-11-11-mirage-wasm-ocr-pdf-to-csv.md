# Prototype Mirage WASM OCR fallback for scanned pages in PDF to CSV

> Back to [[experiments-index]]

Source: **[Vision, OCR, Decision Model in a Browser with Web Assembly: Cactus Compute Mirage 22MB](https://www.youtube.com/watch?v=j5DBU4SBLpc)** · joem · 2026-11-11

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we load Cactus Compute's 1.2MB cactus.wasm runtime and the 22MB Mirage model in a throwaway page and run it on self-made scanned receipt and table images, then we learn whether in-browser OCR with text bounding boxes is accurate enough to feed scanned pages into PDF to CSV, because the video shows Mirage returning OCR text boxes entirely client-side with no backend.

## What they did

Joe installed the Cactus Compute CLI and ran 'cactus mirage describe' on an image, getting structured JSON with scene description, text bounding boxes and object masks, which he filtered with jq. He wrapped it in a Bun server (0.68 s per image). He then compiled the WebAssembly bundle (cactus.js plus a 1.2MB cactus.wasm), which downloads the 22MB model into browser memory. He hosted it on GitHub Pages and ran OCR on a German receipt, and on a phone photo of a desk, with no server. Caveats: it needs Cactus's own runtime (not llama.cpp), and it can misclassify ambiguous shapes.

## Relevance to YOLO loop

none: This is a local-model tooling trial, not an AI development practice technique.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-11-11 | `backlog` | Extracted from YOLO Watch Log sheet (Gemini) |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `joem-2026-11-11-mirage-wasm-ocr-pdf-to-csv` |
| Channel | joem |
| Video | [Vision, OCR, Decision Model in a Browser with Web Assembly: Cactus Compute Mirage 22MB](https://www.youtube.com/watch?v=j5DBU4SBLpc) |
| Published | 2026-11-11 |
| Ingested upstream | 2026-11-11 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
