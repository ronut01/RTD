# Team mode for level5 and the level6 fix loop

You are the **lead**: the session the human talks to. Workers and verifiers are native
subagents (`spawn_agent` + `wait_agent`, or this Codex's equivalent). No subagent tool -> do the
same steps yourself, one slice at a time.
Only the lead talks to the human, edits docs/ (Plan, VERIFICATION, DECISIONS, WORKLOG, HANDOFF),
commits, and decides stops. Workers only change code in the files they own.

## 1. Batch
- From `## Plan`, take the pending slices whose file lists do not overlap. A file two slices need
  (e.g. the web entry point) gets one owner; the other slice waits for the next batch.
- Periphery: all independent slices at once, at most 3 workers. Core: one worker for the core
  slice; independent periphery workers may run beside it. Core slices still stop for the human.

## 2. Brief (spawn with no forked history; <= 15 lines, self-contained)
```
TASK: S<k> <what> - closes C<n>: <pass condition verbatim from TASK.md>
OWN FILES: <only these may change>   READ: TASK.md 조건 장부, DESIGN.md §<x>, AGREEMENT A<n>
METHOD: <core: the DESIGN.md method, seeded from the best baseline | periphery: smallest change>;
        build on the DESIGN.md §2 출처 it names (adapt, add what our case needs) instead of reinventing
RUN: <exact scenario command>; own server on port <8100+k>, stop it before you finish
DO NOT: commit, edit docs/ or other files, install packages, start the human's server, ask the human
DELIVER: files changed, scenario command + last output lines, `metric | baseline | ours` for core,
         anything NOT RUN, one weakest point (file:function)
STOP WHEN: the scenario passes, or the same failure twice (report it, change nothing more)
```

## 3. While workers run
- Call `wait_agent` with a short timeout (60-120 s) in a loop; between waits answer the human at
  once (status in one sentence, steering, `담당자 답:`). Do not start heavy work of your own.
- New information that affects a running worker (stakeholder answer, changed rule) -> stop or
  re-brief that worker now; do not let it finish on stale facts.

## 4. Check, then record
- A worker's report is a claim, not evidence. Re-run each C<n> scenario yourself, or spawn one
  read-only verifier ("run these scenarios exactly, report output; edit nothing") for long checks.
  Web: open each role's main page on a fresh start too.
- FAIL -> re-brief the same worker once with the failing output; a second FAIL ends the slice by
  the retry rule (stop, ask the human one precise question).
- `git status --short` shows only owned files changed -> RECORD and COMMIT one commit per slice.
- Receipts name the worker: `C<n> PASS | <evidence> | <hash> | worker S<k>`.

## 5. level6 fix loop (no `$level5` needed from the human)
After the fresh run and the review verdict, the lead fixes every FAIL and cited issue the same way:
one worker per criterion (disjoint files), check, commit, then re-run step 1 of level6 for the
touched criteria. At most 2 rounds. A fix that would change a criterion, add a feature or pass
Freeze stops for the human.
