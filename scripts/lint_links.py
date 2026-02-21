#!/usr/bin/env python3
import requests, yaml, sys
from pathlib import Path

REQ = ["name","year","type","scope","key_idea","links","category"]

p = Path("data/entries.yaml")
entries = yaml.safe_load(p.read_text())

errors, warns = [], []
seen = set()

for i,e in enumerate(entries):
    for k in REQ:
        if k not in e or e[k] in (None, ""):
            errors.append(f"missing field {k} at index {i}")
    key = (str(e.get("name","")) .strip().lower(), str(e.get("year","")))
    if key in seen:
        errors.append(f"duplicate name+year: {e.get('name')} ({e.get('year')})")
    seen.add(key)
    if not isinstance(e.get("links",[]), list) or not e.get("links"):
        errors.append(f"links must be non-empty list for {e.get('name')}")

for e in entries:
    for url in e.get("links",[])[:2]:
        try:
            r = requests.head(url, timeout=8, allow_redirects=True)
            if r.status_code >= 400 or r.status_code < 100:
                r = requests.get(url, timeout=8, allow_redirects=True)
            if r.status_code >= 400:
                warns.append(f"dead-ish link [{r.status_code}] {url} ({e['name']})")
        except Exception as ex:
            warns.append(f"link check failed {url} ({e['name']}): {ex}")

if warns:
    print("WARNINGS:")
    for w in warns[:100]:
        print("-", w)

if errors:
    print("ERRORS:")
    for er in errors:
        print("-", er)
    sys.exit(1)

print(f"OK: {len(entries)} entries, {len(warns)} link warnings, 0 hard errors")
