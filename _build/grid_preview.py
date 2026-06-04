# -*- coding: utf-8 -*-
"""Make downscaled grid-overlay previews labeled in ORIGINAL pixel coords."""
from PIL import Image, ImageDraw, ImageFont
import glob, os, sys

SCALE = 1/3.0
STEP = 200  # grid spacing in original px

try:
    font = ImageFont.load_default(16)
except Exception:
    font = ImageFont.load_default()

pages = sys.argv[1:] or sorted(glob.glob('pages/p*.png'))
os.makedirs('grid', exist_ok=True)
for f in pages:
    im = Image.open(f).convert('RGB')
    W, H = im.size
    pw, ph = int(W*SCALE), int(H*SCALE)
    sm = im.resize((pw, ph))
    d = ImageDraw.Draw(sm)
    for x in range(0, W, STEP):
        X = int(x*SCALE)
        d.line([(X, 0), (X, ph)], fill=(255, 0, 0), width=1)
        d.text((X+1, 1), str(x), fill=(200, 0, 0), font=font)
    for y in range(0, H, STEP):
        Y = int(y*SCALE)
        d.line([(0, Y), (pw, Y)], fill=(0, 0, 255), width=1)
        d.text((1, Y+1), str(y), fill=(0, 0, 200), font=font)
    out = os.path.join('grid', 'grid_'+os.path.basename(f))
    sm.save(out)
    print(out, '(orig %dx%d)' % (W, H))
