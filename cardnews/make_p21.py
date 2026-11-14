"""No.21 윤아 가방 속 관리템 3가지 (5장, 11/14 12:00 뉴스) 카드뉴스 .dc.html 만들기 (2026-11-14).
공통 함수는 make_p17_p18.py 앞부분을 그대로 씀.
표지 문구 바꾸기: python3 cardnews/make_p21.py 21B  (21A/21B/21C)
"""
import os
import sys

_src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'make_p17_p18.py'), encoding='utf-8').read()
exec(_src.split('# ───────── No.17')[0])

pick = {a[:2]: a[2:] for a in sys.argv[1:]}

COVER = '/_blob/4cc92d63d397dc718225927ac33b7ae6'   # W KOREA 영상 캡처(엑스포츠뉴스 게재본) 세로 크롭, 자막 아래 잘라냄
ITEMS = '/_blob/e3cf614282c34a1222cfcc64ab04cc87'   # W KOREA 영상 대표 이미지 속 아이템 부분
S21 = '출처: W KOREA 유튜브(2026.11.10) · OSEN · 엑스포츠뉴스 · 사진: W KOREA 유튜브 캡처'

C21 = {
    'A': f'윤아 가방에\n늘 있는\n{yl("관리템 3")}',
    'B': f'“{yl("한 번만")} 해줘도\n컨디션이\n좋아진다”',
    'C': f'36세 윤아가\n매일 챙기는\n{yl("이것")}',
}
write('P21-1-Cover.dc.html', '윤아 가방 커버',
      cover(21, COVER, '50% 0%', C21[pick.get('21', 'A')]))


def quote(text, who='윤아', size=36):
    return f'''<div style="background: #FFFFFF; border-radius: 20px; padding: 36px 42px; display: flex; flex-direction: column; gap: 16px">
<div style="font-size: {size}px; line-height: 1.55">“{text}”</div>
<div style="font-size: 27px; font-weight: 700; color: {{{{accent}}}}">{who}</div>
</div>'''


write('P21-2-What.dc.html', '가방 속 3가지', page(2, 5, f'윤아 가방 속\n{acc("몸 챙기는 템 3가지")}', f'''
<div style="height: 470px; border-radius: 20px; overflow: hidden; background: #111315"><img src="{ITEMS}" alt="윤아 가방 속 아이템" style="width: 100%; height: 100%; object-fit: cover; object-position: 50% 60%; display: block"></div>
{bullets(["11월 10일 W KOREA 유튜브 ‘인 마이 백’에서 윤아가 가방 속을 직접 공개했어요", "카메라·대본 사이에 들어 있던 몸 관리템은 스트레칭 밴드 · 괄사 · 마스크팩"], 34)}
<div style="background: #FFFFFF; border-radius: 20px; padding: 30px 40px; font-size: 34px; font-weight: 700; line-height: 1.45">하루 종일 앉아 있다 굳은 몸, 나는?<br>{acc("A. 그냥 버틴다")} vs {acc("B. 1분이라도 편다")}</div>''', S21))

write('P21-3-Band.dc.html', '스트레칭 밴드', page(3, 5, f'① 분홍 스트레칭 밴드\n“{acc("번쩍 만세")}로 풀어요”', f'''
{quote("이건 진짜 요즘 꼭 들고 다닌다. 가장 좋아하는 번쩍 만세를 해서 풀어준다. 한 번만 해줘도 컨디션이 좋아진다", size=40)}
{quote("항상 이런 아이템들을 갖고 오면 핑크를 하게 되는 것 같다", size=34)}
{bullets(["스트레칭 밴드는 고무처럼 늘어나는 얇은 운동용 끈이에요", "접으면 손바닥만 해서 가방·파우치에 넣고 다니기 좋아요"], 34)}''', S21))

write('P21-4-Guasha.dc.html', '괄사와 마스크팩', page(4, 5, f'② 괄사 · ③ 마스크팩\n{acc("들고 다니기 편한 것")}만', f'''
<div style="display: flex; gap: 24px; align-items: stretch">
<div style="flex: 1; background: #FFFFFF; border-radius: 20px; padding: 34px 36px; display: flex; flex-direction: column; gap: 16px">
<div style="font-family: {GOTHIC}; font-size: 40px; font-weight: 800; color: {{{{accent}}}}">괄사</div>
<div style="font-size: 33px; line-height: 1.55">“혈액순환을 풀어준다. 간편하고 들고 다니기 편하다”</div>
</div>
<div style="flex: 1; background: #FFFFFF; border-radius: 20px; padding: 34px 36px; display: flex; flex-direction: column; gap: 16px">
<div style="font-family: {GOTHIC}; font-size: 40px; font-weight: 800; color: {{{{accent}}}}">마스크팩</div>
<div style="font-size: 33px; line-height: 1.55">“요즘에는 팩을 하루에 한 번씩은 꼭 하려고 하는 그런 습관이 생겼다. 해외 갈 때도 챙긴다”</div>
</div>
</div>
{quote("저는 오늘 깨달았어요. 저는 미니멀리스트다. 작고 아기자기한 필수템들만 있다", size=36)}
<div style="font-size: 28px; line-height: 1.5; color: #5F646B">※ 모두 윤아가 영상에서 직접 한 말이에요.</div>''', S21))

items = [('스트레칭 밴드', '앉아 있다 굳은 어깨·등, 팔 위로 쭉 펴기'),
         ('괄사', '손바닥만 한 크기, 파우치에 쏙'),
         ('시트 마스크', '하루 한 장, 여행 갈 때도')]
irows = ''.join(f'''<div style="display: flex; gap: 26px; align-items: center; background: #FFFFFF; border-radius: 20px; padding: 26px 36px">
<div style="font-family: {GOTHIC}; font-size: 44px; font-weight: 800; color: {{{{accent}}}}; width: 50px; flex-shrink: 0">{i}</div>
<div style="display: flex; flex-direction: column; gap: 6px"><div style="font-size: 36px; font-weight: 700">{n}</div><div style="font-size: 29px; color: #5F646B">{t}</div></div>
</div>''' for i, (n, t) in enumerate(items, 1))
write('P21-5-List.dc.html', '내 가방에 넣기', page(5, 5, f'내 가방에도 {acc("3가지")}', f'''
<div style="display: flex; flex-direction: column; gap: 18px">{irows}</div>
<div style="background: #FFFFFF; border-left: 10px solid {{{{accent}}}}; border-radius: 12px; padding: 24px 32px; font-size: 29px; line-height: 1.5">새로 나와요 · 자주 ‘마사지 쿨링 괄사’ 11월 17일 출시<br>냉장 보관해 얼굴·몸에 쓰는 괄사예요</div>
<div style="background: {{{{accent}}}}; color: #FFFFFF; border-radius: 20px; padding: 30px 40px; font-size: 33px; font-weight: 700; line-height: 1.5">가방 정리할 때 꺼내 보게 저장해 두세요 📌<br><span style="color: {Y}">여러분 가방에 꼭 있는 관리템은?</span></div>''',
      'W KOREA 유튜브(2026.11.10) · 자주 신제품: 아시아경제(2026.11.11)'))
