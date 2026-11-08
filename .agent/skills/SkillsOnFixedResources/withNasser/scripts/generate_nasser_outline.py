"""
withNasser Course Indexer & Deep Outline Generator
Generates:
1. toc.json & table_of_contents.md under references/
2. withNasser_Complete_Course_Outline.md under Skills_Output/withNasser_output/outline/
"""

import os
import re
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[5]
COURSE_DIR = BASE_DIR / "Skills_Input" / "udemy" / "withNasser"
SKILL_DIR = BASE_DIR / ".agent" / "skills" / "SkillsOnFixedResources" / "withNasser"
REFERENCES_DIR = SKILL_DIR / "references"
OUTLINE_DIR = BASE_DIR / "Skills_Output" / "withNasser_output" / "outline"

def generate_index_and_outline():
    sections = sorted([d for d in COURSE_DIR.iterdir() if d.is_dir()])
    
    index = {
        "course_title": "Fundamentals of Database Engineering (withNasser)",
        "instructor": "Hussein Nasser",
        "sections": []
    }
    
    outline_lines = []
    outline_lines.append("# withNasser: Complete Course Curriculum & Deep Topic Outline\n")
    outline_lines.append("> **Course**: Fundamentals of Database Engineering\n")
    outline_lines.append("> **Instructor**: Hussein Nasser\n")
    outline_lines.append("> **Coverage**: Exhaustive index of all 18 sections, lectures, database internals topics, PDF/PPTX slides, and SQL scripts for surgical searching and query retrieval.\n\n")
    outline_lines.append("---\n\n")
    outline_lines.append("## ⚡ Fast Jump Table of Contents\n\n")

    for s_idx, sec in enumerate(sections, 1):
        clean_name = sec.name
        anchor = clean_name.lower().replace(" ", "-").replace("&", "").replace("(", "").replace(")", "").replace(",", "").replace("+", "")
        anchor = re.sub(r'[^a-z0-9\-]', '', anchor)
        outline_lines.append(f"{s_idx}. [{clean_name}](#{anchor})\n")
    
    outline_lines.append("\n---\n\n")

    for s_idx, sec in enumerate(sections, 1):
        outline_lines.append(f"## {sec.name}\n\n")
        files = sorted(list(sec.glob("*")))
        
        sec_dict = {
            "section_number": s_idx,
            "section_name": sec.name,
            "lectures": []
        }
        
        for f in files:
            f_rel = f.relative_to(BASE_DIR).as_posix()
            
            if f.suffix.lower() == ".md":
                sec_dict["lectures"].append({
                    "name": f.stem,
                    "relative_path": f_rel
                })
                outline_lines.append(f"### 📄 {f.stem}\n")
                outline_lines.append(f"- **Transcript File**: `{f_rel}`\n")
                
                # Extract headings and concepts
                try:
                    with open(f, "r", encoding="utf-8", errors="ignore") as lf:
                        content = lf.read()
                    
                    headings = re.findall(r'^(#{2,4})\s+(.+)$', content, flags=re.MULTILINE)
                    subtopics = []
                    if headings:
                        for level, title in headings:
                            indent = "  " * (len(level) - 1)
                            subtopics.append(f"{indent}- **{title.strip()}**")
                    
                    # Look for database internal keywords
                    keywords = re.findall(r'\b(ACID|ATOMICITY|CONSISTENCY|ISOLATION|DURABILITY|SERIALIZABLE|REPEATABLE READ|READ COMMITTED|READ UNCOMMITTED|PHANTOM|DIRTY READ|MVCC|2PL|TWO-PHASE LOCKING|OPTIMISTIC|PESSIMISTIC|WAL|REDO|UNDO|CHECKPOINT|PAGE|SLOTTED PAGE|B-TREE|B\+TREE|LSM-TREE|SSTABLE|SHARDING|PARTITIONING|REPLICATION|LEADERLESS|SINGLE-LEADER|CONSISTENT HASHING|INDEX SCAN|BITMAP INDEX SCAN|INDEX SEEK|TABLE SCAN|EXPLAIN ANALYZE|POSTGRES|MYSQL|INNODB|SQLITE|CURSOR|BLOOM FILTER)\b', content, re.IGNORECASE)
                    unique_kw = sorted(list(set([k.upper() for k in keywords])))
                    
                    if subtopics:
                        outline_lines.append("- **Subtopics & Key Concepts**:\n")
                        for st in subtopics:
                            outline_lines.append(f"{st}\n")
                    
                    if unique_kw:
                        outline_lines.append(f"- *Key Engine Mechanisms*: `{', '.join(unique_kw[:12])}`\n")
                    
                    outline_lines.append("\n")
                except Exception as e:
                    outline_lines.append(f"- *Error reading: {e}*\n\n")
            
            elif f.suffix.lower() in [".pdf", ".pptx", ".odp", ".epub"]:
                outline_lines.append(f"- 📑 **Companion Slide Deck / Book**: `{f.name}` (`{f_rel}`)\n\n")
            elif f.suffix.lower() in [".sql", ".txt"]:
                outline_lines.append(f"- 💻 **Companion Script / Command File**: `{f.name}` (`{f_rel}`)\n\n")

        index["sections"].append(sec_dict)
        outline_lines.append("---\n\n")

    # Write toc.json
    REFERENCES_DIR.mkdir(parents=True, exist_ok=True)
    with open(REFERENCES_DIR / "toc.json", "w", encoding="utf-8") as jf:
        json.dump(index, jf, indent=2)

    # Write references/table_of_contents.md
    with open(REFERENCES_DIR / "table_of_contents.md", "w", encoding="utf-8") as tf:
        tf.write("# withNasser: Table of Contents\n\n")
        for s in index["sections"]:
            tf.write(f"### {s['section_name']}\n")
            for l in s["lectures"]:
                tf.write(f"- [{l['name']}](../../../../{l['relative_path']})\n")
            tf.write("\n")

    # Write full outline in outline/
    OUTLINE_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTLINE_DIR / "withNasser_Complete_Course_Outline.md", "w", encoding="utf-8") as of:
        of.writelines(outline_lines)

    print(f"✅ Generated outlines and indices for withNasser.")

if __name__ == "__main__":
    generate_index_and_outline()
