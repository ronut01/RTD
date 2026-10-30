---
name: level7
description: "Step 7 of 7 (wrap-up + engineering handoff). Use after level6, when work is frozen and before handing the workspace over: finalizes docs, runs presubmit until exit 0, and writes a Review Q&A section in docs/HANDOFF.md answering likely reviewer questions (weakness -> risk -> next check, with file:line)."
---
# level7 - wrap-up and handoff

1. Read the real state: `git log --oneline`, `git diff --stat <first commit>..HEAD`,
   DECISIONS.md, VERIFICATION.md. Do not invent anything not in code or docs.
2. Finalize docs (short, true): VERIFICATION known weaknesses, DECISIONS "포기한 것",
   WORKLOG accepted/modified/rejected, HANDOFF full state (`Current level: 7 / Next: handoff`).
3. Fill `## Review Q&A` in `docs/HANDOFF.md` (Korean): 6-8 questions a code reviewer taking
   over this work would ask, covering at least:
   왜 이렇게 설계했나 / 장애가 나면 어떻게 대응하나 / 버린 대안과 이유 / 알려진 한계.
   Answer each in 2-3 sentences, in this order:
   ① 구체적 약점 지점 (`file:line`) ② 왜 위험한가 (파급) ③ 다음에 무엇을 확인·개선할지.
   If a likely question rests on a wrong premise about the code, state the actual behavior first.
   Anything not verified is written as not verified.
4. Run `python3 .agents/scripts/presubmit.py .` -> fix until exit 0 (placeholders, empty docs,
   secrets, uncommitted files). Final commit `docs: finalize handoff and review notes`.
Never push.

## Next
Report in Korean, then STOP:
- 3 lines: presubmit 결과와 커밋 수 / 가장 약한 지점 / 리뷰어에게 강조할 결정 (D번호).
- Next: 핸드오프 준비 완료. 요구된 산출물 경로를 확인한 뒤 작업 공간을 제출(전달)하세요.
- 리뷰 답변 순서: 결론 한 줄 → ① 약점 지점(파일/함수) → ② 왜 위험한가 → ③ 다음 확인·개선.
