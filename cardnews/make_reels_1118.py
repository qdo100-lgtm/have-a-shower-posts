"""11/18 릴스 2편 (촬영 없이: 모션 카드 + 무료 영상).
R1 = 겨울 '가려움' 바디로션 골라드림 / R2 = 샤워 전 7분 (7일 따라하기)
사용: python3 cardnews/make_reels_1118.py <출력폴더> [r1] [r2]
결과: <출력폴더>/r1.mp4, r2.mp4 (1080x1920, 30fps, 무음 오디오 트랙 포함)
"""
import os, sys, subprocess
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMGD = os.path.join(ROOT, 'briefs/images/2026-11-18')
LOGO_W = 'file://' + os.path.join(ROOT, 'cardnews/img/logo_white.png')
LOGO_C = 'file://' + os.path.join(ROOT, 'cardnews/img/logo_cream.png')
FONT = "'Noto Sans CJK KR', sans-serif"
CO, CR, Y, INK = '#1B3FEF', '#F6F2E8', '#FFE14A', '#17191C'
PINK, YEL = '#FFB8D9', '#FFE14A'
W, H = 1080, 1920
MUSIC_START = {'m_funkorama.mp3': 6}  # 곡별 시작 위치(초)
# 릴스 화면 안전 구역: 위 220px, 아래 420px, 오른쪽 140px 피하기
BASE = f"*{{box-sizing:border-box}} body{{margin:0;width:{W}px;height:{H}px;font-family:{FONT};word-break:keep-all;letter-spacing:-0.03em}}"


def img(name):
    return 'file://' + os.path.join(IMGD, name)


def hl(t, c=Y):
    return f'<span style="color:{c}">{t}</span>'


# ---------- 레이어 HTML ----------
def hook(tag, tagc, title, sub, credit):
    """영상 위 첫 장면(투명 배경)."""
    return f'''<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,12,14,.55) 0%,rgba(10,12,14,.1) 30%,rgba(10,12,14,.35) 55%,rgba(10,12,14,.9) 100%)"></div>
<img src="{LOGO_W}" style="position:absolute;left:50%;top:250px;transform:translateX(-50%);height:58px">
<div style="position:absolute;left:80px;right:160px;top:860px;color:#fff">
<div style="display:inline-block;padding:12px 26px;border-radius:40px;background:{tagc};color:{INK};font-size:34px;font-weight:800">{tag}</div>
<h1 style="margin:34px 0 0;font-size:104px;font-weight:900;line-height:1.18;white-space:pre-line;text-shadow:0 4px 22px rgba(0,0,0,.45)">{title}</h1>
<div style="margin-top:30px;font-size:40px;font-weight:600;line-height:1.4;color:rgba(255,255,255,.92)">{sub}</div>
</div>
<div style="position:absolute;left:80px;bottom:440px;font-size:22px;color:rgba(255,255,255,.6)">{credit}</div>'''


def card(bg, color, body, src='', page=''):
    """색 배경 카드(불투명)."""
    sub = 'rgba(255,255,255,.7)' if color == '#fff' else '#5F646B'
    logo = LOGO_W if color == '#fff' else LOGO_C
    return f'''<div style="position:absolute;inset:0;background:{bg};color:{color}">
<div style="position:absolute;left:80px;right:80px;top:250px;display:flex;justify-content:space-between;align-items:center;font-size:28px;font-weight:800;letter-spacing:.12em">
<div style="color:{Y if color == '#fff' else CO}">HAVE A SHOWER</div><div style="color:{sub};letter-spacing:.04em">{page}</div></div>
<div style="position:absolute;left:80px;right:160px;top:400px;bottom:440px;display:flex;flex-direction:column;justify-content:center">{body}</div>
<div style="position:absolute;left:80px;right:160px;bottom:380px;font-size:22px;color:{sub};text-align:left">{src}</div>
</div>'''


