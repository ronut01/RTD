# INSTALL (for the coding agent)

Install this harness into the task workspace. Do exactly these steps, nothing else.

Rules during install: do NOT install packages (npm/pip), do NOT update Codex, do NOT edit
`~/.codex/` or any global/platform config, do NOT add hooks, do NOT `git push`.

1. Find the workspace root: the directory that contains the task `README.md`
   (usually the current directory). Run `pwd && ls`. If README.md is not there, ask the human.
2. Clone outside the workspace:
   `git clone https://github.com/ronut01/RTD /tmp/RTD`
   (if `/tmp/RTD` already exists, skip cloning and reuse it.)
3. Install (idempotent; never overwrites existing files; appends to an existing AGENTS.md):
   `bash /tmp/RTD/scripts/setup.sh <workspace_root>`
   The Codex sandbox protects `.agents/` and `.git/` even inside the workspace, so this command
   needs approval: request it with escalated permissions in one call. If setup exits 1
   ("INCOMPLETE") or approval is not possible, do not work around the sandbox and do not change
   settings; ask the human to paste the one-liner below into a terminal tab, then re-check.
4. Confirm the result and show it to the human:
   `ls <workspace_root>/AGENTS.md <workspace_root>/.agents/skills <workspace_root>/docs ~/.agents/skills`
   Expected: `AGENTS.md`, `.agents/skills/level1` .. `level7`, `.agents/scripts/{recon,presubmit}.py`,
   `docs/{TASK,AGREEMENT,DESIGN,DECISIONS,VERIFICATION,WORKLOG,HANDOFF}.md`, and level1..level7 under
   `~/.agents/skills` (fallback). setup.sh already printed the `recon.py` output; summarize it
   in Korean in 3 lines (python/node versions, port, anything missing).
5. Tell the human (in Korean): "Codex를 종료했다가 다시 `codex`로 시작하고, `/skills`에서
   level1~level7이 보이는지 확인한 다음 `$level1`로 시작하세요." Then stop.

Human one-liner (run in the workspace root):
`git clone https://github.com/ronut01/RTD /tmp/RTD && bash /tmp/RTD/scripts/setup.sh .`
