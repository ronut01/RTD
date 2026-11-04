---
name: level4
description: "Step 4 of 7 (approach research + design + one-pass plan check). Use after level3 wrote the contract in docs/TASK.md and before writing feature code: identifies the core problem's class, researches and compares 2-3 recognised methods, fixes quality metrics, baselines and realism bounds in docs/DESIGN.md after a short practitioner/method/reference-code research, waits for the human to choose, then drafts the build plan and gets one independent plan review in a new session (OKAY / ITERATE max 3 / REJECT)."
---
# level4 - approach research, design, plan check

Goal: the human approves a core method that a practitioner would accept, and a plan to build
it, before any feature code. Budget ~20 min (research <=8, design ~7, independent review ~5).
Get it right once; rewriting the core later costs more than this step.

## Part A - research the core approach (write `docs/DESIGN.md` sections 1-4)
1. **Formulate** the core from TASK.md + AGREEMENT.md, in plain words then structured:
   decision (what we choose), objective (what we minimise/maximise, in priority order),
   hard constraints (must never break), soft constraints (prefer), data scale (rows, items).
   Real tasks often chain several sub-problems; split them and formulate each. Treat the risky
   engineering parts (consistency under concurrent use, time handling, imports...) as sub-problems too.
2. **Find what each sub-problem is an instance of**, so the method comes from known work, not
   invention: describe it in plain words, then search for the names practitioners and the literature
   use for it (`<plain description> algorithm`, `... best practice`, `... open source`). For each, name
   a naive baseline and 1-2 recognised better methods with a reason they fit our data and time box.
   Nothing recognised fits -> say so, design from first principles, and still measure against the baseline.
   **Research (<=8 min, <=4 web searches; without web search say so and use your knowledge):**
   (i) how practitioners run this kind of service (the limits operators enforce, what they measure,
   what users complain about); (ii) the recognised method for each sub-problem; (iii) 1-2 public
   reference implementations or patterns (permissive license) for the core and the riskiest engineering part. Reuse what fits: adapt it, add what our case needs,
   cite it in DESIGN.md §2 `출처: <URL> - 가져온 것 / 고친 점`; never paste a whole solution or search for this task's answer. Unstated practitioner constraints -> `assumed:`.
3. **Compare 2-3 candidates** in DESIGN.md: method / expected quality / complexity at our data
   scale / implementation time in this time box / explainability / main risk. Prefer the
   method that is clearly better than naive, fits the remaining time, and the human can explain.
   Show two product shapes: the minimum that passes the criteria, and what the in-house users
   would actually run day to day; name the IS rows each leaves unmet. Default to the second.
   During research, `pip install` the proven library the core needs (a solver, a model, a parser) into ./.venv once; log it in D1.
4. **Fix measurement before code:**
   - Metrics: primary objective + 2-3 secondary + violations counted per H-id of `조건 장부`.
   - Baselines: (a) the current process from the data/stakeholder - if it is described as a rule
     (e.g. "nearest ~5 per person"), implement that rule as baseline (a), do not mark it
     unmeasurable; (b) a naive method (the one a hurried engineer would write first). The chosen method must beat both.
   - Realism bounds: numbers that would look absurd to a practitioner (too many resources,
     near-empty or over-full units, extreme max times, unserved items, core runtime > ~30 s). Take them from
     AGREEMENT or mark `assumed:`. These become checks in the core quality criterion. The main
     complaint about today's process must be a metric the chosen method improves, not a warning.
   - Small-case check: a tiny input where the answer is known by hand or brute force.
5. Keep DESIGN.md short: sections 1-4 <= ~45 lines, whole file <= ~80 lines; tables over
   prose, no derivations the human will not read. Write DESIGN.md sections 1-4 and `### D1` in DECISIONS.md (chosen method, the rejected
   candidates and why, what we give up). Then **STOP and ask the human to choose** (Korean,
   <=6 lines): candidates in one line each, your recommendation and the deciding reason.

## Part B - after the human chooses: design map + plan + one check
6. Fill DESIGN.md section 5-7: data flow (input -> validation -> state -> output, who owns
   each state), roles if more than one user type (what each sees/does; heavy computation runs
   once and is saved; a fresh start loads the saved result, never an empty page), deterministic code vs LLM
   with reason and cost, modules with one-line jobs.
7. Draft `## Plan` in `docs/TASK.md`, max ~12 lines: vertical slices in dependency order.
   Slice 1 is a thin end-to-end path ending on the surface README names (screen, API or CLI). Each slice line:
   `S<k> [core|periphery] <what> - <files> - closes C<n>`. Core slices, one Plan line each, in this order:
   evaluator + naive baseline (metrics written independently of the core) -> chosen method seeded with the best baseline
   -> comparison on the real input. Unsure = `core`; so is any slice that can fail only under simultaneous use or a restart.
8. Self-check: every IS row has a criterion and a slice; every periphery slice traces to a
   criterion; no core step marked periphery. Commit, then ask the human to open a NEW Codex
   session with the review model (PROMPTS §0), paste this prompt verbatim, and STOP until the
   verdict is pasted back:
   ```
   너는 읽기 전용 계획 리뷰어다. 파일을 수정하지 마. 너는 이 서비스를 매일 쓸 회사 내부 운영 담당자이자 시니어 엔지니어다. README.md, docs/AGREEMENT.md, docs/TASK.md(사용자와 이상 상태, Contract, Plan), docs/DESIGN.md만 끝까지 읽어. 다음만 보고, 판단마다 근거 파일:줄을 붙여: ① 이상 상태(IS) 행마다 증명하는 기준과 슬라이스가 있나 ② 핵심 방법이 실무에서 쓰는 방식이고 기준선(현행·단순)을 이길 설계인가, README의 규칙이 모두 조건 장부 H/S에 있고 평가기가 H마다 위반을 세나, 실무자가 지키는 현실 제약을 빠뜨리지 않았나 ③ 운영자·구성원이 결과 화면을 보고 바로 쓸 수 있나 ④ 남은 시간 안에 끝낼 수 있나(과설계도 지적). 결과는 한국어로: VERDICT: OKAY / ITERATE / REJECT, ISSUES 최대 3개(각각 근거 파일:줄과 고칠 내용), NOTES 최대 3개. 5분 안에 끝내.
   ```
9. Verdict pasted: OKAY -> done; ITERATE -> apply the max-3 fixes once, but only those that keep
   every criterion passable with the given data (else note it), log them in WORKLOG (오류 발견
   if the plan was wrong), no second review; REJECT -> stop.
Update HANDOFF line: `Current level: 4 / Next: $level5`. Commit `docs: add design and build plan`.

## Next
Report in Korean, then STOP and wait:
- 3 lines: 고른 핵심 방법과 기준선 / 판정(OKAY/ITERATE/REJECT)과 바뀐 점 / 가장 위험한 슬라이스.
- OKAY or ITERATE resolved: next `$level5` - Slice 1부터 구현. 주변부는 이어서, 핵심 슬라이스마다 멈춤.
- REJECT: back to `$level2` (ask the stakeholder the blocking question) or `$level3` (fix contract).
- Time: show current clock, elapsed since Start, and minutes left to Freeze (from HANDOFF.md).
