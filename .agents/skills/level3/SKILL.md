---
name: level3
description: "Step 3 of 7 (goal contract). Use after level2 when docs/AGREEMENT.md exists and before any planning or feature code: turns the agreement into an outcome, deliverables, binary success criteria each with scenario and evidence, assumed: constraints, out-of-scope list and a stop condition, written into docs/TASK.md."
---
# level3 - goal contract

Write a `## Contract` section in `docs/TASK.md`:

- Outcome: one sentence, user-visible result (not an activity like "implement X").
- Deliverables: literal paths (code entry point, output files, docs README requires).
- Criteria table, numbered C1..Cn, ordered by priority from AGREEMENT. LIGHT: 3-5 rows.
  Each criterion traces to a README/AGREEMENT line; your own defaults (e.g. error handling
  nobody asked for) stay as `assumed:` notes, not criteria. Keep each cell to one short line:
  `| C1 | 통과 조건 (binary) | 실행할 명령·조작 | 남길 증거 |`
  - Include happy path, the riskiest edge (bad/missing input, boundary value), and for
    data tasks a hand-computed expected value from a real input row.
  - Include at least one **core quality criterion**: on the real input, hard constraints have 0
    violations AND the primary metric beats the baseline (current process or naive method)
    AND realism bounds hold, e.g. `제약 위반 0건, <지표> <= 기준선, <자원> 이용률 >= X%`.
    Numbers come from the stakeholder; if missing, set them as `assumed:` and say so. The exact
    baseline value may be filled in level4, but the comparison must be fixed now.
  - Scenario = exact command or UI steps with concrete inputs. "잘 동작하는지 확인" is invalid.
  - Evidence = `curl -i` status line, test name, output path, or what the preview shows; it is
    pasted into the VERIFICATION.md row (no separate evidence files or extra scripts).
  - If a criterion cannot fail, rewrite it.
- Constraints: stakeholder words verbatim; your own defaults as `assumed: <x> - <reason>`.
- Out of scope: explicit list (each with why).
- Stop condition: "All C1..Cn PASS with evidence in VERIFICATION.md, or the Freeze time in HANDOFF.md is reached."
- Size check: if criteria imply new modules, auth, external integration, schema or concurrency,
  label the task HEAVY and say so; otherwise LIGHT. LIGHT tasks get the smallest structure.

Copy C1..Cn as rows into `docs/VERIFICATION.md` with status `TODO`.
Do not pick the core method here; level4 researches and compares methods first.
Update HANDOFF line: `Current level: 3 / Next: $level4`. Commit `docs: add goal contract`.

## Next
Report in Korean, then STOP and wait for approval of the contract:
- 3 lines: 기준 개수와 핵심 / 왜 이 기준인가 / 가장 불확실한 가정.
- Next: `$level4` - 핵심 문제 유형 파악, 알고리즘 후보 조사·비교, 설계(DESIGN.md), 계획 1패스 점검.
- Time: show current clock, elapsed since Start, and minutes left to Freeze (from HANDOFF.md).
