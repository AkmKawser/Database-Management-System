#!/usr/bin/env python3
"""
scripts/audit_rendering.py
Universal Zero-Failure Markdown & Diagram Rendering Auditor

Optimized Single-Pass (O(N)) Validator:
1. Git-Aware Diff Detection: Reads only changed/staged Markdown files via git status/diff.
   Falls back to auditing all files if requested via '--all'.
2. Single-Pass Token Scanning:
   - Tracks code fence state (``` or ````).
   - Tracks Mermaid block boundaries.
   - Detects raw dollar signs ($) in prose (outside backticks and code blocks).
   - Detects raw HTML tags (<br>, <b>, etc.) inside Mermaid diagram nodes.
   - Detects broken KaTeX escape sequences and unbalanced code fences.
   - Verifies relative image paths exist on disk.
"""

import sys
import re
import subprocess
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

def get_target_files(all_files: bool = False) -> list[Path]:
    """Gets markdown files to audit using git diff/status for O(1) file scaling."""
    if all_files:
        return sorted(list(ROOT_DIR.glob("**/*.md")))

    # Get changed/untracked markdown files via git
    try:
        res = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=ROOT_DIR,
            capture_output=True,
            text=True,
            check=True
        )
        changed_paths = []
        for line in res.stdout.strip().split("\n"):
            if not line:
                continue
            path_str = line[3:].strip()
            # Handle renames e.g. R old -> new
            if " -> " in path_str:
                path_str = path_str.split(" -> ")[1].strip()
            p = ROOT_DIR / path_str
            if p.suffix.lower() == ".md" and p.exists():
                changed_paths.append(p)
        
        # If no uncommitted files, audit query/ and chat/ by default
        if not changed_paths:
            query_files = list((ROOT_DIR / "Skills_Output" / "query").glob("*.md"))
            return sorted(query_files)
        return sorted(changed_paths)
    except Exception:
        # Fallback to all query files
        return sorted(list((ROOT_DIR / "Skills_Output" / "query").glob("*.md")))

def audit_file(file_path: Path) -> list[str]:
    """Audits a single markdown file in one linear pass O(Lines)."""
    errors = []
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        return [f"Unable to read file: {e}"]

    lines = content.split("\n")
    in_code_block = False
    in_mermaid = False
    fence_count = 0
    
    for line_idx, line in enumerate(lines, start=1):
        stripped = line.strip()
        
        # 1. Code Fence Tracking
        if stripped.startswith("```"):
            fence_count += 1
            if in_code_block:
                in_code_block = False
                in_mermaid = False
            else:
                in_code_block = True
                if stripped.startswith("```mermaid"):
                    in_mermaid = True
            continue
            
        # 2. Mermaid Internal Syntax Checks
        if in_mermaid:
            # Check for illegal HTML tags in Mermaid labels (<b>, <br>, <i>, etc.)
            html_tags = re.findall(r"</?(?:b|i|br|span|div|p|strong|em)[^>]*>", line, re.IGNORECASE)
            if html_tags:
                errors.append(f"Line {line_idx}: Raw HTML tags {html_tags} found inside Mermaid diagram block.")
            continue
            
        # 3. Code Block Internal (Skip prose checks for code blocks)
        if in_code_block:
            continue
            
        # 4. Prose Checks (Outside code blocks)
        # Strip inline backtick code spans before scanning prose
        clean_prose = re.sub(r"`[^`]*`", "", line)
        
        # Detect raw unescaped dollar signs ($) in prose
        if "$" in clean_prose:
            errors.append(f"Line {line_idx}: Raw unescaped '$' found in prose text: '{line.strip()}'")
            
        # Detect broken pseudo-math KaTeX escape sequences (e.g. \to, \alpha, \frac, \begin)
        # Avoid flagging Windows directory backslashes (e.g. \Users, \withBara)
        if re.search(r"\\[a-zA-Z]{3,}", clean_prose):
            latex_keywords = {"frac", "sqrt", "alpha", "beta", "gamma", "sum", "int", "times", "cdot", "begin", "end", "theta", "rightarrow", "leftarrow", "partial"}
            found = [kw for kw in latex_keywords if f"\\{kw}" in clean_prose]
            if found:
                errors.append(f"Line {line_idx}: Unescaped LaTeX math command {found} in prose: '{line.strip()}'")
            
        # 5. Relative Image Existence Check
        image_matches = re.findall(r"!\[.*?\]\((?!https?://)(.*?)\)", line)
        for img_rel in image_matches:
            clean_rel = img_rel.split()[0].strip()
            # resolve relative to file location
            target_img = (file_path.parent / clean_rel).resolve()
            if not target_img.exists():
                errors.append(f"Line {line_idx}: Broken local image reference '{clean_rel}' (Path not found: {target_img})")

    # 6. Fence Parity Check
    if fence_count % 2 != 0:
        errors.append(f"Unbalanced code fences! Total '```' count is {fence_count} (must be even).")

    return errors

def main():
    check_all = "--all" in sys.argv
    files = get_target_files(all_files=check_all)
    
    total_files = len(files)
    failed_files = 0
    all_issues = []

    print(f"[*] Running Optimized Single-Pass Rendering Auditor on {total_files} file(s)...")

    for f in files:
        rel_path = f.relative_to(ROOT_DIR)
        issues = audit_file(f)
        if issues:
            failed_files += 1
            print(f"[FAIL] {rel_path}")
            for iss in issues:
                print(f"       - {iss}")
            all_issues.append((rel_path, issues))
        else:
            print(f"[OK]   {rel_path}")

    print("=" * 60)
    if failed_files == 0:
        print(f"[SUCCESS] All {total_files} file(s) passed the Zero-Failure Rendering Audit.")
        sys.exit(0)
    else:
        print(f"[ERROR] {failed_files} of {total_files} file(s) failed the audit.")
        sys.exit(1)

if __name__ == "__main__":
    main()
