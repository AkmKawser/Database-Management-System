"""
Precision Query & Search CLI for withNasser
Searches transcripts (.md), slide decks (.pdf), and SQL scripts.
"""

import sys
import os
import argparse
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[5]
COURSE_DIR = BASE_DIR / "Skills_Input" / "udemy" / "withNasser"

def search_nasser(keyword):
    print(f"\n🔍 Searching withNasser (Database Internals) for: '{keyword}'...\n" + "="*65)
    matches = []
    
    # 1. Search transcripts
    for md_file in COURSE_DIR.rglob("*.md"):
        try:
            with open(md_file, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
                if keyword.lower() in content.lower():
                    lines = content.splitlines()
                    snippets = [l.strip() for l in lines if keyword.lower() in l.lower()]
                    matches.append({
                        "file": str(md_file.relative_to(BASE_DIR)).replace("\\", "/"),
                        "section": md_file.parent.name,
                        "lecture": md_file.stem,
                        "snippets": snippets[:3]
                    })
        except:
            pass

    print(f"Found {len(matches)} matching lectures/transcripts:\n")
    for m in matches[:12]:
        print(f"📁 [{m['section']}] -> 📄 {m['lecture']}")
        print(f"   Path: {m['file']}")
        for s in m["snippets"]:
            snippet_clean = s[:120] + "..." if len(s) > 120 else s
            print(f"   💬 \"{snippet_clean}\"")
        print("-" * 50)

    # 2. Check Companion Scripts & Presentations
    companion_matches = []
    for comp in COURSE_DIR.rglob("*.*"):
        if comp.suffix.lower() in [".sql", ".txt", ".pdf", ".pptx"]:
            if keyword.lower() in comp.name.lower():
                companion_matches.append(str(comp.relative_to(BASE_DIR)).replace("\\", "/"))

    if companion_matches:
        print("\n📦 Matching Companion Scripts & Slides:")
        for cm in companion_matches:
            print(f"   📑 {cm}")
        print("="*65)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Query withNasser Database Engineering resources")
    parser.add_argument("keyword", help="Topic or keyword to search (e.g., 'MVCC', 'B+Tree', 'WAL', 'phantom read')")
    args = parser.parse_args()
    search_nasser(args.keyword)
