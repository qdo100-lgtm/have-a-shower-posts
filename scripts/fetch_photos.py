"""표지용 배경 사진을 무료 사진 사이트에서 받아와요.

키가 있는 사이트를 씀: PIXABAY_KEY(우선) 또는 PEXELS_KEY.
사용법: python scripts/fetch_photos.py briefs/images/2026-11-08/queries.txt

queries.txt 형식 (한 줄에 하나, # 은 메모):
    sauna | finnish sauna wooden

결과: 같은 폴더에 sauna_1.jpg ... 와 credits.txt(사진작가·원본 링크)
"""
import json
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path

PER_QUERY = 3


def get(url, headers=None):
    req = urllib.request.Request(url, headers={"User-Agent": "have-a-shower-photos", **(headers or {})})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def search_pixabay(query, key):
    params = urllib.parse.urlencode({"key": key, "q": query, "image_type": "photo",
                                     "orientation": "vertical", "per_page": PER_QUERY, "safesearch": "true"})
    hits = json.loads(get(f"https://pixabay.com/api/?{params}")).get("hits", [])
    return [(h["largeImageURL"], h["user"], h["pageURL"], {}) for h in hits[:PER_QUERY]]


def search_pexels(query, key):
    params = urllib.parse.urlencode({"query": query, "orientation": "portrait", "per_page": PER_QUERY})
    auth = {"Authorization": key}
    photos = json.loads(get(f"https://api.pexels.com/v1/search?{params}", auth)).get("photos", [])
    return [(p["src"]["large2x"], p["photographer"], p["url"], auth) for p in photos]


def main():
    pixabay = os.environ.get("PIXABAY_KEY", "").strip()
    pexels = os.environ.get("PEXELS_KEY", "").strip()
    sites = []
    if pixabay:
        sites.append(("Pixabay", search_pixabay, pixabay, ""))
    if pexels:
        # 2026-11-23: Pixabay만으로는 내용과 안 맞는 사진이 많아 Pexels도 같이 받음 (파일명 name_p1.jpg …)
        sites.append(("Pexels", search_pexels, pexels, "p"))
    if not sites:
        print("사진 사이트 키가 아직 없어요. 저장소 Settings → Secrets 에 PIXABAY_KEY 를 넣어 주세요. (이번엔 건너뜀)")
        return
    qfile = Path(sys.argv[1])
    folder = qfile.parent
    credits = []
    for line in qfile.read_text(encoding="utf-8").splitlines():
        line = line.split("#", 1)[0].strip()
        if not line or "|" not in line:
            continue
        name, query = [s.strip() for s in line.split("|", 1)]
        for site, search, key, prefix in sites:
            try:
                results = search(query, key)
            except Exception as e:
                print(f"{name}: '{query}' {site} 실패 – {e}")
                continue
            print(f"{name}: '{query}' → {len(results)}장 ({site})")
            for i, (url, author, page, headers) in enumerate(results, 1):
                out = folder / f"{name}_{prefix}{i}.jpg"
                if out.exists():
                    continue
                out.write_bytes(get(url, headers))
                credits.append(f"{out.name}\t{site}\t{author}\t{page}")
    if credits:
        with open(folder / "credits.txt", "a", encoding="utf-8") as f:
            f.write("\n".join(credits) + "\n")


if __name__ == "__main__":
    main()
