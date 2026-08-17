#!/bin/sh
set -eu

ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
SOURCE="$ROOT/.agents/skills/test-guard/adapters/cursor/test-guard.mdc"
TARGET_DIR="$ROOT/.cursor/rules"
TARGET="$TARGET_DIR/test-guard.mdc"

if [ ! -f "$SOURCE" ]; then
  echo "test-guard Cursor adapter not found at: $SOURCE" >&2
  echo "Install the skill for Cursor first:" >&2
  echo "  npx skills add furkananter/skills --skill test-guard -a cursor" >&2
  exit 1
fi

mkdir -p "$TARGET_DIR"
cp "$SOURCE" "$TARGET"

echo "Installed Cursor Always rule: $TARGET"
