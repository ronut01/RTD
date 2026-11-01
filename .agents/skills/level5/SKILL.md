---
name: level5
description: "Step 5 of 7 (build loop, one criterion per run). Use after level4 returned OKAY and the human chose the core method in docs/DESIGN.md, to implement exactly one pending criterion from docs/VERIFICATION.md via READ -> CHANGE -> RUN -> RECORD -> COMMIT; core slices are measured against the baseline. Repeat $level5 per criterion; switch to level6 when all pass or the Freeze time is reached."
---
# level5 - one criterion: READ -> CHANGE -> RUN -> RECORD -> COMMIT

Check time first: `date "+%H:%M"` vs `Freeze:` in HANDOFF.md. If Freeze is reached, do not
start new work: set HANDOFF `Next: $level6`, report, and send the human to `$level6` (freeze rule).

Follow the ## Plan slice order in docs/TASK.md. The first $level5 run builds Slice 1 (thin end-to-end path, input to output on the real surface) and commits it before any other criterion.

Pick the highest-priority `TODO`/`FAIL` row C<n> in `docs/VERIFICATION.md`.
1. READ: only files the slice touches; grep/head for the rest.
2. CHANGE: periphery -> smallest change that can make C<n> pass, no extra features, no
   speculative abstractions. Core -> implement the method chosen in DESIGN.md as designed
   (not a simpler stand-in); if you must deviate, stop and say why first.
   Servers bind `0.0.0.0` with the port in one constant/env var.
   Rules/thresholds/calculations in plain deterministic code with named constants.
   Core slice order: evaluator (metrics + constraint check, independent of the solver) ->
   naive baseline -> chosen method -> comparison table on the real input.
3. RUN: execute C<n>'s scenario exactly (curl -i / Browser preview / real input file).
   Add or update a small test only when it protects C<n>; its expected value must be
   hand-derived, not computed by the same code. For a bug: reproduce first, then fix.
   Core: print `metric | baseline | ours` from code, then the realism bounds from DESIGN.md.
   If ours does not beat the baseline or a bound is absurd, it is FAIL, not "done".
4. RECORD: in VERIFICATION.md set PASS/FAIL, evidence (command + key output or path), and one
   known weakness. In WORKLOG.md one line: what you proposed, what the human accepted /
   changed / rejected and why. New design choice -> `### D<n>` in DECISIONS.md.
   After a core slice: Korean explain-back (<=6 lines: input -> steps -> output, why this
   method over the runner-up, weakest point `file:function`); fix DESIGN.md if the code moved.
5. COMMIT: `git add -A && git commit -m "feat: <what> (C<n>)"`. Never push.

3 failed approaches on C<n> -> stop, revert only your edits, log in WORKLOG, ask one question.
At the human's handoff checkpoints, refresh HANDOFF.md fully and suggest a fresh session.
Update HANDOFF line: `Current level: 5 / Next: $level5 (C<next>)` or `$level6`.

## Next
Report in Korean, then STOP and wait:
- 3 lines: C<n> 결과(PASS/FAIL)와 증거 / 왜 이렇게 구현했나 / 어디서 깨질 수 있나.
  (core slice: add the metric table and the explain-back below the 3 lines)
- Criteria left and before Freeze: next `$level5` - 다음 기준 C<next>.
- All PASS, or Freeze reached (regardless of remaining criteria): next `$level6` - 실제 화면 검증 + 독립 리뷰.
- Time: show current clock, elapsed since Start, and minutes left to Freeze (from HANDOFF.md).
