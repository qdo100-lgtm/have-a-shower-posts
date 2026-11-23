"""No.33 🔍 홍진경 멜라토닌 20mg(6장) · No.34 ⭐ 채령 TV 보며 홈케어(6장) – 11/23, 이전(No.31) 스타일
사진: briefs/images/2026-11-23(Pixabay·대표 제공 셀럽 사진), 2026-11-23d(Unsplash). 실행하면 cardnews/img/<md5>.jpg 로 복사.
표지 바꾸기: python3 cardnews/make_p33_p34.py 33B 34C  (기본 A)
"""
import hashlib
import os
import shutil
import sys

_dir = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(_dir, 'make_p17_p18.py'), encoding='utf-8').read().split('# ───────── No.17')[0])
_s = open(os.path.join(_dir, 'make_p25_p26.py'), encoding='utf-8').read()
exec(_s[_s.index('def card('):_s.index('def item(')])
_s = open(os.path.join(_dir, 'make_p30_p31.py'), encoding='utf-8').read()
exec(_s[_s.index('def photo('):_s.index("TAG['다이소 품절템']")])

B = os.path.join(_dir, '..', 'briefs', 'images')
PICK = {
    'hong': '2026-11-23/hong_user.png', 'pills': '2026-11-23d/product_pillsdark_1.jpg', 'awake': '2026-11-23d/product_awake_1.jpg',
    'bottle': '2026-11-23d/product_bottle_1.jpg', 'caps': '2026-11-23/supplement_2.jpg', 'lamp': '2026-11-23d/product_lamp_1.jpg',
    'chae': '2026-11-23/chae_user.png', 'clean': '2026-11-23d/product_cleaning_1.jpg', 'scalp': '2026-11-23d/product_scalpmassager_1.jpg',
    'tools': '2026-11-23d/product_tools_1.jpg', 'gun': '2026-11-23d/product_massager_1.jpg', 'roller': '2026-11-23d/product_foamroller_1.jpg',
    'roller2': '2026-11-23d/product_foamroller_2.jpg', 'sauna': '2026-11-23/sauna_3.jpg', 'towel': '2026-11-23b/towel_2.jpg',
}
IMG = {}
for k, f in PICK.items():
    src = os.path.join(B, f)
    h = hashlib.md5(open(src, 'rb').read()).hexdigest()
    dst = os.path.join(_dir, 'img', h + ('.png' if f.endswith('.png') else '.jpg'))
    if not os.path.exists(dst):
        from PIL import Image
        im = Image.open(src)
        im.thumbnail((2000, 2000))
        im.convert('RGB').save(dst) if dst.endswith('.jpg') else im.save(dst)
    IMG[k] = '/_blob/' + h
pick = {a[:2]: a[2:] for a in sys.argv[1:]}
TAG['팩트 체크'] = '#7FD4FF'
import re as _re
_cover3 = cover3


def cover3(*a, **k):  # 11/23 대표: 코너 이름표(팩트 체크·셀럽 루틴) 빼기
    return _re.sub(r'<div style="position: absolute; left: 72px; bottom: 470px;[^>]*>[^<]*</div>\n', '', _cover3(*a, **k))

# ───────── No.33 홍진경 멜라토닌 (6장) ─────────
S33 = '출처: 유튜브 ‘공부왕찐천재 홍진경’(2026.11.19) · iMBC 연예(11.20)'
C33 = {
    'A': (f'멜라토닌 {yl("20mg")},\n14시간 잤대요', '홍진경 유튜브 ‘공부왕찐천재’ 11.19'),
    'B': (f'선물 받은 {yl("20mg")},\n홍진경은 14시간 잤어요', '멜라토닌, 한국에선 처방약이에요'),
    'C': (f'멜라토닌, 한국에선\n{yl("처방약")}이에요', '홍진경 ‘20mg 14시간’ 이후 정리'),
}
t, s = C33[pick.get('33', 'A')]
write('P33-1-Cover.dc.html', '홍진경 멜라토닌 커버', cover3(33, IMG['hong'], '47% 35%', '팩트 체크', t, s, '사진: [사진 출처]'))

