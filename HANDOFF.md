# have.a.shower 운영 인수인계 (2026-11-11)

매일 아침 '소재 후보' 세션이 이 파일을 먼저 읽고 일해요. 대표(사용자)는 그 세션에서 후보를 고르고, 같은 세션에서 제작·게시까지 이어가요.

## 1. 계정과 방향
- 인스타 @have.a.shower: 웰니스 매거진. 운영사 NOTRAC, 바디 브랜드 Nufill(우유팩 리필형, 2027년 1월 출시)의 사전 채널.
- 범위: '몸을 돌보는 모든 것'(씻기·바디, 수면·회복, 두피·헤어, 향, 이너뷰티, 운동, 마음 웰니스). 색조 메이크업·패션은 제외.
- 공식: 셀럽(얼굴) + 왜 그런지(근거) + 뭘 쓰면 되는지(제품·가격·판매처). 브랜드·셀럽 @태그. 저장할 이유를 꼭 넣기.
- 하루 2개: 12:00 '바디·웰니스 뉴스'(4~5장), 18:00 '루틴·과학 + 제품 목록'(5~10장).
- 카드뉴스 규칙: 프로젝트 문서 `claude/carousel_guide.md` (18가지 규칙·체크리스트). 이 저장소의 `carousel_guide.md`는 사본.
- 스레드 글 규칙: 프로젝트 문서 `claude/threads_guide.md` (1~3줄 반말, 질문으로 끝, 기사형 금지). 저장소 `threads_guide.md`는 사본.

## 2. 꼭 지킬 규칙
- **인스타 게시는 대표가 "올려줘"라고 할 때만.** 이때 스레드에는 올리지 않음.
- **스레드 게시는 대표가 "스레드에 올려줘"라고 따로 말할 때만.** (11/4 자동으로 같이 올렸다가 대표가 삭제함)
- 게시 전 반드시 점검 실행(publish=false) → 성공하면 게시(publish=true) → posted.txt 확인.
- **표지(첫 장) 사진은 얼굴이 잘 보이거나 제품이 예쁘게 보이는 것만**(11/13 대표 결정). 얼굴이 작으면 크롭해서 크게. 안쪽 장 사진은 자유.
- 숫자·셀럽 발언은 출처 원문 그대로. 루머 금지. 다른 매체의 로고·워터마크를 지우지 않음. 사진 출처는 캡션에 표기.
- 토큰(IG_TOKEN, THREADS_TOKEN)은 GitHub 시크릿에만 있음. 채팅·파일·로그에 절대 적지 않음.
- 대표는 쉬운 한국어, 짧은 답을 선호. 표지 문구는 대표가 직접 고르는 경우가 많으니 2~3안 제시.

## 3. 일정·진행 중
- **⚠️ 11/11 18시부터 media_publish가 403 `action is blocked`(code 4, subcode 2207051)를 돌려주지만 실제로는 게시됨**(11/13 insights로 확인: No.16~No.19 모두 올라가 있음). 실패로 보여도 **재시도 금지(중복 게시 위험)** → 먼저 `insights.yml` 실행 후 `insights/latest.json` 최신 글을 확인하고, 올라갔으면 posted.txt를 손으로 기록.
- 매일 08:50 소재 후보 → `briefs/YYYY-MM-DD.md`. 대표가 고르면 '📝 진행' 칸에 기록.
- **11/14(토) 수능 전날 편**: 수능 11/19. "수능 전날, 이렇게 씻으면 잠이 잘 와요"(잠들기 1~2시간 전 40~42°C 샤워·목욕, Haghayegh 2019 메타분석·Tai 2021 연구 = No.01 근거 재활용 + 시험 당일 아침 팁). 부모·친구가 공유할 각도.
- 보류 초안: 스레드 `posts/th01_shower_order`(샤워 순서 ①②③, 미게시 — 스레드 가이드상 더 짧게 고쳐야 함), 캔버스 P04 보습 타이밍.
- 인스타 토큰 갱신 알림 12/8, 스레드 토큰도 60일마다 갱신(발급 11/2 → 12/31 전).
- 성과(11/7 기준): 카드뉴스 도달 평균 4~6명, 제니 바세린 릴스 도달 167명. 릴스는 대표 결정으로 보류 중(카드뉴스 위주).

