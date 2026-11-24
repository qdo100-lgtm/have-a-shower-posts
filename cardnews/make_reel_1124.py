"""11/24 릴스: 카즈하 코어 루틴 5동작 (대표 제공 사진 + 동작별 Pexels/Mixkit 영상).
사용: python3 cardnews/make_reel_1124.py <출력폴더> [음악 절대경로]
결과: <출력폴더>/r1124.mp4 (1080x1920, 30fps)
동작 영상 바꾸기: 아래 CLIPS 의 (파일, 시작초, 가로중심 0~1, 세로중심 0~1)
"""
import os, sys, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import make_reels_1118 as M

ROOT = M.ROOT
D = os.path.join(ROOT, 'briefs/images/2026-11-24')
CO, CR, Y, INK = M.CO, M.CR, M.Y, M.INK
W, H = M.W, M.H
BOX_W, BOX_H, BOX_X, BOX_Y = 900, 760, 90, 300
SRC = '카즈하 루틴 · 유튜브 ‘Allure’(2026.11.18)'
PHOTO_CREDIT = os.environ.get('KAZUHA_CREDIT', '')

CLIPS = {  # 동작: (파일, 시작초, 가로중심, 세로중심)
    1: ('2026-11-24c/v_pxlegraise1.mp4', 1.0, 0.5, 0.9),
    2: ('2026-11-24c/v_pxabs1.mp4', 0.3, 0.5, 0.72),
    3: ('2026-11-24c/v_pxlegraise2.mp4', 0.5, 0.5, 0.58),
    4: ('2026-11-24c/v_pxside1.mp4', 1.0, 0.5, 0.55),
    5: ('2026-11-24c/v_pxplank2.mp4', 0.5, 0.5, 0.58),
}
MOVES = [
    ('다리 들고 발끝 터치', '누워서 두 다리를 위로 세우고<br>배 힘으로 상체 들어 발끝 쪽으로'),
    ('무릎·팔꿈치 만나기', '누워서 손은 머리 뒤,<br>무릎과 반대쪽 팔꿈치를 비틀어 만나기'),
    ('엉덩이 들기', '무릎 세우고 엉덩이를 들었다 내리기<br>허리 말고 엉덩이 힘으로'),
    ('사이드 플랭크', '팔꿈치로 옆을 짚고 몸을 일자로<br>골반이 처지지 않게 · 양쪽'),
    ('플랭크', '팔꿈치로 짚고 머리부터 발끝까지 일자<br>엉덩이 너무 올리지 않기'),
]


def hl(t, c=Y):
    return f'<span style="color:{c}">{t}</span>'


def hook():
    return f'''<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,12,14,.45) 0%,rgba(10,12,14,0) 22%,rgba(10,12,14,0) 45%,rgba(10,12,14,.75) 68%,rgba(10,12,14,.92) 100%)"></div>
<img src="{M.LOGO_W}" style="position:absolute;left:50%;top:250px;transform:translateX(-50%);height:58px">
<div style="position:absolute;left:80px;right:160px;top:1010px;color:#fff">
<h1 style="margin:0;font-size:96px;font-weight:900;line-height:1.18;text-shadow:0 4px 22px rgba(0,0,0,.45)">카즈하가<br>투어 중에도 하는<br>{hl("코어 운동")} 5</h1>
<div style="margin-top:28px;font-size:40px;font-weight:600;line-height:1.4;color:rgba(255,255,255,.92)">르세라핌 카즈하 · 유튜브 ‘Allure’ 11.18</div>
</div>
<div style="position:absolute;left:80px;bottom:420px;font-size:22px;color:rgba(255,255,255,.6)">{PHOTO_CREDIT}</div>'''


def quote_card():
    return M.card(CR, INK, f'''<div style="font-size:44px;font-weight:700;color:#5F646B">카즈하가 직접 한 말</div>
<div style="margin-top:24px;font-size:76px;font-weight:900;line-height:1.3">“발레를 어렸을 때부터<br>많이 해서, 운동하는 게<br><span style="color:{CO}">습관</span>이 되어 있다”</div>
<div style="margin-top:50px;font-size:40px;font-weight:600;line-height:1.5">원래 루틴은 10가지가 넘어요<br>그중 집에서 하기 쉬운 <b style="color:{CO}">5개</b>만 골랐어요</div>''',
        '출처: 유튜브 ‘Allure’ 카즈하 코어 운동 영상(2026.11.18) · 뉴스1(11.19)', '')


def move(i, name, how, dark):
    bg, color = (CO, '#fff') if dark else (CR, INK)
    big = Y if dark else CO
    sub = 'rgba(255,255,255,.7)' if dark else '#5F646B'
    return f'''<div style="position:absolute;inset:0;background:{bg};color:{color}">
<div style="position:absolute;left:80px;right:80px;top:230px;display:flex;justify-content:space-between;align-items:center;font-size:28px;font-weight:800;letter-spacing:.12em">
<div style="color:{big}">HAVE A SHOWER</div><div style="color:{sub};letter-spacing:.04em">{i} / 5</div></div>
<div style="position:absolute;left:80px;right:160px;top:1095px;display:flex;align-items:center;gap:26px">
<div style="width:104px;height:104px;border-radius:52px;background:{big};color:{bg};display:flex;align-items:center;justify-content:center;font-size:64px;font-weight:900;flex-shrink:0">{i}</div>
<div style="font-size:80px;font-weight:900;line-height:1.1">{name}</div></div>
<div style="position:absolute;left:80px;right:140px;top:1230px;font-size:42px;font-weight:600;line-height:1.42;opacity:.92">{how}</div>
<div style="position:absolute;left:80px;top:1375px;padding:10px 26px;border-radius:50px;border:4px solid {big};font-size:38px;font-weight:800;color:{big}">30초 · 힘들면 15초</div>
<div style="position:absolute;left:80px;right:160px;bottom:390px;font-size:22px;color:{sub}">{SRC} · 영상: Pexels</div>
</div>'''


