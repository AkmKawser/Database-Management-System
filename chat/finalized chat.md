# Finalized Operational Rules & Architectural Directives

This document stores all **Universal Rules** and **Finalized Operational Guidelines** that the AI Agent **must always follow** across every interaction, prompt, code change, and session in this repository.

Whenever the user provides an instruction that is later modified or refined, only the **most up-to-date, finalized version** is recorded here to maintain a clear single source of truth.

---

## 🌐 1. Universal Rules (Mandatory for Every Prompt & Action)

These rules are permanent operational constraints. The agent must enforce them proactively on every step:

### Rule 1: Continuous Conversation Logging
- **Directive**: Every interaction, prompt, architectural decision, and action must be systematically recorded in [`chat/chat.md`](chat.md) in chronological session format.
- **Enforcement**: Never complete a turn involving project updates without appending the session details to `chat/chat.md`.

### Rule 2: Strict Rendering & Formatting Audit (Images & LaTeX Math)
- **Directive**: Always double-check and audit all Markdown files for rendering integrity before finalizing changes:
  1. **LaTeX Math & Dollar Signs**: In prose, escape every literal dollar sign with a backslash (e.g. `\$500`, not `$500`). Unescaped dollar signs cause KaTeX parsers to collapse entire paragraphs into corrupted math blocks.
  2. **Image & File Embed Links**: Ensure all referenced images (e.g. `.png`, `.jpg`, diagrams) use valid relative paths that resolve on disk.
  3. **Mermaid Diagrams**: Quote node labels containing special characters (parentheses, brackets, colons) to prevent parser crashes.
  4. **HTML / Markdown Hygiene**: Ensure all `<details>`, `<table>`, and code fences are properly balanced and closed.

### Rule 3: Git Synchronization Guarantee
- **Directive**: Whenever files are created, updated, or reorganized, verify git status, commit with clean semantic messages, and push directly to `origin/main` so GitHub is always 100% in sync.

### Rule 4: Human-in-the-Loop (HITL) for Architectural Choices
- **Directive**: The agent must never unilaterally guess categories or pick arbitrary designs when trade-offs exist (e.g. skill types, schema normalization levels, indexing structures). Present options with trade-offs and seek explicit user confirmation.

### Rule 5: Non-Destructive Ingestion & Zero Data Loss
- **Directive**: Raw source files, staging workbooks, or challenge documents dropped into `put the file here/` or `write here.docx` must **never** be deleted or cleared until the extracted entry is 100% verified inside `question bank.md`.

---

## 🏛️ 2. Finalized Repository Architecture & Output Guidelines

### Finalized Rule on Query Hub Structure:
- **Rule**: There is **only ONE centralized query folder** in the repository:
  [`Skills_Output/query/`](../Skills_Output/query/)
- **Reasoning**: A query may require more than one Udemy course, a blend of textbooks, or a mix of theoretical skills and dynamic problem benchmarks (e.g. `withBara` for SQL syntax + `withNasser` for storage engine internals + `DBMSSkill` for real-world scenarios).
- **Enforcement**: Never create individual `query/` folders inside individual skill outputs. All deep-dive query manuals must be placed in `Skills_Output/query/<NNN>_<topic>.md` and registered in [`Skills_Output/query/Query_Hub_README.md`](../Skills_Output/query/Query_Hub_README.md).

### Finalized Rule on Fixed Resource Outlines:
- **Rule**: Every Type 1 skill (`SkillsOnFixedResources`) must maintain an exhaustive, hierarchical curriculum outline in:
  `Skills_Output/<skill_name>_output/outline/<skill_name>_Complete_Course_Outline.md`
- **Coverage**: Must list all Sections, Lectures, Headings, Subtopics, Slide Decks, and Companion Scripts to enable zero-token topic discovery.

### Finalized Rule on README Navigation:
- **Rule**: The **Skill Outputs Hub** must be the **very first section** at the top of [`README.md`](../README.md) right below the title header, providing direct button links to:
  1. Universal Query Output Hub (`Query_Hub_README.md` and query badges).
  2. `DBMSSkill` Outputs (Question Bank, Solution Archive, Formatting Specs).
  3. Curriculum Outlines (`withBara`, `withNasser`).
  4. System Tools (`SkillGenerator`, Roadmap, Chat Logs).

---

## 🧠 3. Finalized Manual Authorship & Reasoning Standards

### Rule on Blending Course Knowledge with Engineering Insights:
- **Directive**: Using skills does not restrict the agent to reciting course lecture notes. The agent is **explicitly mandated to add its own engineering reasoning**, simplify difficult mechanics, and inject architectural insights into every manual:
  - Add formal state machine models (e.g. Transaction lifecycle states).
  - Add storage layer physics (RAM Buffer Pool, OS cache traps, `fsync()`, Dirty pages, Slotted pages).
  - Add concurrency anomaly deep-dives (Dirty reads, Non-repeatable reads, Phantom reads, Lost updates).
  - Compare engine dialect differences (e.g. PostgreSQL tuple versioning vs. MySQL InnoDB Undo logs).
  - Include ASCII matrices and visual Mermaid flowcharts/sequence diagrams.
