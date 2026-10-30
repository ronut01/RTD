#!/usr/bin/env bash
# OPTIONAL: copy reviewer/explorer subagents into <ws>/.codex/agents (project level only).
# Usage: bash install.sh <workspace> <review_model> [explore_model]
# Model names: copy exactly from `/model` on the day. This script is the only place they are set.
set -eu
WS="${1:?workspace}"; REVIEW="${2:?review model from /model}"; EXPLORE="${3:-$REVIEW}"
case "$(printf '%s %s' "$REVIEW" "$EXPLORE" | tr 'A-Z' 'a-z')" in
  *"$(printf '\x61\x73\x74\x72\x61')"*) echo "refusing: that model is not allowed"; exit 1;;
esac
SRC="$(cd "$(dirname "$0")" && pwd)"; mkdir -p "$WS/.codex/agents"
for a in reviewer explorer; do
  dst="$WS/.codex/agents/$a.toml"
  [ -e "$dst" ] && { echo "= $dst exists, skipped"; continue; }
  sed -e "s/__REVIEW_MODEL__/$REVIEW/" -e "s/__EXPLORE_MODEL__/$EXPLORE/" "$SRC/$a.toml" > "$dst"
  echo "+ $dst"
done
echo "Restart Codex to load. Global ~/.codex/ was not touched."
