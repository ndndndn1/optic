# -*- coding: utf-8 -*-
"""Parse terminology_optical_sensor.md -> terminology_optical_sensor.json
Entry format (per file header rules):
  ## KEY | English Full Name | 한글명
  EN: ...
  KO: ...
  ABBR: ...
  CATEGORY: ...
  DESC:
  <multi-line>
  FORMULA: ...
  RELATED: [[a]], [[b]]
  ---
"""
import json, re, pathlib

ROOT = pathlib.Path(r"D:\doc\master\2-1display\optic\up")
SRC = ROOT / "terminology_optical_sensor.md"
OUT = ROOT / "terminology_optical_sensor.json"

FIELDS = ["EN", "KO", "ABBR", "CATEGORY", "DESC", "FORMULA", "RELATED"]
field_re = re.compile(r'^(' + '|'.join(FIELDS) + r'):[ \t]?(.*)$')

text = SRC.read_text(encoding="utf-8")

entries = []
cur = None
field = None
buf = []

def flush():
    global field, buf
    if cur is not None and field is not None:
        cur[field.lower()] = "\n".join(buf).strip()
    field = None
    buf = []

for line in text.splitlines():
    if line.startswith("## "):
        flush()
        if cur is not None:
            entries.append(cur)
        header = line[3:].strip()
        parts = [p.strip() for p in header.split("|")]
        cur = {
            "key": parts[0] if parts else "",
            "header_en": parts[1] if len(parts) > 1 else "",
            "header_ko": parts[2] if len(parts) > 2 else "",
        }
        field = None
        buf = []
        continue
    if cur is None:
        continue
    if line.strip() == "---":
        flush()
        continue
    m = field_re.match(line)
    if m:
        flush()
        field = m.group(1)
        buf = [m.group(2)] if m.group(2) else []
    else:
        if field is not None:
            buf.append(line)

flush()
if cur is not None:
    entries.append(cur)

# normalize related -> list of keys from [[...]]
link_re = re.compile(r'\[\[([^\]]+)\]\]')
terms = {}
alias = {}
for e in entries:
    key = e["key"]
    rel = link_re.findall(e.get("related", ""))
    obj = {
        "key": key,
        "en": e.get("en", "") or e.get("header_en", ""),
        "ko": e.get("ko", "") or e.get("header_ko", ""),
        "abbr": e.get("abbr", ""),
        "category": e.get("category", ""),
        "desc": e.get("desc", ""),
        "formula": e.get("formula", ""),
        "related": rel,
    }
    terms[key] = obj
    # alias index: lowercase key, and each ABBR token
    alias[key.lower()] = key
    for tok in re.split(r'[,/]', e.get("abbr", "")):
        tok = tok.strip()
        if tok and tok != "—":
            alias.setdefault(tok.lower(), key)

data = {"terms": terms, "alias": alias}
OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")

# verification counts
n_headers = sum(1 for ln in text.splitlines() if ln.startswith("## "))
print("## headers in md :", n_headers)
print("entries parsed   :", len(entries))
print("terms in json    :", len(terms))
print("alias keys       :", len(alias))
missing = [k for k, v in terms.items() if not v["desc"]]
print("entries w/o desc :", missing)
