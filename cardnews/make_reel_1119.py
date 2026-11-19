"""11/19 릴스: 냄새 좋아지는 제품 추천 (46cm 바디워시 + 11월 향 신상).
v2(대표 피드백): 진한 파랑 배경 → 연한 하늘·크림, 46cm 2장 → 1장, 센녹은 얼굴 없이 제품만.
사용: python3 cardnews/make_reel_1119.py <출력폴더> [음악파일명]   예) m_carefree.mp3
결과: <출력폴더>/r1119.mp4 (1080x1920, 30fps)
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import make_reels_1118 as M

ROOT = M.ROOT
D19 = os.path.join(ROOT, 'briefs/images/2026-11-19')
CO, CR, INK, PINK = M.CO, M.CR, M.INK, M.PINK
SKY = '#BFE6F7'      # 46cm 사진 배경과 같은 하늘색
SKY2 = '#DDF1FA'     # 마무리 카드용 연한 하늘
GRAY = '#5F646B'


def img(n):
    return 'file://' + os.path.join(D19, n)


def b(t):
    return f'<span style="color:{CO}">{t}</span>'


def cover():
    return f'''<div style="position:absolute;inset:0;background:{SKY}"></div>
<img src="{img('product_46cm_1.jpg')}" style="position:absolute;left:0;top:300px;width:1080px;height:760px;object-fit:cover;object-position:50% 70%">
<div style="position:absolute;left:0;right:0;top:900px;bottom:0;background:linear-gradient(180deg,rgba(191,230,247,0) 0%,{SKY} 16%)"></div>
<img src="{M.LOGO_C}" style="position:absolute;left:50%;top:230px;transform:translateX(-50%);height:58px;filter:brightness(0);opacity:.8">
<div style="position:absolute;left:80px;right:160px;top:1060px;color:{INK}">
<div style="display:inline-block;padding:12px 26px;border-radius:40px;background:{PINK};color:{INK};font-size:34px;font-weight:800">골라드림</div>
<h1 style="margin:30px 0 0;font-size:112px;font-weight:900;line-height:1.15">{b('냄새')} 좋아지는<br>제품 추천</h1>
<div style="margin-top:26px;font-size:42px;font-weight:600;line-height:1.4;color:#33373D">샤워부터 손끝까지, 3개만 골랐어요</div>
</div>
<div style="position:absolute;left:80px;bottom:385px;font-size:22px;color:rgba(23,25,28,.5)">사진: LG생활건강 보도자료(뉴스와이어)</div>'''


def card46():
    li = lambda a, s: f'''<div style="display:flex;gap:20px;align-items:flex-start;margin-top:22px">
<div style="flex-shrink:0;width:14px;height:14px;margin-top:20px;border-radius:7px;background:{CO}"></div>
<div><div style="font-size:44px;font-weight:900;line-height:1.25">{a}</div><div style="margin-top:4px;font-size:30px;font-weight:600;color:{GRAY};line-height:1.4">{s}</div></div></div>'''
    return M.card(CR, INK, f'''<div style="width:100%;height:400px;border-radius:36px;overflow:hidden;background:{SKY}">
<img src="{img('product_46cm_1.jpg')}" style="width:100%;height:100%;object-fit:cover;object-position:50% 60%"></div>
<div style="margin-top:26px;font-size:30px;font-weight:800;color:{CO};letter-spacing:.06em">01 / 03 · 46cm 데오드란트 바디워시</div>
<div style="margin-top:6px;display:flex;align-items:baseline;gap:18px;flex-wrap:wrap">
<div style="font-size:54px;font-weight:800">한 번 쓰면 체취</div>
<div style="font-size:150px;font-weight:900;line-height:1;letter-spacing:-0.05em;color:{CO}">97%</div>
<div style="font-size:64px;font-weight:900">개선</div></div>
{li('효과 ' + b('48시간') + ' 지속', '피부를 약산성으로 유지하는 특허 기술')}
{li('별명 \'발을씻자 몸 버전\'', '발을씻자 연구진이 만들었대요 · 최근 그린티 향 추가')}
{li('누적 ' + b('130만 개'), '하루 평균 2,000개 넘게 팔렸어요')}''',
        '출처: LG생활건강 발표(아시아경제 2026-11-17) · 97%·48시간은 회사 설명 · 사진: 뉴스와이어', '체취 바디워시')


def prod(i, pic, pos, fit, brand, name, big, lines, src, bg='#fff', blur=False):
    back = f'<img src="{img(pic)}" style="position:absolute;inset:-40px;width:calc(100% + 80px);height:calc(100% + 80px);object-fit:cover;filter:blur(28px) brightness(.85)">' if blur else ''
    body = f'''<div style="position:relative;width:100%;height:760px;border-radius:36px;overflow:hidden;background:{bg}">{back}
<img src="{img(pic)}" style="position:relative;width:100%;height:100%;object-fit:{fit};object-position:{pos}"></div>
<div style="margin-top:34px;font-size:30px;font-weight:800;color:{CO};letter-spacing:.06em">{i:02d} / 03 · {brand}</div>
<div style="margin-top:8px;font-size:62px;font-weight:900;line-height:1.15">{name}</div>
<div style="margin-top:14px;font-size:46px;font-weight:800;color:{CO};line-height:1.3">{big}</div>
<div style="margin-top:14px;font-size:34px;font-weight:600;color:{GRAY};line-height:1.5">{lines}</div>'''
    return M.card(CR, INK, body, src, '11월 향 신상')


def closing():
    return M.card(SKY2, INK, f'''<div style="font-size:44px;font-weight:700;color:{GRAY}">씻을 때 체취 잡고 → 손끝에 향</div>
<div style="margin-top:20px;font-size:100px;font-weight:900;line-height:1.2">저장해두고<br>{b('올영 갈 때')}<br>꺼내 보세요</div>
<div style="margin-top:56px;font-size:44px;font-weight:600;line-height:1.5">'냄새 좋다' 소리 들은 템 있어요?<br>댓글로 알려주세요</div>
<img src="{M.LOGO_C}" style="margin-top:64px;height:56px;align-self:flex-start;filter:brightness(0);opacity:.8">''', '', '')


def scenes():
    return [
        dict(d=2.4, html=cover()),
        dict(d=3.4, html=card46()),
        dict(d=2.4, html=prod(2, 'product_snk_bottle.jpg', '50% 50%', 'contain', '센녹', '노 모어 키스',
             '\'말랑머스크\' 향',
             '플럼·무화과 → 화이트로즈·매그놀리아 → 머스크<br>11월 올영픽 기획세트, 첫날 조기 품절(회사 발표)',
             '출처: 스페셜타임스·위키트리(2026-10-29) · 사진: 뉴스에이(화보 일부)', bg='#26305E', blur=True)),
        dict(d=2.4, html=prod(3, 'product_loegp_1.jpg', '50% 50%', 'contain', '로에', '레이지 바닐라 핸드크림',
             '라떼 바닐라 향',
             '끈적이지 않는 새틴 같은 보습<br>11월 신상 · 50ml (사진은 같은 향 향수)',
             '출처: 얼루어 코리아(2026-11-12) · 사진: 글로우픽')),
        dict(d=2.6, html=closing()),
    ]


if __name__ == '__main__':
    out = sys.argv[1]
    music = sys.argv[2] if len(sys.argv) > 2 else None
    M.IMGD = os.path.join(ROOT, 'briefs/images/2026-11-18')  # 음악 파일 위치
    os.makedirs(out, exist_ok=True)
    M.build('r1119', scenes(), out, music)