def product(i, n, pimg, name, size, before, after, note, badge=''):
    badge_html = f'<div style="position:absolute;right:30px;top:30px;padding:10px 22px;border-radius:30px;background:#E5484D;color:#fff;font-size:30px;font-weight:800">{badge}</div>' if badge else ''
    price = (f'<span style="font-size:36px;color:#8A8F96;text-decoration:line-through;font-weight:600">{before}</span> '
             f'<span style="font-size:76px;font-weight:900;color:{CO}">{after}</span>') if before else \
            f'<span style="font-size:76px;font-weight:900;color:{CO}">{after}</span>'
    body = f'''<div style="position:relative;width:640px;height:640px;margin:0 auto;border-radius:36px;background:#fff;box-shadow:0 18px 50px rgba(0,0,0,.08);overflow:hidden">
<img src="{pimg}" style="width:100%;height:100%;object-fit:contain">{badge_html}</div>
<div style="margin-top:46px;font-size:30px;font-weight:800;color:{CO};letter-spacing:.06em">{i:02d} / {n:02d}</div>
<div style="margin-top:10px;font-size:58px;font-weight:900;line-height:1.2">{name}</div>
<div style="margin-top:8px;font-size:34px;color:#5F646B;font-weight:600">{size}</div>
<div style="margin-top:16px;line-height:1.1">{price}</div>
<div style="margin-top:18px;font-size:34px;font-weight:600;line-height:1.4">{note}</div>'''
    return card(CR, INK, body, '올리브영 온라인몰 가격 · 11/18 오전 기준(바뀔 수 있어요)', '겨울 가려움 바디로션')


def move(i, name, how, bg, color):
    """동작 카드: 위쪽(300~1060px)은 비워 두고 동작 애니메이션을 얹음."""
    big = Y if color == '#fff' else CO
    sub = 'rgba(255,255,255,.7)' if color == '#fff' else '#5F646B'
    return f'''<div style="position:absolute;inset:0;background:{bg};color:{color}">
<div style="position:absolute;left:80px;right:80px;top:250px;display:flex;justify-content:space-between;align-items:center;font-size:28px;font-weight:800;letter-spacing:.12em">
<div style="color:{big}">HAVE A SHOWER</div><div style="color:{sub};letter-spacing:.04em">{i} / 7</div></div>
<div style="position:absolute;left:80px;right:160px;top:1075px;display:flex;align-items:center;gap:26px">
<div style="width:110px;height:110px;border-radius:55px;background:{big};color:{bg};display:flex;align-items:center;justify-content:center;font-size:70px;font-weight:900;flex-shrink:0">{i}</div>
<div style="font-size:92px;font-weight:900;line-height:1.1">{name}</div></div>
<div style="position:absolute;left:80px;right:160px;top:1215px;font-size:46px;font-weight:600;line-height:1.42;opacity:.92">{how}</div>
<div style="position:absolute;left:80px;top:1365px;padding:12px 28px;border-radius:50px;border:4px solid {big};font-size:40px;font-weight:800;color:{big}">60초</div>
<div style="position:absolute;left:80px;right:160px;bottom:380px;font-size:22px;color:{sub}">출처: Tom\'s Guide 피트니스 에디터 30일 체험기(2026-11-15)</div>
</div>'''


