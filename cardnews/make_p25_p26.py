"""No.25 골라드림: 벨라 하디드 '캐시미어 밀크' + 겨울 우유·바닐라 바디템 (5장, 11/17 11:40)
No.26 셀럽 루틴: 캔디스 스와넵풀 "에브리띵 샤워는 주 2~3번" (6장, 11/17 17:40)
공통 함수는 make_p17_p18.py 앞부분(cover3 포함)을 그대로 씀.
표지 문구 바꾸기: python3 cardnews/make_p25_p26.py 25B 26C  (기본 A)
사진 id는 cardnews/img_p25_p26.json (cardnews/img/<id>.jpg)
"""
import json
import os
import sys

_dir = os.path.dirname(os.path.abspath(__file__))
_src = open(os.path.join(_dir, 'make_p17_p18.py'), encoding='utf-8').read()
exec(_src.split('# ───────── No.17')[0])

pick = {a[:2]: a[2:] for a in sys.argv[1:]}
IMG = json.load(open(os.path.join(_dir, 'img_p25_p26.json'), encoding='utf-8'))


def card(rows):
    return '<div style="display: flex; flex-direction: column; gap: 18px">' + rows + '</div>'


def closing(title, rows_html, share, ask):
    return f'''<div style="width: 1080px; height: 1350px; box-sizing: border-box; padding: 80px 72px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 42px; background: #1B3FEF; color: #FBF7EC; font-family: {FONT}; text-align: center; word-break: keep-all; overflow: hidden">
<div style="font-family: {GOTHIC}; font-size: 56px; font-weight: 800; line-height: 1.3">{title}</div>
<div style="display: flex; flex-direction: column; gap: 22px; background: rgba(255,255,255,0.1); border-radius: 22px; padding: 40px 48px; align-self: stretch">{rows_html}</div>
<div style="font-size: 32px; line-height: 1.55">{share}</div>
<img src="{LOGO_C}" alt="have a shower 로고" style="width: 360px; display: block">
<div style="font-size: 30px; line-height: 1.6">몸을 돌보는 시간에 대한 연구, 매일 전해요</div>
<div style="font-size: 30px; font-weight: 700; color: {Y}">{ask}</div>
</div>'''


def crow(rows):
    return ''.join(f'''<div style="display: flex; gap: 22px; align-items: flex-start; text-align: left"><div style="font-family: {GOTHIC}; font-size: 40px; font-weight: 800; color: {Y}; width: 40px; flex-shrink: 0">{i}</div><div style="font-size: 34px; line-height: 1.45">{t}</div></div>''' for i, t in enumerate(rows, 1))


def item(tag, name, line1, line2):
    return f'''<div style="display: flex; flex-direction: column; gap: 8px; background: #FFFFFF; border-radius: 20px; padding: 28px 36px">
<div style="display: flex; gap: 14px; align-items: center"><div style="padding: 6px 16px; border-radius: 30px; background: {{{{accent}}}}; color: #FFFFFF; font-size: 24px; font-weight: 700; flex-shrink: 0">{tag}</div><div style="font-size: 36px; font-weight: 800; line-height: 1.3">{name}</div></div>
<div style="font-size: 29px; line-height: 1.45; color: #17191C">{line1}</div>
<div style="font-size: 26px; line-height: 1.4; color: #5F646B">{line2}</div>
</div>'''


# ───────── No.25 골라드림: 우유 냄새 겨울 향 (5장) ─────────
SW = '출처: Who What Wear(2026.11.03) · Bella Hadid 인터뷰'
C25 = {
    'A': (f'올겨울 향은\n{yl("우유")} 냄새래요', '벨라 하디드 새 향 + 한국에서 사는 법'),
    'B': (f'벨라 하디드가 고른\n겨울 향은 {yl("우유")}?', '새 향 ‘캐시미어 밀크’와 비슷한 바디템'),
    'C': (f'포근한 {yl("살냄새")}\n바디템 골라드림', '우유·바닐라 향, 해외 신상부터 국내까지'),
}
t, s = C25[pick.get('25', 'A')]
write('P25-1-Cover.dc.html', '우유 향 커버',
      cover3(25, IMG['cover25'], IMG['pos25'], '골라드림', t, s, IMG['credit25']))

