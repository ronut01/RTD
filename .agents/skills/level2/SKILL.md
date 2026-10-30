---
name: level2
description: "Step 2 of 7 (stakeholder interview + agreement). Use after level1 produced docs/TASK.md with open questions, when the human is about to talk to the 업무 담당자 (stakeholder) in the messenger: proposes the next 2-3 questions, files the pasted answers into docs/AGREEMENT.md, and drafts the agreement for confirmation. Not for coding."
---
# level2 - stakeholder interview ladder

The human types in the messenger; you never contact the stakeholder. Budget 15-20 min total.
The stakeholder refuses "list all requirements" style asks; small concrete questions work.

Ladder (go in order, skip rungs README already answers):
1. Episode - "최근에 이 일 때문에 곤란했던 구체적인 상황 하나를 말해 주실 수 있나요?"
2. Current workaround - how it is done today, what breaks.
3. Quantify - how often, how many rows/users/requests, how fast it must be.
4. Who - who uses the output, who acts on it.
5. Boundaries - exceptions, invalid/missing data, edge values, and what we do NOT need to do.
6. Priority - if only one thing works at the end, which one.

Each turn:
- Propose 2-3 candidate questions (Korean, one sentence each, no solution words such as
  "DB", "React", "API"), each with your guessed answer. Mark the one you recommend.
- Ask only 1-2 per message. Prefer questions answerable in a few words or by choice.
- When the human pastes the answer, record it in `docs/AGREEMENT.md` (question -> answer ->
  impact on criteria) and move resolved items out of TASK.md open questions.
- Before stopping, rung 5 must have been asked at least once in plain words
  ("판정/처리에서 빼야 하는 경우나 예외가 있나요?", "안 해도 되는 건?"), plus every data
  anomaly from level1. Do not spend more than 2 questions drilling one topic.
- Stop asking when you can predict the next 3 answers, or after ~20 min.

Then draft the agreement (in AGREEMENT.md): 이해한 문제 / 원인 / 성공 기준 / 만들 것 /
안 만들 것 / 제약. Give the human a short Korean message (<=6 lines) to paste to the
stakeholder for confirmation; record the reply. Unanswered items become `assumed:`.
Update HANDOFF line: `Current level: 2 / Next: $level3`. Commit `docs: record stakeholder agreement`.

## Next
Report in Korean, then STOP and wait:
- 3 lines: 무엇을 확인했나 / 왜 중요한가 / 아직 가정으로 남은 것.
- Next: `$level3` - 합의를 binary 성공 기준 + 시나리오 + 증거로 바꾸는 목표 계약.
- Time: show current clock, elapsed since Start, and minutes left to Freeze (from HANDOFF.md).
