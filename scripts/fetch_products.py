"""제품 사진(보도자료·공식 페이지 이미지)을 받아와요.

사용법: python scripts/fetch_products.py briefs/images/2026-11-08/products.txt

products.txt 형식 (한 줄에 하나, # 은 메모):
    beyond | https://.../news_123.jpg          ← 이미지 주소면 그대로 받음
    beyond | https://news.site/article/123     ← 페이지 주소면 대표 이미지(og:image)를 받음
결과: 같은 폴더에 product_beyond_1.jpg ... 와 credits.txt(원본 주소)
"""
import re
import sys
import urllib.request
from pathlib import Path

UA = "Mozilla/5.0 (compatible; have-a-shower-photos)"
IMG = re.compile(r"\.(jpe?g|png|webp)(\?.*)?$", re.I)


def get(url, referer=None):
    headers = {"User-Agent": UA}
    if referer:
        headers["Referer"] = referer
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=30) as r:
        return r.read(), r.headers.get_content_type()


def og_image(page):
    html, _ = get(page)
    html = html.decode("utf-8", "ignore")
    for pat in (r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)',
                r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image'):
        m = re.search(pat, html, re.I)
        if m:
            return m.group(1).replace("&amp;", "&")
    return None


def main():
    qfile = Path(sys.argv[1])
    folder = qfile.parent
    counts, credits = {}, []
    for line in qfile.read_text(encoding="utf-8").splitlines():
        line = line.split(" #", 1)[0].strip()
        if not line or line.startswith("#") or "|" not in line:
            continue
        name, url = [s.strip() for s in line.split("|", 1)]
        try:
            img = url if IMG.search(url) else og_image(url)
            if not img:
                print(f"{name}: 대표 이미지를 못 찾음 {url}")
                continue
            data, ctype = get(img, referer=url)
            if not ctype.startswith("image/"):
                print(f"{name}: 이미지가 아님({ctype}) {img}")
                continue
            counts[name] = counts.get(name, 0) + 1
            ext = {"image/png": "png", "image/webp": "webp"}.get(ctype, "jpg")
            out = folder / f"product_{name}_{counts[name]}.{ext}"
            out.write_bytes(data)
            credits.append(f"{out.name}\t{url}")
            print(f"{name}: 저장 {out.name} ({len(data)//1024}KB)")
        except Exception as e:  # 한 곳이 막혀도 나머지는 계속
            print(f"{name}: 실패 {url} ({e})")
    if credits:
        with open(folder / "credits.txt", "a", encoding="utf-8") as f:
            f.write("\n".join(credits) + "\n")


if __name__ == "__main__":
    main()
