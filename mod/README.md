# Slay The Spire 2 - MCP Server

A mod for [**Slay the Spire 2**](https://store.steampowered.com/app/2868840/Slay_the_Spire_2/) that lets AI agents play the game. Exposes game state and actions via a localhost REST API, with an optional MCP server for Claude Desktop / Claude Code integration.

Singleplayer and multiplayer (co-op) supported. Tested against STS2 `v0.99.1`.

> [!warning]
> This mod allows external programs to read and control your game via a localhost API. Use at your own risk with runs you care less about.

> [!caution]
> Multiplayer support is in **beta** — expect bugs. Any multiplayer issues encountered with this mod installed are very likely caused by the mod, not the game. Please disable the mod and verify the issue persists before reporting bugs to the STS2 developers.

## For Players

### Install

1. Copy `STS2_MCP.dll` and `STS2_MCP.json` to `<game_install>/mods/`
2. Launch the game and enable mods in settings (a consent dialog appears on first launch)
3. The mod starts an HTTP server on `localhost:15526` automatically

### Connect to Claude

Requires [Python 3.11+](https://www.python.org/) and [uv](https://docs.astral.sh/uv/).

**Claude Code** — add to your project's `.mcp.json`:

```json
{
  "mcpServers": {
    "sts2": {
      "command": "uv",
      "args": ["run", "--directory", "/path/to/STS2_MCP/mcp", "python", "server.py"]
    }
  }
}
```

**Claude Desktop** — add to `claude_desktop_config.json` with the same config as above.

The MCP server accepts `--host` and `--port` flags if you need non-default settings.

Full tool reference: [mcp/README.md](./mcp/README.md) | Raw HTTP API: [docs/raw_api.md](./docs/raw_api.md)

## For Developers

### Build & Install

Build the DLL and copy it along with the manifest JSON to `<game_install>/mods/`. Requires [.NET 9 SDK](https://dotnet.microsoft.com/download/dotnet/9.0).

### Features

**Singleplayer** — full coverage of all game screens:

Combat (play cards, use potions, end turn, in-combat card selection), rewards (claim, pick/skip cards), map navigation (full DAG with lookahead), rest sites, shop, events & ancients, card selection overlays (transform, upgrade, remove), relic selection, treasure rooms, keyword glossary across all entities.

**Multiplayer (beta)** — all singleplayer features plus:

End-turn voting (submit/undo), map node voting, shared event voting, treasure relic bidding, all-players state summary, per-player ready/vote tracking. Endpoints are mutually guarded (singleplayer endpoint rejects multiplayer runs and vice versa).

## How It Works

STS2MCP is a C# mod that runs inside the game process. It combines three layers to expose full game control over HTTP:

### 1. Mod loading (entry point)

Slay the Spire 2 is built on [Godot 4](https://godotengine.org/) with C#/.NET 9. MegaCrit ships an official mod loading framework (`MegaCrit.Sts2.Core.Modding`) that scans the `mods/` directory for DLLs and invokes methods marked with `[ModInitializer]`. This is our entry point — no injection or patching needed.

### 2. Godot scene tree introspection (reading state)

Godot's scene tree is a live, traversable node hierarchy — essentially a DOM for the game's UI and state. Every screen, button, card, and enemy is a typed node (e.g. `NConfirmButton`, `NCardGridSelectionScreen`, `NCombatScreen`).

The mod walks this tree each time it receives an API request:

```
SceneTree.Root
  └─ GameManager
       └─ CurrentScreen (varies by game state)
            ├─ HandContainer → card nodes → CardModel (name, cost, description, ...)
            ├─ EnemyContainer → enemy nodes → HP, intent, debuffs, ...
            ├─ OrbContainer → orb nodes → type, passive/evoke values
            └─ ConfirmButton, EndTurnButton, ...
```

Since STS2 ships its game logic as a .NET assembly (`sts2.dll`) with full type metadata, the mod can reference types like `CardModel`, `RunState`, and `EnemyModel` directly — no decompilation or reverse engineering required.

### 3. HTTP bridge (executing actions)

On initialization, the mod starts an `HttpListener` on `localhost:15526` in a background thread. Incoming requests are deserialized, and the corresponding actions (play a card, click a button, end turn) are queued onto Godot's main thread via `SceneTree.ProcessFrame`:

```
HTTP request → background thread parses route/params
  → action enqueued to ConcurrentQueue
  → Godot main thread dequeues & executes on next frame
  → result serialized as JSON → HTTP response
```

This two-thread design is necessary because Godot's scene tree is only safe to access from the main thread.

### Why this approach works well for STS2

- **C# = zero-cost reflection.** .NET assemblies carry full type metadata. All public types, methods, and fields in `sts2.dll` are directly referenceable without decompilation.
- **Godot scene tree = built-in introspection.** The engine is designed for traversable node hierarchies. `FindAll<T>()`, `GetNodeOrNull<T>()`, and node signals are first-class engine APIs, not hacks.
- **Turn-based = discrete state machine.** The game naturally rests in stable states (map, combat, event, shop) between player actions, making "read state → decide → act" straightforward.

### Generalizing to other Godot games

Any Godot + C# game is theoretically controllable with the same pattern, even without official mod support. The injection point changes (e.g. `DOTNET_STARTUP_HOOKS`, BepInEx, or assembly patching), but once inside the process, the scene tree and .NET reflection are always available. The real variable is how readable the game's node naming and type structure are — STS2 happens to use semantic names throughout, which makes building a clean API practical.

## License

MIT
