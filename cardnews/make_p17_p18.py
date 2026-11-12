"""No.17(르 쁘띠 마르세예) · No.18(먹는 스킨케어) 카드뉴스 .dc.html 만들기 (2026-11-12)."""
import os

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'project')
LOGO_W = '/_blob/11234708ce8dd667817c59a15d245c81'
LOGO_C = '/_blob/291cad6575aa62613f2a8a37dce482f8'
Y = '#FFE14A'
FONT = "'Noto Sans KR', 'Apple SD Gothic Neo', sans-serif"
GOTHIC = "'Gothic A1', 'Noto Sans KR', sans-serif"
HELMET = ('<helmet>\n<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Gothic+A1:wght@700;800'
          '&amp;family=Noto+Sans+KR:wght@400;500;700;900&amp;display=swap">\n<style>\nbody{margin:0}\na{color:inherit}\n</style>\n</helmet>')
SCRIPT = ('<script type="text/x-dc" data-dc-script data-props=\'{"accent":{"editor":"color","default":"#1B3FEF",'
          '"options":["#1B3FEF","#8A4B3C","#3D4F8A","#17191C"]},"$preview":{"width":1080,"height":1350}}\'>\n'
          'class Component extends DCLogic {\nrenderVals() {\nreturn { accent: this.props.accent ?? \'#1B3FEF\' };\n}\n}\n</script>')


def write(name, title, body):
    html = (f'<!doctype html>\n<html lang="ko">\n<head>\n<meta charset="utf-8">\n<title>{title}</title>\n'
            f'<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n{HELMET}\n{body}\n</x-dc>\n{SCRIPT}\n</body>\n</html>\n')
    open(os.path.join(P, name), 'w', encoding='utf-8').write(html)
    print(name)


def cover(no, img, pos, title_html):
    return f'''<div style="position: relative; width: 1080px; height: 1350px; overflow: hidden; background: #111315; color: #FFFFFF; font-family: {FONT}; word-break: keep-all">
<img src="{img}" alt="" style="position: absolute; left: 0; top: 0; width: 1080px; height: 1350px; object-fit: cover; object-position: {pos}; display: block">
<div style="position: absolute; left: 0; right: 0; bottom: 0; height: 860px; background: linear-gradient(180deg, rgba(10,12,14,0) 0%, rgba(10,12,14,0.6) 38%, rgba(10,12,14,0.92) 78%)"></div>
<h1 style="position: absolute; left: 72px; right: 72px; bottom: 150px; margin: 0; font-family: {FONT}; font-size: 124px; font-weight: 900; line-height: 1.18; letter-spacing: -0.045em; color: #FFFFFF; text-shadow: 0 4px 24px rgba(0,0,0,0.45); white-space: pre-line">{title_html}</h1>
<img src="{LOGO_W}" alt="have a shower 로고" style="position: absolute; left: 72px; bottom: 64px; height: 56px; display: block">
<div style="position: absolute; right: 72px; bottom: 78px; font-size: 26px; font-weight: 700; letter-spacing: 0.08em; color: rgba(255,255,255,0.75)">No.{no}</div>
</div>'''


def page(num, total, h2, inner, src):
    return f'''<div style="width: 1080px; height: 1350px; box-sizing: border-box; padding: 72px; display: flex; flex-direction: column; gap: 36px; background: #F6F2E8; color: #17191C; font-family: {FONT}; word-break: keep-all; overflow: hidden">
<div style="display: flex; justify-content: space-between; align-items: center; font-size: 26px; font-weight: 700; letter-spacing: 0.12em">
<div style="color: {{{{accent}}}}">HAVE A SHOWER</div>
<div style="color: #5F646B; letter-spacing: 0.04em">{num:02d} / {total:02d}</div>
</div>
<h2 style="margin: 0; font-family: {GOTHIC}; font-size: 62px; font-weight: 800; line-height: 1.25; letter-spacing: -0.02em; white-space: pre-line">{h2}</h2>
{inner}
<div style="margin-top: auto; display: flex; justify-content: space-between; gap: 24px; font-size: 23px; color: #5F646B">
<div>@have.a.shower</div>
<div style="text-align: right">{src}</div>
</div>
</div>'''


