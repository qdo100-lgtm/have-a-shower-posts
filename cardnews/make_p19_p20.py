"""No.19(그래비티 퀵 드라이 샴푸) · No.20(운동 후 냉탕 vs 온탕) 카드뉴스 .dc.html 만들기 (2026-11-13).
공통 함수(write, cover, page, bullets, bigbox, acc, yl)는 make_p17_p18.py 앞부분을 그대로 씀.
표지 문구 바꾸기: python3 cardnews/make_p19_p20.py 19B  (19A/19B/19C, 20A/20B/20C)
"""
import os
import sys

_src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'make_p17_p18.py'), encoding='utf-8').read()
exec(_src.split('# ───────── No.17')[0])

pick = {a[:2]: a[2:] for a in sys.argv[1:]}

# ───────── No.19 그래비티 퀵 드라이 샴푸 (5장, 12:00 뉴스) ─────────
S19 = '출처: 스포츠월드·한국경제(2026.11.12) · 사진: 그래비티 제공'
C19 = {
    'A': f'머리 말리기\n{yl("1.9배")} 빨라진\n샴푸 나왔다',
    'B': f'말리기 싫어서\n{yl("안 감은 적")}\n있죠?',
    'C': f'{yl("24분")} 만에\n품절된 샴푸,\n뭐가 달라?',
}
write('P19-1-Cover.dc.html', '퀵 드라이 샴푸 커버',
      cover(19, '/_blob/3e0a339ed6344ddbbe08e3067de06fe3', '50% 22%', C19[pick.get('19', 'A')]))

write('P19-2-What.dc.html', '뭐가 나왔나', page(2, 5, f'감기만 해도 빨리 마르는\n{acc("‘퀵 드라이 샴푸’")}', f'''
<div style="height: 420px; border-radius: 20px; overflow: hidden; background: #E9EBEE"><img src="/_blob/eafcb01b05f46978d3e1e828f0574bc3" alt="그래비티 퀵 드라이 샴푸" style="width: 100%; height: 100%; object-fit: cover; object-position: 50% 45%; display: block"></div>
{bullets(["카이스트 이해신 교수팀 기술로 만든 그래비티 신제품이 11월 12일 정식 출시됐어요", "11월 5일 올리브영 선출시 때 준비한 물량이 24분 만에 품절됐어요", "드라이어가 아니라 ‘샴푸’로 말리는 시간을 줄이겠다는 제품이에요"], 34)}
<div style="background: #FFFFFF; border-radius: 20px; padding: 30px 40px; font-size: 34px; font-weight: 700; line-height: 1.45">말리기 귀찮은 날 나는?<br>{acc("A. 덜 말리고 그냥 잔다")} vs {acc("B. 아예 안 감는다")}</div>''', S19))

write('P19-3-Why.dc.html', '왜 빨리 마르나', page(3, 5, f'물이 머리카락에\n{acc("맺혀 흘러내리게")}', f'''
{bullets(["폴리페놀 기반 기술 ‘DryMax 609™’가 머리카락 표면에 얇은 막을 만들어요", "남은 물기가 스며들지 않고 방울로 맺혀 흘러내리게 해서, 말리는 시간을 줄이는 원리예요", "식약처에 ‘탈모 증상 완화’ 기능성 화장품으로 보고된 제품이에요"], 35)}
<div style="display: flex; gap: 28px; align-items: stretch">
<div style="width: 300px; flex-shrink: 0; border-radius: 20px; overflow: hidden"><img src="/_blob/953b35a21f7d60a2b2f89a71d98cac37" alt="그래비티 퀵 드라이 샴푸와 실험 도구" style="width: 100%; height: 100%; object-fit: cover; object-position: 50% 30%; display: block"></div>
<div style="flex: 1; background: #FFFFFF; border-radius: 20px; padding: 34px 38px; display: flex; flex-direction: column; gap: 16px">
<div style="font-size: 32px; line-height: 1.55">“머리카락이 마르는 과정은 단순히 드라이어의 성능만으로 결정되는 것이 아니라, 모발 표면에 수분이 어떻게 머물고 빠져나가는지와도 밀접하게 관련돼 있어요”</div>
<div style="font-size: 27px; font-weight: 700; color: {{{{accent}}}}">이해신 KAIST 석좌교수</div>
</div>
</div>''', S19))