write('P33-2-What.dc.html', '무슨 일', page(2, 6, f'선물 받은 멜라토닌,\n{acc("20mg")}인 줄 몰랐대요', f'''
{photo('pills', 400, '50% 55%')}
{quote('누가 선물을 해줬는데 그게 20mg인 줄 몰랐어', '홍진경 – 유튜브 ‘공부왕찐천재’')}
{quote('나 어제 14시간 잤어', '홍진경')}
<div style="font-size: 27px; line-height: 1.5; color: #5F646B">전날 “알레르기가 너무 심해서” 약도 먹었다고 했어요</div>''', '사진: Unsplash · ' + S33))

write('P33-3-React.dc.html', '반응', page(3, 6, f'옆에서 바로\n{acc("나온 말")}', f'''
{photo('awake', 230, '45% 40%')}
{steprows([('송', '“왜 2mg도 아니고 20mg을 먹었어?”', '송은이'), ('숙', '“보통 3mg, 5mg 먹지 않아?”', '김숙'),
           ('국', '“알레르기약도 잠 오잖아”', '김종국')], 34)}
<div style="background: #FFFFFF; border-radius: 18px; padding: 24px 30px; font-size: 28px; line-height: 1.5">💡 14시간이 멜라토닌 때문인지는 <b>영상만으로 알 수 없어요</b></div>''', '사진: Unsplash · ' + S33))

write('P33-4-Korea.dc.html', '한국에선', page(4, 6, f'한국에선\n{acc("처방받는 약")}이에요', f'''
{photo('bottle', 360, '60% 50%')}
{bullets(['식약처: “멜라토닌은 국내에서 <b>전문의약품</b>으로 허가돼 있는 성분이다.”', '올해 식약처가 산 해외직구 수면 제품 11개 중 <b>9개</b>에서 멜라토닌 검출', '“고함량을 장기간 복용할 경우 의존성과 함께 두통, 어지러움, 우울 등 부작용이 나타날 수 있다.”'], 31)}''',
    '사진: Unsplash · 출처: 뉴시스(2026.7.2, 식약처 발표)'))

write('P33-5-Label.dc.html', '라벨', page(5, 6, f'적힌 용량과\n{acc("실제")}가 다를 수 있어요', f'''
<div style="display: flex; gap: 20px">{bigbox('표시보다 적게', '−83%', 104)}{bigbox('표시보다 많이', '+478%', 104)}</div>
{bullets(['캐나다 겔프대 연구팀이 멜라토닌 보충제 <b>31개</b>를 분석', '<b>71% 넘게</b> 표시 용량에서 10% 이상 벗어났어요', '같은 제품도 통마다 최대 465% 차이'], 31)}
{photo('caps', 260, '50% 70%')}''', '사진: Pixabay · 출처: Erland & Saxena, Journal of Clinical Sleep Medicine(2017)'))

write('P33-6-Closing.dc.html', '마무리', closing('잠 안 오는 밤, 먼저 이렇게', crow([
    '직구 전: ‘해외직구식품 올바로’에서 확인',
    '먹어야 한다면: 의사 처방 + 약사 복약지도',
    '오늘 밤: 잠들기 1~2시간 전 따뜻한 샤워']),
    '(해외직구 멜라토닌 쟁여둔 친구 소환) 📌 저장해두고 직구 장바구니 담기 전에 꺼내 보세요', '잠 안 올 때 뭐부터 하세요? 💬'))

