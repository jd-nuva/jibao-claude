# STS2 Modding Setup (macOS)

## Mod Directory

The correct mod path on macOS is **inside the .app bundle, next to the executable**:

```
<steam_library>/Slay the Spire 2/SlayTheSpire2.app/Contents/MacOS/mods/{mod_folder}/
```

NOT `Contents/Resources/mods/`, NOT `~/Library/Application Support/SlayTheSpire2/mods/`.

The game discovers mods via `ReadModsInDirRecursive` starting from this directory.

## Mod Manifest Format

Each mod folder must contain a JSON manifest named `{mod_id}.json` (NOT `mod_manifest.json`). Required fields:

```json
{
  "id": "MyMod",
  "name": "My Mod Display Name",
  "author": "author",
  "description": "What it does",
  "version": "0.1.0",
  "has_pck": false,
  "has_dll": true,
  "affects_gameplay": false
}
```

- `id` — must match the JSON filename (e.g., `MyMod.json` for `"id": "MyMod"`)
- `has_pck` — set `true` if the mod includes a `.pck` file, add `"pck_name": "FileName"` (without extension)
- `has_dll` — set `true` if the mod includes a `.dll` assembly

## Enabling Mods

Mods require `mods_enabled: true` in the game settings file:

```
~/Library/Application Support/SlayTheSpire2/steam/<steam_id>/settings.save
```

Set `"mod_settings": { "mods_enabled": true }` in this JSON file. On first launch with mods detected, the game may show a consent dialog.

## Modded Profile

The game uses a **separate save profile** for modded runs:

```
~/Library/Application Support/SlayTheSpire2/steam/<steam_id>/modded/profile1/saves/
```

This is independent from the unmodded profile at `profile1/saves/`. Character unlocks, epoch progress, and run history are tracked separately. The original save is untouched.

## Character Unlock in Modded Mode

Since modded mode starts with a fresh profile, characters need to be re-unlocked. Use the [SlaytheSpire2.unlockAll](https://github.com/cccccyccccc/SlaytheSpire2.unlockAll) mod to bypass this.

## Installed Mods

| Mod | Purpose | Source |
|-----|---------|--------|
| STS2MCP | Game driver — exposes state + commands via HTTP | [Gennadiyev/STS2MCP](https://github.com/Gennadiyev/STS2MCP) |
| UnlockAllMod | Unlocks all characters, cards, epochs | [cccccyccccc/SlaytheSpire2.unlockAll](https://github.com/cccccyccccc/SlaytheSpire2.unlockAll) |

## Game Logs

```bash
tail -f ~/Library/Application\ Support/SlayTheSpire2/logs/godot.log
```

Look for `Found mod manifest file` and `Loaded N mods` to confirm mod loading.

## Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| Mod not detected | Wrong directory | Must be `Contents/MacOS/mods/`, not Resources or user data |
| Mod not detected | Wrong manifest filename | Must be `{id}.json`, not `mod_manifest.json` |
| Mod not detected | Missing manifest fields | Need `id`, `has_dll`, `has_pck` at minimum |
| Characters locked | Fresh modded profile | Install UnlockAllMod |
| `mods_enabled` resets | Game overwrites settings | Edit settings.save while game is closed |