stats = [
    ('70명 / 100명', '머리 말리기 귀찮아서 머리 감기를 미루거나 건너뛴 적 있다 (여성 100명 조사)'),
    ('23.56%↑', '사용 후 뿌리 볼륨 개선, 22명 중 21명이 “빨리 마른다” 체감 (인체적용시험)'),
]
srows = ''.join(f'''<div style="display: flex; gap: 30px; align-items: center; background: #FFFFFF; border-radius: 20px; padding: 30px 38px">
<div style="font-family: {GOTHIC}; font-size: 50px; font-weight: 800; color: {{{{accent}}}}; width: 330px; flex-shrink: 0; letter-spacing: -0.02em">{n}</div>
<div style="font-size: 31px; line-height: 1.5">{t}</div>
</div>''' for n, t in stats)
write('P19-4-Number.dc.html', '숫자로 보면', page(4, 5, f'숫자로 보면\n{acc("얼마나")} 빨라요?', f'''
{bigbox("2분 30초~5분 말렸을 때 겉수분 감소 · 56.14% vs 기존 29.46%", "1.9배 더 빨리", 104)}
<div style="display: flex; flex-direction: column; gap: 20px">{srows}</div>
<div style="font-size: 28px; line-height: 1.5; color: #5F646B">※ 회사가 의뢰한 시험이에요. 건조 속도는 사람 머리가 아닌 모발 묶음으로 쟀어요(PNK피부임상연구센터).</div>''', S19))

write('P19-5-Where.dc.html', '어디서 사나', page(5, 5, f'어디서, {acc("얼마에")} 사요?', f'''
<div style="display: flex; gap: 30px; align-items: center; background: #FFFFFF; border-radius: 20px; padding: 30px 40px">
<img src="/_blob/fc5ec16f7e4bfa5f7acf3d1ffca8bbe7" alt="그래비티 퀵 드라이 샴푸" style="width: 300px; height: 300px; object-fit: cover; object-position: 25% 50%; border-radius: 14px; display: block">
<div style="display: flex; flex-direction: column; gap: 12px">
<div style="font-size: 34px; font-weight: 700; line-height: 1.35">그래비티<br>퀵 드라이 샴푸 350ml</div>
<div style="font-family: {GOTHIC}; font-size: 64px; font-weight: 800; color: {{{{accent}}}}">28,000원</div>
</div>
</div>
{bullets(["판매처: 올리브영 · 그래비티 공식몰 등", "쓰는 법: 미온수로 두피·모발을 충분히 적신 뒤 마사지하고 깨끗이 헹구기", "탈모 ‘치료’가 아니라 ‘증상 완화’ 기능성이에요"], 33)}
<div style="background: {{{{accent}}}}; color: #FFFFFF; border-radius: 20px; padding: 32px 40px; font-size: 33px; font-weight: 700; line-height: 1.5">샴푸 바꿀 때 꺼내 보게 저장해 두세요 📌<br><span style="color: {Y}">여러분은 머리 말리는 데 몇 분 걸려요?</span></div>''',
      '가격: 그래비티 공식몰(11/13 확인) · 한국경제(2026.11.12)'))

# ───────── No.20 운동 후 냉탕 vs 온탕 (8장, 18:00 루틴·과학) ─────────
S20 = '출처: Freya Bayne, 영국 이스트런던대(The Conversation, 2026.11.12)'
C20 = {
    'A': f'운동 끝나고\n냉탕 vs {yl("온탕")},\n뭐가 나을까?',
    'B': f'운동 후 {yl("냉탕")},\n40명에게\n시켜봤더니',
    'C': f'근육통 vs {yl("회복")}\n정답이\n달랐어요',
}
write('P20-1-Cover.dc.html', '냉탕 온탕 커버',
      cover(20, '/_blob/6092733fc9fe1049e072d39ca79a9801', '62% 40%', C20[pick.get('20', 'A')]))

