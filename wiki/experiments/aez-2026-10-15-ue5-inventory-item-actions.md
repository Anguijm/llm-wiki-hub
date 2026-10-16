# Implement a gameplay-tag-driven item action system in UE5 so inventory interactions are context-aware and data-driven

> Back to [[experiments-index]]

Source: **[Data Driven Inventory System (Part 15: UI Item Actions) | Unreal Engine 5](https://www.youtube.com/watch?v=7mxkcQeiR-s)** · aez · 2026-10-15

**Status:** `backlog` · **Effort:** `medium`

---

## Hypothesis

If we define all inventory item actions (use, equip, unequip, drop, destroy) as gameplay tags and map each tag to display text, icon, and color in a single widget function, then adding or changing actions requires only tag registration with no widget code changes, because the single get_display_options function and the get_available_actions function serve as the sole extension points for new contexts.

## What they did

Ali built a UE5 inventory action prompt system. Each action (use, equip, unequip, drop, destroy) is registered as a gameplay tag. A W_InventoryAction widget accepts an action tag on spawn and calls get_display_options to resolve text, icon (input-binding image), and color. A container widget queries get_available_actions on the item to build the prompt list dynamically. A hover-end/destruct fix prevents stale prompts when items disappear. He noted that context-dependence (e.g. sell vs. equip when near a shopkeeper) should be handled inside get_available_actions as the single extension point.

## Relevance to YOLO loop

none: UI widget pattern in UE5 Blueprints, not related to AI dev loop.

## Notes

Part 15 of a series. Part 16 covers hotbar. Extended Patreon lesson adds a fully data-driven input system. Key pattern: get_available_actions() is the single context-aware extension point—check context, check equipped state, return tag list. Destruct event should call hover_end to prevent stale prompt widgets.

## Status history

| Date | Status | Note |
|---|---|---|
| 2026-10-15 | `backlog` | Extracted from YouTube RSS |

---

## Metadata

| Field | Value |
|---|---|
| Experiment ID | `aez-2026-10-15-ue5-inventory-item-actions` |
| Channel | aez |
| Video | [Data Driven Inventory System (Part 15: UI Item Actions) | Unreal Engine 5](https://www.youtube.com/watch?v=7mxkcQeiR-s) |
| Published | 2026-10-15 |
| Ingested upstream | 2026-10-15 |
| Source | [yolo-projects/experiments.json](https://github.com/Anguijm/yolo-projects/blob/main/experiments.json) |

---

## Related pages

- [[yolo-projects]] - upstream pipeline that synthesized this experiment
- [[yolo-phase4-integration]] - how experiments are synced into this wiki
- [[experiments-index]] - all experiments
- [[index]] - wiki home
