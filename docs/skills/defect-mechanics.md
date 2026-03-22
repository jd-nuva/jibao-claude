# Defect Mechanics — Learnings from Gameplay

Hard-won knowledge from actual combat. These aren't theory — they're verified in-game.

## Orb System

### Passive/Evoke with Focus

Focus adds to BOTH passive and evoke values:

| Orb | Base Passive | Base Evoke | With Focus 2 |
|-----|-------------|------------|--------------|
| Lightning | 3 dmg/turn | 8 dmg (random enemy) | 5 / 10 |
| Frost | 2 block/turn | 5 block | 4 / 7 |
| Dark | +6 growth/turn | 6+ dmg (lowest HP) | +8 growth / 8+ dmg |

Dark orb is the sleeper MVP. With Focus 2 it grows by 8 per turn — after 3 turns it evokes for 30+. Let it cook during setup turns.

### Channeling into Full Slots

When you channel with all slots full, the **leftmost** orb is evoked to make room. This is controllable:

- Channel Lightning → evoke leftmost (could be Frost for block or Lightning for damage)
- Plan your orb order: put disposable orbs on the left, valuable ones on the right
- Rainbow+ channels Lightning → Frost → Dark in sequence, so 3 evokes cascade through

### Rainbow+ Evoke Cascade

With 3 full orb slots, Rainbow+ triggers 3 evokes in sequence. The resulting orbs are always [Lightning, Frost, Dark]. Track what evokes to predict damage/block gained:

Example: Start [Lightning, Frost, Lightning]
1. Channel Lightning → evoke leftmost Lightning (10 dmg) → [Frost, Lightning, Lightning]
2. Channel Frost → evoke leftmost Frost (7 block) → [Lightning, Lightning, Frost]
3. Channel Dark → evoke leftmost Lightning (10 dmg) → [Lightning, Frost, Dark]
Result: 20 damage + 7 block + fresh Dark orb

### Dualcast Behavior

"Evoke your rightmost Orb twice." In practice: first evoke consumes the rightmost orb, second evoke targets the NEW rightmost. So it evokes 2 different orbs, not the same one twice.

Example: Orbs [Frost, Dark, Lightning]
- 1st evoke: Lightning (10 dmg), consumed → [Frost, Dark]
- 2nd evoke: Dark (22 dmg to lowest HP), consumed → [Frost]

This means Dualcast can chain into Dark evoke for massive damage if Dark is second-from-right.

## Enemy Mechanics

### Skittish (Phantasmal Gardeners)

"First time hit each turn, gains X Block."

Key discovery: **multi-hit attacks resolve ALL hits before Skittish triggers.** Barrage with 3 orbs deals 7+7+7 = 21 damage, THEN Skittish applies Block. This makes Barrage the hard counter to Skittish enemies.

Single-hit attacks: damage resolves first, then Block is applied. So a 6-damage Strike on a 6-HP Skittish enemy kills it before Block matters.

Against Skittish: concentrate attacks on one target. Use Claw+ (0-cost) to "pop" the Skittish on one, then follow up with real damage on the same target while Block from Skittish remains.

### Ravenous (Corpse Slugs)

"When an enemy dies, Corpse Slug immediately eats it, becoming Stunned and gaining X Strength."

Chain kills are powerful: kill one → others are Stunned → free offense turn → kill another → remaining stunned again. Can keep 2+ enemies permanently stunned by killing them one at a time.

### Ritual (Cultists)

Gains X Strength at end of each turn. Damage ramps fast. Damp Cultist has Ritual 5 — extremely dangerous if not killed quickly. Prioritize the higher-Ritual cultist.

### Plating (Lagavulin Matriarch)

"At the end of your turn, gain X Block. Reduced by 1 at start of your turn."

- Boss regains Block AFTER your orb passives fire
- Lightning passive is absorbed by Plating Block every turn
- Attack during YOUR turn when Boss has 0 Block — that's the damage window
- Plating decreases by 1 each turn, so the fight gets easier over time

### Asleep (Lagavulin Matriarch)

"Awakens upon losing HP or after N turns."

- Use sleep turns to set up: play Powers (Feral), use Focus Potion, channel orbs
- Lightning passive deals damage but is absorbed by Plating Block — doesn't wake Boss
- Attacks absorbed by Block also don't wake (no HP loss)
- Boss wakes after N turns regardless — plan to have engine ready

## Key Card Combos

### The Recursive Engine (Claw+ + Feral + All for One + Helix Drill)

The deck's core is not "Claw does damage." It's a four-layer recursive system where each 0-cost card's value is multiplied 3-4x by the retrieval loop:

```
Layer 1: Power Cell pulls 0-costs to opening hand (free)
Layer 2: Play Claw+ (0) → Feral returns it → play again (2 plays, 0 energy)
Layer 3: All for One (2) → retrieves ALL 0-costs from discard → play them all again
Layer 4: Helix Drill (0) → 3 dmg per energy spent → play LAST for free burst
```