# ---------- 장면 목록 ----------
def r1():
    S = []
    S.append(dict(video='v_shower_2.mp4', ss=2, d=2.4, html=hook('골라드림', PINK,
        f'겨울만 되면\n정강이 {hl("가려운")} 사람?', '올리브영 바디로션 5개, 가격까지 정리했어요', '영상: Pixabay')))
    S.append(dict(d=2.4, html=card(CO, '#fff', f'''<div style="font-size:44px;font-weight:700;opacity:.85">올리브영엔 아예</div>
<div style="margin-top:14px;font-size:104px;font-weight:900;line-height:1.18">'{hl("가려움")}'<br>기획전이 있어요</div>
<div style="margin-top:50px;font-size:44px;font-weight:600;line-height:1.5">"'가려움' 관련 키워드가<br>겨울철에는 {hl("2배")}나 더 검색"</div>''',
        '출처: 올리브영 기획전 \'겨울철 인기 검색어, 가려움\' 문구', '')))
    P = [
        ('product_physiogel_1.jpg', '피지오겔 DMT 바디로션', '400ml', '33,500원', '25,900원', '지금 <b>일시품절</b>일 만큼 인기', '일시품절'),
        ('product_aestura_1.jpg', '에스트라 아토베리어365 바디로션', '400ml', '33,000원', '28,000원', '피지오겔 품절이면 이걸로', ''),
        ('product_cetaphil_1.jpg', '세타필 모이스춰라이징 로션', '1L 대용량', '25,600원~', '20,900원~', '샤워글로브 증정 · 온 가족용', ''),
        ('product_raybi_1.jpg', '레이비 산양유 바디로션·워시', '대용량 골라담기', '', '22,900원~', '로션·워시 같이 사고 싶을 때', ''),
        ('product_johnsons_1.jpg', '존슨즈베이비 베드타임 로션', '500ml + 500ml', '', '37,400원~', '자기 전에 바르는 순한 로션', ''),
    ]
    for k, p in enumerate(P, 1):
        S.append(dict(d=1.8, html=product(k, len(P), img(p[0]), *p[1:])))
    S.append(dict(d=2.5, html=card(CR, INK, f'''<div style="font-size:44px;font-weight:700;color:#5F646B">근데 뭘 바르냐보다</div>
<div style="margin-top:14px;font-size:104px;font-weight:900;line-height:1.18">샤워 후<br><span style="color:{CO}">3분 안에</span><br>바르기</div>
<div style="margin-top:46px;font-size:40px;font-weight:600;line-height:1.5">씻고 3~4분 안에 피부 수분이<br>크게 떨어졌어요 (15명 작은 연구)</div>''',
        '출처: 미국 OHSU 피부과 연구(Dermatitis, 2025, 15명)', '')))
    S.append(dict(d=2.6, html=card(CO, '#fff', f'''<div style="font-size:96px;font-weight:900;line-height:1.2">저장해두고<br>{hl("올영 갈 때")}<br>꺼내 보세요</div>
<div style="margin-top:56px;font-size:44px;font-weight:600;line-height:1.5">여러분 겨울 최애 로션은?<br>댓글로 알려주세요</div>
<img src="{LOGO_W}" style="margin-top:70px;height:56px;align-self:flex-start">''', '', '')))
    return S


