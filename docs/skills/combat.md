# Combat Strategy

## The Scaling Clock (铁律)

Most elites and bosses gain Strength every turn. The fight gets harder the longer it goes:

| Enemy | Scaling | Implication |
|-------|---------|-------------|
| Byrdonis | +1 Str/turn (Territorial) | 16 → 20 → 24... by turn 5 |
| Bygone Effigy | +10 Str on buff turn | From 0 to 25 damage in one turn |
| Kin Priest Followers | +2 Str per buff turn | Minion damage doubles over 3-4 turns |
| Slimed Berserker | +3 Str/turn | Hits 33 by turn 4 |
| Devoted Sculptor | +9 Str/turn (Ritual 9) | Hits 40+ by turn 3 |

**Every turn you DON'T kill them, the block requirement goes up.** Playing defensively against scaling enemies is a losing strategy — you fall behind the curve. Balance offense and defense, but lean offense. When in doubt, kill faster.

## Decision Priority (never violate this order)

1. **Survive this turn** — if incoming damage > current HP + achievable block, use potions or kill the threat
2. **Lethal check** — can we kill an enemy? Especially elites/bosses. Killing = 0 future damage from that enemy
3. **Minimize damage taken** — block efficiently, kill highest-damage enemy first
4. **Race the clock** — scaling enemies punish slow play. Don't turtle when you should be dealing damage
5. **Maximize scaling** — play Strength/Dexterity powers, apply Vulnerable/Weak
6. **Don't waste** — don't over-block, don't exhaust key cards, don't use potions unnecessarily

## Card Play Sequencing

Within a turn, play cards in this order:

1. **Free (0-cost) utility**: draw cards, setup, cantrips
2. **Potions that buff**: Flex Potion, Strength Potion (before attacks!)
3. **Powers**: Strength, Dexterity, Demon Form, etc.
4. **Debuffs on enemies**: Vulnerable, Weak (before attacks!)
5. **Attacks**: biggest attacks last (they benefit from accumulated Strength/Vulnerable)
6. **Block**: with remaining energy, block against incoming damage
7. **Don't play a card just because you can** — sometimes ending with unspent energy is correct if remaining cards would dilute future draws (e.g., shuffling weak cards into draw pile)

## Intent Reading

| Intent | Meaning | Response |
|--------|---------|----------|
| Attack (number shown) | Exact damage incoming | Block at least that much, or kill them |
| Multi-attack (NxM) | N hits of M damage each | Block = N*M total. Thorns/retaliate effects trigger N times |
| Block/Buff | Enemy is NOT attacking | Go all-in offense. Don't waste energy blocking |
| Debuff | Usually no damage | Offense turn, but consider debuff impact |
| Unknown/? | Could be anything | Assume moderate attack, hedge |

## Enemy Priorities

- **Kill order**: highest damage intent > lowest HP (easiest kill) > buffers (before they scale)
- **Minions**: kill the leader, minions die. Don't waste cards on minions unless leader is unkillable this turn
- **AoE vs single-target**: if multiple enemies, prefer AoE. If one big enemy, single-target

## Energy Math

Before playing anything, count:
- Available energy (usually 3, check powers/relics)
- Total cost of cards you want to play
- If short on energy: cut the least impactful card
- If you have excess: consider if playing more cards is actually good (some decks want thin turns)

## Defect-Specific Combat

For detailed orb mechanics, enemy behaviors, and card combos, see `docs/skills/defect-mechanics.md`.

Key quick rules:
- **Channeling into full orb slots evokes the leftmost orb** — plan orb order accordingly
- **Dark orb grows each turn** — let it cook during setup turns, evoke later for burst
- **Multi-hit attacks (Barrage) resolve all hits before Skittish triggers** — hard counter
- **Dualcast evokes rightmost, then NEW rightmost** — chains through 2 orbs
- **Boss Plating resets each turn** — attack during YOUR turn when Boss has 0 Block
- **Focus Potion on turn 1 of elites/bosses** — compounds value over entire fight

## Relic Synergy Combos (verified in-game)

### Razor Tooth + Pocketwatch
**Razor Tooth** (auto-upgrade every card played) + **Pocketwatch** (draw 3 extra if <=3 cards played) is a top-tier combo:
- Razor Tooth makes ALL cards upgraded, including Strikes (6→9), Defends (5→8), and 0-cost cards
- Pocketwatch rewards lean turns — play 3 strong upgraded cards, draw 7 next turn
- **Tension**: playing more cards = more Razor Tooth value, but breaks Pocketwatch. Solution: play 3 high-impact cards per turn
- 0-cost cards (Claw, FTL, Dualcast+, Zap+) are MVP because they deal damage/setup without costing energy or breaking Pocketwatch count

### Venerable Tea Set + Charge Battery
**Venerable Tea Set** (+2 energy after rest sites) makes first combat after rest a 5-energy blowout. Stack with **Charge Battery** (+1 energy next turn) for sustained 4-energy turns. Route through rest sites before hard fights.

### Nunchaku + 0-cost attacks
**Nunchaku** (every 10 attacks = +1 energy) triggers faster with Claw (0E) and FTL (0E). In long fights the bonus energy adds up.

