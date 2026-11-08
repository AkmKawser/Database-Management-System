"""
Generate an exhaustive, hierarchical outline of the withBara course,
capturing all Sections, Lectures, Headings (H2, H3, H4), and Key Concepts.
"""

import os
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[5]
COURSE_DIR = BASE_DIR / "Skills_Input" / "udemy" / "withBara"
OUTLINE_DIR = BASE_DIR / "Skills_Output" / "withBara_output" / "outline"
RESOURCES_DIR = COURSE_DIR / "Resources"

def generate_complete_outline():
    sections = sorted([d for d in COURSE_DIR.iterdir() if d.is_dir() and d.name != "Resources"])
    
    outline_lines = []
    outline_lines.append("# withBara: Complete Course Curriculum & Deep Topic Outline\n")
    outline_lines.append("> **Course**: The Complete SQL Bootcamp (30 Hours): Go from Zero to Hero\n")
    outline_lines.append("> **Instructor**: Basel (Big Data & Data Engineering Lead at Mercedes-Benz)\n")
    outline_lines.append("> **Coverage**: Exhaustive index of all 28 sections, lectures, subtopics, and companion resources for surgical searching and query retrieval.\n\n")
    outline_lines.append("---\n\n")
    outline_lines.append("## ⚡ Fast Jump Table of Contents\n\n")

    for s_idx, sec in enumerate(sections, 1):
        clean_name = sec.name
        anchor = clean_name.lower().replace(" ", "-").replace("&", "").replace("(", "").replace(")", "").replace(",", "")
        anchor = re.sub(r'[^a-z0-9\-]', '', anchor)
        outline_lines.append(f"{s_idx}. [{clean_name}](#{anchor})\n")
    
    outline_lines.append(f"{len(sections)+1}. [Curated Companion Resources (Slides, Datasets, Scripts)](#curated-companion-resources)\n")
    outline_lines.append("\n---\n\n")

    # Now iterate each section and every lecture
    for s_idx, sec in enumerate(sections, 1):
        outline_lines.append(f"## {sec.name}\n\n")
        lectures = sorted([f for f in sec.glob("*.md")])
        
        for l_idx, lec in enumerate(lectures, 1):
            lec_name = lec.stem
            outline_lines.append(f"### {lec_name}\n")
            outline_lines.append(f"- **File**: `{lec.relative_to(BASE_DIR).as_posix()}`\n")
            
            # Read content to extract headings and key conceptual topics
            try:
                with open(lec, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                    
                # Extract markdown headings inside lecture
                headings = re.findall(r'^(#{2,4})\s+(.+)$', content, flags=re.MULTILINE)
                subtopics = []
                if headings:
                    for level, title in headings:
                        indent = "  " * (len(level) - 1)
                        subtopics.append(f"{indent}- **{title.strip()}**")
                
                # If no explicit headings, extract key bulleted points or concepts from first few lines / keywords
                if not subtopics:
                    # Look for keywords like "In this lecture", "We will cover", or key SQL clauses
                    keywords = re.findall(r'\b(SELECT|FROM|WHERE|GROUP BY|HAVING|ORDER BY|DISTINCT|TOP|JOIN|INNER JOIN|LEFT JOIN|RIGHT JOIN|FULL JOIN|CROSS JOIN|UNION|UNION ALL|INTERSECT|EXCEPT|PARTITION BY|OVER|ROW_NUMBER|RANK|DENSE_RANK|LEAD|LAG|FIRST_VALUE|LAST_VALUE|CTE|WITH|VIEW|TEMPORARY TABLE|INDEX|CLUSTERED|NON-CLUSTERED|PARTITION|TRANSACTION|COMMIT|ROLLBACK|SARGABLE|STORED PROCEDURE|TRIGGER)\b', content, re.IGNORECASE)
                    unique_kw = sorted(list(set([k.upper() for k in keywords])))
                    if unique_kw:
                        subtopics.append(f"  - *Core Concepts / Syntax*: `{', '.join(unique_kw[:10])}`")
                    else:
                        subtopics.append("  - *Lecture Notes & Walkthrough*")
                
                outline_lines.append("- **Subtopics & Key Concepts**:\n")
                for st in subtopics:
                    outline_lines.append(f"{st}\n")
                outline_lines.append("\n")
            except Exception as e:
                outline_lines.append(f"- *Error reading lecture: {e}*\n\n")
        
        outline_lines.append("---\n\n")

    # Add Companion Resources
    outline_lines.append("## Curated Companion Resources\n\n")
    if RESOURCES_DIR.exists():
        docs = sorted([f for f in (RESOURCES_DIR / "02_docs").glob("*")])
        scripts = sorted([f for f in (RESOURCES_DIR / "03_scripts").glob("*.sql")])
        
        outline_lines.append("### 📑 Presentation Decks & Architecture Diagrams (`Resources/02_docs`)\n\n")
        for d in docs:
            outline_lines.append(f"- **{d.name}** (`{d.relative_to(BASE_DIR).as_posix()}`)\n")
        outline_lines.append("\n")
        
        outline_lines.append("### 💻 Reference SQL Implementations (`Resources/03_scripts`)\n\n")
        for sc in scripts:
            outline_lines.append(f"- **{sc.name}** (`{sc.relative_to(BASE_DIR).as_posix()}`)\n")
        outline_lines.append("\n")

    OUTLINE_DIR.mkdir(parents=True, exist_ok=True)
    outline_file = OUTLINE_DIR / "withBara_Complete_Course_Outline.md"
    with open(outline_file, "w", encoding="utf-8") as f:
        f.writelines(outline_lines)
    
    print(f"Exhaustive outline generated at {outline_file}")

if __name__ == "__main__":
    generate_complete_outline()

