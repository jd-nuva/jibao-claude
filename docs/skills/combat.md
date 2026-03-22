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

## Common Mistakes

- Blocking when enemies are buffing (pure waste)
- Playing attacks before applying Vulnerable (lose 50% bonus damage)
- Using potions on easy fights (save for elites/bosses)
- Not checking if you can lethal before committing to a defensive turn
- Exhausting cards you'll need later in long fights
