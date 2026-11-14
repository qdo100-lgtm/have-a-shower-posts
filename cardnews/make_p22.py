"""No.22 수능 전날 샤워·수면 (7장, 11/14 18:00 루틴·과학) 카드뉴스 .dc.html 만들기 (2026-11-14).
공통 함수는 make_p17_p18.py 앞부분을 그대로 씀.
표지 문구 바꾸기: python3 cardnews/make_p22.py 22A  (22A/22B/22C, 기본 C)
"""
import os
import sys

_src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'make_p17_p18.py'), encoding='utf-8').read()
exec(_src.split('# ───────── No.17')[0])

pick = {a[:2]: a[2:] for a in sys.argv[1:]}

COVER = '/_blob/55a627e0c082588fb6f7e1d4716f316c'   # Unsplash bruce mars, 세로 크롭
STEAM = '/_blob/aa885ee38caf06747531b8c4885c95b9'   # Pixabay erikaferencz48 (No.20에서 쓴 김 나는 온탕)
S1 = '출처: Haghayegh 외, Sleep Medicine Reviews(2019) · 텍사스대 오스틴'
S2 = '출처: Tai 외, J Clin Sleep Med(2021) · Haghayegh 외(2019)'
S3 = '출처: 경북매일 ‘D-7 수능’(2026.11.10)'

C22 = {
    'A': f'수능 전날\n잠 빨리 드는\n{yl("샤워 시간")}',
    'B': f'수능 전날 밤\n{yl("90분")} 전에\n씻으세요',
    'C': f'잠드는 시간\n{yl("10분")} 줄이는\n수능 전날 샤워',
}
write('P22-1-Cover.dc.html', '수능 전날 샤워 커버',
      cover(22, COVER, '50% 30%', C22[pick.get('22', 'C')]))

write('P22-2-Question.dc.html', '질문', page(2, 7, '수능 전날 밤, 나라면?', f'''
<div style="display: flex; flex-direction: column; gap: 20px">
<div style="background: #FFFFFF; border-radius: 20px; padding: 40px 44px; font-size: 44px; font-weight: 700">A. {acc("자기 직전")}에 샤워</div>
<div style="background: #FFFFFF; border-radius: 20px; padding: 40px 44px; font-size: 44px; font-weight: 700">B. 자기 {acc("1~2시간 전")}에 샤워</div>
</div>
{bullets(["미국 텍사스대 오스틴 연구팀이 ‘자기 전 따뜻한 샤워·목욕’ 연구 5,322건을 살펴봤어요", "조건에 맞는 17개를 골라, 그중 13개의 데이터를 한데 모아 다시 분석했어요(메타분석)", "정답은 다음 장에서 👉"], 35)}''', S1))

write('P22-3-Why.dc.html', '원리', page(3, 7, f'따뜻하게 씻으면\n{acc("몸속 온도")}가 내려가요', f'''
<div style="height: 380px; border-radius: 20px; overflow: hidden"><img src="{STEAM}" alt="김이 나는 따뜻한 물" style="width: 100%; height: 100%; object-fit: cover; object-position: 50% 45%; display: block"></div>
{bullets(["따뜻한 물이 피를 손발 쪽으로 보내요", "손발로 열이 빠져나가면서 몸속 온도가 내려가요", "몸속 온도가 내려가는 건 우리 몸이 잠들 준비를 하는 자연스러운 신호예요"], 36)}''', S2))

write('P22-4-Number.dc.html', '숫자', page(4, 7, f'정답은 B.\n{acc("1~2시간 전")}이었어요', f'''
{bigbox("잠들기 1~2시간 전, 40~42.5°C 물로 샤워·목욕했을 때", "평균 10분 더 빨리 잠들었어요", 84)}
<div style="display: flex; gap: 30px; align-items: center; background: #FFFFFF; border-radius: 20px; padding: 30px 38px">
<div style="font-family: {GOTHIC}; font-size: 60px; font-weight: 800; color: {{{{accent}}}}; width: 230px; flex-shrink: 0">약 90분</div>
<div style="font-size: 32px; line-height: 1.5">연구팀이 가장 좋은 때로 꼽은 시간이에요</div>
</div>
<div style="font-size: 30px; line-height: 1.5; color: #5F646B">연구 13개의 데이터를 모아 본 결과예요. 씻는 ‘때’가 중요하다는 뜻이에요.</div>''', S1))

