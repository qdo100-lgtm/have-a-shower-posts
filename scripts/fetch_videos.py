"""릴스 배경용 무료 영상(세로)을 받아와요. Pexels(세로 우선) → 없으면 Pixabay.

사용법: python scripts/fetch_videos.py briefs/images/2026-11-18/videos.txt

videos.txt 형식 (한 줄에 하나, # 은 메모):
    squat | woman squat exercise home

결과: 같은 폴더에 v_squat_1.mp4 ... 와 credits.txt(작가·원본 링크)
"""
import json
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path

PER_QUERY = 2


def get(url, headers=None):
    req = urllib.request.Request(url, headers={"User-Agent": "have-a-shower-videos", **(headers or {})})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def pick_pexels(files):
    # 세로 영상 중 1080~1440 높이 이상, 너무 크지 않은 것
    files = [f for f in files if f.get("height") and f.get("width") and f["file_type"] == "video/mp4"]
    files.sort(key=lambda f: abs(f["height"] - 1920))
    return files[0]["link"] if files else None


def search_pexels(query, key):
    params = urllib.parse.urlencode({"query": query, "orientation": "portrait", "per_page": PER_QUERY + 2, "size": "medium"})
    auth = {"Authorization": key}
    vids = json.loads(get(f"https://api.pexels.com/videos/search?{params}", auth)).get("videos", [])
    out = []
    for v in vids:
        if v.get("height", 0) < v.get("width", 1):
            continue
        link = pick_pexels(v.get("video_files", []))
        if link:
            out.append((link, v.get("user", {}).get("name", ""), v.get("url", ""), {}))
    return out[:PER_QUERY]


def search_pixabay(query, key):
    params = urllib.parse.urlencode({"key": key, "q": query, "per_page": PER_QUERY + 3, "safesearch": "true"})
    hits = json.loads(get(f"https://pixabay.com/api/videos/?{params}")).get("hits", [])
    out = []
    for h in hits:
        v = h["videos"].get("large") or h["videos"].get("medium")
        if v and v.get("url"):
            out.append((v["url"], h["user"], h["pageURL"], {}))
    return out[:PER_QUERY]


def main():
    pexels = os.environ.get("PEXELS_KEY", "").strip()
    pixabay = os.environ.get("PIXABAY_KEY", "").strip()
    qfile = Path(sys.argv[1])
    folder = qfile.parent
    credits = []
    for line in qfile.read_text(encoding="utf-8").splitlines():
        line = line.split("#", 1)[0].strip()
        if not line or "|" not in line:
            continue
        name, query = [s.strip() for s in line.split("|", 1)]
        results, site = [], ""
        if pexels:
            try:
                results, site = search_pexels(query, pexels), "Pexels"
            except Exception as e:
                print(f"{name}: Pexels 오류 {e}")
        if not results and pixabay:
            try:
                results, site = search_pixabay(query, pixabay), "Pixabay"
            except Exception as e:
                print(f"{name}: Pixabay 오류 {e}")
        print(f"{name}: '{query}' → {len(results)}개 ({site})")
        for i, (url, author, page, headers) in enumerate(results, 1):
            out = folder / f"v_{name}_{i}.mp4"
            if out.exists():
                continue
            try:
                out.write_bytes(get(url, headers))
                credits.append(f"{out.name}\t{site}\t{author}\t{page}")
            except Exception as e:
                print(f"  {out.name} 받기 실패: {e}")
    if credits:
        with open(folder / "credits.txt", "a", encoding="utf-8") as f:
            f.write("\n".join(credits) + "\n")


if __name__ == "__main__":
    main()