def bullets(items, size=36):
    rows = ''.join(f'''<div style="display: flex; gap: 18px; align-items: flex-start">
<div style="width: 10px; height: 10px; border-radius: 5px; margin-top: {int(size*0.45)}px; flex-shrink: 0; background: {{{{accent}}}}"></div>
<div style="font-size: {size}px; line-height: 1.5">{t}</div>
</div>''' for t in items)
    return f'<div style="display: flex; flex-direction: column; gap: 20px">{rows}</div>'


def bigbox(label, big, size=96):
    return f'''<div style="background: {{{{accent}}}}; border-radius: 20px; padding: 44px 52px; display: flex; flex-direction: column; gap: 14px"><div style="font-size: 30px; font-weight: 700; color: rgba(255,255,255,0.85)">{label}</div><div style="font-family: {GOTHIC}; font-size: {size}px; font-weight: 800; line-height: 1.15; letter-spacing: -0.03em; color: {Y}">{big}</div></div>'''


def acc(t):
    return f'<span style="color: {{{{accent}}}}">{t}</span>'


def yl(t):
    return f'<span style="color: {Y}">{t}</span>'


# ───────── No.17 르 쁘띠 마르세예 (5장) ─────────
S17 = '출처: CMN(2026.11.09) · 원다컴퍼니'
write('P17-1-Cover.dc.html', '르 쁘띠 마르세예 커버',
      cover(17, '/_blob/38545f4ca8ce68b2b861d4d6bc861935', '50% 30%', f'프랑스 8년 연속\n{yl("1위")} 바디워시,\n한국 왔다'))

write('P17-2-What.dc.html', '뭐가 들어왔나', page(2, 5, f'프랑스 국민 바디워시\n{acc("르 쁘띠 마르세예")}', f'''
<div style="height: 400px; border-radius: 20px; overflow: hidden; background: #EDE6F7"><img src="/_blob/66465d299e8a4921eca2984f00682573" alt="르 쁘띠 마르세예 바디워시 5종" style="width: 100%; height: 100%; object-fit: cover; object-position: 50% 62%; display: block"></div>
{bullets(["프랑스 마트·드럭스토어에서 직구해 오던 그 사각 병이에요", "원다컴퍼니가 국내 독점 유통 계약을 맺고 공식 판매를 시작했어요", "바디워시 5종 + 핸드워시 3종으로 먼저 들어왔어요"], 34)}
<div style="background: #FFFFFF; border-radius: 20px; padding: 30px 40px; font-size: 34px; font-weight: 700; line-height: 1.45">샤워할 때 나는? {acc("A. 향이 먼저")} vs {acc("B. 거품이 먼저")}</div>''', S17))

write('P17-3-Story.dc.html', '왜 1위인가', page(3, 5, f'마르세유 비누 한 조각이\n{acc("40년 1위 브랜드")}가 되기까지', f'''
<div style="display: flex; flex-direction: column; gap: 22px">
''' + ''.join(f'''<div style="display: flex; gap: 32px; align-items: flex-start; background: #FFFFFF; border-radius: 20px; padding: 32px 40px">
<div style="font-family: {GOTHIC}; font-size: 46px; font-weight: 800; line-height: 1.15; color: {{{{accent}}}}; flex-shrink: 0; width: 150px">{y}</div>
<div style="font-size: 33px; line-height: 1.5">{t}</div>
</div>''' for y, t in [
    ('1984', '전통 마르세유 비누를 작은 큐브로 만들고 ‘작은 마르세유 비누’라는 이름을 붙였어요'),
    ('2008', '프랑스 샤워 시장점유율 첫 1위'),
    ('지금', '닐슨 2024년 조사 기준 프랑스 샤워·비누 점유율 1위, 최근 8년 연속 샤워 1위'),
]) + f'''
</div>
{bigbox("프랑스 샤워 카테고리", "8년 연속 1위", 104)}''', '출처: CMN(2026.11.09) · 닐슨(2024) 회사 발표'))

