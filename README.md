# 鸡煲claude (jibao-claude)

AI agent plays the Defect in Slay the Spire 2.

The Defect is a robot. Its cards are literally called "Machine Learning", "Creative AI", "Compile Driver". Now an actual AI agent is piloting it. Three layers of meta. Peak irony.

## What

[STS2MCP](https://github.com/Gennadiyev/STS2MCP) mod exposes game state over HTTP (like CDP for Chrome). We read JSON, think hard, send commands. No screenshots, no mouse clicking. Just a robot controlling a robot playing robot cards.

```
STS2 Game ◄──── STS2MCP mod (HTTP localhost:15526) ────► 鸡煲claude (the brain)
  Unity          game driver                               Claude Code + Python
```

The brain is built as **Claude Code skills** — strategy docs that load on demand. In combat? Load combat strategy. Picking cards? Load deckbuilding. No wasted context.

## Setup

Python 3.12+, [uv](https://docs.astral.sh/uv/), [STS2MCP mod](https://github.com/Gennadiyev/STS2MCP), [Claude Code](https://docs.anthropic.com/en/docs/claude-code).

```bash
git clone https://github.com/jiaodong/jibao-claude.git
cd jibao-claude
uv sync --extra dev
```

## Play

1. Launch STS2 with STS2MCP mod
2. Start a run (pick the Defect obviously)
3. Open Claude Code in this repo
4. `/play`

Manual control:

```bash
jb state              # what's happening
jb play 2             # play card 2
jb play 0 JAW_WORM_0  # play card 0 at target
jb end                # end turn
jb path 1             # choose map node
jb pick 0             # take card reward
jb skip               # skip
```

## Architecture

```
src/jibao/
  driver.py        # game driver (STS2MCP HTTP client)
  cli.py           # jb command
  models.py        # game state types
  game/            # state tracking
  knowledge/       # card/relic/enemy data
  strategy/        # decision engine
  probability/     # pile math, draw calcs

.claude/commands/
  play.md          # /play — gameplay loop
  analyze.md       # /analyze — deep analysis

docs/skills/       # strategy docs (progressive disclosure)
  combat.md        # combat sequencing
  deckbuilding.md  # card evaluation
  pathing.md       # map navigation
  probability.md   # probability engine
```

No MCP between us and the game. Direct HTTP via httpx. Token efficiency > protocol ceremony.

## Status

Building the brain.

- [x] Game driver + CLI (`jb`)
- [x] Strategy skills (combat, deckbuilding, pathing, probability)
- [x] Progressive disclosure skill architecture
- [ ] Knowledge base (cards, relics, enemies)
- [ ] Probability engine
- [ ] Strategy engine
- [ ] Run history

## License

MIT