steps = [('언제', '잠들기 1~2시간 전', '밤 11시에 잔다면 9시 반쯤'),
         ('몇 도', '40~42.5°C', '따뜻하다고 느끼는 정도'),
         ('얼마나', '10분 이상', '몸이 충분히 데워질 만큼')]
srows = ''.join(f'''<div style="display: flex; align-items: center; gap: 28px; background: #FFFFFF; border-radius: 20px; padding: 30px 38px">
<div style="font-family: {GOTHIC}; font-size: 50px; font-weight: 800; color: {{{{accent}}}}; width: 60px; flex-shrink: 0">{i}</div>
<div style="width: 150px; flex-shrink: 0; font-size: 32px; font-weight: 700; color: #5F646B">{a}</div>
<div style="display: flex; flex-direction: column; gap: 6px"><div style="font-family: {GOTHIC}; font-size: 44px; font-weight: 800">{b}</div><div style="font-size: 28px; color: #5F646B">{c}</div></div>
</div>''' for i, (a, b, c) in enumerate(steps, 1))
write('P22-5-HowTo.dc.html', '따라 하기', page(5, 7, f'수능 전날 밤\n{acc("이렇게")} 씻어요', f'''
<div style="display: flex; flex-direction: column; gap: 20px">{srows}</div>
<div style="font-size: 29px; line-height: 1.5; color: #5F646B">샤워든 목욕이든 괜찮아요. ‘10분 이상’은 평균 72세 1,094명을 측정한 연구(Tai 2021) 기준이에요.</div>''', S2))

morning = [('⏰', '1교시는 오전 8시 40분', '그 시간에 맞춰 일어나는 시간을 미리 정해 두기'),
           ('🍚', '식사·잠은 평소처럼', '규칙적인 식사와 충분한 수면으로 컨디션 유지'),
           ('💊', '안 먹던 약은 그날 처음 먹지 않기', '우황청심환·안정제 등 임의 복용은 부작용 우려')]
mrows = ''.join(f'''<div style="display: flex; align-items: flex-start; gap: 26px; background: #FFFFFF; border-radius: 20px; padding: 30px 36px">
<div style="font-size: 48px; width: 64px; text-align: center; flex-shrink: 0">{e}</div>
<div style="display: flex; flex-direction: column; gap: 8px"><div style="font-size: 37px; font-weight: 700">{t}</div><div style="font-size: 29px; line-height: 1.45; color: #5F646B">{d}</div></div>
</div>''' for e, t, d in morning)
write('P22-6-Morning.dc.html', '당일 아침', page(6, 7, f'그리고 {acc("당일 아침")}엔', f'''
<div style="display: flex; flex-direction: column; gap: 20px">{mrows}</div>''', S3))

todo = ''.join(f'''<div style="display: flex; gap: 22px; align-items: flex-start; text-align: left"><div style="font-family: {GOTHIC}; font-size: 40px; font-weight: 800; color: {Y}; width: 40px; flex-shrink: 0">{i}</div><div style="font-size: 35px; line-height: 1.45">{t}</div></div>''' for i, t in enumerate(["자기 1~2시간 전 따뜻한 샤워", "40~42.5°C로 10분 이상", "아침 8시 40분에 맞춰 기상"], 1))
write('P22-7-Closing.dc.html', '마무리', f'''<div style="width: 1080px; height: 1350px; box-sizing: border-box; padding: 80px 72px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 44px; background: #1B3FEF; color: #FBF7EC; font-family: {FONT}; text-align: center; word-break: keep-all; overflow: hidden">
<div style="font-family: {GOTHIC}; font-size: 56px; font-weight: 800; line-height: 1.3">수능 전날 밤, 이것만</div>
<div style="display: flex; flex-direction: column; gap: 22px; background: rgba(255,255,255,0.1); border-radius: 22px; padding: 40px 48px; align-self: stretch">{todo}</div>
<div style="font-size: 32px; line-height: 1.55">수험생 가족·친구에게 공유해 주세요 📌</div>
<img src="{LOGO_C}" alt="have a shower 로고" style="width: 380px; display: block">
<div style="font-size: 30px; line-height: 1.6; white-space: pre-line">몸을 돌보는 시간에 대한 연구, 매일 전해요</div>
<div style="font-size: 30px; font-weight: 700; color: {Y}">수험생에게 응원 한마디 남겨 주세요 💙</div>
</div>''')
