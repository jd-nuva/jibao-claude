# STS2 Game Driver

A Godot C# mod for [**Slay the Spire 2**](https://store.steampowered.com/app/2868840/Slay_the_Spire_2/) that exposes game state and actions via a localhost REST API (`localhost:15526`). Forked from [STS2MCP](https://github.com/Gennadiyev/STS2MCP) — this fork drops the MCP protocol layer in favor of direct HTTP for lower latency and fewer tokens per call.

Tested against STS2 `v0.99.1`. Singleplayer and multiplayer (co-op) supported.

> [!warning]
> This mod allows external programs to read and control your game via a localhost API. Use at your own risk with runs you care less about.

## Install

1. Build the DLL (requires [.NET 9 SDK](https://dotnet.microsoft.com/download/dotnet/9.0)):
   ```bash
   ./build.sh        # builds + copies to game mods directory
   ```
2. Launch the game and enable mods in settings
3. The mod starts an HTTP server on `localhost:15526` automatically

## Usage

The API is plain HTTP — call it from any language. This repo uses a Python client (`src/jibao/driver.py`) and CLI (`jb`):

```bash
jb state              # GET /state → markdown overview
jb state --json       # GET /state → full JSON
jb play 0             # POST /action {play card 0}
jb play 2 JAW_WORM_0  # POST /action {play card 2 at target}
jb end                # POST /action {end turn}
```

No MCP server, no tool schemas, no protocol overhead — just HTTP request/response. See [docs/api-reference.md](../docs/api-reference.md) for the full endpoint list.

## Features

**Singleplayer** — full coverage of all game screens:

Combat (play cards, use potions, end turn, in-combat card selection), rewards (claim, pick/skip cards), map navigation (full DAG with lookahead), rest sites, shop, events & ancients, card selection overlays (transform, upgrade, remove), relic selection, treasure rooms, keyword glossary across all entities.

**Multiplayer (beta)** — all singleplayer features plus:

End-turn voting, map node voting, shared event voting, treasure relic bidding, all-players state summary, per-player ready/vote tracking.

### Fork differences from upstream STS2MCP

- Confirm button fallback (`FindAll<NConfirmButton>`) for enchant screens and non-standard layouts
- Full pile contents in combat state (draw, discard, exhaust)
- Deck/relics/potions available in map state
- No GET side effects (shop/chest auto-open removed)
- New actions: `discard_potion`, `open_chest`, `open_shop`, `open_map`
- Enchant screen type detection

## How It Works

The mod runs inside the game process as a C# DLL. Three layers make it work:

### 1. Mod loading (entry point)

STS2 is built on [Godot 4](https://godotengine.org/) with C#/.NET 9. MegaCrit ships an official mod loading framework (`MegaCrit.Sts2.Core.Modding`) that scans `mods/` for DLLs and calls methods marked `[ModInitializer]`. This is the entry point — no injection or patching needed.

### 2. Godot scene tree introspection (reading state)

Godot's scene tree is a live, traversable node hierarchy — essentially a DOM for the game UI. Every screen, button, card, and enemy is a typed node (`NConfirmButton`, `NCardGridSelectionScreen`, `NCombatScreen`, etc.).

The mod walks this tree on each API request:

```
SceneTree.Root
  └─ GameManager
       └─ CurrentScreen (varies by game state)
            ├─ HandContainer → card nodes → CardModel (name, cost, description, ...)
            ├─ EnemyContainer → enemy nodes → HP, intent, debuffs, ...
            ├─ OrbContainer → orb nodes → type, passive/evoke values
            └─ ConfirmButton, EndTurnButton, ...
```

Since STS2 ships its game logic as a .NET assembly (`sts2.dll`) with full type metadata, the mod references types like `CardModel`, `RunState`, and `EnemyModel` directly — no decompilation required.

### 3. HTTP bridge (executing actions)

On init, the mod starts an `HttpListener` on `localhost:15526` in a background thread. Actions are queued onto Godot's main thread via `SceneTree.ProcessFrame`:

```
HTTP request → background thread parses route/params
  → action enqueued to ConcurrentQueue
  → Godot main thread dequeues & executes on next frame
  → result serialized as JSON → HTTP response
```

This two-thread design is necessary because Godot's scene tree is only safe to access from the main thread.

### Why this works well

- **C# = zero-cost reflection.** .NET assemblies carry full type metadata — all public types, methods, and fields in `sts2.dll` are directly referenceable.
- **Godot scene tree = built-in introspection.** `FindAll<T>()`, `GetNodeOrNull<T>()`, and node signals are first-class engine APIs, not hacks.
- **Turn-based = discrete state machine.** The game rests in stable states (map, combat, event, shop) between player actions, making "read → decide → act" straightforward.
- **Direct HTTP > MCP for local agents.** No tool schema negotiation, no stdio pipes, no extra process. One HTTP call = one game action. Latency matters when you're chaining 10+ actions per turn.

### Generalizing to other Godot games

Any Godot + C# game is theoretically controllable with the same pattern, even without official mod support. The injection point changes (`DOTNET_STARTUP_HOOKS`, BepInEx, or assembly patching), but once inside the process, the scene tree and .NET reflection are always available. The real variable is how readable the game's node naming and type structure are — STS2 uses semantic names throughout, which makes building a clean API practical.

## License

MIT
