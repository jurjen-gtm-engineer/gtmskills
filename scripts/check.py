#!/usr/bin/env python3
"""Repo check. Run before every push: python3 scripts/check.py

Fails when a skill folder and the catalog disagree, when a SKILL.md has bad
frontmatter, when publication-sweep patterns appear (dashes, private paths,
key-like strings), or when a shipped script stops working.
"""
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
errors = []


def err(msg):
    errors.append(msg)


catalog = json.loads((ROOT / "catalog.json").read_text())
listed = [s["slug"] for g in catalog["groups"] for s in g["skills"]]
folders = sorted(p.name for p in SKILLS.iterdir() if p.is_dir())
for slug in sorted(set(folders) - set(listed)):
    err(f"{slug}: folder exists but is not in catalog.json")
for slug in sorted(set(listed) - set(folders)):
    err(f"{slug}: in catalog.json but has no folder")
if len(listed) != len(set(listed)):
    err("catalog.json lists a skill twice")

readme = (ROOT / "README.md").read_text()
for slug in listed:
    if f"(skills/{slug})" not in readme:
        err(f"{slug}: missing from README.md, run scripts/build_readme.py")

for slug in folders:
    path = SKILLS / slug / "SKILL.md"
    if not path.exists():
        err(f"{slug}: no SKILL.md")
        continue
    text = path.read_text()
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        err(f"{slug}: no frontmatter")
        continue
    front = m.group(1)
    name = re.search(r"^name:\s*(.+)$", front, re.M)
    desc = re.search(r"^description:\s*(.+)$", front, re.M)
    if not name or name.group(1).strip().strip('"') != slug:
        err(f"{slug}: frontmatter name does not match the folder")
    if not desc:
        err(f"{slug}: no description")
    elif len(desc.group(1)) > 1024:
        err(f"{slug}: description is over 1,024 characters")
    elif not desc.group(1).startswith(('"', "'")) and (": " in desc.group(1) or " #" in desc.group(1)):
        err(f"{slug}: description has ': ' or ' #' and must be quoted, or YAML parsers skip the skill")

# Publication sweep over everything that ships.
TEXT = {".md", ".py", ".json", ".jsonl", ".txt", ".yaml", ".yml", ".csv", ".ts", ".sh"}
PATTERNS = [
    (re.compile("[–—]"), "em or en dash"),
    (re.compile(r"/Users/|knowledge_base/|00_foundation/|clients/\{|\[\[(feedback_|deepline|edge-|wbd-)"), "private path or internal link"),
    (re.compile(r"hooks\.slack\.com|api\.clay\.com/v\d+/sources/webhook|sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|apify_api_[A-Za-z0-9]+"), "secret or webhook"),
]
for path in [ROOT / "README.md", ROOT / "CREDITS.md", *(ROOT / "docs").rglob("*"), *SKILLS.rglob("*")]:
    if not path.is_file() or path.suffix not in TEXT:
        continue
    try:
        text = path.read_text()
    except UnicodeDecodeError:
        continue
    for rx, label in PATTERNS:
        hit = rx.search(text)
        if hit:
            line = text.count("\n", 0, hit.start()) + 1
            err(f"{path.relative_to(ROOT)}:{line}: {label}")


def run(args, cwd=ROOT, expect=None):
    r = subprocess.run([sys.executable, *args], cwd=cwd, capture_output=True, text=True)
    if r.returncode != 0:
        err(f"{' '.join(args)} failed: {r.stderr.strip()[-300:]}")
    elif expect and expect not in r.stdout:
        err(f"{' '.join(args)}: expected '{expect}' in the output")


for py in SKILLS.rglob("*.py"):
    run(["-m", "py_compile", str(py)])
run(["skills/tam-data-cost-estimate/scripts/estimate.py", "--scope", "skills/tam-data-cost-estimate/examples/scope.json"], expect="One-off build data")
run(["skills/crm-enrichment-cost-estimate/scripts/estimate.py", "--scope", "skills/crm-enrichment-cost-estimate/examples/scope.json"], expect="**321,000** | **648,000**")

if errors:
    print("\n".join(errors))
    sys.exit(f"\n{len(errors)} problem(s)")
print(f"ok: {len(folders)} skills, catalog and README in sync, sweep clean, scripts run")