### Slow (enemy power) + card order optimization
**Slow** enemies take 10% more damage from Attacks per card played that turn. Play skills/0-cost first to stack %, then heavy attacks last. Evoke damage from Dualcast does NOT benefit from Slow (it's not an Attack card).

## Act 1 Elite/Boss Patterns

### Byrdonis (Elite, 92 HP)
- **Territorial**: gains +1 Strength at end of each turn. Damage scales linearly — kill fast
- Pattern: big single attack → multi-hit → repeat, interspersed with +1 Str
- With +10 Str by turn 5, attacks hit for 20+. This fight punishes slow decks
- Block every attack turn, go all-in on buff turns

### Bygone Effigy (Elite, 127 HP)
- **Sleeping** turn 1: attacks do NOT wake it. Free setup turn!
- **Slow** power: stacks 10% per card played. Play many cheap cards then big attacks
- After waking: buffs +10 Strength(!) on buff turn. Then attacks hard
- Kill before Strength snowballs — aim for 3-4 turn kill after wake

### Kin Priest (Boss, 190 HP) + 2 Kin Followers
- **Key insight**: Kill Priest → followers flee (Minion power). Focus ALL damage on Priest
- Followers buff and attack (7-9 damage each). Priest attacks 8-10 + debuffs (Frail, Weak)
- **Total incoming damage from 3 enemies can exceed 25/turn** — need serious block
- Vulnerable Potion on Priest turn 1 is massive (50% more Attack damage for 3 turns)
- **Lightning evoke is RANDOM** — Dualcast may hit followers instead of Priest. Targeted attacks (Ball Lightning, Strike) are more reliable for boss damage
- Deck needs both offense AND defense. Pure offense decks die to 3-way attacks

## Act 2 Elite/Boss Patterns

### Thieving Hopper
- Attacks + steals a card via **Swipe**. "Returned on kill" is unreliable — may lose the card permanently
- Has **Flutter** after buffing: 50% less Attack damage, need 5 attack hits to Stun
- Kill fast before **Escape Artist** timer runs out (steals gold and flees)
- Multi-hit attacks (Barrage) count multiple hits toward Stun threshold

### Bowlbug (Rock)
- **Imbalanced**: if you fully block its attack, it becomes **Stunned** next turn
- Prioritize exact block math: Defend + Frost passives can precisely hit the threshold
- Free offense turn after Stun — go all-in damage

### Decimillipede (3 segments)
- **Reattach**: killed segments revive in 2 turns if ANY other segment is alive
- Must kill all segments within 2 turns of each other — Hailstorm+ equalizes HP across segments
- Segments rotate intents (Attack, Buff, Debuff) — they get Strength over time
- AoE is king: Hailstorm+ (8/turn to all) does the heavy lifting

### Infested Prism (Elite, 200 HP)
- **Vital Spark**: first Attack damage per turn grants +1 Energy (only triggers on HP damage, NOT blocked damage)
- Alternates Attack and Buff/Defend turns — use Buff turns for Powers and setup
- High HP pool requires sustained engine damage — Dark orb + Barrage are key
- Opens with 22 damage, escalates with Strength

### The Insatiable (Act 2 Boss, 321 HP)
- **Sandpit**: death timer (eaten alive). Starts around 4 turns, ticks down each round
- **Frantic Escape** status cards: playing them EXTENDS the timer (+1 Sandpit). Costs energy though
- Turn 1 is always Buff + StatusCard (no attack) — go full setup: all Powers + Vulnerable Potion
- StatusCards (6 per cast) massively clog the deck — draw/thin is critical
- DPS race: need ~75 damage/turn. Barrage (5 orbs = 35) + Claw engine + Hailstorm + passives
- Use Frantic Escape strategically if timer gets to 2 or less

## Potion Timing (Act 2 additions)

| Potion | When to Use |
|--------|------------|
| Vulnerable Potion | Boss/elite turn 1. +50% Attack damage for 3 turns. Use BEFORE attacks. |
| Dexterity Potion | Long fights (elite/boss). Compounds block value over many turns. |
| Skill Potion | Energy-starved turns or when you need emergency block. Can find TURBO for +2 energy. |

## Common Mistakes

- Blocking when enemies are buffing (pure waste)
- Playing attacks before applying Vulnerable (lose 50% bonus damage)
- Using potions on easy fights (save for elites/bosses)
- Not checking if you can lethal before committing to a defensive turn
- Exhausting cards you'll need later in long fights
- Playing wrong card due to index shift (re-read state or play right-to-left)
- Waking sleeping bosses accidentally with passive orb damage through Block
- Using Dualcast expecting same-orb double evoke (it's 2 different orbs)
- **Dualcasting away your last Frost** — kills Hailstorm+ trigger, loses passive block
- **Not playing Frantic Escape** against The Insatiable when timer is low — it's not a waste card, it's a lifeline
- **Chaining `jb play` commands without re-reading state** — index shifts cause wrong-card plays constantly
- **Going pure offense against multi-enemy bosses** — 3 enemies dealing 25+ total/turn kills you fast if you skip block
- **Using Dualcast to target a specific enemy** — evoke is RANDOM, it will hit followers/minions. Use targeted attacks (Ball Lightning, Strike) for boss damage
- **Taking HP-cost events (Chosen Cheese, blood shrine) before boss** — the 14 HP loss directly contributed to our death
- **Over-valuing Pocketwatch trigger** — sometimes playing 4 cards for more block is better than playing 3 for extra draw. Survival > draw
