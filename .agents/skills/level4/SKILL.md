---
name: level4
description: "Step 4 of 7 (approach research + design + one-pass plan check). Use after level3 wrote the contract in docs/TASK.md and before writing feature code: identifies the core problem's class, researches and compares 2-3 recognised methods, fixes quality metrics, baselines and realism bounds in docs/DESIGN.md, waits for the human to choose, then drafts the build plan and checks it once (OKAY / ITERATE max 3 / REJECT)."
---
# level4 - approach research, design, plan check

Goal: the human approves a core method that a practitioner would accept, and a plan to build
it, before any feature code. Budget ~15 min. Get it right once; rewriting the core later costs
more than this step.

## Part A - research the core approach (write `docs/DESIGN.md` sections 1-4)
1. **Formulate** the core from TASK.md + AGREEMENT.md, in plain words then structured:
   decision (what we choose), objective (what we minimise/maximise, in priority order),
   hard constraints (must never break), soft constraints (prefer), data scale (rows, items).
   Real tasks often chain several sub-problems (e.g. choose sites -> assign people -> order
   visits); split them and formulate each.
2. **Name the problem class** of each sub-problem with its standard name, so the method comes
   from known work, not invention. Common classes (not exhaustive):
   | class | typical methods (baseline -> better) |
   |---|---|
   | vehicle/visit routing, sequencing | nearest neighbour -> savings / sweep / insertion + 2-opt, or-opt; cluster-first route-second |
   | site/location selection, coverage | greedy add/drop -> p-median / set cover / k-medoids + swap |
   | assignment with capacities | greedy -> Hungarian / min-cost flow / greedy + swap |
   | scheduling, timetabling, shifts | first-fit / list scheduling -> constraint search with backtracking, local search |
   | packing, selection under budget | first-fit decreasing / ratio greedy -> knapsack DP, local search |
   | grouping, segmentation | fixed rules -> k-means / k-medoids / DBSCAN |
   | rule-based judgement, scoring | explicit rule table with priority order -> weighted score + sensitivity check |
   | forecasting | last value / seasonal naive -> moving average, simple regression |
   | matching, dedup | exact key after normalisation -> fuzzy match with threshold |
   Use your own knowledge first. If web search is available inside this Codex, one quick check
   of the standard approach is fine; never look for a solution to this specific task.
3. **Compare 2-3 candidates** in DESIGN.md: method / expected quality / complexity at our data
   scale / implementation time in this time box / explainability / main risk. Prefer the
   method that is clearly better than naive, fits the remaining time, and the human can explain.
   Only stdlib unless a package was approved. Exact solvers only if the size is tiny.
4. **Fix measurement before code:**
   - Metrics: primary objective + 2-3 secondary + hard-constraint violation count.
   - Baselines: (a) the current process from the data/stakeholder, if any; (b) a naive method
     (the one a hurried engineer would write first). The chosen method must beat both.
   - Realism bounds: numbers that would look absurd to a practitioner (too many resources,
     near-empty or over-full units, extreme max times, unserved items). Take them from
     AGREEMENT or mark `assumed:`. These become checks in the core quality criterion.
   - Small-case check: a tiny input where the answer is known by hand or brute force.
5. Keep DESIGN.md short: sections 1-4 <= ~45 lines, whole file <= ~80 lines; tables over
   prose, no derivations the human will not read. Write DESIGN.md sections 1-4 and `### D1` in DECISIONS.md (chosen method, the rejected
   candidates and why, what we give up). Then **STOP and ask the human to choose** (Korean,
   <=6 lines): candidates in one line each, your recommendation and the deciding reason.

## Part B - after the human chooses: design map + plan + one check
6. Fill DESIGN.md section 5-7: data flow (input -> validation -> state -> output, who owns
   each state), roles if more than one user type (what each sees/does; heavy computation runs
   once in an operator action and is stored, users read results), deterministic code vs LLM
   with reason and cost, modules with one-line jobs.
7. Draft `## Plan` in `docs/TASK.md`, max ~12 lines: vertical slices in dependency order.
   Slice 1 is a thin end-to-end path (input -> output on the real surface). Each slice line:
   `S<k> [core|periphery] <what> - <files> - closes C<n>`. Core slices, in this order:
   evaluator + naive baseline (metrics written independently of the solver) -> chosen method
   -> comparison on the real input. Anything unsure is `core` (core slices stop for the human).
8. Review once, read-only, against README + AGREEMENT + Contract + DESIGN:
   contradictions (cite both sides), ambiguous terms, missing constraints; does each scenario
   name a real command/input; periphery slices not traced to a criterion -> remove;
   a core step marked periphery -> fix; core method trivial or not beating baseline by
   design -> fix. Riskiest 1-2 parts get a note.
9. Verdict: OKAY (default) / ITERATE (max 3 fixes, apply, re-check once) / REJECT (missing
   file, impossible criterion, or stakeholder decision needed).
Update HANDOFF line: `Current level: 4 / Next: $level5`. Commit `docs: add design and build plan`.

## Next
Report in Korean, then STOP and wait:
- 3 lines: 고른 핵심 방법과 기준선 / 판정(OKAY/ITERATE/REJECT)과 바뀐 점 / 가장 위험한 슬라이스.
- OKAY or ITERATE resolved: next `$level5` - Slice 1부터 구현. 주변부는 이어서, 핵심 슬라이스마다 멈춤.
- REJECT: back to `$level2` (ask the stakeholder the blocking question) or `$level3` (fix contract).
- Time: show current clock, elapsed since Start, and minutes left to Freeze (from HANDOFF.md).
