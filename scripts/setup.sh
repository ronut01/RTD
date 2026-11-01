#!/usr/bin/env bash
# Install the RTD harness into a task workspace. Idempotent, never overwrites.
# Usage: bash /tmp/RTD/scripts/setup.sh <workspace_root>   (default: .)
# Does NOT: install packages, update Codex, edit ~/.codex/*, add hooks, git push.
set -u

HARNESS="$(cd "$(dirname "$0")/.." && pwd)"
WS="$(cd "${1:-.}" 2>/dev/null && pwd)" || { echo "workspace not found: ${1:-.}"; exit 1; }
MARK="<!-- RTD-HARNESS v1 -->"
added=0; skipped=0; failed=0

# copy_tree SRC DST: copy every file under SRC into DST, skipping files that exist.
copy_tree() {
  local src="$1" dst="$2" rel f
  while IFS= read -r f; do
    rel="${f#"$src"/}"
    if [ -e "$dst/$rel" ]; then
      skipped=$((skipped + 1))
    else
      if mkdir -p "$(dirname "$dst/$rel")" 2>/dev/null && cp "$f" "$dst/$rel" 2>/dev/null; then
        added=$((added + 1)); echo "  + ${dst/#$HOME/~}/$rel"
      else
        failed=$((failed + 1)); echo "  ! FAILED ${dst/#$HOME/~}/$rel"
      fi
    fi
  done < <(find "$src" -type f ! -name '.DS_Store' | sort)
}

echo "== RTD setup -> $WS"
[ -f "$WS/README.md" ] || echo "  ! no README.md in $WS - is this the task workspace root?"

# 1. AGENTS.md: create, or append once (marker guards re-runs)
if [ ! -f "$WS/AGENTS.md" ]; then
  cp "$HARNESS/AGENTS.md" "$WS/AGENTS.md"; added=$((added + 1)); echo "  + AGENTS.md (new)"
elif grep -qF "$MARK" "$WS/AGENTS.md"; then
  skipped=$((skipped + 1)); echo "  = AGENTS.md already has RTD section"
else
  printf '\n\n' >> "$WS/AGENTS.md"; cat "$HARNESS/AGENTS.md" >> "$WS/AGENTS.md"
  added=$((added + 1)); echo "  + AGENTS.md (appended RTD section, original kept above)"
fi

# 2. skills (workspace) + read-only helper scripts
copy_tree "$HARNESS/.agents/skills" "$WS/.agents/skills"
mkdir -p "$WS/.agents/scripts" 2>/dev/null
for s in recon.py presubmit.py; do
  if [ -e "$WS/.agents/scripts/$s" ]; then skipped=$((skipped + 1))
  elif cp "$HARNESS/scripts/$s" "$WS/.agents/scripts/$s" 2>/dev/null; then added=$((added + 1)); echo "  + .agents/scripts/$s"
  else failed=$((failed + 1)); echo "  ! FAILED .agents/scripts/$s"; fi
done

# 3. Korean doc templates -> docs/*.md (presubmit fails while {{...}} remain)
copy_tree "$HARNESS/docs/templates" "$WS/docs"

# 4. user-level fallback so /skills still finds level1..7 if cwd differs (optional: failure is a warning)
#    These level1..7 dirs are harness-owned, so refresh them (a stale copy would shadow updates).
ws_failed=$failed
for d in "$HARNESS"/.agents/skills/level*; do
  rm -rf "$HOME/.agents/skills/$(basename "$d")" 2>/dev/null
done
copy_tree "$HARNESS/.agents/skills" "$HOME/.agents/skills"
home_failed=$((failed - ws_failed)); failed=$ws_failed

# 5. git: init if needed; set identity locally only if missing
if ! git -C "$WS" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  git -C "$WS" init -q && echo "  + git init" || { failed=$((failed + 1)); echo "  ! FAILED git init"; }
fi
if [ -z "$(git -C "$WS" config user.name)" ]; then
  git -C "$WS" config user.name "rtd-user" 2>/dev/null && echo "  + git user.name (repo-local)" \
    || { failed=$((failed + 1)); echo "  ! FAILED git config user.name"; }
fi
if [ -z "$(git -C "$WS" config user.email)" ]; then
  git -C "$WS" config user.email "rtd-user@example.invalid" 2>/dev/null && echo "  + git user.email (repo-local)" \
    || { failed=$((failed + 1)); echo "  ! FAILED git config user.email"; }
fi

echo "== done: $added added, $skipped already present (not overwritten), $failed failed"
[ "$home_failed" -gt 0 ] && echo "  ! ~/.agents/skills fallback not written ($home_failed files) - fine if /skills shows level1..7"
echo "== recon:"
python3 "$WS/.agents/scripts/recon.py" "$WS" || echo "  ! recon failed (python3 missing?)"
echo
if [ "$failed" -gt 0 ]; then
  echo "INCOMPLETE: writes were blocked (Codex sandbox protects .agents/ and .git/)."
  echo "Run this same command yourself in a terminal tab, or re-run it with approval/escalation."
  exit 1
fi
echo "NEXT: restart Codex (exit, then run 'codex'), check /skills shows level1..level7, then type \$level1"
