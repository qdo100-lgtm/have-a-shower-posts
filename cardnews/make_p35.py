"""No.35 🔍 몸 두 번 씻기 판정(5장) – 11/24, 이전(No.31) 스타일. 사진: briefs/images/2026-11-24 (Unsplash).
표지 바꾸기: python3 cardnews/make_p35.py 35B  (기본 A)
"""
import hashlib
import os
import sys

_dir = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(_dir, 'make_p17_p18.py'), encoding='utf-8').read().split('# ───────── No.17')[0])
_s = open(os.path.join(_dir, 'make_p25_p26.py'), encoding='utf-8').read()
exec(_s[_s.index('def card('):_s.index('def item(')])
_s = open(os.path.join(_dir, 'make_p30_p31.py'), encoding='utf-8').read()
exec(_s[_s.index('def photo('):_s.index("TAG['다이소 품절템']")])

B = os.path.join(_dir, '..', 'briefs', 'images')
PICK = {
    'back': '2026-11-24/product_bodywash_2.jpg', 'hand': '2026-11-24/product_bodywash_1.jpg',
    'oil': '2026-11-24/product_oil_1.jpg', 'foam': '2026-11-24/product_foam_2.jpg',
    'lotion': '2026-11-24/product_lotion_2.jpg', 'head': '2026-11-23c/showernight_1.jpg',
}
IMG = {}
for k, f in PICK.items():
    src = os.path.join(B, f)
    h = hashlib.md5(open(src, 'rb').read()).hexdigest()
    dst = os.path.join(_dir, 'img', h + '.jpg')
    if not os.path.exists(dst):
        from PIL import Image
        im = Image.open(src)
        im.thumbnail((2000, 2000))
        im.convert('RGB').save(dst, quality=90)
    IMG[k] = '/_blob/' + h
pick = {a[:2]: a[2:] for a in sys.argv[1:]}
import re as _re
_cover3 = cover3


def cover3(*a, **k):  # 11/23 대표: 코너 이름표 빼기
    return _re.sub(r'<div style="position: absolute; left: 72px; bottom: 470px;[^>]*>[^<]*</div>\n', '', _cover3(*a, **k))


S = '출처: Allure(2026.11.20) · 피부과 전문의 3명 인터뷰'
C35 = {
    'A': (f'몸 두 번 씻기,\n피부과 의사는 {yl("‘필요 없다’")}', '미국 틱톡 유행 ‘바디 더블 클렌징’ 판정'),
    'B': (f'바디워시 {yl("두 번")},\n오히려 피부가 말라요', '피부과 전문의 3명이 내린 판정'),
    'C': (f'틱톡에서 유행하는\n{yl("몸 두 번 씻기")}, 판정 나왔어요', '피부과 전문의 3명 · Allure 11.20'),
}
t, s = C35[pick.get('35', 'A')]
write('P35-1-Cover.dc.html', '몸 두 번 씻기 커버', cover3(35, IMG['back'], '50% 40%', '진짜일까?', t, s, '사진: Unsplash'))

write('P35-2-What.dc.html', '유행', page(2, 5, f'얼굴처럼 몸도\n{acc("두 번")} 씻는 게 유행이에요', f'''
<div style="display: flex; gap: 20px">
<div style="flex: 1">{photo('oil', 420, '50% 55%')}</div>
<div style="flex: 1">{photo('foam', 420, '50% 50%')}</div>
</div>
{steprows([('1', '오일 클렌저로 한 번', '선크림·바디오일·피지를 녹인다는 이유'),
           ('2', '바디워시로 또 한 번', '같은 바디워시로 두 번 씻는 사람도 있어요')], 38)}''', '사진: Unsplash · ' + S))

write('P35-3-Doctors.dc.html', '의사들', page(3, 5, f'피부과 의사 3명의\n{acc("대답")}', f'''
{quote('대부분은 몸을 두 번 씻을 필요가 없어요. 한 번이면 보통 충분해요', '아리엘 오스타드 – 뉴욕 피부과 전문의')}
{quote('너무 씻으면 피부 장벽이 무너져 건조·자극·습진 악화로 이어질 수 있어요. 기온이 떨어질 땐 더더욱', '크리스 토마시안 – 캘리포니아 피부과 전문의')}
{quote('한 번 씻어서 안 깨끗하면, 두 번째가 아니라 다른 바디워시가 필요한 거예요', '안젤로 란드리시나 – 뉴욕 피부과 전문의')}''', S))

rows = ''.join(f'''<div style="display: flex; align-items: center; gap: 26px; background: #FFFFFF; border-radius: 20px; padding: 26px 32px">
<div style="font-size: 62px; width: 76px; flex-shrink: 0; text-align: center">{m}</div>
<div style="display: flex; flex-direction: column; gap: 6px"><div style="font-family: {GOTHIC}; font-size: 38px; font-weight: 800">{a}</div><div style="font-size: 27px; line-height: 1.4; color: #5F646B">{b}</div></div>
</div>''' for m, a, b in [
    ('❌', '매일 두 번 씻기', '평소 하루를 보낸 몸은 한 번이면 충분'),
    ('🔺', '바디 메이크업 · 워터프루프 선크림 바른 날', '이런 날만 두 번 – 순한 제품으로, 스크럽·센 비누는 빼고'),
    ('❌', '등드름 때문에 두 번', '횟수보다 성분 – 살리실산·벤조일퍼옥사이드 세정제'),
])
write('P35-4-Verdict.dc.html', '판정', page(4, 5, f'그래서 {acc("판정")}은', f'''
{card(rows)}
{photo('hand', 250, '50% 45%')}''', '사진: Unsplash · ' + S))

write('P35-5-Closing.dc.html', '마무리', closing('두 번 씻을 시간에, 이렇게', crow([
    '한 번만 씻기 (양도 조금만)',
    '수건으로 톡톡, 물기 살짝 남기기',
    '그때 바로 바디로션·크림 바르기']),
    '(샤워할 때 바디워시 두 번 짜는 친구 소환) 📌 저장해두고 오늘 샤워 때 꺼내 보세요', '여러분은 몸 몇 번 씻어요? 💬'))
