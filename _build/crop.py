# -*- coding: utf-8 -*-
"""Crop full figures + sub-panels from rendered pages into web-sized JPEGs.
Boxes are in page-pixel coords (pages rendered at 300 DPI, 2481x3508)."""
from PIL import Image
import os

PAGES = "pages"
OUT = "panels"
os.makedirs(OUT, exist_ok=True)

# full-figure box per page, and explicit panel boxes (page coords)
FIGS = {
    "fig01": {"page": "p3",  "full": [140, 285, 2340, 2362], "panels": {}},
    "fig02": {"page": "p4",  "full": [148, 1444, 2338, 2653], "panels": {
        "a": [148, 1444, 868, 2025], "b": [872, 1444, 1592, 2025],
        "c": [1596, 1444, 2338, 2025], "d": [460, 2030, 1410, 2653],
        "e": [1415, 2030, 2205, 2653]}},
    "fig03": {"page": "p9",  "full": [180, 315, 2304, 1662], "panels": {
        "a": [180, 315, 1240, 985], "b": [1245, 315, 2304, 985],
        "c": [180, 990, 1240, 1662], "d": [1245, 990, 2304, 1662]}},
    "fig04": {"page": "p11", "full": [173, 290, 2319, 1817], "panels": {
        "a": [173, 290, 880, 1078], "b": [885, 290, 1592, 1078],
        "c": [1596, 290, 2319, 1078], "d": [173, 1085, 1205, 1817],
        "e": [1210, 1085, 2319, 1817]}},
    "fig05": {"page": "p13", "full": [205, 301, 2280, 2056], "panels": {
        "a": [205, 301, 1238, 888], "b": [1243, 301, 2280, 888],
        "c": [205, 893, 1238, 1473], "d": [1243, 893, 2280, 1473],
        "e": [205, 1478, 1238, 2056], "f": [1243, 1478, 2280, 2056]}},
    "fig06": {"page": "p15", "full": [177, 464, 2303, 1959], "panels": {
        "a": [177, 464, 1235, 963], "b": [1240, 464, 2303, 963],
        "c": [177, 968, 1235, 1461], "d": [1240, 968, 2303, 1461],
        "e": [177, 1466, 1235, 1959], "f": [1240, 1466, 2303, 1959]}},
    "fig07": {"page": "p17", "full": [164, 488, 2265, 1790], "panels": {
        "a": [164, 488, 1206, 1122], "b": [1211, 488, 2265, 1122],
        "c": [164, 1127, 1206, 1790], "d": [1211, 1127, 2265, 1790]}},
    "fig08": {"page": "p20", "full": [180, 295, 2335, 2675], "panels": {
        "a": [180, 300, 1185, 1030], "b": [1195, 300, 2335, 1710],
        "c": [180, 1040, 1185, 1700], "d": [180, 1710, 1010, 2210],
        "e": [1015, 1710, 2335, 2670], "f": [180, 2215, 1010, 2670]}},
    "fig09": {"page": "p23", "full": [170, 290, 2330, 2678], "panels": {
        "a": [170, 290, 2330, 1365], "b": [170, 1375, 2330, 2678]}},
    "fig10": {"page": "p24", "full": [165, 285, 2330, 2608], "panels": {
        "a": [165, 290, 1180, 965], "b": [1190, 290, 2330, 965],
        "c": [165, 975, 2330, 1640], "d": [165, 1650, 1395, 2608],
        "e": [1400, 1650, 2330, 2608]}},
    "fig11": {"page": "p26", "full": [110, 300, 2300, 1545], "panels": {}},
}

def save(im, box, name, maxw):
    crop = im.crop(tuple(box))
    w, h = crop.size
    m = max(w, h)
    if m > maxw:
        s = maxw / m
        crop = crop.resize((int(w*s), int(h*s)), Image.LANCZOS)
    crop.convert("RGB").save(os.path.join(OUT, name+".jpg"), quality=83, optimize=True)
    return crop.size

DENSE = {"fig08", "fig09", "fig10"}
manifest = {}
for fid, cfg in FIGS.items():
    im = Image.open(os.path.join(PAGES, cfg["page"]+".png")).convert("RGB")
    full_w = 1400 if fid in DENSE else 1200
    panel_w = 1300 if fid in DENSE else 1040
    sz = save(im, cfg["full"], fid, full_w)
    manifest[fid] = {"full": sz, "panels": {}}
    for pk, box in cfg["panels"].items():
        psz = save(im, box, fid+pk, panel_w)
        manifest[fid]["panels"][pk] = psz

for fid in FIGS:
    print(fid, manifest[fid]["full"], "panels:", list(manifest[fid]["panels"].keys()))

import glob
total = sum(os.path.getsize(f) for f in glob.glob(os.path.join(OUT, "*.jpg")))
print("TOTAL jpg bytes:", round(total/1024/1024, 2), "MB across",
      len(glob.glob(os.path.join(OUT, "*.jpg"))), "files")
