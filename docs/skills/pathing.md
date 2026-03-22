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

## Act 2 Validated Route (Right Column)

Our actual Act 2 path and what it taught:

```
Ancient → Monster → Shop → Monster → Monster → Elite → Shop → Rest →
Treasure → Rest → Unknown → Rest → Elite → Unknown → Rest → Boss
```

Key stats: 4 Rest Sites, 2 Shops, 2 Elites, 1 Treasure, 2 Unknowns, 3 Monsters.

Lessons:
- **Double elite is viable** if the path has enough Rest Sites between/after them. We dropped to 16 HP and 38 HP after elites but recovered both times.
- **Shop timing matters more than shop contents.** First shop (Floor 20): removed Strike. Second shop (Floor 24): bought Capacitor. Card removal early, card addition later.
- **Rest vs Smith**: at <65% HP, rest. We rested 4 times and smithed 0. In hindsight, one Smith at 65% HP for Coolheaded+ (draw 2) would have been worth the risk.

## Event Decisions (Act 2 learnings)

| Event | Choice | Outcome | Lesson |
|-------|--------|---------|--------|
| Tezcatara (Ancient) | Very Hot Cocoa | +4 energy turn 1, full heal | Best possible Act 2 opener. Cocoa is transformative. |
| Slippery Bridge | Re-roll 3x (12 HP), remove Defend | Deck thinned | Worth paying HP to re-roll until a starter card shows. 12 HP = cheap card removal. |
| This or That? | Clumsy curse + random relic | Got Unsettling Lamp | Ethereal curses are nearly free — auto-exhaust after 1 turn. Take the relic. |

## General Rules

- **Never path into an elite below 50% HP** unless you're certain your deck can win taking <10 damage
- **Always path through a rest site before the boss** if available and below 80% HP
- **Treasure nodes are free value** — always prefer paths that include them
- **Shop routing**: if you have 100+ gold, route through a shop even if it means skipping a monster
- **Unknown nodes can be fights** — don't assume they're free events at low HP
- **Silver Crucible tradeoff** — first 3 card rewards upgraded, but first treasure chest is empty. Still worth it (upgrades > 1 relic)
- **Pre-boss shop**: remove a Strike + buy Focus Potion = massive boss prep
- **Plating bosses (Lagavulin)**: rest before boss is critical — fight is long, HP buffer matters
- **HP is a resource, not a score.** Taking 12 damage at Slippery Bridge to remove a Defend was correct. Taking 14 damage from skipping block to play Feral against The Insatiable was correct. Spending HP now to improve all future turns is an investment.
