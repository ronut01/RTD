---
name: level5
description: "Step 5 of 7 (build loop by Plan slice). Use after level4 returned OKAY and the human chose the core method in docs/DESIGN.md: builds the ## Plan slices of docs/TASK.md via READ -> CHANGE -> RUN -> CLEAN -> RECORD -> COMMIT, the session leading parallel worker subagents (TEAM.md). Periphery slices chain; every core slice, FAIL or criterion-changing assumption stops for the human. Repeat $level5 until all criteria pass; switch to level6 when all pass or the Freeze time is reached."
---
# level5 - build by Plan slice: READ -> CHANGE -> RUN -> CLEAN -> RECORD -> COMMIT

Unit = one `## Plan` slice of docs/TASK.md; Slice 1 first. You lead per TEAM.md: workers build, you verify.
If the first pending slice is `core` (unmarked = core), build only that slice, then stop.
Otherwise chain `periphery` slices: after COMMIT print `C<n> PASS|진행(k/n) | <evidence> | <short hash>`
and take the next one. A red run you fix inside the slice does not stop the chain. STOP at:
the next `core` slice, a FAIL the retry rule ends, any core-quality FAIL, a new `assumed:` or
`### D<n>` that changes a criterion or the core (other assumptions go in the receipt), a step
only the human can do, after building it and running every check you can (a decision, the stakeholder; a commit prompt
does not end the chain), Freeze, or all PASS.
`$level5 C2 C3` = exactly those slices, then stop.
Before each slice: `date "+%H:%M"` vs `Freeze:` in HANDOFF.md; at or past Freeze start nothing
and set `Next: $level6`. Start every run by printing the remaining slices as a short list
(`S<k> C<n> <path>: <action> - verify by <scenario>`) and keep it current with `update_plan` when that tool exists.

1. READ: only files the slice touches; grep/head for the rest.
2. CHANGE: periphery -> smallest change for C<n>, no extra features. Core -> the DESIGN.md method
   (no simpler stand-in) seeded with the best baseline so it never ends worse; to deviate, stop first.
3. RUN: execute C<n>'s scenario exactly (curl -i / Browser preview / real input file). Rerun
   every earlier PASS criterion whose Plan slice lists a file in `git diff --name-only`.
   Web: start your own server on a port other than the human's (e.g. theirs + 1) for `curl -i`;
   stop it in CLEAN. Every web slice's receipt ends with `미리보기 확인: <URL> <what to see>`.
   Bug: reproduce first, then fix. Add a test only when it protects C<n>; its expected value is
   hand-derived, not computed by the code under test.
   Core: print `metric | baseline | ours` (first core slice, evaluator + naive baseline: the
   DESIGN.md small-case check + baseline metrics; its row reads `진행(1/3)`, never PASS/FAIL).
   Ours not beating the baseline, or an absurd realism bound, is FAIL. Every objective the stakeholder
   named gets a metric row; one that only ties the baseline is reported as the top weakness at the stop.
4. CLEAN: stop processes you started (never the human's server tab), delete scratch files;
   `git status --short` lists only files this slice commits.
5. RECORD: VERIFICATION row (PASS/FAIL, evidence, one weakness). WORKLOG: one row per stop
   (a chained batch is one row); every FAIL->fix cycle or human rejection is a 오류 발견 row:
   what was wrong | how it was caught | fix commit. New design choice -> `### D<n>` citing
   A<n>/C<n>. Refresh HANDOFF `## 지금 상태`. After a core slice: Korean explain-back (<=6
   lines: input -> steps -> output, why this method, weakest `file:function`); keep DESIGN.md true.
6. COMMIT: mark the slice `[x]` in `## Plan` (keep its core/periphery tag), then
   `git add -A && git commit -m "feat: <what> (C<n>)"`.
   One commit per slice. Never push.

Same failure output twice, or 3 different approaches on one slice -> stop, revert only your
edits, log it in WORKLOG, ask one precise question.
Update HANDOFF line: `Current level: 5 / Next: $level5 (<next slice>)` or `$level6`.

## Next
Report in Korean, then STOP and wait:
- Receipts (one line per chained slice), then 3 lines: 결과와 증거 / 왜 이렇게 구현했나 / 어디서
  깨질 수 있나. Core slice: add the metric table and the explain-back.
- Next is a core slice: `$level5` - 핵심 슬라이스 <이름>: 무엇을 만들지 한 줄.
- FAIL, criterion-changing assumption or human step: exactly what the human must do or decide.
- All PASS, or Freeze reached: `$level6` - 실제 화면 검증 + 독립 리뷰.
- Time: current clock, elapsed since Start, minutes left to Freeze (from HANDOFF.md).
