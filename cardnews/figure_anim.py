"""릴스용 운동 동작 애니메이션 (옆모습 사람 실루엣, 투명 PNG 프레임).
python3 cardnews/figure_anim.py <출력폴더> squat 2.4   → 출력폴더/000.png ... (900x760)
동작: squat pushup catcow shoulder lunge situp superman
"""
import math
import os
import sys
from PIL import Image, ImageDraw

W, H = 900, 760        # 프레임 크기
SS = 2                 # 2배로 그린 뒤 줄여서 부드럽게
FLOOR_Y = 640          # 바닥 위치(프레임 안)
L_TH, L_SH, L_UA, L_FA = 150, 150, 118, 108
HEAD_R, NECK = 44, 16
TH = 40                # 팔다리 굵기


def add(a, b): return (a[0] + b[0], a[1] + b[1])
def sub(a, b): return (a[0] - b[0], a[1] - b[1])
def mul(a, k): return (a[0] * k, a[1] * k)
def norm(a):
    d = math.hypot(*a) or 1
    return (a[0] / d, a[1] / d)


def ik(root, target, l1, l2, bend):
    """두 마디(허벅지-정강이 / 위팔-아래팔). bend=+1/-1 로 무릎·팔꿈치 꺾이는 방향."""
    d = sub(target, root)
    dist = min(math.hypot(*d), l1 + l2 - 0.01)
    dist = max(dist, abs(l1 - l2) + 0.01)
    base = math.atan2(d[1], d[0])
    cosA = (l1 * l1 + dist * dist - l2 * l2) / (2 * l1 * dist)
    A = math.acos(max(-1, min(1, cosA)))
    ang = base + bend * A
    joint = add(root, (l1 * math.cos(ang), l1 * math.sin(ang)))
    end = add(joint, mul(norm(sub(target, joint)), l2))
    return joint, end


def lerp(a, b, t):
    if isinstance(a, tuple):
        return tuple(lerp(x, y, t) for x, y in zip(a, b))
    return a + (b - a) * t


# 좌표: x 오른쪽(얼굴 방향), y 위쪽이 음수, 바닥 y=0
# 자세 = hip, sh(어깨), foot, hand, kb(무릎 방향), eb(팔꿈치 방향), curve(등 휘기), head(머리 각도 보정)
STAND = dict(hip=(0, -300), sh=(0, -490), foot=(8, 0), hand=(8, -268), kb=-1, eb=1, curve=0, head=0)
POSES = {
    'squat': (STAND,
              dict(hip=(-120, -165), sh=(-25, -340), foot=(8, 0), hand=(200, -330), kb=-1, eb=1, curve=0, head=-15)),
    'pushup': (dict(hip=(-90, -150), sh=(100, -230), foot=(-330, 0), hand=(105, 0), kb=1, eb=-1, curve=0, head=0, knee='straight'),
               dict(hip=(-125, -55), sh=(150, -95), foot=(-330, 0), hand=(105, 0), kb=1, eb=-1, curve=0, head=0, knee='straight')),
    'catcow': (dict(hip=(-150, -150), sh=(60, -228), foot=(-300, 0), hand=(62, 0), kb=-1, eb=1, curve=-70, head=55),
               dict(hip=(-150, -150), sh=(60, -228), foot=(-300, 0), hand=(62, 0), kb=-1, eb=1, curve=45, head=-35)),
    'shoulder': (dict(hip=(0, -300), sh=(6, -490), foot=(8, 0), hand=(228, -470), kb=-1, eb=1, curve=0, head=0),
                 dict(hip=(0, -300), sh=(-4, -490), foot=(8, 0), hand=(60, -455), kb=-1, eb=1, curve=14, head=-8)),
    'lunge': (dict(STAND, foot2=(8, 0)),
              dict(hip=(-70, -175), sh=(-62, -365), foot=(60, 0), hand=(-62, -150), kb=-1, eb=1, curve=0, head=0, foot2=(-285, 0))),
    'situp': (dict(hip=(0, -24), sh=(-190, -24), foot=(230, 0), hand=(-120, -50), kb=1, eb=1, curve=0, head=-8, lying=True),
              dict(hip=(0, -24), sh=(-115, -175), foot=(230, 0), hand=(-60, -150), kb=1, eb=1, curve=-25, head=-25, lying=True)),
    'superman': (dict(hip=(0, -24), sh=(190, -26), foot=(-300, -12), hand=(415, -18), kb=1, eb=1, curve=0, head=0),
                 dict(hip=(0, -24), sh=(182, -62), foot=(-285, -90), hand=(400, -120), kb=1, eb=1, curve=18, head=-18)),
}


