# Combat Strategy

## Decision Priority (never violate this order)

1. **Survive this turn** — if incoming damage > current HP + achievable block, use potions or kill the threat
2. **Lethal check** — can we kill an enemy? Especially elites/bosses. Killing = 0 future damage from that enemy
3. **Minimize damage taken** — block efficiently, kill highest-damage enemy first
4. **Maximize scaling** — play Strength/Dexterity powers, apply Vulnerable/Weak
5. **Don't waste** — don't over-block, don't exhaust key cards, don't use potions unnecessarily

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
