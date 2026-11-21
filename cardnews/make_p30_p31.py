"""No.30 다이소 3,000원 마그네슘 품절템(5장, 11/21 11:30) · No.31 ⭐ 이지혜 세신 4만 원 목욕탕(7장, 11/21 17:30)
사진: briefs/images/2026-11-21/ (Pixabay + 제품 사진). 실행하면 cardnews/img/<md5>.jpg 로 복사하고 /_blob/<md5> 로 씀.
표지 바꾸기: python3 cardnews/make_p30_p31.py 30B 31C  (기본 A)
"""
import hashlib
import os
import shutil
import sys

_dir = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(_dir, 'make_p17_p18.py'), encoding='utf-8').read().split('# ───────── No.17')[0])
_s = open(os.path.join(_dir, 'make_p25_p26.py'), encoding='utf-8').read()
exec(_s[_s.index('def card('):_s.index('def item(')])

PH = os.path.join(_dir, '..', 'briefs', 'images', '2026-11-21')
PICK = {
    'cover30': 'asleep2_1.jpg', 'sleep30': 'asleep_1.jpg', 'mag': 'product_mag_2.jpg', 'mag_box': 'product_mag_1.webp',
    'drbear': 'product_drbear_1.jpg', 'almond': 'nut_2.jpg', 'pumpkin': 'cashew_2.jpg',
    'spinach': 'spinachleaf_3.jpg', 'choco': 'spinach_3.jpg',
    'cover31': 'leejihye_ig.png', 'robe': 'bathwoman_1.jpg', 'bath': 'bucket_3.jpg', 'cucumber': 'cucumber_1.jpg', 'salt': 'salt_3.jpg',
    'towel': 'bathhouse_3.jpg', 'foot': 'foot_2.jpg', 'cream': 'scrub_1.jpg', 'gounbal': 'product_gounbal_1.jpg',
    'bucket': 'bucket_1.jpg',
}
PICK.update(dict(a.split('=', 1) for a in sys.argv[1:] if '=' in a))
IMG = {}
for k, f in PICK.items():
    src = os.path.join(PH, f)
    if not os.path.exists(src):
        print('사진 없음:', k, f)
        continue
    h = hashlib.md5(open(src, 'rb').read()).hexdigest()
    ext = '.png' if f.endswith(('.png', '.webp')) else '.jpg'
    dst = os.path.join(_dir, 'img', h + ext)
    if f.endswith('.webp'):
        from PIL import Image
        Image.open(src).save(dst)
    elif not os.path.exists(dst):
        shutil.copy(src, dst)
    IMG[k] = '/_blob/' + h
pick = {a[:2]: a[2:] for a in sys.argv[1:] if '=' not in a}


def photo(key, h, pos='50% 50%', fit='cover', bg='#FFFFFF', radius=22):
    return (f'<div style="height: {h}px; border-radius: {radius}px; overflow: hidden; background: {bg}; flex-shrink: 0">'
            f'<img src="{IMG.get(key, "")}" alt="" style="width: 100%; height: 100%; object-fit: {fit}; object-position: {pos}; display: block"></div>')


def tile(key, name, line, h=250, fit='cover', pos='50% 50%'):
    return f'''<div style="flex: 1; display: flex; flex-direction: column; gap: 12px; background: #FFFFFF; border-radius: 20px; padding: 14px 14px 22px">
{photo(key, h, pos, fit, '#F1ECE0', 14)}
<div style="font-family: {GOTHIC}; font-size: 33px; font-weight: 800; padding: 0 8px">{name}</div>
<div style="font-size: 25px; line-height: 1.4; color: #5F646B; padding: 0 8px">{line}</div>
</div>'''


def thumbrow(key, name, line, fit='cover', pos='50% 50%'):
    return f'''<div style="display: flex; gap: 26px; align-items: center; background: #FFFFFF; border-radius: 20px; padding: 16px 28px 16px 16px">
<div style="width: 150px; height: 150px; border-radius: 14px; overflow: hidden; flex-shrink: 0; background: #F1ECE0"><img src="{IMG.get(key, "")}" alt="" style="width: 100%; height: 100%; object-fit: {fit}; object-position: {pos}; display: block"></div>
<div style="display: flex; flex-direction: column; gap: 6px"><div style="font-family: {GOTHIC}; font-size: 38px; font-weight: 800">{name}</div><div style="font-size: 27px; line-height: 1.4; color: #5F646B">{line}</div></div>
</div>'''


def steprows(steps, size=40):
    return card(''.join(f'''<div style="display: flex; align-items: center; gap: 28px; background: #FFFFFF; border-radius: 20px; padding: 26px 36px">
<div style="font-family: {GOTHIC}; font-size: 54px; font-weight: 800; color: {{{{accent}}}}; width: 50px; flex-shrink: 0">{n}</div>
<div style="display: flex; flex-direction: column; gap: 6px"><div style="font-family: {GOTHIC}; font-size: {size}px; font-weight: 800">{a}</div><div style="font-size: 28px; line-height: 1.4; color: #5F646B">{b}</div></div>
</div>''' for n, a, b in steps))


