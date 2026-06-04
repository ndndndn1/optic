# -*- coding: utf-8 -*-
"""Auto-detect each figure's tight bbox on a page via color-saturation
projections (figures are colorful; body text & captions are black)."""
import numpy as np
from PIL import Image
import glob, os, json

S_THRESH = 38
ROW_FRAC = 0.03
COL_FRAC = 0.02
GAP = 150          # merge figure row-runs separated by <=GAP px (gutters)
MARGIN = 22

os.makedirs('crops', exist_ok=True)

def segments(flags, gap):
    segs, start, last = [], None, None
    for i, v in enumerate(flags):
        if v:
            if start is None:
                start = i
            last = i
        else:
            if start is not None and i - last > gap:
                segs.append((start, last + 1)); start = None
    if start is not None:
        segs.append((start, last + 1))
    return segs

results = {}
for f in sorted(glob.glob('pages/p*.png')):
    page = os.path.splitext(os.path.basename(f))[0]
    im = Image.open(f).convert('RGB')
    W, H = im.size
    sat = np.asarray(im.convert('HSV'))[:, :, 1].astype(np.int32)
    mask = sat > S_THRESH
    rowsum = mask.sum(axis=1)
    row_fig = rowsum > ROW_FRAC * W
    segs = segments(row_fig, GAP)
    if not segs:
        print(page, 'NO FIGURE FOUND'); continue
    # pick segment with greatest saturated mass
    r0, r1 = max(segs, key=lambda s: rowsum[s[0]:s[1]].sum())
    sub = mask[r0:r1, :]
    colsum = sub.sum(axis=0)
    col_fig = colsum > COL_FRAC * (r1 - r0)
    cols = np.where(col_fig)[0]
    c0, c1 = int(cols.min()), int(cols.max()) + 1
    x0, y0 = max(0, c0 - MARGIN), max(0, r0 - MARGIN)
    x1, y1 = min(W, c1 + MARGIN), min(H, r1 + MARGIN)
    im.crop((x0, y0, x1, y1)).save('crops/full_%s.png' % page)
    results[page] = [x0, y0, x1, y1]
    print(page, 'bbox', [x0, y0, x1, y1], 'size', [x1 - x0, y1 - y0])

json.dump(results, open('fig_bboxes.json', 'w'), indent=1)
