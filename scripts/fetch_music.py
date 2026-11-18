"""릴스 배경음악(무료 라이선스) 받기. 이 클라우드 환경에선 음악 사이트가 막혀 있어 GitHub Actions에서 받아요.

사용법: python scripts/fetch_music.py briefs/images/2026-11-18/music.txt
music.txt 형식: 이름 | mp3 주소 | 크레딧(캡션에 적을 문구)
결과: 같은 폴더에 m_이름.mp3 와 credits.txt
"""
import sys
import urllib.request
from pathlib import Path


def main():
    qfile = Path(sys.argv[1])
    folder, credits = qfile.parent, []
    for line in qfile.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or line.count("|") < 1:
            continue
        parts = [s.strip() for s in line.split("|")]
        name, url, credit = parts[0], parts[1], (parts[2] if len(parts) > 2 else "")
        out = folder / f"m_{name}.mp3"
        if out.exists():
            continue
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (have-a-shower-music)"})
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            out.write_bytes(data)
            credits.append(f"{out.name}\t{credit}\t{url}")
            print(f"{name}: {len(data)//1024}KB")
        except Exception as e:
            print(f"{name}: 받기 실패 {e} ({url})")
    if credits:
        with open(folder / "credits.txt", "a", encoding="utf-8") as f:
            f.write("\n".join(credits) + "\n")


if __name__ == "__main__":
    main()
