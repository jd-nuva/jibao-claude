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

### Claw+ + Feral + All for One

The infinite engine:
1. Play Claw+ (0-cost) → damage + scaling (+3 per play this combat)
2. Feral returns it to hand (first 0-cost attack each turn)
3. Play Claw+ again → more damage, goes to discard
4. Play All for One (2 energy) → returns Claw+ from discard + deals 10 damage
5. Play Claw+ a third time

4+ Claw+ plays per turn. By turn 5, each Claw+ deals 16+ damage. Scales infinitely.

### Coolheaded + Full Orbs

Coolheaded channels Frost → evokes leftmost orb (if slots full). Use it to:
- Evoke a Dark orb for burst damage
- Evoke Lightning for chip damage
- Get a Frost orb for defense + draw a card

### Power Cell + 0-Cost Cards

Power Cell pulls 2 zero-cost cards from draw pile to hand at combat start. Synergizes with:
- **Claw+**: immediate damage + scaling
- **Chill**: channels Frost per enemy (huge in multi-enemy fights)
- Both in hand turn 1 = 2 free plays before spending energy

## Potion Timing

| Potion | When to Use |
|--------|------------|
| Focus Potion | Elite/Boss turn 1. Compounds value over entire fight. |
| Flex Potion | Lethal turn only. +5 Str wears off at end of turn. Perfect for finishing enemies. |
| Fruit Juice | Use from map immediately. Permanent +5 HP. |

## Index Management

Card indices shift after each play. Two approaches:
1. **Re-read state between every play** (safe but slow)
2. **Play right-to-left** (highest index first — lower indices don't shift)

When in doubt, re-read. A misplay (wrong card) can lose runs.
