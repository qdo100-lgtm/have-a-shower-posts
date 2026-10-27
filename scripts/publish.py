"""have.a.shower 카드뉴스 인스타그램 업로드 스크립트 (GitHub Actions에서 실행).

사용: python scripts/publish.py <게시물 폴더> [--publish]
  --publish 없이 실행하면 점검만 해요 (토큰 확인, 이미지 주소 확인, 캡션 미리보기).
  --publish 를 붙여야 실제로 게시해요.

게시물 폴더 구성:
  01.jpg, 02.jpg, ...   (JPEG, 1080x1350, 2~10장)
  caption.txt           (본문 글 + 해시태그)
  first_comment.txt     (선택: 첫 댓글)
  posted.txt            (게시 후 자동 생성. 있으면 중복 게시를 막아요)
"""
import json, os, sys, time, glob, urllib.request, urllib.parse, urllib.error

API = "https://graph.instagram.com/v21.0"
TOKEN = os.environ.get("IG_TOKEN", "").strip()


def call(method, path, params=None):
    params = dict(params or {})
    params["access_token"] = TOKEN
    data = urllib.parse.urlencode(params).encode()
    url = f"{API}/{path}"
    if method == "GET":
        req = urllib.request.Request(url + "?" + data.decode())
    else:
        req = urllib.request.Request(url, data=data, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace").replace(TOKEN, "***")
        sys.exit(f"인스타그램 API 오류 ({path}): {e.code} {body}")


def check_url(u):
    req = urllib.request.Request(u, method="HEAD")
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.status, r.headers.get("Content-Type")


def main():
    if len(sys.argv) < 2:
        sys.exit("게시물 폴더를 지정해 주세요. 예: posts/no01")
    folder = sys.argv[1].strip("/")
    publish = "--publish" in sys.argv
    if not TOKEN:
        sys.exit("IG_TOKEN 시크릿이 없어요. 저장소 Settings > Secrets and variables > Actions 에 등록해 주세요.")
    if os.path.exists(os.path.join(folder, "posted.txt")):
        sys.exit(f"{folder} 는 이미 게시됐어요 (posted.txt 있음). 다시 올리려면 posted.txt를 지우세요.")

    reel = os.path.join(folder, "reel.mp4")
    if os.path.exists(reel):
        return publish_reel(folder, reel, publish)

    images = sorted(glob.glob(os.path.join(folder, "*.jpg")) + glob.glob(os.path.join(folder, "*.jpeg")))
    if not 2 <= len(images) <= 10:
        sys.exit(f"캐러셀은 사진 2~10장이 필요해요. 지금 {len(images)}장이에요.")
    caption = open(os.path.join(folder, "caption.txt"), encoding="utf-8").read().strip()
    if len(caption) > 2200:
        sys.exit(f"캡션이 너무 길어요 ({len(caption)}자, 최대 2200자).")
    if caption.count("#") > 30:
        sys.exit("해시태그는 최대 30개예요.")
    fc_path = os.path.join(folder, "first_comment.txt")
    first_comment = open(fc_path, encoding="utf-8").read().strip() if os.path.exists(fc_path) else ""

    repo = os.environ["GITHUB_REPOSITORY"]
    sha = os.environ["GITHUB_SHA"]
    urls = [f"https://raw.githubusercontent.com/{repo}/{sha}/{urllib.parse.quote(p)}" for p in images]

    me = call("GET", "me", {"fields": "user_id,username"})
    ig_id = me.get("user_id") or me.get("id")
    print(f"계정: @{me.get('username')}")
    print(f"사진 {len(urls)}장:")
    for u in urls:
        status, ctype = check_url(u)
        print(f"  {status} {ctype} {u}")
        if status != 200:
            sys.exit("사진 주소를 열 수 없어요. 저장소가 공개(Public)인지 확인해 주세요.")
    print("\n----- 캡션 -----\n" + caption + "\n----------------")
    if first_comment:
        print("첫 댓글: " + first_comment)

    if not publish:
        print("\n점검만 했어요. 실제로 올리려면 '게시하기'를 체크하고 다시 실행하세요.")
        return

    children = []
    for u in urls:
        r = call("POST", f"{ig_id}/media", {"image_url": u, "is_carousel_item": "true"})
        children.append(r["id"])
        print("사진 준비:", r["id"])
    box = call("POST", f"{ig_id}/media", {"media_type": "CAROUSEL", "children": ",".join(children), "caption": caption})
    cid = box["id"]
    for _ in range(30):
        st = call("GET", cid, {"fields": "status_code"}).get("status_code")
        print("상태:", st)
        if st == "FINISHED":
            break
        if st in ("ERROR", "EXPIRED"):
            sys.exit("인스타그램에서 게시물 준비에 실패했어요.")
        time.sleep(5)
    else:
        sys.exit("게시물 준비가 너무 오래 걸려요. 잠시 후 다시 실행해 주세요.")
    media = call("POST", f"{ig_id}/media_publish", {"creation_id": cid})
    mid = media["id"]
    link = call("GET", mid, {"fields": "permalink"}).get("permalink", "")
    print("게시 완료:", link)
    if first_comment:
        call("POST", f"{mid}/comments", {"message": first_comment})
        print("첫 댓글 완료")
    with open(os.path.join(folder, "posted.txt"), "w", encoding="utf-8") as f:
        f.write(f"media_id: {mid}\nlink: {link}\nposted_at: {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())}\n")


def publish_reel(folder, reel, publish):
    """릴스(영상 1개) 게시. 폴더에 reel.mp4 + caption.txt, 선택으로 thumb_ms.txt(표지 위치, 밀리초)."""
    caption = open(os.path.join(folder, "caption.txt"), encoding="utf-8").read().strip()
    if len(caption) > 2200:
        sys.exit(f"캡션이 너무 길어요 ({len(caption)}자, 최대 2200자).")
    if caption.count("#") > 30:
        sys.exit("해시태그는 최대 30개예요.")
    tpath = os.path.join(folder, "thumb_ms.txt")
    thumb = open(tpath).read().strip() if os.path.exists(tpath) else ""
    repo = os.environ["GITHUB_REPOSITORY"]
    sha = os.environ["GITHUB_SHA"]
    url = f"https://raw.githubusercontent.com/{repo}/{sha}/{urllib.parse.quote(reel)}"

    me = call("GET", "me", {"fields": "user_id,username"})
    ig_id = me.get("user_id") or me.get("id")
    print(f"계정: @{me.get('username')}")
    status, ctype = check_url(url)
    print(f"릴스 영상: {status} {ctype} {url}")
    if status != 200:
        sys.exit("영상 주소를 열 수 없어요.")
    print("\n----- 캡션 -----\n" + caption + "\n----------------")
    if not publish:
        print("\n점검만 했어요. 실제로 올리려면 '게시하기'를 체크하고 다시 실행하세요.")
        return

    params = {"media_type": "REELS", "video_url": url, "caption": caption, "share_to_feed": "true"}
    if thumb:
        params["thumb_offset"] = thumb
    cid = call("POST", f"{ig_id}/media", params)["id"]
    for _ in range(60):
        st = call("GET", cid, {"fields": "status_code,status"})
        print("상태:", st.get("status_code"), st.get("status", ""))
        if st.get("status_code") == "FINISHED":
            break
        if st.get("status_code") in ("ERROR", "EXPIRED"):
            sys.exit("인스타그램에서 영상 처리에 실패했어요: " + str(st.get("status")))
        time.sleep(10)
    else:
        sys.exit("영상 처리가 너무 오래 걸려요. 잠시 후 다시 실행해 주세요.")
    mid = call("POST", f"{ig_id}/media_publish", {"creation_id": cid})["id"]
    link = call("GET", mid, {"fields": "permalink"}).get("permalink", "")
    print("게시 완료:", link)
    with open(os.path.join(folder, "posted.txt"), "w", encoding="utf-8") as f:
        f.write(f"media_id: {mid}\nlink: {link}\nposted_at: {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())}\n")


if __name__ == "__main__":
    main()
