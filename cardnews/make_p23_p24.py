"""No.23 진짜일까? '안 씻기' 소문 3개 판정 (6장, 11/16 11:30) · No.24 웃긴데 진짜: 잠들다 움찔 (6장, 11/16 17:30).
공통 함수는 make_p17_p18.py 앞부분(cover3 포함)을 그대로 씀.
표지 문구 바꾸기: python3 cardnews/make_p23_p24.py 23B 24C  (기본 A)
사진 id는 아래 IMG_* (cardnews/img/<id>.jpg)
"""
import os
import sys

_src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'make_p17_p18.py'), encoding='utf-8').read()
exec(_src.split('# ───────── No.17')[0])

pick = {a[:2]: a[2:] for a in sys.argv[1:]}
IMG = json_ids = __import__('json').load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img_p23_p24.json'), encoding='utf-8'))


def card(rows):
    return '<div style="display: flex; flex-direction: column; gap: 18px">' + rows + '</div>'


def verdict(mark, color, word, line):
    return f'''<div style="display: flex; align-items: center; gap: 34px; background: #FFFFFF; border-radius: 22px; padding: 34px 44px">
<div style="width: 150px; height: 150px; border-radius: 75px; background: {color}; display: flex; align-items: center; justify-content: center; font-size: 86px; font-weight: 900; color: #FFFFFF; flex-shrink: 0">{mark}</div>
<div style="display: flex; flex-direction: column; gap: 10px"><div style="font-family: {GOTHIC}; font-size: 54px; font-weight: 800">{word}</div><div style="font-size: 31px; line-height: 1.45; color: #5F646B">{line}</div></div>
</div>'''


def closing(title, rows_html, share, ask):
    return f'''<div style="width: 1080px; height: 1350px; box-sizing: border-box; padding: 80px 72px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 42px; background: #1B3FEF; color: #FBF7EC; font-family: {FONT}; text-align: center; word-break: keep-all; overflow: hidden">
<div style="font-family: {GOTHIC}; font-size: 56px; font-weight: 800; line-height: 1.3">{title}</div>
<div style="display: flex; flex-direction: column; gap: 22px; background: rgba(255,255,255,0.1); border-radius: 22px; padding: 40px 48px; align-self: stretch">{rows_html}</div>
<div style="font-size: 32px; line-height: 1.55">{share}</div>
<img src="{LOGO_C}" alt="have a shower 로고" style="width: 360px; display: block">
<div style="font-size: 30px; line-height: 1.6">몸을 돌보는 시간에 대한 연구, 매일 전해요</div>
<div style="font-size: 30px; font-weight: 700; color: {Y}">{ask}</div>
</div>'''


RED, ORG, GRN = '#E5484D', '#F2A33A', '#2FA36B'

# ───────── No.23 진짜일까? 안 씻기 소문 (6장) ─────────
SA = '출처: Forbes(2026.08.16) · Fast Company(2026.09.03)'
SB = '출처: 뉴시스(2026.11.14) · 유튜브 ‘피부는 성현철’'
SC = '출처: HELLO!(2026.08.27) · Haghayegh 외(2019)'

C23 = {
    'A': (f'데이트 전엔\n{yl("안 씻는")} 게 유행?', '해외·국내 씻기 소문 3개, 판정해 봤어요'),
    'B': (f'안 씻으면\n{yl("더 매력적")}이다?', '틱톡 유행부터 피부과 의사 말까지, 3개 판정'),
    'C': (f'샤워 소문 3개\n{yl("진짜")}일까?', '안 씻기 · 이틀에 한 번 · 불 끄고 샤워'),
}
t, s = C23[pick.get('23', 'A')]
write('P23-1-Cover.dc.html', '안 씻기 소문 커버',
      cover3(23, IMG['cover23'], IMG.get('pos23', '50% 30%'), '진짜일까?', t, s, IMG.get('credit23', '')))

qs = [('①', '데이트 전에 안 씻으면 페로몬이 나와 더 끌린다'),
      ('②', '겨울엔 샤워 이틀에 한 번이면 충분하다'),
      ('③', '불 끄고 깜깜하게 샤워하면 잠이 잘 온다')]
qrows = ''.join(f'''<div style="display: flex; gap: 26px; align-items: center; background: #FFFFFF; border-radius: 20px; padding: 34px 40px">
<div style="font-family: {GOTHIC}; font-size: 54px; font-weight: 800; color: {{{{accent}}}}; flex-shrink: 0">{n}</div>
<div style="font-size: 38px; font-weight: 700; line-height: 1.4">{q}</div></div>''' for n, q in qs)
write('P23-2-Question.dc.html', '질문', page(2, 6, f'요즘 도는 씻기 소문,\n{acc("진짜")}는 몇 개?', f'''
{card(qrows)}
<div style="font-size: 34px; line-height: 1.5; color: #5F646B">⭕ 맞다 · 🔺 반만 맞다 · ❌ 아니다<br>댓글로 먼저 찍고 넘겨 보세요 👉</div>''', '@have.a.shower 정리'))