scents = [
    ('#F2B8C6', '체리 블라썸', '플로럴', '은은한 꽃향이 좋다면'),
    ('#F3D58A', '바닐라', '달콤하고 포근한 향', '자기 전 포근한 잔향'),
    ('#8FD8CF', '티아레 플라워', '이국적인 꽃 향', '휴양지 기분 내고 싶을 때'),
    ('#7FA3D9', '소나무 & 씨펜넬', '청량한 마린 우디', '깔끔한 향을 좋아한다면'),
    ('#E9E07A', '버베나 & 레몬', '상큼한 시트러스', '아침 샤워로 잠 깨기'),
]
rows = ''.join(f'''<div style="display: flex; align-items: center; gap: 26px; background: #FFFFFF; border-radius: 18px; padding: 30px 34px">
<div style="width: 26px; height: 80px; border-radius: 8px; flex-shrink: 0; background: {c}"></div>
<div style="display: flex; flex-direction: column; gap: 4px; flex: 1">
<div style="font-size: 36px; font-weight: 700">{n} <span style="font-size: 28px; font-weight: 500; color: #5F646B">· {d}</span></div>
<div style="font-size: 29px; color: #3A3E44">→ {w}</div>
</div>
</div>''' for c, n, d, w in scents)
write('P17-4-Scents.dc.html', '향 5종', page(4, 5, f'바디워시 5종,\n{acc("나한테 맞는 향은?")}',
      f'<div style="display: flex; flex-direction: column; gap: 22px">{rows}</div>',
      '향 설명: CMN(2026.11.09) · → 추천: have.a.shower 에디터'))

write('P17-5-Where.dc.html', '어디서 사나', page(5, 5, f'어디서, {acc("얼마에")} 사요?', f'''
<div style="display: flex; gap: 24px">
''' + ''.join(f'''<div style="flex: 1; background: #FFFFFF; border-radius: 20px; padding: 28px; display: flex; flex-direction: column; gap: 14px; align-items: center; text-align: center">
<img src="{im}" alt="" style="width: 260px; height: 260px; object-fit: contain; display: block">
<div style="font-size: 30px; font-weight: 700; line-height: 1.35">{n}</div>
<div style="font-family: {GOTHIC}; font-size: 54px; font-weight: 800; color: {{{{accent}}}}">{p}</div>
</div>''' for im, n, p in [
    ('/_blob/7d3a8f05593f16af2c66a9ec7f039b40', '바디워시 650ml<br>(바닐라)', '16,800원'),
    ('/_blob/3dc545c62c19a8b70df237dbd1136cd2', '핸드워시 300ml<br>(올리브)', '14,800원'),
]) + f'''
</div>
{bullets(["매장: 롯데백화점 콘란샵 6개점", "온라인: 네이버 스마트스토어 '르쁘띠마르세예'"], 34)}
<div style="background: {{{{accent}}}}; color: #FFFFFF; border-radius: 20px; padding: 32px 40px; font-size: 33px; font-weight: 700; line-height: 1.5">바디워시 바꿀 때 꺼내 보게 저장해 두세요 📌<br><span style="color: {Y}">어떤 향부터 써 볼래요? 댓글로 알려주세요</span></div>''',
      '가격: 공식 스마트스토어 기준 · 출처: CMN(2026.11.09)'))

# ───────── No.18 먹는 스킨케어 (6장) ─────────
S18 = '출처: The Optimist Daily(2026.11.09)'
write('P18-1-Cover.dc.html', '먹는 스킨케어 커버',
      cover(18, '/_blob/89ff3c819832d466d9e2b9c99b16a8e7', '50% 35%', f'{yl("먹는 선크림")},\n진짜 있을까?\n의사 답은'))

write('P18-2-Trend.dc.html', '틱톡 유행', page(2, 6, f'미국 틱톡에서 뜬\n{acc("‘먹는 스킨케어’")}', f'''
{bullets(["세럼 대신 음식으로 피부를 관리한다는 영상이 넘쳐요", "연어를 많이 먹기 시작해서 보톡스 예약을 취소했다는 사람까지 나왔어요", "더 나가서 ‘먹는 선크림’이라는 말도 돌아요"], 36)}
<div style="height: 360px; border-radius: 20px; overflow: hidden"><img src="/_blob/5f09fa729943e9f77bfcab43fdac2bfc" alt="연어·달걀·아보카도 토스트" style="width: 100%; height: 100%; object-fit: cover; object-position: 50% 82%; display: block"></div>
<div style="background: #FFFFFF; border-radius: 20px; padding: 30px 40px; font-size: 34px; font-weight: 700; line-height: 1.45">피부에 돈 쓴다면 나는?<br>{acc("A. 세럼 하나 더")} vs {acc("B. 연어·아보카도 장보기")}</div>''', S18))

