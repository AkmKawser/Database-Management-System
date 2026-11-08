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

### Rule 6: Skill Reference Grounding & Autonomous Reasoning for Depth
- **Directive**: The agent must always use skills as authoritative reference points, but is **explicitly empowered and required to inject its own reasoning, architectural deep dives, and simplifications** to provide greater insight than the source lecture alone.

### Rule 7: Mandatory Skill Source Attribution & Quotes
- **Directive**: In every `.md` manual or output file generated using skills, the agent **must explicitly quote and cite the exact skill(s), sections, and lecture materials** from which the content was derived (e.g. `> Synthesized from @withBara (Section 01, Lecture 08) & @withNasser (Section 02: ACID)`).

### Rule 8: Continuous Synchronization of the Canonical Folder Structure
- **Directive**: The agent must maintain and continuously update the **latest, complete folder structure tree** inside this document (`chat/finalized chat.md`). Whenever directories are moved, added, or restructured, the canonical architecture diagram in Section 2 must be refreshed immediately to reflect the exact state of the project.

---

## 🏛️ 2. Finalized Repository Architecture & Output Guidelines

### Canonical Repository Folder Structure (Always Kept Up to Date)

```
Database Management System/
├── .agent/
│   └── skills/
│       ├── SkillGenerator/                         # Universal HITL Skill Scaffolder (scripts/, SKILL.md, SkillArchitecture/)
│       ├── SkillsOnFixedResources/                 # Type 1: Textbooks & Static Course Skills
│       │   ├── withBara/                           # SQL Engine Internals (scripts/, references/, SKILL.md, SkillArchitecture/)
│       │   └── withNasser/                         # Database Engineering & Storage (scripts/, references/, SKILL.md, SkillArchitecture/)
│       ├── SkillsOnDynamicResources/               # Type 2: Dynamic Practice & Ingestion Skills
│       │   └── DBMSSkill/                          # Schema modeling, query tuning & question bank manager
│       └── type of skills.md                       # Skill Typology Specification
├── Skills_Input/
│   ├── books/                                      # Curated Textbooks (Fundamentals/, Internals/, Distributed/)
│   ├── udemy/                                      # Video Course Transcripts & Assets
│   │   ├── withBara/                               # 28 Modules, Slides (02_docs/), Scripts (03_scripts/)
│   │   └── withNasser/                             # 18 Sections, Slides, Benchmark Scripts
│   └── Templates/                                  # Mathematical Blueprints & Step-by-Step Problem Solving
│       ├── Relational_Schema_Normalization_Template.md # 1NF -> 2NF -> 3NF -> BCNF derivations
│       └── Query_Optimization_&_Index_Template.md      # EXPLAIN ANALYZE, selectivity, composite indexing
├── Skills_Output/
│   ├── query/                                      # 🌟 UNIFIED QUERY HUB (All Single & Combined Syntheses)
│   │   ├── Query_Hub_README.md                     # Master index table of all generated manuals
│   │   ├── 001_sql_logical_execution_order_internals.md
│   │   ├── 002_types_of_sql_commands.md
│   │   └── 003_dcl_tcl_acid_properties_internals.md
│   ├── withBara_output/
│   │   ├── outline/                                # Deep curriculum outlines
│   │   │   └── withBara_Complete_Course_Outline.md
│   │   └── withBara_Output_README.md               # Resource Hub
│   ├── withNasser_output/
│   │   ├── outline/
│   │   │   └── withNasser_Complete_Course_Outline.md
│   │   └── withNasser_Output_README.md
│   └── DBMSSkill_output/
│       ├── Problem Files/                          # Ingestion staging & Master Question Bank
│       │   ├── Source of Problem/put the file here/
│       │   ├── problem formatting.md
│       │   └── question bank.md
│       └── Solution Files/                         # Categorized multi-dialect SQL solutions
│           └── Solution formatting.md
├── Upcoming Updates/
│   └── Upcoming Updates.md                         # Milestones & Feature Roadmap
├── chat/
│   ├── chat.md                                     # Chronological conversation & implementation log (Sessions 1 to N)
│   └── finalized chat.md                           # Single source of truth for Universal Rules & Directives
└── README.md                                       # Master navigation hub with vertical badge layout
```

---

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
- **Rule**: The **Skill Outputs Hub** must be the **very first section** at the top of [`README.md`](../README.md) right below the title header, arranged in a **single-column vertical structure** (one badge per line).
- **Badge Nomenclature**: Query badges must use the clean convention **`Query 1`**, **`Query 2`**, **`Query 3`** (without symbols or leading zeroes like `⚡` or `00`).
- **Direct Links**:
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

