#!/usr/bin/env python3
"""Search and validate the original, offline Visual Design Intelligence style catalog.

Uses only Python stdlib. Read-only: never writes to the project or any app.
"""
import argparse
import json
import sys
from pathlib import Path

CATALOG = Path(__file__).resolve().parents[1] / 'data' / 'style-recipes.json'
REQUIRED = {'id', 'name', 'keywords', 'ideal_for', 'thesis', 'layout', 'typography', 'palette', 'surfaces', 'motion', 'risks_to_check'}

def load():
    obj = json.loads(CATALOG.read_text(encoding='utf-8'))
    if not isinstance(obj.get('recipes'), list):
        raise ValueError('Catalog missing recipes list')
    return obj['recipes']

def validate(items):
    errs, seen = [], set()
    for i, item in enumerate(items):
        missing = REQUIRED - set(item)
        if missing:
            errs.append(f'entry {i} missing: {", ".join(sorted(missing))}')
        name = item.get('id', '')
        if not name or name in seen:
            errs.append(f'duplicate/blank id at entry {i}: {name}')
        seen.add(name)
        palette = item.get('palette', {})
        for k in ['bg','surface','text','accent','border']:
            v = palette.get(k, '') if isinstance(palette, dict) else ''
            if not (isinstance(v, str) and len(v)==7 and v[0]=='#' and all(c in '0123456789ABCDEFabcdef' for c in v[1:])):
                errs.append(f'{name} invalid palette {k}: {v!r}')
    return errs

def search(items, query):
    toks = [s.lower() for s in query.split() if s.strip()]
    def score(item):
        hay = ' '.join(str(x) for x in [item['id'],item['name'],*item['keywords'],*item['ideal_for'],item['thesis'],item['layout']]).lower()
        return sum(3 if t in item['keywords'] else 2 if t in item['id'] or t in item['name'].lower() else 1 if t in hay else 0 for t in toks)
    ranked = sorted(((score(x),x) for x in items), key=lambda tup:(-tup[0],tup[1]['id']))
    return [item for s,item in ranked if s > 0]

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    sp=ap.add_subparsers(dest='cmd',required=True)
    sp.add_parser('list')
    s=sp.add_parser('search'); s.add_argument('--query',required=True)
    s=sp.add_parser('show'); s.add_argument('--id',required=True)
    sp.add_parser('validate')
    args=ap.parse_args()
    try:
        items=load()
        errs=validate(items)
        if errs:
            for msg in errs: print('ERROR:',msg,file=sys.stderr)
            return 1
        if args.cmd=='validate':
            print(f'PASS: {len(items)} original style recipes; unique ids and valid palette hex values')
        elif args.cmd=='list':
            for item in items: print(f"{item['id']:<28} {item['name']}")
        elif args.cmd=='search':
            results=search(items,args.query)
            if not results:
                print('No matching recipes. Try other terms; do not invent matches.')
            else:
                for item in results: print(f"{item['id']}: {item['name']} — {item['thesis']}")
        else:
            found=next((item for item in items if item['id']==args.id),None)
            if not found:
                print('Unknown style id',file=sys.stderr); return 2
            print(json.dumps(found,ensure_ascii=False,indent=2))
    except (OSError,ValueError,json.JSONDecodeError) as e:
        print('Catalog error:',e,file=sys.stderr); return 1
    return 0

if __name__ == '__main__':
    sys.exit(main())
