# Probability Engine

## Pile Tracking

In StS2 combat, cards cycle through three piles:
- **Draw pile** — cards are drawn from here each turn (default 5)
- **Discard pile** — played/discarded cards go here
- **Exhaust pile** — permanently removed from this combat

When draw pile is empty and a draw is needed, discard pile shuffles into draw pile.

### What We Know

| Pile | Knowledge |
|------|-----------|
| Hand | Fully known (visible) |
| Discard pile | Fully known (always visible in game) |
| Exhaust pile | Fully known |
| Draw pile | **Size known, contents known** (= full deck - hand - discard - exhaust) |

This means we can compute exact probabilities for next draw.

## Key Calculations

### P(drawing card X next turn)

If draw pile has N cards and contains K copies of card X, and we draw D cards:

```
P(at least one X) = 1 - C(N-K, D) / C(N, D)
```

Where C(n, r) = binomial coefficient.

If draw pile is empty (will shuffle discard), compute against the discard pile contents.

### Expected Damage

For each card in draw pile, compute its expected damage contribution:
```
E[damage] = sum over all cards: P(drawing card) * card_damage(with_current_buffs)
```

Factor in Strength, Vulnerable on enemies, multi-hit, etc.

### Block Sufficiency

Same approach — compute expected block from next hand:
```
E[block] = sum over all cards: P(drawing card) * card_block(with_current_dexterity)
```

Compare against expected enemy damage (from intents + patterns).

### Lethal Probability

Can we kill enemy X within N turns?
- Turn 1: exact (we see our hand)
- Turn 2+: probabilistic (depends on draws)
- Monte Carlo: simulate N random draws from draw pile, compute kill rate

## Shuffle Prediction

When draw pile empties mid-turn (e.g., from draw effects), the discard pile shuffles in. After shuffle:
- New draw pile = old discard pile (randomized)
- This resets probability calculations — re-derive from new pile contents

## When to Use This

- **Must-block turns**: compute P(drawing enough block) to decide if a potion is needed
- **Lethal attempts**: compute P(drawing enough damage to kill) vs playing safe
- **Long fights**: track if our damage output is trending up (scaling) or down (enemy scaling faster)
- **Key card dependency**: if the deck revolves around 1-2 key cards, track P(drawing them)

## Implementation Notes

Use `src/jibao/probability/` for the math. Key functions to build:
- `draw_probability(draw_pile: list[Card], target: Card, draw_count: int) -> float`
- `expected_damage(hand: list[Card], draw_pile: list[Card], player: Player, enemies: list[Enemy]) -> float`
- `simulate_turns(state: GameState, n_turns: int, n_sims: int) -> SimResult`