write('P23-3-Pheromone.dc.html', '① 페로몬', page(3, 6, f'① 안 씻으면\n{acc("페로몬")}이 나온다?', f'''
{verdict('✕', RED, '아니에요', '사람이 성 페로몬을 내는지조차 아직 확인되지 않았어요')}
{bullets(["미국 틱톡의 ‘페로몬 맥싱’: 데이트 전에 샤워·데오드란트를 일부러 건너뛰는 유행이에요", "의사 브루스 Y. 리(포브스): 사람 몸에서 성 페로몬을 따로 찾아낸 연구는 아직 없어요", "“사람이 만든 화학 신호에 일관되고 강한 행동 반응이 있다는 증거는 없다” (사이언티픽 아메리칸)", "페로몬만 남기고 땀·먼지만 골라 씻을 수도 없어요"], 32)}''', SA))

write('P23-4-EveryOther.dc.html', '② 이틀에 한 번', page(4, 6, f'② 겨울엔 샤워\n{acc("이틀에 한 번")}이면 충분?', f'''
{verdict('△', ORG, '반만 맞아요', '피부과 전문의 한 명의 의견이에요. 땀 흘린 날은 그날 씻어요')}
{bullets(["성현철 피부과 전문의(유튜브 구독자 25만): “겨울에는 이틀에 한 번이면 충분”", "대신 이렇게: “미온수는 온수가 아니다. 체온과 비슷한 온도” · “3분~5분 만에 끝내는 게 좋다”", "수건은 “문지르지 말고 톡톡 눌러서”, 씻은 뒤엔 바로 보습 – “씻었으면 채워줘야 한다”"], 32)}''', SB))

write('P23-5-Dark.dc.html', '③ 어둠 샤워', page(5, 6, f'③ 불 끄고 샤워하면\n{acc("잠")}이 잘 온다?', f'''
{verdict('△', ORG, '반만 맞아요', '원리는 맞지만, 이 방법만 따로 연구한 적은 없어요')}
{bullets(["수면 전문의 디아스 가르시아: “원리는 맞지만 직접 증거가 없어 유행일 뿐, 치료법은 아니다”", "증명된 건 따로 있어요: 잠들기 1~2시간 전 40~42.5°C 샤워·목욕 → 평균 10분 더 빨리 잠듦(연구 13개)", "완전히 깜깜하면 미끄러질 수 있어요. 은은한 조명이면 충분해요"], 32)}''', SC))

srows = ''.join(f'''<div style="display: flex; gap: 22px; align-items: center; text-align: left"><div style="width: 64px; height: 64px; border-radius: 32px; background: {c}; display: flex; align-items: center; justify-content: center; font-size: 36px; font-weight: 900; color: #FFFFFF; flex-shrink: 0">{m}</div><div style="font-size: 33px; line-height: 1.4">{t}</div></div>''' for m, c, t in [
    ('✕', RED, '안 씻으면 페로몬 → 근거 없음'),
    ('△', ORG, '겨울 이틀에 한 번 → 의사 한 명 의견'),
    ('△', ORG, '불 끄고 샤워 → 원리만 맞음')])
write('P23-6-Closing.dc.html', '마무리', closing('씻기 소문 판정표', srows,
      '이상한 샤워 꿀팁 받으면 꺼내 보게 저장 📌', '다음엔 어떤 소문을 판정할까요? 댓글로 💬'))

# ───────── No.24 웃긴데 진짜: 잠들다 움찔 (6장) ─────────
SD = '출처: Grünberger 외, PLOS Mental Health(2026) · Neuroscience News(2026.11.11)'

C24 = {
    'A': (f'잠들다 {yl("움찔!")}\n하고 깨는 이유', '194명을 조사한 새 연구(2026.11)'),
    'B': (f'자다가 {yl("움찔")},\n나만 그런 거 아니죠?', '194명 조사한 새 연구가 나왔어요'),
    'C': (f'{yl("움찔")} 하고 깨는 사람\n공통점 찾았다', '독일·오스트리아 194명 조사(2026.11)'),
}
t, s = C24[pick.get('24', 'A')]
write('P24-1-Cover.dc.html', '움찔 커버',
      cover3(24, IMG['cover24'], IMG.get('pos24', '50% 30%'), '웃긴데 진짜', t, s, IMG.get('credit24', '')))

