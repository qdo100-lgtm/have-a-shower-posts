"""표지 v3 시안 (2026-11-15): 피드 그리드 일관성용.
규칙: 사진 전체 + 아래 어둡게 / 위 가운데 작은 로고 / 왼쪽 위 코너 태그 / 아래 왼쪽 제목 2줄(84px, 노란 강조 1곳) + 부제 1줄 / 맨 아래 출처(왼)·No.(오)
제목·부제는 인스타 그리드(3:4) 잘림 안쪽(위아래 각 135px 바깥 금지)에 둔다.
사용: python3 cardnews/make_cover_v3.py  → project/V3-*.dc.html
"""
import os

_src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'make_p17_p18.py'), encoding='utf-8').read()
exec(_src.split('# ───────── No.17')[0])

# 코너별 태그 색 (그리드에서 코너가 한눈에 보이게)
TAG = {
    '7일 따라하기': '#FFE14A',
    '진짜일까?': '#7FD4FF',
    '골라드림': '#FFB8D9',
    '웃긴데 진짜': '#B6F5A1',
    '셀럽 루틴': '#FFFFFF',
    '신상': '#FFFFFF',
}


def cover3(no, img, pos, tag, title_html, sub, credit=''):
    tc = TAG.get(tag, '#FFFFFF')
    return f'''<div style="position: relative; width: 1080px; height: 1350px; overflow: hidden; background: #111315; color: #FFFFFF; font-family: {FONT}; word-break: keep-all">
<img src="{img}" alt="" style="position: absolute; left: 0; top: 0; width: 1080px; height: 1350px; object-fit: cover; object-position: {pos}; display: block">
<div style="position: absolute; left: 0; right: 0; top: 0; height: 300px; background: linear-gradient(180deg, rgba(10,12,14,0.45) 0%, rgba(10,12,14,0) 100%)"></div>
<div style="position: absolute; left: 0; right: 0; bottom: 0; height: 760px; background: linear-gradient(180deg, rgba(10,12,14,0) 0%, rgba(10,12,14,0.55) 35%, rgba(10,12,14,0.92) 80%)"></div>
<img src="{LOGO_W}" alt="have a shower 로고" style="position: absolute; left: 50%; top: 150px; transform: translateX(-50%); height: 54px; display: block">
<div style="position: absolute; left: 72px; bottom: 470px; padding: 10px 22px; border-radius: 40px; background: {tc}; color: #111315; font-size: 30px; font-weight: 800; letter-spacing: -0.01em">{tag}</div>
<h1 style="position: absolute; left: 72px; right: 72px; bottom: 250px; margin: 0; font-family: {FONT}; font-size: 84px; font-weight: 900; line-height: 1.22; letter-spacing: -0.04em; color: #FFFFFF; text-shadow: 0 3px 18px rgba(0,0,0,0.45); white-space: pre-line">{title_html}</h1>
<div style="position: absolute; left: 72px; right: 72px; bottom: 190px; font-size: 34px; font-weight: 500; line-height: 1.35; color: rgba(255,255,255,0.88)">{sub}</div>
<div style="position: absolute; left: 72px; bottom: 70px; font-size: 20px; color: rgba(255,255,255,0.55)">{credit}</div>
<div style="position: absolute; right: 72px; bottom: 66px; font-size: 24px; font-weight: 700; letter-spacing: 0.08em; color: rgba(255,255,255,0.7)">No.{no}</div>
</div>'''


samples = [
    ('V3-1-Yoona', 21, '/_blob/4cc92d63d397dc718225927ac33b7ae6', '50% 0%', '셀럽 루틴',
     f'윤아 가방 속\n{yl("관리템 3가지")}', 'W KOREA ‘인 마이 백’에서 직접 꺼낸 것', '사진: W KOREA 유튜브'),
    ('V3-2-Suneung', 22, '/_blob/55a627e0c082588fb6f7e1d4716f316c', '50% 30%', '따라하기',
     f'잠드는 시간\n{yl("10분")} 줄이는 샤워', '수능 전날 밤, 수험생 가족에게 공유하세요', '사진: Unsplash'),
    ('V3-3-Hair7', 23, '/_blob/3e0a339ed6344ddbbe08e3067de06fe3', '50% 22%', '7일 따라하기',
     f'탈모 막는\n하루 루틴 {yl("7일")}', 'Day 1부터 저장하고 하나씩 따라 하세요', '사진: Pixabay'),
    ('V3-4-Cold', 24, '/_blob/308f20327d5a6478a42089ef495b3b60', '50% 30%', '진짜일까?',
     f'운동 끝나고\n냉탕 vs {yl("온탕")}', '40명을 72시간 지켜본 연구의 답', '사진: Pixabay'),
    ('V3-5-Scent', 25, '/_blob/38545f4ca8ce68b2b861d4d6bc861935', '50% 40%', '골라드림',
     f'향 좋은 바디워시\n{yl("향 계열별")} 5개', '비누향·머스크·과일향, 올영에서 바로', '사진: 브랜드 제공'),
    ('V3-6-Funny', 26, '/_blob/aa885ee38caf06747531b8c4885c95b9', '50% 45%', '웃긴데 진짜',
     f'벽에 다리 올리고\n{yl("10분")}, 효과 있대요', '자기 전 누워서 하는 제일 쉬운 습관', '사진: Pixabay'),
]
for name, no, img, pos, tag, t, sub, cr in samples:
    write(name + '.dc.html', f'표지 v3 시안 {name}', cover3(no, img, pos, tag, t, sub, cr))