def half(emoji, label, temp, bg):
    return f'''<div style="flex: 1; display: flex; flex-direction: column; gap: 14px">
<div style="height: 380px; border-radius: 20px; background: {bg}; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 10px"><div style="font-size: 120px; line-height: 1">{emoji}</div><div style="font-family: {GOTHIC}; font-size: 72px; font-weight: 800; color: #FFFFFF">{temp}</div></div>
<div style="font-family: {GOTHIC}; font-size: 40px; font-weight: 800; text-align: center">{label}</div>
</div>'''

write('P20-2-Question.dc.html', '질문', page(2, 8, f'운동 끝나고 나는?', f'''
<div style="display: flex; gap: 24px">{half("❄️", f'A. {acc("얼음물")} 냉탕', "10°C", "#5B8DEF")}{half("♨️", f'B. {acc("뜨끈한")} 온탕', "42°C", "#E8613C")}</div>
{bullets(["영국 이스트런던대 연구팀이 활동적인 성인 40명(남 31·여 9)으로 직접 비교했어요", "허벅지 앞 근육이 뻐근해지는 운동을 시킨 뒤, 회복 방법만 달리해서 72시간 지켜봤어요"], 34)}''', S20))

groups = [('❄️', '찬물에 몸 담그기', '10°C'), ('♨️', '따뜻한 물에 몸 담그기', '42°C'),
          ('🔥', '뜨거운 공기 (사우나식)', '60°C'), ('🪑', '그냥 앉아서 쉬기', '30분')]
grows = ''.join(f'''<div style="display: flex; align-items: center; gap: 28px; background: #FFFFFF; border-radius: 20px; padding: 30px 38px">
<div style="font-size: 54px; width: 70px; text-align: center; flex-shrink: 0">{e}</div>
<div style="flex: 1; font-size: 36px; font-weight: 700">{n}</div>
<div style="font-family: {GOTHIC}; font-size: 50px; font-weight: 800; color: {{{{accent}}}}">{t}</div>
</div>''' for e, n, t in groups)
write('P20-3-Groups.dc.html', '4가지 방법', page(3, 8, f'이렇게 {acc("4그룹")}으로 나눴어요', f'''
<div style="display: flex; flex-direction: column; gap: 20px">{grows}</div>
<div style="font-size: 32px; line-height: 1.5">그룹마다 10명씩. 근력·근육통·몸속 회복 지표를 72시간 동안 쟀어요.</div>''', S20))

write('P20-4-Strength.dc.html', '결과1 근력', page(4, 8, f'결과 ① 힘이 돌아오는 속도는\n{acc("거의 같았어요")}', f'''
<div style="background: #FFFFFF; border-radius: 20px; padding: 40px 44px; display: flex; flex-direction: column; gap: 30px">
<div style="font-size: 30px; font-weight: 700; color: #5F646B">72시간 뒤, 운동 전 근력의 몇 %까지 돌아왔나</div>
''' + ''.join(f'''<div style="display: flex; align-items: center; gap: 24px">
<div style="width: 250px; flex-shrink: 0; font-size: 34px; font-weight: 700">{n}</div>
<div style="flex: 1; height: 56px; background: #ECE7DA; border-radius: 12px; overflow: hidden"><div style="width: {w}%; height: 100%; background: {c}; border-radius: 12px"></div></div>
<div style="width: 170px; text-align: right; font-family: {GOTHIC}; font-size: 46px; font-weight: 800; color: {{{{accent}}}}">{t}</div>
</div>''' for n, w, c, t in [('❄️ 찬물', 82, '#8FB3F5', '약 82%'), ('♨️🔥🪑 나머지', 88.5, '{{accent}}', '88~89%')]) + f'''
</div>
{bullets(["어떤 방법도 다른 방법보다 근력을 ‘확실히 더 빨리’ 돌려놓지는 못했어요", "찬물 그룹이 숫자로는 조금 낮았지만, 의미 있는 차이로 보기는 어려웠어요"], 36)}''', S20))

write('P20-5-Soreness.dc.html', '결과2 근육통', page(5, 8, f'결과 ② 덜 아픈 느낌은\n{acc("찬물이 1등")}', f'''
{bigbox("❄️ 찬물 그룹", "느끼는 근육통 ↓ 가장 많이", 76)}
{bullets(["찬물에 담근 그룹이 ‘느끼는 근육통’을 가장 잘 줄였어요", "하지만 몸속 회복 지표(근육 손상·염증)는 찬물에서 좋아지지 않았어요", "아픈 느낌을 줄여 주는 것과, 몸이 회복하는 것은 다를 수 있다는 뜻이에요"], 35)}''', S20))