write('P25-2-News.dc.html', '캐시미어 밀크', page(2, 5, f'벨라 하디드 새 향\n{acc("‘캐시미어 밀크’")}', f'''
{bigbox("Ôrəbella(오레벨라) 7번째 향 · 퍼퓸", "$100", 120)}
{bullets(["향: 크리미 밀크 · 재스민 밀크 · 바닐라 캐비어 · 앰버 · 캐시미어 우드 · 통카빈", "벨라 하디드: “첫눈 온 뒤 조용한 순간(quiet moment after the first snowfall)” 같은 향", "알코올 없는 ‘피부 먼저’ 향수 – 보습 오일 베이스에 시더우드·시나몬·베르가못 오일"], 32)}''', SW))

steps = [('1', '피부에 먼저', '캐시미어 밀크를 맨살에 바로 뿌리기'),
         ('2', '달콤하게 한 겹', '바닐라 미스트 ‘Vanilla’s Touch’($39)를 위에 겹치기'),
         ('3', '저녁엔 더 깊게', '‘Nightcap’($72)과 섞으면 “더 관능적”')]
srows = ''.join(f'''<div style="display: flex; align-items: center; gap: 28px; background: #FFFFFF; border-radius: 20px; padding: 30px 38px">
<div style="font-family: {GOTHIC}; font-size: 56px; font-weight: 800; color: {{{{accent}}}}; width: 50px; flex-shrink: 0">{n}</div>
<div style="display: flex; flex-direction: column; gap: 6px"><div style="font-family: {GOTHIC}; font-size: 44px; font-weight: 800">{a}</div><div style="font-size: 29px; line-height: 1.4; color: #5F646B">{b}</div></div>
</div>''' for n, a, b in steps)
write('P25-3-Layer.dc.html', '레이어링', page(3, 5, f'벨라가 직접 말한\n{acc("겹쳐 뿌리기")} 순서', f'''
{card(srows)}
<div style="font-size: 30px; line-height: 1.5; color: #5F646B">“방 전체를 채우는 향보다, 가까이 와야 알아채는 향이 특별해요” – 벨라 하디드</div>''', SW))

items = (item('바디워시', '해피바스 산양유 ‘밀크 블랑쉬’', '코튼 + 머스크 · 910g', '10/7 출시 · 쿠팡·아모레몰 등')
         + item('바디워시', '해피바스 산양유 ‘바닐라 머스크’', '바닐라 + 머스크 · 910g', '같은 라인 · 같은 판매처')
         + item('바디 토너', '노크 멜트 인 바디 토너 ‘서울바닐라’', '“진한 풍미의 바닐라 향” · 300ml 정가 36,000원', '공식몰·쿠팡 · 판매처마다 할인가 달라요'))
write('P25-4-Korea.dc.html', '한국에서', page(4, 5, f'한국에서 찾는\n{acc("우유·바닐라")} 바디템', f'''
{card(items)}
<div style="font-size: 27px; line-height: 1.45; color: #5F646B">씻을 때 우유 향 → 바른 뒤 바닐라 향으로 겹치면 벨라 순서와 같아요</div>''', '출처: 뉴스프리존(2026.10.07) · 노크 공식몰 · 언파'))

write('P25-5-Closing.dc.html', '마무리', closing('겨울 살냄새 3줄 정리', crow([
    '벨라 하디드 새 향 = 우유 + 바닐라 + 캐시미어 우드',
    '맨살에 먼저 뿌리고, 바닐라 미스트를 한 겹',
    '국내는 해피바스 산양유 · 노크 서울바닐라']),
    '살냄새 향 좋아하는 친구 소환 📌', '우유 향 vs 바닐라 향, 뭐가 더 좋아요? 💬'))

# ───────── No.26 셀럽 루틴: 에브리띵 샤워 주 2~3번 (6장) ─────────
SC = '출처: Who What Wear(2026.11.12) · Candice Swanepoel 인터뷰'
C26 = {
    'A': (f'1시간 샤워는\n{yl("주 2~3번")}만', '빅토리아 시크릿 모델 캔디스의 루틴'),
    'B': (f'매일 1시간 씻나요?\n모델은 {yl("주 2~3번")}', '캔디스 스와넵풀이 직접 말한 에브리띵 샤워'),
    'C': (f'VS 모델의\n{yl("에브리띵 샤워")} 루틴', '횟수 · 시간 · 쓰는 것 다 공개'),
}
t, s = C26[pick.get('26', 'A')]
write('P26-1-Cover.dc.html', '에브리띵 샤워 커버',
      cover3(26, IMG['cover26'], IMG['pos26'], '셀럽 루틴', t, s, IMG['credit26']))

