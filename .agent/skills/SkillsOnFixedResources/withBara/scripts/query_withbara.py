"""
withBara Course Search & Query Utility
Searches through lecture transcripts, notes, and references.
"""

import sys
import os
import json
import argparse
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[5]
COURSE_DIR = BASE_DIR / "Skills_Input" / "udemy" / "withBara"
TOC_FILE = BASE_DIR / ".agent" / "skills" / "SkillsOnFixedResources" / "withBara" / "references" / "toc.json"

def search_course(keyword):
    print(f"\n🔍 Searching withBara course for keyword: '{keyword}'...\n" + "="*60)
    matches = []
    
    # 1. Search transcripts
    for md_file in COURSE_DIR.rglob("*.md"):
        if "Resources" in md_file.parts:
            continue
        try:
            with open(md_file, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
                if keyword.lower() in content.lower():
                    # extract snippets
                    lines = content.splitlines()
                    matched_lines = [l.strip() for l in lines if keyword.lower() in l.lower()]
                    matches.append({
                        "file": str(md_file.relative_to(BASE_DIR)).replace("\\", "/"),
                        "section": md_file.parent.name,
                        "lecture": md_file.stem,
                        "snippets": matched_lines[:3]
                    })
        except Exception as e:
            pass

    print(f"Found {len(matches)} matching lectures/transcripts:\n")
    for m in matches:
        print(f"📁 [{m['section']}] -> 📄 {m['lecture']}")
        print(f"   Path: {m['file']}")
        for s in m["snippets"]:
            print(f"   💬 \"{s[:120]}...\"" if len(s) > 120 else f"   💬 \"{s}\"")
        print("-" * 50)

    # 2. Check Resources (Scripts & Docs)
    res_dir = COURSE_DIR / "Resources"
    res_matches = []
    if res_dir.exists():
        for sql_file in (res_dir / "03_scripts").glob("*.sql"):
            if keyword.lower() in sql_file.name.lower():
                res_matches.append(str(sql_file.relative_to(BASE_DIR)).replace("\\", "/"))
            else:
                try:
                    with open(sql_file, "r", encoding="utf-8", errors="ignore") as f:
                        if keyword.lower() in f.read().lower():
                            res_matches.append(str(sql_file.relative_to(BASE_DIR)).replace("\\", "/"))
                except:
                    pass

    if res_matches:
        print("\n📦 Matching Companion SQL Scripts in Resources:")
        for rm in set(res_matches):
            print(f"   💻 {rm}")
        print("="*60)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Query withBara Course transcripts and resources")
    parser.add_argument("keyword", help="Topic or keyword to search (e.g., 'execution order', 'index', 'partition', 'join')")
    args = parser.parse_args()
    search_course(args.keyword)
