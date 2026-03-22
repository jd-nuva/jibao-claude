# /play — Gameplay Loop

Read the current game state and make the optimal decision. One step at a time.

## Procedure

1. **Read state**: `jb state` (markdown for overview) or `jb state --json` (for computation)
2. **Identify screen type** from the state output
3. **Load the relevant strategy doc** (and ONLY that doc — don't load everything):

| Screen | Read | Then |
|--------|------|------|
| Combat (`monster`/`elite`/`boss`) | `docs/skills/combat.md` | Sequence card plays, execute one at a time |
| Map | `docs/skills/pathing.md` | Evaluate paths, choose node |
| Card reward | `docs/skills/deckbuilding.md` | Evaluate cards against current deck |
| Shop | `docs/skills/deckbuilding.md` (shop section) | Prioritize removals > relics > cards |
| Rest site | Rest if <70% HP, smith best upgrade target otherwise |
| Event | Evaluate risk/reward vs current HP/gold/deck |
| Card select (transform/upgrade/remove) | `docs/skills/deckbuilding.md` | Pick weakest to remove, best to upgrade |

4. **Execute the decision**: `jb <command> <args>`
5. **Re-read state** to confirm the action landed, then decide next action

## Combat Flow (most complex)

```
jb state --json → read hand, enemies, intents, energy
  → Am I dead if I don't block? (survival check)
  → Can I kill an enemy this turn? (lethal check)
  → Sequence: 0-cost setup → buffs/debuffs → attacks → block with remaining energy
  → Play cards RIGHT-TO-LEFT by index (indices shift after each play)
  → jb play <index> [target]  (repeat for each card)
  → jb end
```

## Important

- **Re-read state after every action** — indices shift, state changes
- **Don't play all cards blindly** — sometimes saving energy or not playing is correct
- **Use potions before cards** when they buff (potions don't cost energy)
- **One step at a time** — don't try to plan 5 moves ahead without re-reading state
