"""No.27 🔍 진짜일까?: "1시간 일찍 잠들면 8주에 약 0.6kg" – NYU 연구 (6장, 11/18 11:30 피드)
공통 함수는 make_p17_p18.py, closing/crow 는 make_p25_p26.py 와 같은 모양.
표지 문구 바꾸기: python3 cardnews/make_p27.py B  (기본 A)
"""
import os
import sys

_dir = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(_dir, 'make_p17_p18.py'), encoding='utf-8').read().split('# ───────── No.17')[0])
_s = open(os.path.join(_dir, 'make_p25_p26.py'), encoding='utf-8').read()
exec(_s[_s.index('def card('):_s.index('def item(')])

COVER = '/_blob/8719478b82f0a596a52a4527cbeee693'
SRC = '출처: NYU 간호대 · Nursing Research(2026) · EurekAlert(2026.11.02)'

C = {
    'A': (f'일찍 자면\n{yl("살")}이 빠진다?', '같은 시간을 자도? 196명 · 8주 연구'),
    'B': (f'1시간 일찍 자면\n{yl("0.6kg")}?', '잠 길이보다 ‘잠드는 시간’이 중요하대요'),
    'C': (f'몇 시에 자느냐가\n{yl("몸무게")}랑 관련?', '뉴욕대 196명 · 8주 연구, 진짜일까?'),
}
t, s = C[(sys.argv[1:] or ['A'])[0]]
write('P27-1-Cover.dc.html', '일찍 자면 커버', cover3(27, COVER, '50% 30%', '진짜일까?', t, s, '사진: Pixabay(Pexels)'))

vs = f'''<div style="display: flex; gap: 20px">
<div style="flex: 1; background: #FFFFFF; border-radius: 22px; padding: 36px 30px; display: flex; flex-direction: column; gap: 12px"><div style="font-family: {GOTHIC}; font-size: 72px; font-weight: 800; color: {{{{accent}}}}">A</div><div style="font-size: 40px; font-weight: 800; line-height: 1.3">밤 1시 잠들고<br>아침 8시 기상</div><div style="font-size: 28px; color: #5F646B">7시간</div></div>
<div style="flex: 1; background: #FFFFFF; border-radius: 22px; padding: 36px 30px; display: flex; flex-direction: column; gap: 12px"><div style="font-family: {GOTHIC}; font-size: 72px; font-weight: 800; color: {{{{accent}}}}">B</div><div style="font-size: 40px; font-weight: 800; line-height: 1.3">밤 12시 잠들고<br>아침 7시 기상</div><div style="font-size: 28px; color: #5F646B">7시간</div></div>
</div>'''
write('P27-2-Question.dc.html', '질문', page(2, 6, f'똑같이 7시간 자면\n{acc("A vs B")}, 차이 있을까?', f'''
{vs}
{bullets(["뉴욕대(NYU) 간호대 연구팀이 확인해 봤어요", "대상: 당뇨 전 단계 성인 <b>196명</b>(21~64세), 평소 잠이 6.5시간 안 되는 사람들", "8주 동안 생활습관 프로그램 – 절반은 ‘수면 코칭’까지 받음"], 31)}''', SRC))

write('P27-3-Result.dc.html', '결과', page(3, 6, f'결과: 잠든 시각이\n{acc("1시간 빠를수록")}', f'''
{bigbox("8주 동안 체중 변화(참가자 전체 분석)", "약 0.6kg↓", 128)}
{bullets(["원문: 1시간 일찍 잠들 때마다 약 1.3파운드(0.6kg) 감소와 관련", "<b>잠잔 시간과 상관없이</b> 나타난 연결이에요", "두 그룹 모두 체중은 줄었지만, 혈당은 둘 다 변화가 없었어요"], 31)}''', SRC))

why = [('1', '야식이 줄어요', '“일찍 잠들면 늦은 밤 먹는 걸 줄일 수 있어요” – 말론 교수'),
       ('2', '밤에 빛을 덜 봐요', '늦게까지 화면·조명에 덜 노출'),
       ('3', '식욕 호르몬', '긴장(교감신경)과 배고픔 호르몬(그렐린)이 낮아질 수 있음')]
wrows = ''.join(f'''<div style="display: flex; align-items: center; gap: 28px; background: #FFFFFF; border-radius: 20px; padding: 30px 38px">
<div style="font-family: {GOTHIC}; font-size: 56px; font-weight: 800; color: {{{{accent}}}}; width: 50px; flex-shrink: 0">{n}</div>
<div style="display: flex; flex-direction: column; gap: 6px"><div style="font-family: {GOTHIC}; font-size: 42px; font-weight: 800">{a}</div><div style="font-size: 28px; line-height: 1.4; color: #5F646B">{b}</div></div>
</div>''' for n, a, b in why)
write('P27-4-Why.dc.html', '왜', page(4, 6, f'왜 그럴까?\n{acc("연구팀의 추측")} 3가지', f'''
{card(wrows)}
<div style="font-size: 28px; line-height: 1.5; color: #5F646B">※ 이 3가지는 연구에서 직접 확인한 게 아니라 ‘가능한 이유’예요</div>''', SRC))

judge = [('⭕', '일찍 잠드는 것과 체중 감소는 <b>관련</b>이 있었어요'),
         ('🔺', '일찍 자서 빠진 건지(원인)는 <b>아직 몰라요</b> – 8주 · 196명 · 당뇨 전 단계'),
         ('❌', '“늦게 자도 시간만 채우면 똑같다”고 말하긴 어려워요')]
jrows = ''.join(f'''<div style="display: flex; gap: 24px; align-items: flex-start; background: #FFFFFF; border-radius: 20px; padding: 30px 36px"><div style="font-size: 52px; line-height: 1">{e}</div><div style="font-size: 33px; line-height: 1.45">{t}</div></div>''' for e, t in judge)
write('P27-5-Judge.dc.html', '판정', page(5, 6, f'그래서 판정은\n{acc("🔺 반쯤 진짜")}', f'''
{card(jrows)}
<div style="font-size: 28px; line-height: 1.5; color: #5F646B">“언제 잠드느냐 – 얼마나 자느냐만이 아니라 – 가 중요하지만 놓치고 있던 요소” – 수전 말론 교수</div>''', SRC))

write('P27-6-Closing.dc.html', '마무리', closing('오늘 밤 1시간 당기기', crow([
    '한 번에 말고 조금씩 – 연구 코칭도 ‘점점 당기기’',
    '침대는 잠만 자는 곳 – 폰은 침대 밖에',
    '잠들기 1~2시간 전 따뜻한 샤워(No.01 근거)']),
    '새벽 2시에 자는 친구 소환 📌 저장해두고 오늘 밤 해봐요', '보통 몇 시에 잠드세요? 💬'))
