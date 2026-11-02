"""have.a.shower 스레드 게시 스크립트 (GitHub Actions에서 실행).

사용: python scripts/threads.py <게시물 폴더> [--publish] [--check-token]
  폴더 구성: 01.jpg ... (선택, 최대 20장) + threads.txt (본문, 500자 이내)
  threads.txt 가 없으면 caption.txt 첫 문단들을 500자 안으로 잘라 써요.
  게시 후 threads_posted.txt 를 남겨 중복 게시를 막아요.
"""
import json, os, sys, time, glob, urllib.request, urllib.parse, urllib.error

API = "https://graph.threads.net/v1.0"
TOKEN = os.environ.get("THREADS_TOKEN", "").strip()


def call(method, path, params=None):
    params = dict(params or {})
    params["access_token"] = TOKEN
    data = urllib.parse.urlencode(params).encode()
    url = f"{API}/{path}"
    req = urllib.request.Request(url + "?" + data.decode()) if method == "GET" else urllib.request.Request(url, data=data, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace").replace(TOKEN, "***")
        sys.exit(f"스레드 API 오류 ({path}): {e.code} {body}")


def wait(cid):
    for _ in range(30):
        st = call("GET", cid, {"fields": "status,error_message"})
        if st.get("status") == "FINISHED":
            return
        if st.get("status") in ("ERROR", "EXPIRED"):
            sys.exit("스레드 미디어 준비 실패: " + str(st.get("error_message")))
        time.sleep(4)
    sys.exit("스레드 미디어 준비가 너무 오래 걸려요.")


def main():
    if not TOKEN:
        sys.exit("THREADS_TOKEN 시크릿이 없어요.")
    me = call("GET", "me", {"fields": "id,username"})
    print(f"스레드 계정: @{me.get('username')}")
    if "--check-token" in sys.argv:
        print("토큰 정상")
        return
    folder = sys.argv[1].strip("/")
    publish = "--publish" in sys.argv
    if os.path.exists(os.path.join(folder, "threads_posted.txt")):
        sys.exit(f"{folder} 는 이미 스레드에 게시됐어요.")
    tp = os.path.join(folder, "threads.txt")
    if os.path.exists(tp):
        text = open(tp, encoding="utf-8").read().strip()
    else:
        text = open(os.path.join(folder, "caption.txt"), encoding="utf-8").read().strip().split("\n#")[0][:480]
    if len(text) > 500:
        sys.exit(f"스레드 본문은 500자 이내여야 해요 (지금 {len(text)}자).")
    images = sorted(glob.glob(os.path.join(folder, "*.jpg")))[:20]
    repo, sha = os.environ["GITHUB_REPOSITORY"], os.environ["GITHUB_SHA"]
    urls = [f"https://raw.githubusercontent.com/{repo}/{sha}/{urllib.parse.quote(p)}" for p in images]
    print(f"사진 {len(urls)}장\n----- 본문 ({len(text)}자) -----\n{text}\n----------------")
    if not publish:
        print("점검만 했어요.")
        return
    uid = me["id"]
    if len(urls) >= 2:
        kids = []
        for u in urls:
            k = call("POST", f"{uid}/threads", {"media_type": "IMAGE", "image_url": u, "is_carousel_item": "true"})["id"]
            wait(k); kids.append(k)
        cid = call("POST", f"{uid}/threads", {"media_type": "CAROUSEL", "children": ",".join(kids), "text": text})["id"]
    elif len(urls) == 1:
        cid = call("POST", f"{uid}/threads", {"media_type": "IMAGE", "image_url": urls[0], "text": text})["id"]
    else:
        cid = call("POST", f"{uid}/threads", {"media_type": "TEXT", "text": text})["id"]
    wait(cid)
    mid = call("POST", f"{uid}/threads_publish", {"creation_id": cid})["id"]
    link = call("GET", mid, {"fields": "permalink"}).get("permalink", "")
    print("게시 완료:", link)
    with open(os.path.join(folder, "threads_posted.txt"), "w", encoding="utf-8") as f:
        f.write(f"media_id: {mid}\nlink: {link}\nposted_at: {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())}\n")


if __name__ == "__main__":
    main()
