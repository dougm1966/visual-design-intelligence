#!/usr/bin/env python3
"""Offline smoke tests for a Visual Design Intelligence skill package; stdlib only."""
import json
import subprocess
import sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
required=['SKILL.md','README.md','data/style-recipes.json','scripts/style_catalog.py','references/inspiration-sources.md','references/interface-patterns.md','references/quality-gates.md','references/agent-goal-prompt.md','assets/DESIGN_BRIEF.md','assets/DESIGN_SYSTEM_TEMPLATE.md','assets/prototype-starter.html','examples/README.md']
for f in required:
    if not (root/f).is_file():
        raise SystemExit(f'MISSING {f}')
manifest=(root/'SKILL.md').read_text(encoding='utf8')
assert manifest.startswith('---\nname: visual-design-intelligence\n')
assert 'description:' in manifest.split('---',2)[1]
for forbidden in ('SpeakChart','Mike_Curby','MC³','WyoHost'):
    for f in root.rglob('*'):
        if f.is_file() and f.name != 'validate_package.py' and f.suffix in {'.md','.html','.json','.py'}:
            assert forbidden.lower() not in f.read_text(encoding='utf8').lower(),(f,forbidden)
recipes=json.loads((root/'data/style-recipes.json').read_text(encoding='utf8'))['recipes']
assert len(recipes)==16
res=subprocess.run([sys.executable,str(root/'scripts/style_catalog.py'),'validate'],capture_output=True,text=True,check=True)
assert 'PASS' in res.stdout
html=(root/'assets/prototype-starter.html').read_text(encoding='utf8')
for needle in ['data-mode="editorial"','data-mode="precision"','data-mode="playful"','id="new-task-form"','id="task-list"','prefers-reduced-motion']:
    assert needle in html,needle
print(f'PASS: {len(required)} required skill files; 16 catalog recipes; no current-project coupling; demo scaffold present')
print('NOTE: This does not replace runtime browser or visual tests')