## 4. 카드뉴스 만드는 법
### 디자인 원본(캔버스)
- Design 아티팩트: https://claude.ai/artifact/E2d11ZrLhGmAyDiD53Tfz2 (`project/*.dc.html` + `project/canvas.json`)
- 수정 전에 Artifact `read`(path=project/파일명)로 최신본을 받고, 그 파일을 고쳐서 같은 url로 publish(root = 받은 폴더). 새 세트는 canvas.json `boards`에 1160px 간격, 행마다 1800px 아래로 추가.
- 사진은 Artifact publish `asset:true`로 올리면 `/_blob/<id>`가 나옴 → html의 img src에 그대로.

### 템플릿 (이 저장소 `cardnews/project/`)
- `Cover-v2.dc.html`: 표지. 제목 3줄 이내·한 줄 4~8자·124px 900, 강조 1~2단어 노란색 `<span style="color: #FFE14A">`, 얼굴 사진 우선, 아래쪽 어둡게, 로고+No.
- `P09-2`(번호 목록 3개) · `P09-3`(불릿 3줄 + 큰 박스/사진) · `P09-4`(방법 3단계) · `P09-5`/`Closing-v2`(마무리: 코발트 배경, "몸을 돌보는 시간에 대한 연구, 매일 전해요" + 댓글 질문).
- `P10-*`: 뉴스형(구전 스타일: 실제 인물·출처 태그·기사 페이지).
- `P13-*`: 최근 완성 예(등드름·샤워 순서). 새 세트는 이 파일들을 복사해 문구만 바꾸는 게 가장 빠름. 페이지 번호 `0N / 05`도 같이 고치기.
- 색: 코발트 #1B3FEF(`{{accent}}`), 크림 #F6F2E8, 노랑 #FFE14A. 출처는 각 장 오른쪽 아래 `출처: …`.

### 렌더링(PNG)
```bash
python3 cardnews/render_png.py /절대경로/out P14-1-Cover.dc.html P14-2-....dc.html
```
- Playwright + Noto Sans CJK KR. 새 사진은 `cardnews/img/<blob id>.jpg`로 두면 자동 연결(없으면 경고 출력).
- 결과 확인: 1/2 크기로 줄여 한 장에 이어 붙인 미리보기를 대표에게 보여주기.

### 게시 폴더
- `posts/noNN_주제/01.jpg…`(JPEG 1080×1350, 2~10장) + `caption.txt`(2200자·해시태그 30개 이하) + 스레드용은 `threads.txt`(500자 이하).
- 커밋·푸시 후 워크플로 실행:
```bash
R=qdo100-lgtm/have-a-shower-posts; D=posts/noNN_주제
gh api -X POST repos/$R/actions/workflows/publish.yml/dispatches -f ref=main -f "inputs[folder]=$D" -F "inputs[publish]=false"   # 점검
gh api -X POST repos/$R/actions/workflows/publish.yml/dispatches -f ref=main -f "inputs[folder]=$D" -F "inputs[publish]=true"    # 게시(대표 "올려줘" 후)
gh api repos/$R/contents/$D/posted.txt --jq .content | base64 -d
```
- 실패하면 `last_error.txt`(인스타)·`threads_last.txt`(스레드)에 오류가 남음. 릴스는 폴더에 `reel.mp4`(+`thumb_ms.txt`)를 두면 같은 워크플로로 게시됨.
- 성과: `insights.yml` 실행 → `insights/latest.json`.

## 5. 지금까지 다룬 주제
숙면 샤워(No.01), 생각 많을 때 샤워, 샤워 10분, 샤워볼 세균, 각질·보습, 수건 세탁, 시드니 스위니 비누(뉴스형), 제니 바세린(릴스), 장원영 1시간 샤워, 샤워 사각지대 3곳, 샤워 순서·등드름(No.10), 이후 No.11~16은 `posts/`와 `briefs/`의 진행 기록 참고.
