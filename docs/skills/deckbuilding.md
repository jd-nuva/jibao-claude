# Deckbuilding Strategy

## Core Principle: Adapt to What You're Given (铁律)

The Defect has many viable archetypes — Lightning burst, Frost turtle, Dark scaling, Claw engine, Focus stacking, 0-cost spam, Power spam, and hybrids. **Don't precommit to an archetype.** Let the cards and relics you find guide you.

Decision flow at each card reward:
1. Look at what you already have — what's your deck doing well? What's it missing?
2. Pick the card that fills the biggest gap (block? damage? AoE? draw? scaling?)
3. If nothing fills a gap, skip. Deck quality > deck size

A 15-card deck that draws its key cards every turn beats a 30-card deck with individually strong cards.

## Card Evaluation Framework

When offered a card reward, score each card on:

1. **Does it solve a problem I have right now?**
   - No AoE → AoE card is high priority
   - No scaling → Strength/power cards are high priority
   - No draw → card draw is high priority
   - Not enough block → block/Frost cards are high priority
   - Starter cards still in deck → removal > addition

2. **Does it synergize with what I already have?**
   - Have lots of orbs → Barrage, Dualcast, Multi-Cast become great
   - Have Razor Tooth → 0-cost cards get extra value
   - Have Focus → Frost/Lightning passives scale harder
   - But don't force synergy that doesn't exist yet — a card must be good NOW or have clear future payoff

3. **What act are we in?**
   - Act 1: front-loaded damage, kill hallway fights fast. Also need BLOCK for boss (3 enemies possible)
   - Act 2: AoE mandatory (multi-enemy fights), some scaling
   - Act 3+: scaling and engine required, raw damage falls off

## Card Removal Priority

Remove the weakest card in the deck. Typical order:
1. **Strikes** (starter attacks) — worst damage-per-card in the game
2. **Defends** (starter blocks) — less impactful but still dilute
3. **Curses** — actively harmful, remove ASAP
4. **Low-synergy pickups** — cards that seemed good but don't fit the final deck

## Upgrade Priority

Upgrade the card that gets the biggest delta:
- Cards played every combat (your core engine)
- Cards where the upgrade adds a new effect (not just +1 damage)
- Scaling powers (the upgrade compounds over entire fights)
- Don't upgrade cards you plan to remove

## Shop Strategy

Priority order for spending gold:
1. **Card removal** (always worth it if you have Strikes/Defends left)
2. **Key relics** that synergize with your deck
3. **Key cards** you've been looking for
4. **Potions** (only if slots available and approaching a hard fight)
5. **Random colorless cards** (usually skip)

## Reference Archetypes (examples, not blueprints)

These are builds we've actually run. Use them as pattern recognition — "I have Razor Tooth, what worked with that before?" — not as checklists to force.

### Razor Tooth Lightning (Run 2, died Act 1 Boss)

Emerged from: Razor Tooth + Pocketwatch from Ancient choices.

| Role | Cards | Notes |
|------|-------|-------|
| Core relic | Razor Tooth (auto-upgrade all cards in combat) | Every Strike becomes Strike+, every Defend becomes Defend+ |
| Draw engine | Pocketwatch (<=3 cards = +3 draw) | Play 3 upgraded cards/turn, draw 7 next turn |
| 0-cost damage | FTL (5 dmg + draw), Claw (scales) | Free plays that don't break Pocketwatch |
| Orb burst | Dualcast+ (0 cost with Razor Tooth) | 16 evoke damage for free |
| Orb scaling | Ball Lightning (7+2 Sharp = 9 base → 12 upgraded) | Channels + deals targeted damage |
| Orb AoE | Barrage (5 per orb → 7 per orb upgraded) | With 3 orbs + Flex = 30+ damage |
| Block + energy | Charge Battery (7 block → 10 upgraded + 1E next turn) | Sustains 4E turns |

**Why it died**: not enough block for 3-enemy boss. Need 4+ block cards or Frost orbs for sustained defense. Offense-only loses to multi-enemy scaling.

### Orb Engine + Claw (Run 1, reached Act 3)

Emerged from: Claw + Feral early, then orb support cards appeared.

| Role | Cards | Priority |
|------|-------|----------|
| Engine | Claw+ (0-cost scaling) + Feral (return to hand) | Must-have |
| Burst | All for One (returns all 0-cost from discard) | High |
| Orb setup | Rainbow+, Lightning Rod+, Coolheaded, Zap | Core |
| Orb scaling | Capacitor (+2 orb slots, Power card) | High — Barrage 21→35 |
| AoE | Hailstorm+ (8 to ALL enemies/turn if Frost) | Critical for Act 2+ |
| AoE defense | Chill (0-cost, Frost per enemy, exhausts) | High in multi-enemy |
| Damage | Barrage / Barrage+ (scales with orb count) | Core |
| Late burst | Helix Drill (0-cost, 3 dmg per energy spent) | Good engine piece |
| Draw | Skim (draw 3), Coolheaded (Frost + draw 1) | Medium |
| Scaling | Focus Potion (save for elites/boss) | Critical |

### Relic Synergies
- **Power Cell**: pulls 0-cost cards (Claw+, Chill, Helix Drill) to hand at combat start
- **Very Hot Cocoa**: +4 energy turn 1 — deploy entire engine immediately
- **Oddly Smooth Stone**: +1 Dex at start — passive defense
- **Cracked Core**: free Lightning orb turn 1
- **Gorget**: +4 Plating — free block that decays, acts as buffer for first few turns
- **Permafrost**: first Power played each combat = +6 Block — play Capacitor/Hailstorm+ early
- **Unsettling Lamp**: first debuff card doubled — use with Vulnerable-applying cards

### Card Evaluation for This Archetype
- **0-cost attacks**: very high priority (Feral + All for One + Power Cell synergy)
- **Frost channelers**: high priority (defense scales with Focus)
- **Powers**: play during boss sleep turns or buff turns
- **Strike/Defend**: remove Strikes first, Defends are worse with Dex debuffs

### Shop Priority (Defect Orb Build)
1. Card removal (Strikes first)
2. Focus Potion (if approaching elite/boss)
3. Feral / key engine pieces
4. Frost/Lightning channelers

## Every Deck Needs These (archetype-agnostic)

Regardless of build, your deck MUST have answers for:

| Need | Why | Cards that solve it |
|------|-----|-------------------|
| **Block for 20+/turn** | Bosses and late elites hit this hard | Frost orbs, Defend+, Charge Battery, Glacier, Prolong |
| **Multi-enemy damage** | Act 2+ has many multi-enemy fights | Barrage, Sweeping Beam, Hailstorm, Lightning passive |
| **Burst single-target** | Kill scaling enemies before they ramp | Dualcast, Ball Lightning, Barrage (3 orbs = 15-21) |
| **Card draw** | Drawing your key cards wins fights | FTL, Skim, Coolheaded, card draw relics |
| **Scaling** | Fights that last 5+ turns need scaling | Focus (orbs scale), Claw (+2-3/play), Powers |

If your deck is missing any row, prioritize filling that gap at the next card reward or shop. Don't just pick "the best card" — pick the card that patches your weakest dimension.

## Skip Heuristics

Skip the card reward when:
- Deck is already ≥20 cards and none of the offered cards are exceptional
- All 3 cards are mediocre / don't synergize
- You're in Act 3+ and your deck is tuned — adding cards dilutes draw probability
- You'd rather the gold from the fight than any card offered
