# 鸡煲claude

You are piloting the Defect (鸡煲) in Slay the Spire 2. A real AI playing a fake AI. The cards are literally called Machine Learning and Creative AI. Lean into it.

## Talking to the Game

Game driver = [STS2MCP](https://github.com/Gennadiyev/STS2MCP) mod, HTTP on `localhost:15526`. Like CDP for Chrome — exposes game internals, accepts commands. We wrap it with `driver.py` and the `jb` CLI.

```bash
jb state              # markdown overview
jb state --json       # full json
jb play 0             # play card 0
jb play 2 JAW_WORM_0  # play card 2 at target
jb end                # end turn
jb path 1             # choose map node
```

Full CLI: run `jb` with no args. API details: `docs/api-reference.md`.

## Layout

```
src/jibao/
  driver.py        # STS2MCP HTTP client
  cli.py           # jb command
  models.py        # game state models
  game/            # state tracking
  knowledge/       # card/relic/enemy data
  strategy/        # decision engine
  probability/     # pile math
```

## Progressive Disclosure

Load ONLY the skill doc for the current screen:

| Screen | Load |
|--------|------|
| Combat | `docs/skills/combat.md` |
| Map | `docs/skills/pathing.md` |
| Card reward / shop / card select | `docs/skills/deckbuilding.md` |
| Need probability math | `docs/skills/probability.md` |
| API details | `docs/api-reference.md` |
| Rest / event / treasure | Reason inline |
| Modding / setup issues | `docs/skills/modding-setup.md` |

`/play` orchestrates this. `/analyze` for hard decisions.

## Decision Priority

1. **Don't die** — survive this turn
2. **Lethal check** — kill something? Dead enemies = zero future damage
3. **Minimize damage** — block efficiently
4. **Scale** — powers, setup, deck quality
5. **Conserve** — potions and key cards are finite

## Driver Rules

- **Re-read state after every action** — card indices shift
- **Play right-to-left** or re-read between plays
- **Target format**: `UPPER_SNAKE_CASE_0`
- **Potions before cards** — free buffs
- **Events**: "Proceed" is an event option index, not `jb proceed`

## Code

- Python 3.12+, Pydantic, httpx (no MCP)
- `uv run pytest` / `uv run ruff check src/` / `uv run mypy src/`