# ───────── No.34 채령 홈케어 (6장) ─────────
S34 = '출처: MBC ‘전지적 참견 시점’ 425회(2026.11.21) · 톱스타뉴스(11.23)'
C34 = {
    'A': (f'채령은 드라마 보며\n{yl("두피")}를 풀어요', '전참시 11.21 · TV 보며 하는 홈케어 4'),
    'B': (f'채령의 {yl("2시간")}\n아침 홈케어', '청소부터 폼롤러까지, 전참시 11.21'),
    'C': (f'TV 볼 때 채령 손엔\n{yl("괄사")}가 있어요', '드라마엔 두피 괄사, 야구엔 폼롤러'),
}
t, s = C34[pick.get('34', 'A')]
write('P34-1-Cover.dc.html', '채령 홈케어 커버', cover3(34, IMG['chae'], '50% 10%', '셀럽 루틴', t, s, '사진: [사진 출처]'))

write('P34-2-Morning.dc.html', '아침', page(2, 6, f'일어나서 2시간,\n{acc("청소·홈케어·코디")} 끝', f'''
{photo('clean', 420, '50% 50%')}
{bullets(['ITZY 채령이 MBC ‘전지적 참견 시점’에서 보여 준 아침', '청소 끝나면 <b>부기 관리 팩</b>으로 홈케어 시작', '홈케어는 따로 시간 안 내고 <b>TV 보면서</b>'], 31)}''', '사진: Unsplash · ' + S34))

write('P34-3-Routine.dc.html', 'TV 보며', page(3, 6, f'TV 보면서 하는\n{acc("4가지")}', f'''
{steprows([('1', '두피 괄사', '드라마 볼 때'), ('2', '등 마사지기', '드라마 볼 때'),
           ('3', '종아리 폼롤러', '야구 볼 때'), ('4', '목 스트레칭 봉', '야구 볼 때')], 38)}
{photo('scalp', 200, '50% 55%')}''', '사진: Unsplash · 방송 속 브랜드는 미공개 · ' + S34))

write('P34-4-Science.dc.html', '폼롤러 연구', page(4, 6, f'폼롤러는\n{acc("운동 전")}에 더 잘 맞아요', f'''
{photo('roller', 330, '50% 60%')}
<div style="display: flex; gap: 20px">{bigbox('운동 전 · 유연성', '+4.0%', 96)}{bigbox('운동 뒤 · 근육통 느낌', '−6.0%', 96)}</div>
<div style="background: #FFFFFF; border-radius: 18px; padding: 24px 30px; font-size: 28px; line-height: 1.5">연구 21개를 모아 보니 “회복 도구보다 <b>워밍업</b>으로 쓰는 게 근거가 있다”</div>''',
    '사진: Unsplash · 출처: Wiewelhove 외, Frontiers in Physiology(2019) 메타분석'))

write('P34-5-Sauna.dc.html', '찜질방', page(5, 6, f'주말엔 언니랑\n{acc("찜질방")}', f'''
{photo('sauna', 420, '50% 50%')}
{bullets(['같은 회차에서 언니 이채연과 찜질방 데이트', '가방에서 나온 건 <b>코끼리 때타월</b> + 개인 사우나 방석', '연습생 시절 얘기도 나눴어요'], 31)}''', '사진: Pixabay · 출처: 비즈엔터(2026.11.21)'))

kit = ''.join([
    thumbrow('scalp', '두피 괄사', '드라마 1화 동안 두피 쓸어 주기'),
    thumbrow('gun', '등 마사지기', '손 안 닿는 날개뼈 쪽'),
    thumbrow('roller', '폼롤러', '종아리 · 운동 전이면 더 좋게', 'cover', '50% 65%'),
    thumbrow('towel', '때타월', '주말 찜질방 가방에'),
])
write('P34-6-Kit.dc.html', '홈케어템', page(6, 6, f'TV 보며 하는\n{acc("홈케어템")} .zip', f'''
{card(kit)}
<div style="font-size: 28px; line-height: 1.5; text-align: center">📌 저장해두고 오늘 밤 드라마 틀 때 꺼내 보세요<br><b>TV 볼 때 손에 뭐 들고 있어요? 💬</b></div>''',
    '사진: Unsplash · Pixabay · 방송 속 제품 브랜드는 미공개'))