write('P18-3-Tank.dc.html', '탱크 채우기', page(3, 6, f'음식은 {acc("‘탱크 채우기’")}\n넘치게 먹어도 빨라지지 않아요', f'''
{bullets(["“주름과 콜라겐 감소는 원인이 여러 가지예요. 식단 전체가 부실하거나 햇빛을 많이 받으면, 음식·영양제 하나로 큰 차이는 안 나요”", "비타민C·아미노산은 콜라겐을, 지방산은 피부 장벽을 도와요. 부족한 걸 채우는 역할이에요", "“채워 넣는 건 필요하지만, 넘치게 넣는다고 콜라겐 공장이 더 빨리 돌지 않아요”"], 35)}
{bigbox("비타민C를 너무 많이 먹으면", "위장 문제 · 일부는 신장결석 위험", 62)}''',
      '피부과 전문의 Kseniya Kobets · ' + S18))

write('P18-4-Sunscreen.dc.html', '먹는 선크림', page(4, 6, f'{acc("‘먹는 선크림’")}은 없어요', f'''
{bullets(["카로티노이드·폴리페놀·폴리포디움 추출물이 자외선 손상을 버티게 돕는다는 연구는 있어요", "“추가 방어막 정도지, 먹는 선크림은 절대 아니에요”", "블루베리·녹차·항산화 영양제를 아무리 먹어도 선크림·옷·햇빛 피하는 습관을 대신하지 못해요"], 36)}
{bigbox("겨울에도 그대로", "선크림은 바르고, 덧바르기", 76)}''',
      '피부과 전문의 Kseniya Kobets · ' + S18))

foods = ['달걀', '아보카도', '아마씨', '호두', '연어', '다크초콜릿']
grid = ''.join(f'''<div style="background: #FFFFFF; border-radius: 18px; padding: 30px 20px; text-align: center; font-family: {GOTHIC}; font-size: 44px; font-weight: 800">{f}</div>''' for f in foods)
write('P18-5-List.dc.html', '장보기 6가지', page(5, 6, f'피부과 의사가 꼽은\n{acc("장보기 6가지")}', f'''
<div style="height: 330px; border-radius: 20px; overflow: hidden"><img src="/_blob/dcd836e727cdc49738cfc7bc72a60a79" alt="달걀과 아보카도" style="width: 100%; height: 100%; object-fit: cover; object-position: 50% 50%; display: block"></div>
<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 16px">{grid}</div>
<div style="font-size: 33px; line-height: 1.5">단백질 · 좋은 지방 · 오메가3 · 항산화 성분을 골고루 채워요.<br>“몸 전체 대사 건강에 좋은 게 피부에도 좋아요”</div>''',
      '피부과 전문의 Sapna Palep · Kseniya Kobets · ' + S18))

todo = ''.join(f'''<div style="display: flex; gap: 22px; align-items: flex-start; text-align: left"><div style="font-family: {GOTHIC}; font-size: 40px; font-weight: 800; color: {Y}; width: 40px; flex-shrink: 0">{i}</div><div style="font-size: 35px; line-height: 1.45">{t}</div></div>''' for i, t in enumerate(["음식은 '부족한 것 채우기'로", "선크림·보습 루틴은 그대로", "이번 장보기에 6가지 중 2개만"], 1))
write('P18-6-Closing.dc.html', '마무리', f'''<div style="width: 1080px; height: 1350px; box-sizing: border-box; padding: 80px 72px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 44px; background: #1B3FEF; color: #FBF7EC; font-family: {FONT}; text-align: center; word-break: keep-all; overflow: hidden">
<div style="font-family: {GOTHIC}; font-size: 56px; font-weight: 800; line-height: 1.3">오늘부터 이렇게</div>
<div style="display: flex; flex-direction: column; gap: 22px; background: rgba(255,255,255,0.1); border-radius: 22px; padding: 40px 48px; align-self: stretch">{todo}</div>
<div style="font-size: 32px; line-height: 1.55">장 보러 갈 때 꺼내 보게 저장해 두세요 📌</div>
<img src="{LOGO_C}" alt="have a shower 로고" style="width: 380px; display: block">
<div style="font-size: 30px; line-height: 1.6; white-space: pre-line">몸을 돌보는 시간에 대한 연구, 매일 전해요</div>
<div style="font-size: 30px; font-weight: 700; color: {Y}">여러분은 세럼파? 장보기파? 댓글로 알려주세요</div>
</div>''')
