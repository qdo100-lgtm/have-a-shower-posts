# have.a.shower 카드뉴스 업로드

## 처음 한 번
1. 이 저장소는 **Public**이어야 해요 (인스타그램이 사진 주소를 열 수 있어야 해요).
2. Settings → Secrets and variables → Actions → New repository secret
   - Name: `IG_TOKEN`
   - Secret: 인스타그램 토큰 (Downloads\meta_token.txt 안의 값)
3. 토큰을 갱신하면 여기 값도 새 토큰으로 바꿔 주세요.

## 게시물 올리기
1. `posts/` 아래에 게시물 폴더를 만들어요 (예: `posts/no02`).
   - `01.jpg`, `02.jpg` … (순서대로, JPEG, 2~10장)
   - `caption.txt` : 본문 글과 해시태그
   - `first_comment.txt` : 첫 댓글 (선택)
2. Actions 탭 → **인스타그램 게시** → Run workflow
   - 폴더를 입력하고 **게시하기 체크 없이** 먼저 실행 → 점검 결과(계정, 사진, 캡션) 확인
   - 문제없으면 **게시하기 체크**하고 다시 실행 → 게시
3. 게시가 끝나면 폴더에 `posted.txt`가 생겨요. 같은 게시물이 두 번 올라가지 않게 막아줘요.

공개 저장소라 올려둔 사진은 링크를 아는 사람이 볼 수 있어요. 게시 직전에 올리세요.