def pose_at(name, t):
    a, b = POSES[name]
    p = {}
    for k in a:
        p[k] = lerp(a[k], b[k], t) if isinstance(a[k], (int, float, tuple)) and not isinstance(a[k], bool) else a[k]
    for k in b:
        if k not in p:
            p[k] = b[k]
    if 'elbow_back' in b and t > 0.5:
        p['elbow_back'] = True
    return p


def bez(p0, c, p1, n=24):
    return [add(add(mul(p0, (1 - s) ** 2), mul(c, 2 * (1 - s) * s)), mul(p1, s * s)) for s in (i / n for i in range(n + 1))]


def draw_pose(p, col, col_far, outline=None):
    img = Image.new('RGBA', (W * SS, H * SS), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    ox, oy = W / 2 + 40, FLOOR_Y

    def P(pt):
        return ((pt[0] + ox) * SS, (pt[1] + oy) * SS)

    def seg(pts, c, w=TH, ol=False):
        pts = [P(q) for q in pts]
        if ol and outline:
            seg_raw(pts, outline, w + 12)
        seg_raw(pts, c, w)

    def seg_raw(pts, c, w):
        d.line(pts, fill=c, width=int(w * SS), joint='curve')
        r = w * SS / 2
        for q in pts:
            d.ellipse([q[0] - r, q[1] - r, q[0] + r, q[1] + r], fill=c)

    hip, sh = p['hip'], p['sh']
    tdir = norm(sub(sh, hip))
    perp = (tdir[1], -tdir[0])  # 등 쪽(왼쪽 위) 방향
    mid = mul(add(hip, sh), 0.5)
    ctrl = add(mid, mul(perp, p.get('curve', 0)))

    def leg(foot, c, off=0):
        h = add(hip, (off, 0))
        if p.get('knee') == 'straight':
            k = add(h, mul(norm(sub(foot, h)), L_TH)); f = add(k, mul(norm(sub(foot, h)), L_SH))
        else:
            k, f = ik(h, foot, L_TH, L_SH, p['kb'])
        seg([h, k, f], c, TH, c == col)
        seg([f, add(f, (26, 0))], c, 30)  # 발

    def arm(hand, c, off=0):
        s = add(sh, (off, 0))
        e, w = ik(s, hand, L_UA, L_FA, p['eb'])
        seg([s, e, w], c, 34, c == col)

    # 먼 쪽 팔다리(연하게)
    leg(p['foot2'] if 'foot2' in p else add(p['foot'], (-14, 0)), col_far, -6)
    arm(add(p['hand'], (-14, 4)), col_far, -6)
    # 몸통(곡선)
    seg(bez(hip, ctrl, sh), col, 66)
    # 머리
    ang = math.atan2(tdir[1], tdir[0]) + math.radians(p.get('head', 0))
    hc = add(sh, mul((math.cos(ang), math.sin(ang)), NECK + HEAD_R + 12))
    seg([sh, add(sh, mul((math.cos(ang), math.sin(ang)), NECK + 10))], col, 34)
    r = HEAD_R * SS
    c = P(hc)
    d.ellipse([c[0] - r, c[1] - r, c[0] + r, c[1] + r], fill=col)
    # 가까운 쪽 팔다리
    leg(p['foot'], col)
    arm(p['hand'], col)
    return img.resize((W, H), Image.LANCZOS)


def render(name, out, dur, reps=2, color=(246, 242, 232), floor=(255, 225, 74), outline=(27, 63, 239, 255)):
    os.makedirs(out, exist_ok=True)
    n = int(round(dur * 30))
    far = tuple(int(c * 0.72) for c in color) + (255,)
    for i in range(n):
        ph = (i / n) * reps % 1.0
        t = 0.5 - 0.5 * math.cos(2 * math.pi * ph)  # A→B→A 부드럽게
        if ph < 0.08 or ph > 0.92:
            t = 0
        img = draw_pose(pose_at(name, t), color + (255,), far, outline)
        bg = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        dd = ImageDraw.Draw(bg)
        dd.rounded_rectangle([60, FLOOR_Y + 22, W - 60, FLOOR_Y + 30], radius=4, fill=floor + (255,))
        bg.alpha_composite(img)
        bg.save(os.path.join(out, f'{i:03d}.png'))
    return n


if __name__ == '__main__':
    render(sys.argv[2], sys.argv[1], float(sys.argv[3]))
