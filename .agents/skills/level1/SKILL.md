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
3. Read the task `README.md` fully (it is short). Data files: `wc -l` first. Up to ~200 lines:
   read fully. Larger: profile with a short stdlib script (per column: distinct values, blanks,
   formats) instead of reading. Normalise key case/whitespace before checking uniqueness, and join key columns
   across files (orphans both ways), and compare each numeric column with the matching limit in
   other files (a value no option can satisfy is an anomaly). List anomalies you see (blank/odd values, case variants, mixed
   formats, duplicate-looking rows) - each becomes an open question.
4. Classify the task: (a) web service / API, (b) data + rules -> judgement/report, (c) other.
   Then name the **core**: the one output a domain expert would judge as good or bad (see
   AGENTS.md §3). Write it in TASK.md as `핵심 산출물: <what> - 좋고 나쁨을 가르는 것: <guess>`.
   If the data hints at an existing/current process (current plan, past records, costs), note
   it: it is the natural baseline for level4.
   Treat the task as a service the company's own staff will use every day. In TASK.md
   `## 사용자와 이상 상태`: one line per user role (when they open it, what they decide from
   it), then IS1..ISn (<=6): what each role does/sees and what must never look wrong to them
   (time, capacity, distance, fairness...). Mark each `(추정)` until level2 confirms it.
5. Fill `docs/TASK.md`:
   - Facts: only what README/data literally says, with the source line.
   - `## 조건 장부`: every rule in README/data, one line each with its source line: `H<n>` must
     never break, `S<n>` prefer. Hunt for timing rules and offsets, lists of allowed
     values, who or what is available when (per person/date/item),
     capacities and limits, exceptions for a subgroup. A missed rule makes the whole output wrong.
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
