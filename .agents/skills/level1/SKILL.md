---
name: level1
description: "Step 1 of 7 (recon + task draft). Use at the very start of a new task, right after the harness is installed, before any interview or code: runs read-only environment recon, reads the task README, and drafts docs/TASK.md (facts / assumptions / open questions / not doing). No prerequisite."
---
# level1 - recon and task draft

Goal: in <=15 min the human knows the environment and what the task really asks. No code.

1. Record time: run `date "+%H:%M"`; at the top of `docs/HANDOFF.md` write
   `Current level: 1 / Next: $level2` and `Start: HH:MM / Freeze: HH:MM` (freeze = the
   feature-freeze time the human gives; ask once if missing).
2. Run `python3 .agents/scripts/recon.py .` once. Note python/node/npm/pip versions,
   port availability, and the timestamp-parsing line (Python 3.9 rejects `Z` in fromisoformat).
3. Read the task `README.md` fully (it is short). For data files: `ls -la`, `wc -l`, `head -n 5`
   only; never cat whole files.
4. Classify the task: (a) web service / API, (b) data + rules -> judgement/report, (c) other.
5. Fill `docs/TASK.md`:
   - Facts: only what README/data literally says, with the source line.
   - Assumptions: `assumed: <x> - <why>`.
   - Open questions: ranked by impact (scope > correctness > edge cases > UX), max 7.
     These feed the stakeholder interview in level2.
   - Not doing: things that look tempting but are not asked.
   - Required deliverables: exact file paths/names README demands.
6. Commit: `git add -A && git commit -m "docs: add task draft and harness"`.

Do not design or code yet. Do not message the stakeholder yet.

## Next
Report in Korean, then STOP and wait:
- 3 lines: 무엇을 했나 / 왜 / 어디서 깨질 수 있나 (e.g. a README line you are unsure about).
- Next: `$level2` - 업무 담당자 인터뷰 (질문 후보를 제가 제안, 메신저 입력은 직접).
- Time: show current clock, elapsed since Start, and minutes left to Freeze (from HANDOFF.md).
