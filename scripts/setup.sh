#!/usr/bin/env bash
# Install the RTD harness into a task workspace. Idempotent, never overwrites.
# Usage: bash /tmp/RTD/scripts/setup.sh <workspace_root>   (default: .)
# Does NOT: install packages, update Codex, edit ~/.codex/*, add hooks, git push.
set -u

HARNESS="$(cd "$(dirname "$0")/.." && pwd)"
WS="$(cd "${1:-.}" 2>/dev/null && pwd)" || { echo "workspace not found: ${1:-.}"; exit 1; }
MARK="<!-- RTD-HARNESS v1 -->"
added=0; skipped=0

# copy_tree SRC DST: copy every file under SRC into DST, skipping files that exist.
copy_tree() {
  local src="$1" dst="$2" rel f
  while IFS= read -r f; do
    rel="${f#"$src"/}"
    if [ -e "$dst/$rel" ]; then
      skipped=$((skipped + 1))
    else
      mkdir -p "$(dirname "$dst/$rel")" && cp "$f" "$dst/$rel" && added=$((added + 1)) \
        && echo "  + ${dst/#$HOME/~}/$rel"
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
mkdir -p "$WS/.agents/scripts"
for s in recon.py presubmit.py; do
  if [ -e "$WS/.agents/scripts/$s" ]; then skipped=$((skipped + 1))
  else cp "$HARNESS/scripts/$s" "$WS/.agents/scripts/$s"; added=$((added + 1)); echo "  + .agents/scripts/$s"; fi
done

# 3. Korean doc templates -> docs/*.md (presubmit fails while {{...}} remain)
copy_tree "$HARNESS/docs/templates" "$WS/docs"

# 4. user-level fallback so /skills still finds level1..7 if cwd differs
copy_tree "$HARNESS/.agents/skills" "$HOME/.agents/skills"

# 5. git: init if needed; set identity locally only if missing
if ! git -C "$WS" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  git -C "$WS" init -q && echo "  + git init"
fi
if [ -z "$(git -C "$WS" config user.name)" ]; then
  git -C "$WS" config user.name "rtd-user" && echo "  + git user.name (repo-local)"
fi
if [ -z "$(git -C "$WS" config user.email)" ]; then
  git -C "$WS" config user.email "rtd-user@example.invalid" && echo "  + git user.email (repo-local)"
fi

echo "== done: $added added, $skipped already present (not overwritten)"
echo "== recon:"
python3 "$WS/.agents/scripts/recon.py" "$WS" || echo "  ! recon failed (python3 missing?)"
echo
echo "NEXT: restart Codex (exit, then run 'codex'), check /skills shows level1..level7, then type \$level1"
