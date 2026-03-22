# Game Driver API Reference

Forked from [STS2MCP](https://github.com/Gennadiyev/STS2MCP) v0.2.1. Our version: `0.3.0-jibao` with full screen coverage.

## Connection

- **Base URL**: `http://localhost:15526`
- **Singleplayer**: `/api/v1/singleplayer`

## Read State

```bash
jb state              # markdown (human-readable)
jb state --json       # json (for computation, includes pile contents)
```

## Screen Types

`state_type` field tells you the current screen:

| state_type | Screen | Available Actions |
|------------|--------|-------------------|
| `monster` / `elite` / `boss` | Combat | play, end, potion, hselect, hconfirm |
| `hand_select` | In-combat card selection | hselect, hconfirm |
| `combat_rewards` | Post-combat rewards | claim, proceed |
| `card_reward` | Card reward selection | pick, skip |
| `map` | Map navigation | path |
| `rest_site` | Rest site | rest, proceed |
| `shop` | Shop | shop, openshop, proceed |
| `event` | Event / Ancient | event |
| `card_select` | Transform/upgrade/remove/enchant | select, confirm, cancel |
| `relic_select` | Boss relic choice | relic, skiprelic |
| `treasure` | Treasure room | chest, treasure, proceed |
| `menu` | No run active | -- |

## CLI Commands

| Command | What it does |
|---------|-------------|
| `jb state` | Current screen (markdown) |
| `jb state --json` | Current screen (json) |
| `jb play <idx> [target]` | Play card |
| `jb end` | End turn |
| `jb potion <slot> [target]` | Use potion |
| `jb toss <slot>` | Discard potion |
| `jb path <idx>` | Choose map node |
| `jb pick <idx>` | Pick card reward |
| `jb skip` | Skip card reward |
| `jb shop <idx>` | Buy shop item |
| `jb openshop` | Open shop inventory |
| `jb event <idx>` | Choose event option |
| `jb rest <idx>` | Choose rest option |
| `jb proceed` | Proceed to map |
| `jb claim <idx>` | Claim reward |
| `jb select <idx>` | Select card (card_select screen) |
| `jb confirm` | Confirm selection |
| `jb cancel` | Cancel selection |
| `jb chest` | Open treasure chest |
| `jb treasure <idx>` | Claim treasure relic |
| `jb relic <idx>` | Select relic (boss relic) |
| `jb skiprelic` | Skip relic selection |
| `jb hselect <idx>` | Combat hand card selection |
| `jb hconfirm` | Confirm combat card selection |

## JSON State Enhancements (v0.3.0-jibao)

### Combat state includes full pile contents
- `draw_pile`: list of cards with id, name, cost
- `discard_pile`: list of cards with id, name, cost
- `exhaust_pile`: list of cards with id, name

### Map state includes deck/relics/potions
- `deck`: full card list for decision making
- `relics`: relic list with counters
- `potions`: potion list with slot indices

### No GET side effects
- Shop inventory is NOT auto-opened on state read (use `jb openshop`)
- Treasure chest is NOT auto-opened on state read (use `jb chest`)

## Gotchas

- **Card indices shift** after playing a card. Re-read state between plays.
- **Play right-to-left** (highest index first) to keep lower indices stable, OR re-read state each time.
- **Target format**: entity_id is `lower_snake_case_0` (e.g., `SLUDGE_SPINNER_0`).
- **Potions before cards**: buff potions don't cost energy. Use them first.
- **Events**: "Proceed" is an option with an index, not the `proceed` action. Use `jb event <idx>`.
- **Enchant/upgrade/transform screens**: use `jb select <idx>` then `jb confirm`.
