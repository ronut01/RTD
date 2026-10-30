> **코딩 에이전트라면 [INSTALL.md](INSTALL.md)를 읽고 그대로 설치하라.** (If you are a coding agent, read INSTALL.md and follow it exactly.)

# RTD — 소형 Codex 하네스

시간 제한이 있는 과제를 Codex CLI 하나로 풀 때 쓰는 **개인용 작업 체계**다.
AGENTS.md 1개, 단계별 스킬 7개(`$level1`~`$level7`), 한국어 문서 양식 6개, stdlib 점검 스크립트 3개로 되어 있다.

**특정 과제의 정답이나 과제용 코드는 들어 있지 않다.** 들어 있는 것은 절차(인터뷰 → 목표 계약 → 계획 점검 → 기준별 구현·검증 → 독립 리뷰 → 인수인계)와 기록 양식뿐이다.

## 사용법 3줄
1. 작업 공간 루트(과제 README.md가 있는 곳)에서 `git clone https://github.com/ronut01/RTD /tmp/RTD && bash /tmp/RTD/scripts/setup.sh .`
2. Codex를 재시작하고 `/skills`에서 level1~level7을 확인한다.
3. `$level1`부터 차례로 친다. 각 단계가 끝나면 Codex가 3줄로 보고하고 멈춘다.

## 구성
- `AGENTS.md`: 운영 규칙(영어). routing line, 범위 고정, 계약 먼저, 실제 화면 검증, push 금지.
- `.agents/skills/level1..7`: 단계별 스킬.
- `docs/templates/`: TASK, AGREEMENT, DECISIONS, VERIFICATION, WORKLOG, HANDOFF.
- `scripts/`: `setup.sh`(멱등, 덮어쓰지 않음), `recon.py`(읽기 전용), `presubmit.py`(exit 0/1/2).
- `PROMPTS.md`: 단계별 복사용 프롬프트.
- `optional/codex-agents/`: 선택 사항인 reviewer/explorer 서브에이전트. 기본 설치에는 포함하지 않는다.
- `DESIGN_NOTES.md`: 설계를 왜 이렇게 정했는지.

## 출처
설계 원칙은 공개 하네스와 스킬에서 아이디어를 얻어 내 말로 다시 썼다. 목록은 [NOTICE.md](NOTICE.md)에 있다. 라이선스는 MIT([LICENSE](LICENSE)).