write('P26-2-What.dc.html', '에브리띵 샤워', page(2, 6, f'요즘 유행하는\n{acc("에브리띵 샤워")}가 뭐예요?', f'''
{bigbox("10월 네이버 ‘장원영 샤워법’ 검색량(전월 대비)", "775%↑", 120)}
{bullets(["머리부터 발끝까지 한 번에: 세정 + 헤어팩 + 바디 스크럽 + 보습", "장원영이 8월 아이브 유튜브에서 “공연 끝나고 약 1시간 샤워”라고 말한 뒤 따라 하기가 퍼졌어요", "그럼 이걸 매일 해야 할까요? 👉"], 32)}''', '출처: 매일경제(2026.11.13) · 블랙키위'))

write('P26-3-Candice.dc.html', '캔디스 답', page(3, 6, f'VS 모델 캔디스의 답:\n{acc("주 2~3번")}', f'''
{bigbox("캔디스 스와넵풀 · 빅토리아 시크릿 2026 홀리데이 캠페인", "주 2~3번 · 1시간", 92)}
{bullets(["“일주일에 두세 번 정도, 스케줄에 따라 달라요”", "“시간이 있으면 전체 루틴은 1시간도 쉽게 걸려요”", "“여유 있을 땐 천천히 – 특히 헤어 트리트먼트랑 각질 관리”"], 33)}''', SC))

items = (item('각질', '각질 제거 장갑', '샤워하면서 몸 각질 관리', '브랜드는 말하지 않았어요')
         + item('헤어', 'K18', '헤어 트리트먼트로 쓴다고 직접 언급', '해외 헤어 브랜드 · 국내 판매처 확인 필요')
         + item('보습', '샤워 후 보습', '“항상 꼭 보습해요(always make sure to moisturize)”', '데이트 날엔 VS 바디 루미나이저로 은은한 광')
         + item('쉬기', '도톰한 가운 + 슬리퍼', '“나만의 시간을 갖는 좋은 방법”', '씻고 바로 폰 대신, 잠깐 쉬기'))
write('P26-4-Items.dc.html', '쓰는 것', page(4, 6, f'캔디스가 직접 말한\n{acc("4가지")}', f'''
{card(items)}''', SC))

week = [('월', '풀코스', True), ('화', '기본', False), ('수', '기본', False), ('목', '풀코스', True),
        ('금', '기본', False), ('토', '풀코스', True), ('일', '기본', False)]
wrow = ''.join(f'''<div style="flex: 1; display: flex; flex-direction: column; align-items: center; gap: 12px; padding: 24px 0; border-radius: 18px; background: {"{{accent}}" if full else "#FFFFFF"}; color: {"#FFFFFF" if full else "#17191C"}">
<div style="font-family: {GOTHIC}; font-size: 40px; font-weight: 800">{d}</div><div style="font-size: 24px; font-weight: 700">{w}</div></div>''' for d, w, full in week)
write('P26-5-Week.dc.html', '주간표', page(5, 6, f'따라 하기 쉬운\n{acc("일주일")} 샤워표', f'''
<div style="display: flex; gap: 10px">{wrow}</div>
{bullets(["풀코스(주 2~3번): 헤어 트리트먼트 + 각질 관리 + 보습까지, 천천히", "기본 날: 미온수로 3~5분, 씻을 곳만 – 피부과 전문의 성현철", "어느 날이든 씻고 나면 바로 보습: “씻었으면 채워줘야 한다”"], 32)}''', '출처: Who What Wear(2026.11.12) · 뉴시스(2026.11.14)'))

write('P26-6-Closing.dc.html', '마무리', closing('에브리띵 샤워, 이것만', crow([
    '매일 말고 주 2~3번이면 충분(캔디스)',
    '풀코스 날: 헤어 트리트먼트 · 각질 · 보습',
    '나머지 날은 3~5분, 그리고 바로 보습']),
    '매일 1시간 씻는 친구한테 공유 📌', '여러분은 일주일에 몇 번 풀코스 하세요? 💬'))
