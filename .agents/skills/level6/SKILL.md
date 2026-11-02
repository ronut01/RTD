---
name: level6
description: "Step 6 of 7 (verification + independent review). Use after level5 when all criteria are PASS or the Freeze time is reached: re-runs every criterion on the real surface, checks requirement-to-test 1:1 mapping, and runs one read-only independent review in a different context. Returns OKAY or ITERATE (max 3)."
---
# level6 - real-surface verification and one independent review

1. Fresh run, no reuse of old output: for each C<n>, run its scenario now on the real surface
   (Browser preview at 0.0.0.0:<port>, `curl -i`, or the real input file). Update evidence.
   Build success or green tests alone do not count. PASS only if the criterion's own command
   ran as written; if it does not exist or you used a different check, mark FAIL or NOT RUN and
   say why. Do not add new verification scripts here.
   Core quality: re-run the evaluator on the real input; paste `metric | baseline | ours` and
   the realism bounds into the core criterion's evidence. Read 2-3 concrete output rows as a
   practitioner would (one typical, one extreme) and say whether they make sense.
2. Mapping: table in VERIFICATION.md `requirement -> criterion -> test/scenario`. Flag any
   README/AGREEMENT requirement with no criterion, and any code with no requirement (scope creep).
3. Quick risk pass on the diff (`git diff --stat` then targeted reads): input validation at
   entry points, secrets, error paths, time zones, empty/huge input. Note, do not gold-plate.
4. Independent review, once: ask the human to open a NEW Codex session (or `/model` -> the
   cross-review model) and print the prompt below verbatim in a code block for them to copy,
   replacing `<FIRST_COMMIT>` with `git rev-list --max-parents=0 HEAD` (short hash). The reviewer
   is read-only and returns OKAY or ITERATE with max 3 issues, each citing a failing criterion.
   Non-criterion remarks are notes, not blockers. No second review round.
   ```
   너는 읽기 전용 리뷰어다. 파일을 수정하지 마. AGENTS.md, docs/TASK.md의 Contract, docs/VERIFICATION.md, `git diff <FIRST_COMMIT>..HEAD --stat`과 필요한 부분만 읽어. 주장은 직접 재현한 뒤에만 믿어. 결과는 한국어로: VERDICT: OKAY 또는 ITERATE / ISSUES 최대 3개(각각 실패하는 기준 C번호와 증거 파일:줄 또는 명령 출력) / NOTES 최대 3개. 기준이 요구하지 않는 코드와 실패할 수 없는 테스트도 지적해. docs/DESIGN.md의 핵심 산출물이 기준선보다 실제로 나은지, 현업 담당자가 보기에 말이 되는 결과인지(자원 수, 이용률, 극단값)도 실제 실행 결과로 판단해. docs/TASK.md의 '사용자와 이상 상태'를 읽고 역할별 주 업무를 실제 화면·명령으로 따라가 보며 각 IS가 성립하는지도 판단해.
   ```
5. Fix only cited issues with `$level5 C<n> ...` (list form: those criteria only, no chaining);
   record review result in WORKLOG.md.
Update HANDOFF line: `Current level: 6 / Next: $level7` (or `$level5` if FAIL).
Commit `test: verify all criteria on real surface`.

## Next
Report in Korean, then STOP and wait:
- 3 lines: PASS/FAIL 개수 / 리뷰 판정 / 남은 약점.
- Any FAIL and still before Freeze: back to `$level5 C<n>` for that criterion.
- Otherwise next `$level7` - 문서 마무리 + HANDOFF.md Review Q&A.
- Time: show current clock, elapsed since Start, and minutes left to Freeze (from HANDOFF.md).
