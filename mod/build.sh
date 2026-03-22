#!/bin/bash
# Build and deploy the STS2MCP mod (jibao fork)
set -e

DOTNET="/opt/homebrew/opt/dotnet@9/bin/dotnet"
MOD_DIR="$HOME/Library/Application Support/Steam/steamapps/common/Slay the Spire 2/SlayTheSpire2.app/Contents/MacOS/mods/STS2_MCP"

cd "$(dirname "$0")"

echo "Building STS2_MCP..."
$DOTNET build -c Release

echo "Deploying to game..."
cp bin/Release/net9.0/STS2_MCP.dll "$MOD_DIR/STS2_MCP.dll"

echo "Done! Restart the game to load the new mod."