def closing():
    return M.card(CO, '#fff', f'''<div style="font-size:52px;font-weight:700;opacity:.85">5개 × 30초 = 2분 30초</div>
<div style="margin-top:18px;font-size:100px;font-weight:900;line-height:1.2">끝나면<br>{hl("따뜻한 샤워")}로<br>마무리</div>
<div style="margin-top:56px;font-size:42px;font-weight:600;line-height:1.55">허리가 아프면 동작을 작게,<br>무릎 굽혀서 해도 괜찮아요</div>
<div style="margin-top:56px;font-size:40px;font-weight:800;color:{Y}">저장하고 같이 할 친구 태그하기</div>''', '', '')


def scenes():
    S = [dict(photo=os.path.join(D, 'kazuha_user.png'), d=2.8, html=hook()),
         dict(d=2.6, html=quote_card())]
    for k, (n, h) in enumerate(MOVES, 1):
        S.append(dict(d=3.0, html=move(k, n, h, bool(k % 2)), clip=CLIPS[k]))
    S.append(dict(d=3.0, html=closing()))
    return S


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        print(' '.join(cmd)[:300]); print(r.stderr[-2000:]); sys.exit(1)


def build(out, music=None):
    tmp = os.path.join(out, '_r1124')
    os.makedirs(tmp, exist_ok=True)
    S = scenes()
    M.render_layers(S, tmp)
    from PIL import Image as _I, ImageDraw as _D
    mask = os.path.join(tmp, 'mask.png')
    m = _I.new('L', (BOX_W, BOX_H), 0); _D.Draw(m).rounded_rectangle([0, 0, BOX_W - 1, BOX_H - 1], radius=40, fill=255); m.save(mask)
    parts = []
    for i, s in enumerate(S):
        d, seg, n = s['d'], os.path.join(tmp, f'seg{i:02d}.mp4'), int(round(s['d'] * 30))
        if 'photo' in s:
            # 사진 천천히 확대(1.00→1.06) + 글자 레이어
            run(['ffmpeg', '-v', 'error', '-y', '-loop', '1', '-i', s['photo'], '-loop', '1', '-t', str(d), '-i', s['png'], '-filter_complex',
                 f"[0:v]scale={W*2}:{H*2}:force_original_aspect_ratio=increase,crop={W*2}:{H*2}:(iw-{W*2})/2:0,"
                 f"zoompan=z='1+0.06*on/{n}':x='iw/2-(iw/zoom/2)':y='ih*0.18-(ih/zoom*0.18)':d={n}:s={W}x{H}:fps=30[bg];"
                 f"[1:v]format=rgba[o];[bg][o]overlay=0:0,format=yuv420p[v]",
                 '-map', '[v]', '-frames:v', str(n), '-an', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', seg])
        elif 'clip' in s:
            f, ss, cx, cy = s['clip']
            src = os.path.join(ROOT, 'briefs/images', f)
            run(['ffmpeg', '-v', 'error', '-y', '-loop', '1', '-t', str(d), '-i', s['png'],
                 '-ss', str(ss), '-t', str(d + 0.5), '-i', src, '-loop', '1', '-t', str(d), '-i', mask, '-filter_complex',
                 f"[1:v]setpts=PTS-STARTPTS,fps=30,scale={BOX_W}:{BOX_H}:force_original_aspect_ratio=increase,"
                 f"crop={BOX_W}:{BOX_H}:(iw-{BOX_W})*{cx}:(ih-{BOX_H})*{cy},format=rgba[c];[2:v]format=gray[m];[c][m]alphamerge[cv];"
                 f"[0:v]fps=30[b];[b][cv]overlay={BOX_X}:{BOX_Y},format=yuv420p[v]",
                 '-map', '[v]', '-frames:v', str(n), '-an', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', seg])
        else:
            run(['ffmpeg', '-v', 'error', '-y', '-loop', '1', '-i', s['png'], '-filter_complex',
                 f"[0:v]scale={W*2}:{H*2},zoompan=z='1+0.04*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s={W}x{H}:fps=30,format=yuv420p[v]",
                 '-map', '[v]', '-frames:v', str(n), '-an', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', seg])
        parts.append(seg)
    lst = os.path.join(tmp, 'list.txt')
    open(lst, 'w').write(''.join(f"file '{p}'\n" for p in parts))
    total = sum(s['d'] for s in S)
    dst = os.path.join(out, 'r1124.mp4')
    if music:
        audio = ['-ss', '6', '-i', music, '-af', f'afade=in:d=0.3,afade=out:st={total-1.2:.2f}:d=1.2,loudnorm=I=-15:TP=-1.5']
    else:
        audio = ['-f', 'lavfi', '-t', str(total), '-i', 'anullsrc=r=44100:cl=stereo']
    run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, *audio, '-t', str(total),
         '-c:v', 'libx264', '-preset', 'medium', '-crf', '21', '-profile:v', 'high', '-pix_fmt', 'yuv420p',
         '-c:a', 'aac', '-b:a', '128k', '-shortest', '-movflags', '+faststart', dst])
    print(dst, f'{total:.1f}s')


if __name__ == '__main__':
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    build(out, sys.argv[2] if len(sys.argv) > 2 else None)
