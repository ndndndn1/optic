# -*- coding: utf-8 -*-
"""Assemble the single self-contained HTML:
   shell + css + js + inline TERMS json + base64-embedded panel images."""
import base64, json, os, re, pathlib, glob, sys

BUILD = pathlib.Path(__file__).parent
ROOT = BUILD.parent
ASSETS = BUILD / "assets"
CONTENT = BUILD / "content"
PANELS = BUILD / "panels"
OUT = ROOT / "optic_review1_figures.html"

shell = (ASSETS / "shell.html").read_text(encoding="utf-8")
style = (ASSETS / "style.css").read_text(encoding="utf-8")
app = (ASSETS / "app.js").read_text(encoding="utf-8")
term = json.loads((ROOT / "terminology_optical_sensor.json").read_text(encoding="utf-8"))

# concatenate figure content partials in order
parts = []
for n in range(1, 12):
    f = CONTENT / ("fig%02d.html" % n)
    if not f.exists():
        print("MISSING content:", f.name); sys.exit(1)
    parts.append(f.read_text(encoding="utf-8"))
content = "\n".join(parts)

# embed images: token @figXX -> data URI
img_cache = {}
def datauri(tok):
    if tok in img_cache:
        return img_cache[tok]
    p = PANELS / (tok + ".jpg")
    if not p.exists():
        raise SystemExit("MISSING image: " + str(p))
    b64 = base64.b64encode(p.read_bytes()).decode("ascii")
    uri = "data:image/jpeg;base64," + b64
    img_cache[tok] = uri
    return uri

used = set()
def repl(m):
    tok = m.group(1)
    used.add(tok)
    return datauri(tok)
content = re.sub(r'@(fig\d{2}[a-f]?)\b', repl, content)
# lazy-decode images so the browser only decodes what scrolls into view
content = content.replace('<img class="zoom"', '<img class="zoom" loading="lazy" decoding="async"')

# warn about any panel jpg not used
allimgs = set(os.path.splitext(os.path.basename(p))[0] for p in glob.glob(str(PANELS / "*.jpg")))
unused = sorted(allimgs - used)
if unused:
    print("NOTE unused images:", unused)

# validate data-k references against TERMS/alias
keys = set(term["terms"].keys())
alias = set(term["alias"].keys())
bad = []
for m in re.finditer(r'data-k="([^"]+)"', content):
    k = m.group(1)
    if k in keys or k.lower() in alias or k.lower() in {x.lower() for x in keys}:
        continue
    bad.append(k)
if bad:
    from collections import Counter
    print("BROKEN data-k (no definition):", dict(Counter(bad)))
else:
    print("data-k check: OK (all term references resolve)")

terms_js = ("const TERMS=" + json.dumps(term["terms"], ensure_ascii=False) +
            ";\nconst TALIAS=" + json.dumps(term["alias"], ensure_ascii=False) + ";")

html = (shell.replace("{{STYLE}}", style)
             .replace("{{CONTENT}}", content)
             .replace("{{TERMS}}", terms_js)
             .replace("{{APP}}", app))

OUT.write_text(html, encoding="utf-8")
print("WROTE", OUT, round(len(html.encode("utf-8"))/1024/1024, 2), "MB",
      "| images embedded:", len(used), "| terms:", len(keys))
