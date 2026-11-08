"""Pexels에서 표지용 배경 사진을 받아와요.

사용법: python scripts/fetch_photos.py briefs/images/2026-11-08/queries.txt

queries.txt 형식 (한 줄에 하나, # 은 메모):
    sauna | finnish sauna wooden
    mist  | perfume mist winter knit

결과: 같은 폴더에 sauna_1.jpg, sauna_2.jpg ... 와 credits.txt(사진작가·원본 링크)
"""
import json
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path

PER_QUERY = 3
API = "https://api.pexels.com/v1/search"


def get(url, key):
    req = urllib.request.Request(url, headers={"Authorization": key, "User-Agent": "have-a-shower-photos"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def main():
    key = os.environ.get("PEXELS_KEY", "").strip()
    if not key:
        print("PEXELS_KEY 가 아직 없어요. 저장소 Settings → Secrets 에 넣어 주세요. (이번엔 건너뜀)")
        return
    qfile = Path(sys.argv[1])
    folder = qfile.parent
    credits = []
    for line in qfile.read_text(encoding="utf-8").splitlines():
        line = line.split("#", 1)[0].strip()
        if not line or "|" not in line:
            continue
        name, query = [s.strip() for s in line.split("|", 1)]
        params = urllib.parse.urlencode({"query": query, "orientation": "portrait", "per_page": PER_QUERY})
        data = json.loads(get(f"{API}?{params}", key))
        photos = data.get("photos", [])
        print(f"{name}: '{query}' → {len(photos)}장")
        for i, p in enumerate(photos, 1):
            out = folder / f"{name}_{i}.jpg"
            if out.exists():
                continue
            # portrait = 800x1200, large2x = 원본 비율 고화질
            out.write_bytes(get(p["src"]["large2x"], key))
            credits.append(f"{out.name}\t{p['photographer']}\t{p['url']}")
    if credits:
        with open(folder / "credits.txt", "a", encoding="utf-8") as f:
            f.write("\n".join(credits) + "\n")


if __name__ == "__main__":
    main()
