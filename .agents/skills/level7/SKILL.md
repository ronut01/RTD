---
name: level7
description: "Step 7 of 7 (wrap-up + engineering handoff). Use after level6, when work is frozen and before handing the workspace over: aligns DESIGN.md with the code, finalizes docs, runs presubmit until exit 0, and writes a Review Q&A section in docs/HANDOFF.md (AI collaboration, code vs LLM boundary, data flow, failure handling, scope, trust in results, method choice; weakness -> risk -> next check, with file:line)."
---
# level7 - wrap-up and handoff

1. Read the real state: `git log --oneline`, `git diff --stat <first commit>..HEAD`,
   DESIGN.md, DECISIONS.md, VERIFICATION.md, WORKLOG.md. Do not invent anything not in code or docs.
2. Finalize docs (short, true): DESIGN.md matches the code (data flow, modules, LLM vs code),
   VERIFICATION known weaknesses, DECISIONS "포기한 것", WORKLOG accepted/modified/rejected,
   HANDOFF full state (`Current level: 7 / Next: handoff`).
3. Fill `## Review Q&A` in `docs/HANDOFF.md` (Korean), one question per area below, made
   specific to this code (keep the template's areas, replace the generic wording):
   Q1 AI 협업: AI가 제안한 것 중 받아들인 것 / 고친 것 / 거절한 것과 이유 (WORKLOG 근거)
   Q2 결정론 코드와 LLM(또는 사람 판단)의 경계를 왜 거기에 두었나, 비용·위험은
   Q3 데이터 흐름: 사용자 입력 -> 검증 -> 상태 변화 -> 저장·표시, 각 단계의 책임
   Q4 장애·오류가 나면 어떻게 대응하나, 가장 취약한 곳은
   Q5 구현한 것과 일부러 구현하지 않은 것, 그 이유
   Q6 결과를 어떻게 믿을 수 있나: 데이터 판단(정제·가정)과 검증 방법(기준선 비교, 현실성 점검)
   Q7 핵심 방법을 고른 이유와 버린 대안 (DESIGN 비교표, D1)
   Answer each in 2-3 sentences, in this order:
   ① 구체적 약점 지점 (`file:line`) ② 왜 위험한가 (파급) ③ 다음에 무엇을 확인·개선할지.
   If a likely question rests on a wrong premise about the code, state the actual behavior first.
   Anything not verified is written as not verified.
   Then list in chat the 3 facts most worth memorising: core method name, key metric vs
   baseline (numbers), weakest `file:function`.
4. Run `python3 .agents/scripts/presubmit.py .` -> fix until exit 0 (placeholders, empty docs,
   secrets, uncommitted files). Final commit `docs: finalize handoff and review notes`.
Never push.

## Next
Report in Korean, then STOP:
- 3 lines: presubmit 결과와 커밋 수 / 가장 약한 지점 / 리뷰어에게 강조할 결정 (D번호).
- Next: 핸드오프 준비 완료. 요구된 산출물 경로를 확인한 뒤 작업 공간을 제출(전달)하세요.
- 리뷰 답변 순서: 결론 한 줄 → ① 약점 지점(파일/함수) → ② 왜 위험한가 → ③ 다음 확인·개선.