def r2():
    S = []
    S.append(dict(video='v_squat_1.mp4', ss=1, d=2.4, html=hook('7일 따라하기', YEL,
        f'샤워하기 전\n딱 {hl("7분")}', '물 데워지는 동안 동작 7개 × 60초', '영상: Pixabay')))
    S.append(dict(d=2.5, html=card(CR, INK, f'''<div style="font-size:44px;font-weight:700;color:#5F646B">영국 피트니스 에디터가</div>
<div style="margin-top:14px;font-size:100px;font-weight:900;line-height:1.18">샤워 전 7분,<br><span style="color:{CO}">30일</span> 해봤대요</div>
<div style="margin-top:46px;font-size:42px;font-weight:600;line-height:1.55">푸시업 자세가 좋아지고<br>몸이 좀 더 잘 움직였대요<br><span style="color:#5F646B">눈에 띄는 몸 변화는 없었다고 솔직 후기</span></div>''',
        "출처: Tom's Guide (2026-11-15)", '')))
    # 실제 영상(Mixkit 무료 라이선스)이 있는 동작: (파일, 시작초, 가로중심, 세로중심, 확대)
    CLIPS = {'squat': ('mixkit/v_mk52116.mp4', 3.0, 0.56, 0.43, 1.15),
             'pushup': ('mixkit/v_mk24383.mp4', 1.0, 0.5, 0.5, 1.0),
             'lunge': ('mixkit/v_mk52110.mp4', 0.6, 0.58, 0.62, 1.5),
             'situp': ('mixkit/v_mk5355.mp4', 0.0, 0.42, 0.5, 1.0)}
    KEYS = ['squat', 'pushup', 'lunge', 'situp', 'catcow', 'shoulder', 'superman']  # 실제 영상 4개 먼저, 애니메이션 3개 뒤
    M = [('스쿼트', '의자에 앉듯<br>엉덩이를 뒤로'), ('푸시업', '힘들면<br>무릎 대고 해도 OK'),
         ('리버스 런지', '한 발씩 뒤로,<br>양쪽 번갈아'), ('윗몸일으키기', '목 말고<br>배 힘으로'),
         ('캣카우', '네발 자세에서 등을<br>둥글게 ↔ 오목하게'), ('날개뼈 모으기', '양쪽 날개뼈를<br>등 가운데로 꾹'),
         ('슈퍼맨', '엎드려서 팔·다리<br>동시에 들기')]
    for k, (n, h) in enumerate(M, 1):
        bg, c = (CO, '#fff') if k % 2 else (CR, INK)
        sc = dict(d=2.4, html=move(k, n, h, bg, c), anim=KEYS[k - 1], dark=bool(k % 2))
        if KEYS[k - 1] in CLIPS:
            sc['clip'] = CLIPS[KEYS[k - 1]]
        S.append(sc)
    days = ''.join(f'<div style="width:104px;height:150px;border-radius:22px;background:#fff;color:{INK};display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;font-size:36px;font-weight:800">{d}<div style="width:46px;height:46px;border-radius:12px;border:4px solid {CO}"></div></div>' for d in '월화수목금토일')
    S.append(dict(d=2.5, html=card(CO, '#fff', f'''<div style="font-size:96px;font-weight:900;line-height:1.2">7일만<br>{hl("체크")}해 봐요</div>
<div style="margin-top:50px;display:flex;gap:14px;flex-wrap:wrap">{days}</div>
<div style="margin-top:50px;font-size:42px;font-weight:600;line-height:1.5">끝나면 바로 따뜻한 샤워<br>운동 같이 할 친구 태그하기</div>''', '', '')))
    S.append(dict(d=2.4, html=card(CR, INK, f'''<div style="font-size:96px;font-weight:900;line-height:1.2">저장해두고<br><span style="color:{CO}">내일 아침</span>부터</div>
<div style="margin-top:50px;font-size:44px;font-weight:600;line-height:1.5">몇 번 동작이 제일 힘들었어요?<br>댓글로 알려주세요</div>
<div style="margin-top:70px;font-size:34px;font-weight:800;color:{CO}">@have.a.shower</div>''', '', '')))
    return S


# ---------- 렌더링 ----------
def render_layers(scenes, tmp):
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={'width': W, 'height': H})
        for i, s in enumerate(scenes):
            html = f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><style>{BASE} body{{background:transparent}}</style></head><body>{s["html"]}</body></html>'
            f = os.path.join(tmp, f's{i:02d}.html')
            open(f, 'w', encoding='utf-8').write(html)
            pg.goto('file://' + f)
            pg.wait_for_timeout(250)
            s['png'] = os.path.join(tmp, f's{i:02d}.png')
            pg.screenshot(path=s['png'], omit_background=True)
        b.close()


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        print(r.stderr[-2000:]); sys.exit(1)


