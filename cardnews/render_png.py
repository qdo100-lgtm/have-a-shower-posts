"""카드뉴스 .dc.html → 1080x1350 PNG.
사용: python3 cardnews/render_png.py <출력폴더(절대경로)> <파일명.dc.html ...>  (파일은 cardnews/project/ 안)
"""
import re, sys, os
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(ROOT, 'img')
BLOBS = {
    '8efcc2ede8020a78fa06f70b9bf1c642': 'p13_cover_shower.jpg',
    'f180aaecb1aaeea4cd9db39067693cfa': 'ph_cover.jpg',
    '37c606c0d10a6daf71f8f211bd1ba18e': 'ph_wide.jpg',
    'd84220792d6928b4619a11e9568316da': 'ph_square.jpg',
    'c070717f870959faa04ccf35a26135a8': 'p10_cover_sydney_up.jpg',
    '5ea473ecaa199a16294c9c5f0601192b': 'p10_tub.jpg',
    '6f006d0e37e262783a2e5f7635e64f10': 'p10_product.jpg',
    '668a141f45e1f5a7b49774db7dadb98a': 'p10_plate.jpg',
    '291cad6575aa62613f2a8a37dce482f8': 'logo_cream.png',
    '11234708ce8dd667817c59a15d245c81': 'logo_white.png',
}
ACCENT = '#1B3FEF'

def to_html(src):
    body = re.search(r'<x-dc>(.*)</x-dc>', src, re.S).group(1)
    style = re.search(r'<style>(.*?)</style>', body, re.S).group(1)
    body = re.sub(r'<helmet>.*?</helmet>', '', body, flags=re.S)
    body = body.replace('{{accent}}', ACCENT)
    for k in set(re.findall(r'/_blob/([0-9a-f]{32})', body)) - set(BLOBS):
        # 새 사진: 같은 id 이름의 파일을 img/ 에 두면 자동으로 씀 (예: img/<id>.jpg)
        for ext in ('.jpg', '.png'):
            if os.path.exists(os.path.join(IMG, k + ext)):
                BLOBS[k] = k + ext
        if k not in BLOBS:
            print('사진 없음: /_blob/' + k + ' → Artifact read(path=id)로 받아 img/' + k + '.jpg 로 저장하세요', file=sys.stderr)
    for k, v in BLOBS.items():
        body = body.replace('/_blob/' + k, 'file://' + os.path.join(IMG, v))
    body = re.sub(r"font-family: '[^;\"]*?sans-serif", "font-family: 'Noto Sans CJK KR', sans-serif", body)
    return ('<!doctype html><html lang="ko"><head><meta charset="utf-8"><style>' + style +
            "body{font-family:'Noto Sans CJK KR',sans-serif;word-break:keep-all}</style></head><body>" + body + '</body></html>')

def main(names, outdir):
    os.makedirs(outdir, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium' if os.path.exists('/opt/pw-browsers/chromium') else None)
        pg = b.new_page(viewport={'width': 1080, 'height': 1350}, device_scale_factor=1)
        for i, n in enumerate(names, 1):
            html = to_html(open(os.path.join(ROOT, 'project', n), encoding='utf-8').read())
            tmp = os.path.join(outdir, '_tmp.html')
            open(tmp, 'w', encoding='utf-8').write(html)
            pg.goto('file://' + tmp)
            pg.wait_for_timeout(300)
            out = os.path.join(outdir, n.replace('.dc.html', '.png'))
            pg.screenshot(path=out, clip={'x': 0, 'y': 0, 'width': 1080, 'height': 1350})
            print(out)
        os.remove(tmp)
        b.close()

if __name__ == '__main__':
    main(sys.argv[2:], sys.argv[1])
