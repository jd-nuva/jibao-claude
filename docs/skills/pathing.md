# Map Pathing Strategy

## Node Types and When to Take Them

| Node | Risk | Reward | Take When |
|------|------|--------|-----------|
| Monster | Low | Card reward + gold | Default path filler |
| Elite | High | Relic + card + gold | HP >70%, deck can handle it |
| Rest Site | None | Heal or upgrade | Before boss, or at <50% HP |
| Shop | None | Buy/remove | Have 75+ gold |
| Unknown/? | Variable | Random event | Medium HP, not urgent needs |
| Treasure | None | Free relic | Always good |
| Boss | Very high | Boss relic + next act | End of act (mandatory) |

## Pathing Priorities by Act

### Act 1
- **Goal**: build a functioning deck that can beat the Act 1 boss
- Take 1-2 elites if HP allows (early relics compound value)
- Hit a shop to remove a Strike
- Rest site before boss

### Act 2
- **Goal**: AoE coverage, begin scaling, prepare for harder fights
- Multi-enemy fights are dangerous without AoE — avoid elites if deck is weak
- Shop for removal and key pickups
- Rest sites more valuable (fights hit harder)
- **Early shop path**: route through a shop in the first 3 floors to remove a Strike early
- **Elites are worth it at 70%+ HP**: relics compound — we beat 2 Act 2 elites and the relics (Unsettling Lamp, Lucky Fysh, Permafrost) carried through the boss
- **Rest-heavy right side**: the right column often chains Rest → Treasure → Rest — great for post-elite recovery
- **Tezcatara (Ancient)**: full heal + powerful relic choice. Very Hot Cocoa (+4 energy turn 1) is transformative

### Act 3+
- **Goal**: deck is nearly complete, survive to boss
- Avoid unnecessary fights that risk HP for cards you don't need
- Prioritize rest sites and shops
- Only take elites if confident and the relic would help the boss fight

## Lookahead

STS2MCP provides 1-level lookahead (children of each next option). Use it:
- If a node leads to a rest site, it's safer (you can heal after)
- If a node leads to an elite, plan whether you'll be ready
- Avoid paths that bottleneck into an elite when at low HP

## HP Budget Rule (铁律)

**Before entering any node, calculate: "can I survive the next 2 nodes?"**

- Boss fights have 3+ enemies dealing 20-27 total damage/turn. Enter boss at 40+ HP minimum
- HP-cost events (Chosen Cheese, blood shrines) are traps when <50% HP or within 3 floors of boss
- Two back-to-back elites are viable ONLY with rest site between or very strong deck
- Track cumulative HP loss: if you're losing 15+ HP per monster fight, your deck needs block cards or you need to avoid fights

### Pre-Boss HP Threshold

| Act | Minimum HP for Boss | Reason |
|-----|--------------------|---------|
| 1 | 40+ HP | Kin Priest has 3 enemies, 25+/turn total damage |
| 2 | 50+ HP | The Insatiable is a DPS race with timer mechanic |
| 3 | 60+ HP | Slimed Berserker hits 33 by turn 4, Strength scaling |

## General Rules

- **Never path into an elite below 50% HP** unless you're certain your deck can win taking <10 damage
- **Always path through a rest site before the boss** if available and below 80% HP
- **Treasure nodes are free value** — always prefer paths that include them
- **Shop routing**: if you have 100+ gold, route through a shop even if it means skipping a monster
- **Unknown nodes can be fights** — don't assume they're free events at low HP
- **Silver Crucible tradeoff** — first 3 card rewards upgraded, but first treasure chest is empty. Still worth it (upgrades > 1 relic)
- **Pre-boss shop**: remove a Strike + buy Focus Potion = massive boss prep
- **Plating bosses (Lagavulin)**: rest before boss is critical — fight is long, HP buffer matters
- **Venerable Tea Set routing** — if you have Tea Set, always rest before hard fights for +2 energy turn 1
- **Spoils Map tradeoff** — 600 gold in next act is strong but adds an Unplayable card. Dead draws in combat can cost turns
