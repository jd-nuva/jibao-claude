# /analyze — Deep State Analysis

Analyze the current game state in depth. Use this before boss fights, tough elites, or any decision that feels close.

## Procedure

1. **Get full JSON state**: `jb state --json`
2. **Analyze based on screen type**:

### Combat Analysis
- List each enemy: name, HP, intent (damage amount if attacking)
- Total incoming damage this turn (sum all attack intents)
- Available block from hand (sum all block cards playable within energy)
- Damage output options (enumerate card play sequences)
- Can we kill anything this turn?
- Worst case: what happens if we block optimally but can't kill?
- Potion check: would a potion swing this turn significantly?

### Deck Analysis (any screen)
- Current deck composition: attacks vs skills vs powers
- Key cards (scaling, AoE, draw)
- Weak cards (starter cards still present, low-impact additions)
- Missing coverage: no AoE? no scaling? no draw engine?
- Upgrade priorities

### Map Analysis
- Upcoming path options with lookahead
- Elite count on each path (and our HP/deck readiness for elites)
- Rest site availability before boss
- Shop availability (and do we have gold to spend?)

### Probability (in combat)
Read `docs/skills/probability.md` then compute:
- Draw pile size and known cards
- P(drawing key card next turn)
- Expected damage over next 2 turns
- Is the fight trending toward a win or a slow death?

## Output Format

Present findings as a short brief, then the recommended action with reasoning.
