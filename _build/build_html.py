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
THEME = ROOT / "theme.png"
FAVORITES = ROOT / "optic_review1_qa_favorites.json"

shell = (ASSETS / "shell.html").read_text(encoding="utf-8")
style = (ASSETS / "style.css").read_text(encoding="utf-8")
app = (ASSETS / "app.js").read_text(encoding="utf-8")
term = json.loads((ROOT / "terminology_optical_sensor.json").read_text(encoding="utf-8"))

# merge sidecar: embedded_terms (self-contained sub-glossary) + optional desc_full
sidecar_path = ROOT / "terminology_embedded.json"
if sidecar_path.exists():
    sidecar = json.loads(sidecar_path.read_text(encoding="utf-8"))
    merged = 0
    for k, extra in sidecar.items():
        if k.startswith("_"):
            continue
        if k not in term["terms"]:
            print("WARN sidecar key not in main:", k); continue
        if "embedded_terms" in extra:
            term["terms"][k]["embedded_terms"] = extra["embedded_terms"]
        if "desc_full" in extra:
            term["terms"][k]["desc_full"] = extra["desc_full"]
        merged += 1
    print("sidecar merged:", merged, "/", len(term["terms"]))
else:
    print("NOTE: no terminology_embedded.json sidecar found")

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

theme_uri = ""
if THEME.exists():
    theme_uri = "data:image/png;base64," + base64.b64encode(THEME.read_bytes()).decode("ascii")
else:
    print("NOTE: theme.png not found; CNU theme footer image disabled")

favorites_data = {"version": 1, "favorites": []}
if FAVORITES.exists():
    try:
        loaded_favorites = json.loads(FAVORITES.read_text(encoding="utf-8"))
        if loaded_favorites.get("version") == 1 and isinstance(loaded_favorites.get("favorites"), list):
            favorites_data = loaded_favorites
        else:
            print("WARN favorites JSON ignored: expected version 1 with favorites list")
    except Exception as e:
        print("WARN favorites JSON ignored:", e)
favorites_js = "const INITIAL_FAVORITES=" + json.dumps(favorites_data, ensure_ascii=False) + ";"

html = (shell.replace("{{STYLE}}", style)
             .replace("{{CONTENT}}", content)
             .replace("{{TERMS}}", terms_js)
             .replace("{{FAVORITES}}", favorites_js)
             .replace("{{APP}}", app)
             .replace("{{THEME_IMAGE}}", theme_uri))

OUT.write_text(html, encoding="utf-8")
print("WROTE", OUT, round(len(html.encode("utf-8"))/1024/1024, 2), "MB",
      "| images embedded:", len(used), "| terms:", len(keys))
