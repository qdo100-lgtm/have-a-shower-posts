"""11/19 릴스: 냄새 좋아지는 제품 추천 (46cm 바디워시 + 11월 향 신상).
사용: python3 cardnews/make_reel_1119.py <출력폴더> [음악파일명]   예) m_carefree.mp3
결과: <출력폴더>/r1119.mp4 (1080x1920, 30fps)
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import make_reels_1118 as M

ROOT = M.ROOT
D19 = os.path.join(ROOT, 'briefs/images/2026-11-19')
CO, CR, Y, INK, PINK = M.CO, M.CR, M.Y, M.INK, M.PINK
SKY = '#BFE6F7'


def img(n):
    return 'file://' + os.path.join(D19, n)


def hl(t, c=Y):
    return f'<span style="color:{c}">{t}</span>'


def cover():
    return f'''<div style="position:absolute;inset:0;background:{SKY}"></div>
<img src="{img('product_46cm_1.jpg')}" style="position:absolute;left:0;top:300px;width:1080px;height:760px;object-fit:cover;object-position:50% 70%">
<div style="position:absolute;left:0;right:0;top:820px;bottom:0;background:linear-gradient(180deg,rgba(27,63,239,0) 0%,{CO} 22%)"></div>
<img src="{M.LOGO_C}" style="position:absolute;left:50%;top:230px;transform:translateX(-50%);height:58px;filter:brightness(0);opacity:.8">
<div style="position:absolute;left:80px;right:160px;top:1040px;color:#fff">
<div style="display:inline-block;padding:12px 26px;border-radius:40px;background:{PINK};color:{INK};font-size:34px;font-weight:800">골라드림</div>
<h1 style="margin:30px 0 0;font-size:112px;font-weight:900;line-height:1.15">{hl('냄새')} 좋아지는<br>제품 추천</h1>
<div style="margin-top:26px;font-size:42px;font-weight:600;line-height:1.4;color:rgba(255,255,255,.92)">샤워부터 손끝까지, 3개만 골랐어요</div>
</div>
<div style="position:absolute;left:80px;bottom:385px;font-size:22px;color:rgba(255,255,255,.6)">사진: LG생활건강 보도자료(뉴스와이어)</div>'''


def big97():
    return M.card(CO, '#fff', f'''<div style="font-size:40px;font-weight:800;color:{Y};letter-spacing:.04em">01 · 46cm 데오드란트 바디워시</div>
<div style="margin-top:30px;font-size:60px;font-weight:800;line-height:1.3">한 번 썼더니 체취</div>
<div style="font-size:300px;font-weight:900;line-height:1;letter-spacing:-0.05em;color:{Y}">97%</div>
<div style="font-size:84px;font-weight:900;line-height:1.1">개선</div>
<div style="margin-top:40px;font-size:38px;font-weight:600;line-height:1.5;opacity:.9">별명이 '발을씻자 몸 버전'<br>(발을씻자 연구진이 만들었대요)</div>''',
        '출처: LG생활건강 발표(아시아경제 2026-11-17) · 97%·48시간은 회사 설명', '')


def feat46():
    li = lambda a, b: f'''<div style="display:flex;gap:22px;align-items:flex-start;margin-top:34px">
<div style="flex-shrink:0;width:16px;height:16px;margin-top:22px;border-radius:8px;background:{CO}"></div>
<div><div style="font-size:52px;font-weight:900;line-height:1.25">{a}</div><div style="margin-top:6px;font-size:34px;font-weight:600;color:#5F646B;line-height:1.4">{b}</div></div></div>'''
    return M.card(CR, INK, f'''<div style="width:100%;height:470px;border-radius:36px;overflow:hidden;background:{SKY}">
<img src="{img('product_46cm_1.jpg')}" style="width:100%;height:100%;object-fit:cover;object-position:50% 62%"></div>
<div style="margin-top:20px;font-size:30px;font-weight:800;color:{CO};letter-spacing:.06em">01 / 03 · 46cm</div>
{li('효과 <span style="color:'+CO+'">48시간</span> 지속', '피부를 약산성으로 유지해 체취를 잡는 특허 기술')}
{li('누적 <span style="color:'+CO+'">130만 개</span>', '하루 평균 2,000개 넘게 팔렸어요')}
{li('최근 그린티 향 추가', '이름 46cm = 사람 사이 \'친밀한 거리\'')}''',
        '출처: LG생활건강 발표(아시아경제 2026-11-17) · 사진: 뉴스와이어', '체취 바디워시')


def prod(i, pic, pos, fit, brand, name, big, lines, src, bg='#fff'):
    body = f'''<div style="width:100%;height:760px;border-radius:36px;overflow:hidden;background:{bg}">
<img src="{img(pic)}" style="width:100%;height:100%;object-fit:{fit};object-position:{pos}"></div>
<div style="margin-top:34px;font-size:30px;font-weight:800;color:{CO};letter-spacing:.06em">{i:02d} / 03 · {brand}</div>
<div style="margin-top:8px;font-size:62px;font-weight:900;line-height:1.15">{name}</div>
<div style="margin-top:14px;font-size:46px;font-weight:800;color:{CO};line-height:1.3">{big}</div>
<div style="margin-top:14px;font-size:34px;font-weight:600;color:#5F646B;line-height:1.5">{lines}</div>'''
    return M.card(CR, INK, body, src, '11월 향 신상')


def closing():
    return M.card(CO, '#fff', f'''<div style="font-size:44px;font-weight:700;opacity:.85">씻을 때 체취 잡고 → 손끝에 향</div>
<div style="margin-top:20px;font-size:100px;font-weight:900;line-height:1.2">저장해두고<br>{hl('올영 갈 때')}<br>꺼내 보세요</div>
<div style="margin-top:56px;font-size:44px;font-weight:600;line-height:1.5">'냄새 좋다' 소리 들은 템 있어요?<br>댓글로 알려주세요</div>
<img src="{M.LOGO_W}" style="margin-top:64px;height:56px;align-self:flex-start">''', '', '')


def scenes():
    return [
        dict(d=2.4, html=cover()),
        dict(d=2.6, html=big97()),
        dict(d=2.6, html=feat46()),
        dict(d=2.4, html=prod(2, 'product_sennok_1.jpg', '50% 30%', 'cover', '센녹', '노 모어 키스',
             '\'말랑머스크\' 향',
             '플럼·무화과 → 화이트로즈·매그놀리아 → 머스크<br>11월 올영픽 기획세트, 첫날 조기 품절(회사 발표)',
             '출처: 스페셜타임스·위키트리(2026-10-29) · 사진: 에스콰이어 화보(엔하이픈 선우)')),
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