opts = [('A', '거의 매일 움찔'), ('B', '가끔 움찔'), ('C', '처음 들어봄')]
orows = ''.join(f'''<div style="background: #FFFFFF; border-radius: 20px; padding: 32px 42px; font-size: 42px; font-weight: 700">{a}. {acc(b)}</div>''' for a, b in opts)
write('P24-2-Question.dc.html', '질문', page(2, 6, f'잠들 때 몸이 떨어지는 느낌,\n{acc("움찔!")} 나는?', f'''
{card(orows)}
{bullets(["이걸 ‘수면 놀람(sleep start)’, 입면 경련이라고 불러요", "연구자: “대부분의 사람에게는 잠드는 과정의 무해한 특징”", "댓글로 A·B·C 남겨 주세요 👉"], 33)}''', SD))

write('P24-3-Study.dc.html', '연구', page(3, 6, f'자주 움찔하는 사람만\n{acc("모아서")} 비교했어요', f'''
{bigbox("독일·오스트리아 성인", "194명", 120)}
{bullets(["주 1회 이상 움찔하는 사람 96명 vs 비교 그룹 98명", "잠의 질, 불면, 불안·우울, ‘잠에 대한 생각’까지 설문으로 비교", "학술지 PLOS Mental Health에 실렸어요 (2026년 11월 소개)"], 33)}''', SD))

res = [('😵', '잠의 질이 더 낮았어요', '불면도 더 심했어요'),
       ('😰', '불안할수록 더 자주', '불안·우울 점수가 더 높았어요'),
       ('💭', '스트레스 받을 때 더 많대요', '본인들은 잠 부족보다 ‘감정적 스트레스’ 때를 꼽았어요')]
rrows = ''.join(f'''<div style="display: flex; align-items: flex-start; gap: 26px; background: #FFFFFF; border-radius: 20px; padding: 30px 36px">
<div style="font-size: 50px; width: 64px; text-align: center; flex-shrink: 0">{e}</div>
<div style="display: flex; flex-direction: column; gap: 8px"><div style="font-size: 38px; font-weight: 700">{t}</div><div style="font-size: 29px; line-height: 1.45; color: #5F646B">{d}</div></div>
</div>''' for e, t, d in res)
write('P24-4-Result.dc.html', '결과', page(4, 6, f'자주 움찔하는 사람의\n{acc("공통점")} 3가지', f'''
{card(rrows)}
<div style="font-size: 28px; line-height: 1.5; color: #5F646B">설문 연구라 ‘움찔이 원인’인지 ‘결과’인지는 아직 몰라요.</div>''', SD))

steps = [('잠들기 1~2시간 전', '따뜻한 샤워', '40~42.5°C · 연구 13개에서 평균 10분 빨리 잠듦'),
         ('1~2시간 전부터', '조명·화면 줄이기', '수면 전문의 조언'),
         ('누워서', '긴장 풀기', '호흡·스트레칭 등 – 연구진이 꼽은 후보, 효과는 아직 검증 전')]
prow = ''.join(f'''<div style="display: flex; align-items: center; gap: 28px; background: #FFFFFF; border-radius: 20px; padding: 30px 38px">
<div style="font-family: {GOTHIC}; font-size: 50px; font-weight: 800; color: {{{{accent}}}}; width: 50px; flex-shrink: 0">{i}</div>
<div style="display: flex; flex-direction: column; gap: 6px"><div style="font-size: 28px; font-weight: 700; color: #5F646B">{a}</div><div style="font-family: {GOTHIC}; font-size: 46px; font-weight: 800">{b}</div><div style="font-size: 27px; color: #5F646B">{c}</div></div>
</div>''' for i, (a, b, c) in enumerate(steps, 1))
write('P24-5-Tonight.dc.html', '오늘 밤', page(5, 6, f'오늘 밤 {acc("덜 움찔")}하려면', f'''
{card(prow)}''', '출처: Haghayegh 외(2019) · HELLO!(2026.08.27) · Grünberger 외(2026)'))

trows = ''.join(f'''<div style="display: flex; gap: 22px; align-items: flex-start; text-align: left"><div style="font-family: {GOTHIC}; font-size: 40px; font-weight: 800; color: {Y}; width: 40px; flex-shrink: 0">{i}</div><div style="font-size: 34px; line-height: 1.45">{t}</div></div>''' for i, t in enumerate(["움찔은 대부분 무해해요", "자주 움찔한다면 요즘 스트레스 체크", "자기 1~2시간 전 따뜻한 샤워"], 1))
write('P24-6-Closing.dc.html', '마무리', closing('움찔, 이것만 기억해요', trows,
      '자다가 움찔하는 친구한테 공유 📌', '여러분은 언제 제일 움찔하나요? 💬'))