def quote(t, who):
    return f'''<div style="border-left: 8px solid {{{{accent}}}}; padding: 8px 0 8px 30px; display: flex; flex-direction: column; gap: 10px"><div style="font-family: {GOTHIC}; font-size: 40px; font-weight: 800; line-height: 1.4">“{t}”</div><div style="font-size: 26px; color: #5F646B">{who}</div></div>'''


TAG['다이소 품절템'] = '#FFE14A'

# ───────── No.30 다이소 마그네슘 (5장) ─────────
S30 = '출처: 위키트리(2026.11.15) · 다이소몰(11.21 기준)'
C30 = {
    'A': (f'다이소 3,000원\n{yl("마그네슘")} 품절 이유', '1알에 100원 · 리뷰 7,857개 · 별점 4.8'),
    'B': (f'1알 {yl("100원")},\n다이소 마그네슘', '품절됐다 재입고 – 뭐가 들었나 봤어요'),
    'C': (f'요즘 다이소에서\n{yl("제일 빨리")} 사라지는 것', '3,000원 마그네슘, 재입고되자마자 품절'),
}
t, s = C30[pick.get('30', 'A')]
write('P30-1-Cover.dc.html', '다이소 마그네슘 커버', cover3(30, IMG.get('cover30', ''), '50% 30%', '다이소 품절템', t, s, '사진: Pixabay'))

spec = bullets(['30정 30일분 <b>3,000원</b> (1알 100원꼴)', '1알에 마그네슘 <b>315mg</b> – 하루 기준치 100%', '비타민D 10μg도 같이 (기준치 100%)',
                '대웅제약이 직접 만들어요(횡성 1공장)', '다이소몰 리뷰 <b>4.8점 · 7,857개</b>'], 30)
write('P30-2-What.dc.html', '뭐길래', page(2, 5, f'재입고되자마자 품절,\n{acc("대웅제약")} 마그네슘', f'''
<div style="display: flex; gap: 32px; align-items: stretch">
<div style="width: 400px; flex-shrink: 0">{photo('mag', 560, '50% 40%', 'cover', '#EDE4F7')}</div>
<div style="flex: 1; display: flex; flex-direction: column; justify-content: center">{spec}</div>
</div>
<div style="font-size: 27px; line-height: 1.5; color: #5F646B">다이소에 들어간 대웅제약 ‘닥터베어’ 건강기능식품 중 하나예요 – 한 달분 3,000원·5,000원</div>''',
    '사진: 다이소 · ' + S30))

write('P30-3-Why.dc.html', '왜 찾나', page(3, 5, f'눈 떨림, 다리 쥐,\n그리고 {acc("잠")} 때문에', f'''
{photo('sleep30', 380, '50% 12%')}
{bullets(['마그네슘 기능(제품 표시): <b>에너지 이용 · 신경과 근육 기능 유지</b>에 필요', '부족하면 눈 밑이 파르르 떨리거나 자다가 다리에 쥐가 나기 쉬워요(기사)', '잠 때문에 찾는 사람도 많지만 – 연구 15개를 모아 보니 효과는 <b>엇갈렸어요</b>'], 30)}
<div style="background: #FFFFFF; border-radius: 18px; padding: 24px 30px; font-size: 28px; line-height: 1.5">“부담 적고 저렴한 선택지일 뿐, <b>확실한 해결책은 아니다</b>” – 수면·마그네슘 연구 15개 정리(2026)</div>''',
    '출처: 위키트리(2026.11.15) · Men’s Fitness(2026.11.07)'))

foods = f'''<div style="display: flex; gap: 18px">{tile('almond', '견과류', '아몬드·호두 한 줌')}{tile('pumpkin', '씨앗', '호박씨·해바라기씨')}</div>
<div style="display: flex; gap: 18px">{tile('spinach', '시금치', '초록 잎채소')}{tile('choco', '다크초콜릿', '카카오 높은 걸로')}</div>'''
write('P30-4-Food.dc.html', '음식', page(4, 5, f'알약이 싫다면\n{acc("먹는 걸로")} 채워요', f'''
{foods}
<div style="font-size: 26px; line-height: 1.45; color: #5F646B">견과류·씨앗·초록 채소·통곡물에 마그네슘이 많아요(미국 NIH 영양보충제국)</div>''',
    '사진: Pixabay · 출처: NIH Office of Dietary Supplements'))

write('P30-5-Closing.dc.html', '마무리', closing('사기 전에 체크 4', crow([
    '다이소 앱 ‘매장 상품 찾기’로 재고 먼저',
    '하루 1알, 물과 함께 – 한 번에 많이 먹으면 배탈 날 수 있어요',
    '신장 질환·약 먹는 중이면 약사·의사와 먼저',
    '잠이 목적이면 자기 1~2시간 전 따뜻한 샤워도 같이']),
    '(다이소 털러 가는 친구 소환) 📌 저장해두고 다이소 갈 때 꺼내 보세요', '다이소 영양제 뭐 드세요? 💬'))

