# Game Driver API Reference

The game driver is [STS2MCP](https://github.com/Gennadiyev/STS2MCP) — a BepInEx mod that serves game state over HTTP. Like CDP for Chrome.

## Connection

- **Base URL**: `http://localhost:15526`
- **Singleplayer**: `/api/v1/singleplayer`
- **Multiplayer**: `/api/v1/multiplayer`

## Read State

```bash
jb state              # markdown (human-readable)
jb state --json       # json (for computation)
```

## Screen Types

`state_type` field tells you the current screen:

| state_type | Screen | Available Actions |
|------------|--------|-------------------|
| `monster` / `elite` / `boss` | Combat | play_card, end_turn, use_potion, combat_select_card, combat_confirm_selection |
| `hand_select` | In-combat card selection | combat_select_card, combat_confirm_selection |
| `combat_rewards` | Post-combat rewards | claim_reward, proceed |
| `card_reward` | Card reward selection | select_card_reward, skip_card_reward |
| `map` | Map navigation | choose_map_node |
| `rest_site` | Rest site | choose_rest_option, proceed |
| `shop` | Shop | shop_purchase, proceed |
| `event` | Event / Ancient | choose_event_option, advance_dialogue |
| `card_select` | Transform/upgrade/remove | select_card, confirm_selection, cancel_selection |
| `relic_select` | Boss relic choice | select_relic, skip_relic_selection |
| `treasure` | Treasure room | claim_treasure_relic, proceed |
| `menu` | No run active | -- |

## CLI Commands

| Command | What it does |
|---------|-------------|
| `jb state` | Current screen (markdown) |
| `jb state --json` | Current screen (json) |
| `jb play <idx> [target]` | Play card |
| `jb end` | End turn |
| `jb potion <slot> [target]` | Use potion |
| `jb path <idx>` | Choose map node |
| `jb pick <idx>` | Pick card reward |
| `jb skip` | Skip card reward |
| `jb shop <idx>` | Buy shop item |
| `jb event <idx>` | Choose event option |
| `jb rest <idx>` | Choose rest option |
| `jb proceed` | Proceed to map |
| `jb claim <idx>` | Claim reward |

## Gotchas

- **Card indices shift** after playing a card. Re-read state between plays.
- **Play right-to-left** (highest index first) to keep lower indices stable, OR re-read state each time.
- **Target format**: entity_id is `UPPER_SNAKE_CASE_0` (e.g., `KIN_PRIEST_0`).
- **Potions before cards**: buff potions don't cost energy. Use them first.
- **Events**: "Proceed" is an option with an index, not the `proceed` action. Use `jb event <idx>`.