Verified output from Act 2 Boss Turn 5 (3 energy):
- Barrage+ (1) = 35 → All for One (2) = 10, retrieves Claw+ + Helix Drill
- Claw+ (0) = 16 → Feral returns → Claw+ (0) = 19 → Helix Drill (0) = 9
- **Total: 89 damage from 3 energy.** Plus 17 from end-of-turn passives = 106.

The implication: **0-cost cards are not "free plays." They are recursive fuel.** Every 0-cost Attack you add to the deck gets played 2-3 times per turn via Feral + All for One. Evaluate 0-cost cards at 3x their face value.

### Coolheaded + Full Orbs

Coolheaded channels Frost → evokes leftmost orb (if slots full). Use it to:
- Evoke a Dark orb for burst damage
- Evoke Lightning for chip damage
- Get a Frost orb for defense + draw a card

### Power Cell + 0-Cost Cards

Power Cell pulls 2 zero-cost cards from draw pile to hand at combat start. Synergizes with:
- **Claw+**: immediate damage + scaling
- **Chill**: channels Frost per enemy (huge in multi-enemy fights)
- **Helix Drill**: ready for late-turn burst from the start
- All three in hand turn 1 = 2-3 free plays before spending energy

## Orb Slot Scaling (Capacitor)

Capacitor is a **Power card** (+2 Orb Slots), not a relic. Must be drawn and played each combat.

Orb slot count is a **multiplier**, not an addition. Everything orb-related scales linearly:

| Metric | 3 slots | 5 slots | Change |
|--------|---------|---------|--------|
| Barrage+ damage | 21 | **35** | +67% |
| Lightning passive/turn | 3-6 | 6-9 | ~+100% |
| Frost passive block/turn | 2-4 | 4-6 | ~+50% |
| Dark survival (not evoked early) | Low | High | Qualitative |

Capacitor is highest-priority Power after Hailstorm+ in multi-turn fights. In boss fights with 200+ HP, the compounding difference between 3 and 5 orb slots over 6+ turns is 50-100 total damage.

## Hailstorm+ (AoE Scaling)

"At end of turn, if you have Frost, deal 8 damage to ALL enemies."

Hailstorm+ is not "an AoE card." It is a **passive damage engine** that makes AoE a solved problem for the rest of the run:

- 1 enemy (boss): 8 free damage/turn. Over 6 turns = 48.
- 2 enemies: 16 total/turn. Outpaces most single-target attacks.
- 3 enemies (Decimillipede): 24 total/turn. Equalizes HP across segments for simultaneous kills.

Critical constraint: must have at least 1 Frost orb channeled. This makes **Dualcasting your last Frost** the single worst misplay possible — it shuts off 8+ free damage per turn. Before any Dualcast, check: "Do I keep at least 1 Frost after this?"

Synergy chain: Coolheaded, Chill, Rainbow+ all channel Frost. The deck naturally maintains Frost presence without dedicating cards to it.

In Act 2, Hailstorm+ was the difference between winning and losing every multi-enemy fight. Without it, the Decimillipede's Reattach mechanic (segments revive if others alive) would have been unbeatable — we had no other way to damage all 3 segments simultaneously.

## Helix Drill (Late-Turn Burst)

"Deal 3 damage for each Energy previously spent this turn." 0-cost.

- Play LAST in your turn after spending all energy for maximum damage
- With 3 energy spent: 9 damage (free). With 7 energy (Hot Cocoa turn 1): 21 damage
- Works with All for One (0-cost retrieval), Feral (0-cost return)
- Does NOT count its own play as "spent" — only energy spent before it

## Potion Timing

| Potion | When to Use |
|--------|------------|
| Focus Potion | Elite/Boss turn 1. Compounds value over entire fight. |
| Flex Potion | Lethal turn only. +5 Str wears off at end of turn. Perfect for finishing enemies. |
| Fruit Juice | Use from map immediately. Permanent +5 HP. |
| Vulnerable Potion | Boss/elite turn 1. +50% Attack dmg for 3 turns. Potions don't trigger Unsettling Lamp. |
| Dexterity Potion | Long elite/boss fights. +2 Dex compounds on every block card. |

## Dexterity Interactions

- Dex boosts block from CARDS that say "Gain X Block" (Defend, Lightning Rod+)
- Dex does **NOT** boost Frost passive block or Frost evoke block (orb effects are not cards)
- Dex does **NOT** boost Plating block (it's a power effect, not a card)

## Index Management

Card indices shift after each play. Two approaches:
1. **Re-read state between every play** (safe but slow)
2. **Play right-to-left** (highest index first — lower indices don't shift)

When in doubt, re-read. A misplay (wrong card) can lose runs.