# ───────── No.31 ⭐ 이지혜 목욕탕 (7장) ─────────
S31 = '출처: 유튜브 ‘밉지않은 관종언니’(2026.11.19) · 인사이트(11.20) · MK스포츠·OSEN(11.19)'
C31 = {
    'A': (f'이지혜가 반한\n세신 {yl("4만 원")} 목욕탕', '경주 동네 목욕탕 · 목욕 꿀템까지 공개'),
    'B': (f'이지혜 목욕 가방엔\n{yl("뭐가")} 들었을까', '목욕탕 꿀템 5가지 + 세신 4만 원 풀코스'),
    'C': (f'“여기서 {yl("명인")}을\n만났다”', '이지혜가 다시 가겠다고 한 경주 목욕탕'),
}
t, s = C31[pick.get('31', 'A')]
write('P31-1-Cover.dc.html', '이지혜 목욕탕 커버', cover3(31, IMG.get('cover31', ''), '50% 0%', '셀럽 루틴', t, s, '사진: 이지혜 인스타그램'))

write('P31-2-Where.dc.html', '어디', page(2, 7, f'세신 받으세요?\n{acc("혼자")} 미세요?', f'''
{photo('bath', 380, '50% 55%')}
{bullets(['이지혜가 간 곳: 경북 경주의 동네 목욕탕 ‘부산탕’ – 제작진 PD 부모님이 운영', '입장료 <b>6,500원</b> · 한 달 정기권 <b>10만 원</b> 수준', '세신 + 전신 마사지 + 샴푸까지 <b>4만 원</b>'], 31)}''', S31))

write('P31-3-Course.dc.html', '풀코스', page(3, 7, f'4만 원 풀코스는\n{acc("이 순서")}', f'''
{steprows([('1', '거친 이태리타월', '1차로 각질 밀기'), ('2', '부드러운 타월', '2차로 한 번 더 마무리'),
           ('3', '오일 + 마사지', '어깨부터 전신까지 꼼꼼하게'), ('4', '생오이 팩', '마지막 서비스')], 38)}
{quote('정말로 여기서 명인을 만났다', '이지혜 – 20년 넘게 일한 세신사에게 받고')}''', S31))

write('P31-4-Machine.dc.html', '등밀이 기계', page(4, 7, f'경상도에만 있다는\n{acc("자동 등밀이")} 기계', f'''
{photo('towel', 300, '50% 60%')}
{bullets(['탕 안에 있는 <b>무료</b> 기계 – 등도 발도 밀 수 있어요', '때타월에 비누 바르고 시작 버튼 → 돌아가는 타월에 몸을 대는 방식', '이지혜: “의자가 붙어있네 심지어” → 해보더니 등이 <b>발갛게</b>'], 31)}
{quote('너무 아파요. 사람 손길이 좋아요', '이지혜 – 자동 등밀이 기계 써보고')}
<div style="background: #FFFFFF; border-radius: 18px; padding: 26px 32px; font-size: 29px; line-height: 1.5">💡 세게 민다고 더 깨끗한 건 아니에요. <b>빨개지면 멈추고</b>, 나와서 바로 보습!</div>''', S31))

kit = ''.join([
    thumbrow('salt', '진실의 빚소금', '대구 서문시장에서 품절 대란 났던 소금'),
    thumbrow('towel', '빨간 타월', '세정력 센 때타월'),
    thumbrow('foot', '일본산 뒤꿈치 버퍼', '발뒤꿈치 각질 정리용'),
    thumbrow('cream', '우레아 크림', '병원 전용 제품으로 소개'),
    thumbrow('gounbal', '고운발 크림', '뒤꿈치 각질 크림', 'contain'),
])
write('P31-5-Kit.dc.html', '목욕 꿀템', page(5, 7, f'제작진과 꺼낸\n{acc("목욕탕 꿀템")} 5', f'''
{card(kit)}''', '사진: Pixabay · 제품 사진은 참고용 · ' + S31.replace('출처: ', '')))

write('P31-6-Order.dc.html', '순서', page(6, 7, f'이지혜처럼\n{acc("목욕탕 200%")} 즐기기', f'''
{photo('robe', 220, '50% 20%')}
{steprows([('1', '화장 지우고 샤워 먼저', '탕에 들어가기 전에 – 이지혜도 이것부터'), ('2', '탕에서 몸 불리기', '“야, 진짜 시원해!”'),
           ('3', '세신 → 마사지 → 오이 팩', '빨개지면 멈추기'), ('4', '나와서 바로 보습', '뒤꿈치는 크림 한 번 더')], 34)}''', S31))

write('P31-7-Closing.dc.html', '마무리', closing('주말 목욕탕 체크리스트', crow([
    '입장 전: 화장 지우고 샤워부터',
    '세신: 세게보다 살살, 빨개지면 스톱',
    '나와서: 3분 안에 보습 + 뒤꿈치 크림']),
    '(주말에 목욕탕 같이 갈 친구 소환) 📌 저장해두고 목욕탕 갈 때 꺼내 보세요', '여러분 목욕 가방 필수템은? 💬'))