write('P20-6-Heat.dc.html', '결과3 온열', page(6, 8, f'결과 ③ 몸속 회복 신호는\n{acc("따뜻한 쪽")}이 좋았어요', f'''
{bigbox("♨️ 42°C 따뜻한 물 그룹", "열충격단백질(HSP72) ↑", 76)}
{bullets(["온열(따뜻한 물·뜨거운 공기) 그룹이 근육 손상·염증 지표 변화가 더 좋았어요", "42°C 물에 담근 그룹은 ‘열충격단백질(HSP72)’이 더 높았어요. 몸이 열 스트레스에 반응해 세포를 지키려고 만드는 단백질이에요"], 35)}''', S20))

choice = [('오늘 다리가 너무 아프다', '❄️ 찬물', '덜 아프게'), ('몸 회복을 돕고 싶다', '♨️ 따뜻한 물·사우나', '회복 지표'),
          ('둘 다 어렵다', '🪑 30분 쉬기', '근력 회복은 비슷')]
crows = ''.join(f'''<div style="display: flex; align-items: center; gap: 24px; background: #FFFFFF; border-radius: 20px; padding: 28px 34px">
<div style="flex: 1; font-size: 33px; line-height: 1.4">{s}</div>
<div style="font-size: 30px; color: #5F646B">→</div>
<div style="width: 330px; flex-shrink: 0"><div style="font-family: {GOTHIC}; font-size: 38px; font-weight: 800; color: {{{{accent}}}}">{c}</div><div style="font-size: 26px; color: #5F646B">{w}</div></div>
</div>''' for s, c, w in choice)
write('P20-7-Choose.dc.html', '목적별 선택표', page(7, 8, f'그래서 나는 뭘?\n{acc("목적별 선택표")}', f'''
<div style="display: flex; flex-direction: column; gap: 18px">{crows}</div>
<div style="background: #FFFFFF; border-left: 10px solid {{{{accent}}}}; border-radius: 12px; padding: 26px 32px; font-size: 29px; line-height: 1.55">그룹당 10명인 작은 연구예요. 담그는 시간은 공개되지 않았어요.<br>심장·혈압 문제가 있다면 냉탕·온탕 전에 의료진과 먼저 상의하세요.</div>''',
      '연구자 결론 요약: ' + S20 + ' · 선택표: have.a.shower 에디터'))

todo = ''.join(f'''<div style="display: flex; gap: 22px; align-items: flex-start; text-align: left"><div style="font-family: {GOTHIC}; font-size: 40px; font-weight: 800; color: {Y}; width: 40px; flex-shrink: 0">{i}</div><div style="font-size: 35px; line-height: 1.45">{t}</div></div>''' for i, t in enumerate(["너무 아픈 날엔 찬물로 진정", "회복이 목적이면 따뜻한 물·사우나", "뭐든 무리하지 말고 내 몸 상태 먼저"], 1))
write('P20-8-Closing.dc.html', '마무리', f'''<div style="width: 1080px; height: 1350px; box-sizing: border-box; padding: 80px 72px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 44px; background: #1B3FEF; color: #FBF7EC; font-family: {FONT}; text-align: center; word-break: keep-all; overflow: hidden">
<div style="font-family: {GOTHIC}; font-size: 56px; font-weight: 800; line-height: 1.3">운동 끝나고 이렇게</div>
<div style="display: flex; flex-direction: column; gap: 22px; background: rgba(255,255,255,0.1); border-radius: 22px; padding: 40px 48px; align-self: stretch">{todo}</div>
<div style="font-size: 32px; line-height: 1.55">운동 가방 챙길 때 꺼내 보게 저장해 두세요 📌</div>
<img src="{LOGO_C}" alt="have a shower 로고" style="width: 380px; display: block">
<div style="font-size: 30px; line-height: 1.6; white-space: pre-line">몸을 돌보는 시간에 대한 연구, 매일 전해요</div>
<div style="font-size: 30px; font-weight: 700; color: {Y}">여러분은 운동 후 냉탕파? 온탕파?</div>
</div>''')
