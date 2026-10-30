---
name: level4
description: "Step 4 of 7 (one-pass plan check). Use after level3 wrote the contract in docs/TASK.md and before writing feature code: drafts a short build plan and reviews it once for contradictions, ambiguity, gaps and non-executable QA, returning OKAY / ITERATE (max 3 issues) / REJECT."
---
# level4 - plan check (single pass)

1. Draft `## Plan` in `docs/TASK.md`, max ~12 lines: vertical slices in dependency order.
   Slice 1 is a thin end-to-end path (input -> output on the real surface). Each slice lists
   files touched and which C<n> it closes. Every C<n> maps to a slice; no slice without a C<n>.
2. Review it once, read-only, against README + AGREEMENT + Contract:
   - Contradictions (cite both sides), ambiguous terms, missing constraints.
   - Executability: does each scenario name a real command/input that exists now?
   - Over-engineering: any task not traced to a criterion, or any criterion not traced to
     README/AGREEMENT -> remove or demote to `assumed:`.
   - Risk: the 1-2 riskiest parts (parsing, time zones, boundaries, state) get a detailed note.
3. Verdict:
   - OKAY: plan is executable as is (default).
   - ITERATE: list at most 3 concrete fixes, apply them, re-check once. No third round.
   - REJECT: a needed file is missing, a criterion is impossible, or a stakeholder decision is needed.
4. Record verdict and fixes as `### D<n>` in DECISIONS.md if it changed the approach.
Update HANDOFF line: `Current level: 4 / Next: $level5`. Commit `docs: add build plan`.

## Next
Report in Korean, then STOP and wait:
- 3 lines: 판정(OKAY/ITERATE/REJECT)과 이유 / 바뀐 점 / 가장 위험한 슬라이스.
- OKAY or ITERATE resolved: next `$level5` - 기준 C1부터 하나씩 구현·검증·커밋.
- REJECT: back to `$level2` (ask the stakeholder the blocking question) or `$level3` (fix contract).
- Time: show current clock, elapsed since Start, and minutes left to Freeze (from HANDOFF.md).