def build(name, scenes, out, music=None):
    tmp = os.path.join(out, '_' + name)
    os.makedirs(tmp, exist_ok=True)
    render_layers(scenes, tmp)
    parts = []
    for i, s in enumerate(scenes):
        d, seg = s['d'], os.path.join(tmp, f'seg{i:02d}.mp4')
        if 'video' in s:
            # 영상 + 글자 레이어(아래에서 살짝 올라오며 나타남)
            run(['ffmpeg', '-v', 'error', '-y', '-ss', str(s['ss']), '-t', str(d), '-i', os.path.join(IMGD, s['video']),
                 '-loop', '1', '-t', str(d), '-i', s['png'], '-filter_complex',
                 f"[0:v]setpts=PTS-STARTPTS,scale=-2:{H},crop={W}:{H},fps=30,setsar=1[bg];[1:v]format=rgba[o];"
                 f"[bg][o]overlay=0:0,format=yuv420p[v]",
                 '-map', '[v]', '-an', '-r', '30', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', seg])
        elif 'clip' in s:
            # 동작 카드 + 실제 영상(둥근 모서리 박스)
            from PIL import Image as _I, ImageDraw as _D
            mask = os.path.join(tmp, 'mask.png')
            if not os.path.exists(mask):
                m = _I.new('L', (900, 760), 0); _D.Draw(m).rounded_rectangle([0, 0, 899, 759], radius=40, fill=255); m.save(mask)
            f, ss, cx, cy, z = s['clip']
            vh = int(760 * z) // 2 * 2
            vw = int(vh * 16 / 9) // 2 * 2
            x = int(max(0, min(vw - 900, vw * cx - 450)))
            y = int(max(0, min(vh - 760, vh * cy - 380)))
            run(['ffmpeg', '-v', 'error', '-y', '-loop', '1', '-t', str(d), '-i', s['png'],
                 '-ss', str(ss), '-t', str(d), '-i', os.path.join(IMGD, f), '-loop', '1', '-t', str(d), '-i', mask, '-filter_complex',
                 f"[1:v]setpts=PTS-STARTPTS,fps=30,scale={vw}:{vh},crop=900:760:{x}:{y},format=rgba[c];[2:v]format=gray[m];[c][m]alphamerge[cv];"
                 f"[0:v]fps=30[b];[b][cv]overlay=90:300,format=yuv420p[v]",
                 '-map', '[v]', '-frames:v', str(int(round(d * 30))), '-an', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', seg])
        elif 'anim' in s:
            # 동작 카드 + 사람 애니메이션(2회 반복)
            sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
            import figure_anim as FA
            fd = os.path.join(tmp, f'anim{i:02d}')
            if s['dark']:
                FA.render(s['anim'], fd, d, 2, (246, 242, 232), (255, 225, 74), (27, 63, 239, 255))
            else:
                FA.render(s['anim'], fd, d, 2, (27, 63, 239), (23, 25, 28), (246, 242, 232, 255))
            run(['ffmpeg', '-v', 'error', '-y', '-loop', '1', '-t', str(d), '-i', s['png'],
                 '-framerate', '30', '-i', os.path.join(fd, '%03d.png'), '-filter_complex',
                 "[0:v]fps=30[b];[b][1:v]overlay=90:300,format=yuv420p[v]",
                 '-map', '[v]', '-frames:v', str(int(round(d * 30))), '-an', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', seg])
        else:
            # 카드: 천천히 확대(1.00→1.04) + 첫 0.15초 살짝 밝게
            n = int(d * 30)
            run(['ffmpeg', '-v', 'error', '-y', '-loop', '1', '-i', s['png'], '-filter_complex',
                 f"[0:v]scale={W*2}:{H*2},zoompan=z='1+0.04*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s={W}x{H}:fps=30,"
                 f"format=yuv420p[v]",
                 '-map', '[v]', '-frames:v', str(n), '-an', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', seg])
        parts.append(seg)
    lst = os.path.join(tmp, 'list.txt')
    open(lst, 'w').write(''.join(f"file '{p}'\n" for p in parts))
    total = sum(s['d'] for s in scenes)
    dst = os.path.join(out, name + '.mp4')
    if music:
        audio = ['-ss', str(MUSIC_START.get(music, 0)), '-i', os.path.join(IMGD, music), '-af', f'afade=in:d=0.3,afade=out:st={total-1.2:.2f}:d=1.2,loudnorm=I=-15:TP=-1.5']
    else:
        audio = ['-f', 'lavfi', '-t', str(total), '-i', 'anullsrc=r=44100:cl=stereo']
    run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, *audio, '-t', str(total),
         '-c:v', 'libx264', '-preset', 'medium', '-crf', '21', '-profile:v', 'high', '-pix_fmt', 'yuv420p',
         '-c:a', 'aac', '-b:a', '128k', '-shortest', '-movflags', '+faststart', dst])
    print(dst, f'{total:.1f}s')


if __name__ == '__main__':
    out = sys.argv[1]
    # 사용: ... <출력폴더> r1=m_carefree.mp3 r2=m_funkorama.mp3  (음악 없으면 r1 r2)
    which = sys.argv[2:] or ['r1', 'r2']
    os.makedirs(out, exist_ok=True)
    for w in which:
        k, _, m = w.partition('=')
        build(k, {'r1': r1, 'r2': r2}[k](), out, m or None)
