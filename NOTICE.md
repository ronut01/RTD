# NOTICE — 아이디어 출처

이 repo의 문장은 모두 새로 썼다. 다른 repo의 문장을 그대로 옮긴 곳은 없다. 아래는 아이디어를 얻은 곳이다.

## MIT 라이선스 (아이디어 차용)
| 출처 | 경로 | 가져온 아이디어 | 반영 위치 |
|------|------|-----------------|-----------|
| mattpocock/skills (MIT, © 2026 Matt Pocock) | skills/productivity/grilling | 결정 트리 순서로 질문, 추천 답 첨부, 사실은 직접 찾고 결정만 묻기 | level2 |
| addyosmani/agent-skills (MIT, © 2025 Addy Osmani) | interview-me, idea-refine, spec-driven-development, planning-and-task-breakdown, incremental-implementation | 다음 3개 답을 예측할 수 있으면 인터뷰 종료, Not Doing 목록, 수직 슬라이스, 작은 단위 구현·커밋 | level2·3·4·5 |
| obra/superpowers (MIT, © 2025 Jesse Vincent) | verification-before-completion, systematic-debugging, writing-plans | 증명 명령을 새로 실행하기 전에는 완료라고 하지 않기, 재현 먼저, 3회 실패 시 설계 의심, 요구사항↔작업 매핑 | AGENTS §5·6, level4·6 |
| garrytan/gstack (MIT, © 2026 Garry Tan) | office-hours, review, qa | 해법 단어 없이 현재 업무부터 묻기, diff와 의도를 비교해 scope drift 찾기, 테스트가 무엇을 증명하지 않는지 적기 | level2·6·7 |
| github/spec-kit (MIT, © GitHub, Inc.) | templates/commands/specify, clarify, analyze | 질문을 영향도 순으로 3~7개만, 나머지는 기본값과 Assumptions, 명세·계획 교차 점검 | level1·3·4 |
| hamjoon2003/sk-hynix-2nd-harness (MIT) | scripts/preflight.py | "검사 0개 = exit 2" 규칙, 기능 동결 시각 | presubmit.py, level5 |
| hongkevin/cofathon-prep (MIT) | recon | fromisoformat 'Z' 함정 점검, 기대값을 코드와 같은 방식으로 계산하지 않기 | recon.py, AGENTS §4 |
| AgenticLab-SH/sh-workflows (MIT) | docs/OPTIMIZATION_PLAYBOOK, role-separated-design | 정식화 → 기준선 → 개선 → 비교 순서, 기준선 없이 "최적"이라 하지 않기, 무거운 계산은 운영자 동작에서 한 번 실행·저장 | AGENTS §3·6, level4·5, DESIGN.md |

## 라이선스 불명확 또는 비MIT (아이디어만, 문장 미사용)
- code-yeongyu/oh-my-openagent (NOASSERTION): routing line과 stop condition, ask-type 분류, 목표 계약 필드, 1패스 계획 점검 판정(OKAY/ITERATE/REJECT, 최대 3이슈), READ→CHANGE→RUN 루프, 3회 실패 규칙.
- Yeachan-Heo/oh-my-codex (MIT): clarify → plan → execute 분리, 관련 스킬만 소수 로드.
- Malrangbbobbi/hynix-harness-kit, jincode93/cofa-kit, alslrl/cofathon-kit: HANDOFF 맨 위 현재 단계, 덮어쓰지 않는 setup, WORKLOG 채택/수정/거절, "요구된 것만" 원칙.
- anthropics/claude-code feature-dev, cursor/plugins pstack: 대안 2~3안 비교, 다른 모델로 독립 검토.
