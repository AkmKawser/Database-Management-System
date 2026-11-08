"""
withBara Course Indexer & Query Tool
Generates structured outlines and searches the course transcripts and resources.
"""

import os
import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[5]
COURSE_DIR = BASE_DIR / "Skills_Input" / "udemy" / "withBara"
REFERENCES_DIR = BASE_DIR / ".agent" / "skills" / "SkillsOnFixedResources" / "withBara" / "references"

def build_index():
    index = {
        "course_title": "The Complete SQL Bootcamp / Master Course (withBara)",
        "sections": [],
        "resources": {
            "docs": [],
            "scripts": [],
            "datasets": []
        }
    }

    # 1. Index Sections & Lectures
    sections = sorted([d for d in COURSE_DIR.iterdir() if d.is_dir() and d.name != "Resources"])
    for s_idx, sec in enumerate(sections, 1):
        sec_dict = {
            "section_number": s_idx,
            "section_name": sec.name,
            "lectures": []
        }
        lectures = sorted([f for f in sec.glob("*.md")])
        for l_idx, lec in enumerate(lectures, 1):
            sec_dict["lectures"].append({
                "lecture_number": l_idx,
                "file_name": lec.name,
                "relative_path": str(lec.relative_to(BASE_DIR)).replace("\\", "/")
            })
        index["sections"].append(sec_dict)

    # 2. Index Resources
    res_dir = COURSE_DIR / "Resources"
    if res_dir.exists():
        docs_dir = res_dir / "02_docs"
        scripts_dir = res_dir / "03_scripts"
        datasets_dir = res_dir / "01_datasets"

        if docs_dir.exists():
            for doc in sorted(docs_dir.glob("*")):
                index["resources"]["docs"].append({
                    "name": doc.name,
                    "relative_path": str(doc.relative_to(BASE_DIR)).replace("\\", "/")
                })
        if scripts_dir.exists():
            for sc in sorted(scripts_dir.glob("*.sql")):
                index["resources"]["scripts"].append({
                    "name": sc.name,
                    "relative_path": str(sc.relative_to(BASE_DIR)).replace("\\", "/")
                })
        if datasets_dir.exists():
            for ds in sorted(datasets_dir.glob("*")):
                index["resources"]["datasets"].append({
                    "name": ds.name,
                    "relative_path": str(ds.relative_to(BASE_DIR)).replace("\\", "/")
                })

    # Save to toc.json
    REFERENCES_DIR.mkdir(parents=True, exist_ok=True)
    with open(REFERENCES_DIR / "toc.json", "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2)

    # Generate Markdown Table of Contents
    with open(REFERENCES_DIR / "table_of_contents.md", "w", encoding="utf-8") as f:
        f.write("# withBara Course Curriculum & Resource Index\n\n")
        f.write("A master navigation guide for all 28 course modules, transcripts, slides, and scripts.\n\n")
        f.write("## 📚 Course Modules & Lectures\n\n")
        for s in index["sections"]:
            f.write(f"### Section: {s['section_name']}\n")
            for l in s["lectures"]:
                f.write(f"- [`{l['file_name']}`]({l['relative_path']})\n")
            f.write("\n")
        
        f.write("## 🗄️ Curated Resources\n\n")
        f.write("### 📖 Slide Decks & Documents (`02_docs`)\n")
        for d in index["resources"]["docs"]:
            f.write(f"- [`{d['name']}`]({d['relative_path']})\n")
        f.write("\n")
        f.write("### 💻 Official Reference SQL Scripts (`03_scripts`)\n")
        for sc in index["resources"]["scripts"]:
            f.write(f"- [`{sc['name']}`]({sc['relative_path']})\n")
        f.write("\n")

    print(f"Index successfully generated at {REFERENCES_DIR / 'toc.json'} and {REFERENCES_DIR / 'table_of_contents.md'}")

if __name__ == "__main__":
    build_index()
