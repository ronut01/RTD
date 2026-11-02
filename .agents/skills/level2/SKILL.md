---
name: level2
description: "Step 2 of 7 (stakeholder interview + agreement). Use after level1 produced docs/TASK.md with open questions, when the human is about to talk to the 업무 담당자 (stakeholder) in the messenger: proposes the next 2-3 questions, files the pasted answers into docs/AGREEMENT.md, and drafts the agreement for confirmation. Not for coding."
---
# level2 - stakeholder interview ladder

The human types in the messenger; you never contact the stakeholder. Budget 15-20 min total.
The stakeholder refuses "list all requirements" style asks; small concrete questions work.

Ask the first rung-6 question ("결과가 좋다/나쁘다를 무엇으로 판단하시나요?") in the very first
batch: it decides the objective, so asking it last wastes the earlier design thinking.
Never propose a new rule or limit the README/data does not hint at (e.g. a per-group cap):
a stakeholder may simply approve it and it becomes an invented requirement.

Ladder (go in order, skip rungs README already answers):
1. Episode - "최근에 이 일 때문에 곤란했던 구체적인 상황 하나를 말해 주실 수 있나요?"
2. Current workaround - how it is done today, what breaks.
3. Quantify - how often, how many rows/users/requests, how fast it must be.
4. Who - who uses the output, who acts on it; walk one day: "<역할>님은 이걸 언제 열어서 무엇을
   보고 무엇을 하나요?" (confirms or corrects the IS rows from level1).
5. Boundaries - exceptions, invalid/missing data, edge values, and what we do NOT need to do.
6. Quality and realism of the core - what makes the core output good or bad in practice:
   - "결과가 좋다/나쁘다를 무엇으로 판단하시나요?" (cost, time, count of resources, fairness...)
   - physical/business limits: capacity, maximum time or distance, working hours, budget.
   - resources with no stated limit: "<자원> 수는 적을수록 좋은 건가요, 상한이 있나요?"
   - the current process in numbers and its main complaint (this becomes the baseline).
   - trade-off: "<A>와 <B>가 부딪히면 무엇이 우선인가요?"
7. Priority - if only one thing works at the end, which one.

Each turn:
- Propose 2-3 candidate questions (Korean, one sentence each, no solution words such as
  "DB", "React", "API"), each with your guessed answer. Mark the one you recommend.
- Ask only 1-2 per message. Prefer questions answerable in a few words or by choice.
- When the human pastes the answer, record it in `docs/AGREEMENT.md` as row `A<n>` (question
  -> answer -> impact on criteria) and move resolved items out of TASK.md open questions.
- Before stopping, rung 5 must have been asked at least once in plain words
  ("판정/처리에서 빼야 하는 경우나 예외가 있나요?", "안 해도 되는 건?"), rung 6 at least
  twice (what "good" means + one limit), plus every data anomaly from level1. Do not spend
  more than 2 questions drilling one topic. Each IS row ends confirmed (cite A<n>) or `assumed:`.
- Stop asking when you can predict the next 3 answers, or after ~20 min.

Then draft the agreement (in AGREEMENT.md): 이해한 문제 / 원인 / 성공 기준 / 핵심 품질
지표와 현실 제약 / 만들 것 / 안 만들 것 / 제약. Give the human a short Korean message (<=6 lines) to paste to the
stakeholder for confirmation; record the reply. Unanswered items become `assumed:`.
Update HANDOFF line: `Current level: 2 / Next: $level3`. Commit `docs: record stakeholder agreement`.

## Next
Report in Korean, then STOP and wait:
- 3 lines: 무엇을 확인했나 / 왜 중요한가 / 아직 가정으로 남은 것.
- Next: `$level3` - 합의를 binary 성공 기준 + 시나리오 + 증거로 바꾸는 목표 계약.
- Time: show current clock, elapsed since Start, and minutes left to Freeze (from HANDOFF.md).
