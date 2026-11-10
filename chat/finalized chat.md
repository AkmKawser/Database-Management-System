# Finalized Operational Rules & Architectural Directives

This document stores all **Universal Rules** and **Finalized Operational Guidelines** that the AI Agent **must always follow** across every interaction, prompt, code change, and session in this repository.

Whenever the user provides an instruction that is later modified or refined, only the **most up-to-date, finalized version** is recorded here to maintain a clear single source of truth.

---

## 🌐 1. Universal Rules (Mandatory for Every Prompt & Action)

These rules are permanent operational constraints. The agent must enforce them proactively on every step:

### Rule 1: Continuous Conversation Logging
- **Directive**: Every interaction, prompt, architectural decision, and action must be systematically recorded in [`chat/chat.md`](chat.md) in chronological session format.
- **Enforcement**: Never complete a turn involving project updates without appending the session details to `chat/chat.md`.

### Rule 2: Strict Rendering & Formatting Audit (Zero-Failure Policy via Optimized Algorithm)
- **Directive**: Always run or invoke the **Optimized Single-Pass Rendering Auditor** ([`scripts/audit_rendering.py`](../scripts/audit_rendering.py)) before finalizing any prompt or task.
- **The Optimized Verification Algorithm**:
  Rather than sequentially reading and brute-forcing all 500+ files in the repository (which wastes compute and tokens), the agent uses an **event-driven diff-scoped linear algorithm**:
  1. **Git-Aware Diff Scoping**: Inspects `git status --porcelain` to identify only the subset of files modified, added, or staged in the current conversation (`O(1)` file selection instead of `O(TotalFiles)`).
  2. **Single-Pass Stream Tokenizer**: Evaluates each targeted file in a single linear pass (`O(Lines)`) tracking code fences, Mermaid block contexts, and prose tokens simultaneously.
  3. **Zero Dollar Signs in Prose**: Enforces that no raw dollar symbols appear in prose text (uses explicit words like "dollars" or backticked expressions).
  4. **Pure Mermaid Syntax & Mandatory Double-Quoted Node Labels**:
     - Verifies that no raw HTML tags (`<b>`, `<br/>`, `<span>`, `<div>`) are present inside Mermaid node labels.
     - **CRITICAL**: Every Mermaid node label (`Node["Label"]`) and edge label (`-->|"Label"|`) that contains parentheses `()`, colons `:`, slashes `/`, or ampersands `&` **MUST** be wrapped in double quotes! Unquoted parentheses inside `Node[Label (Val: 10)]` trigger GitHub's Mermaid lexer crash (`Expecting 'SQE' ... got 'PS'`).
  5. **Standardized Table Cells**: Enforces clean textual markers (`PREVENTED`, `ALLOWED`) instead of multi-byte emoji symbols that misalign column borders.
  6. **Parity Check**: Asserts that all markdown code fences (```` ``` ````) are strictly balanced (total fence count is even).
  7. **Asset Reference Validation**: Verifies that every local image reference (`! [alt] (path)`) exists on physical disk.
- **CLI Command**: Run `python scripts/audit_rendering.py` (audits active modified/query files) or `python scripts/audit_rendering.py --all` (full repo audit).

### Rule 3: Git Synchronization Guarantee (Automated Commit & Push on Every Prompt)
- **Directive**: The agent must **automatically commit and push to GitHub (`origin/main`)** on every task, prompt, or file creation/update without waiting to be asked. Verify git status, format a clean semantic commit message (`feat:`, `docs:`, `fix:`), and execute `git push origin main` so that GitHub is always 100% in sync with the local workspace.

### Rule 4: Human-in-the-Loop (HITL) for Architectural Choices
- **Directive**: The agent must never unilaterally guess categories or pick arbitrary designs when trade-offs exist (e.g. skill types, schema normalization levels, indexing structures). Present options with trade-offs and seek explicit user confirmation.

### Rule 5: Non-Destructive Ingestion & Zero Data Loss
- **Directive**: Raw source files, staging workbooks, or challenge documents dropped into `put the file here/` or `write here.docx` must **never** be deleted or cleared until the extracted entry is 100% verified inside `question bank.md`.

### Rule 6: Global Rule on Autonomous Reasoning & Pedagogical Simplification
- **Directive**: Using skills as reference **never** restricts the agent from thinking independently. The agent **MUST** inject its own reasoning, analogies, state machine breakdowns, and step-by-step simplifications so that any reader can understand complex database internals effortlessly.
- **Enforcement**: Every manual must blend the instructor's core concepts with the agent's own intuitive explanations, real-world metaphors, and physical storage insights.

### Rule 7: Global Rule on Mandatory Skill & Concept Source Attribution
- **Directive**: Whenever any concept, quote, diagram, or explanation is generated from a skill, the agent **MUST explicitly state the exact skill name, module/section, and lecture file** where that particular concept or text was taken from (e.g. `> **Source Attribution**: Derived from @withBara (Section 01, Lecture 08) and @withNasser (Section 02: ACID)`).
- **Enforcement**: Every major section of a generated manual must include a clear source attribution callout alongside a dedicated synthesis table mapping which skill contributed which concept.

### Rule 8: Continuous Synchronization of the Canonical Folder Structure
- **Directive**: The agent must maintain and continuously update the **latest, complete folder structure tree** inside this document (`chat/finalized chat.md`). Whenever directories are moved, added, or restructured, the canonical architecture diagram in Section 2 must be refreshed immediately to reflect the exact state of the project.

### Rule 9: Mandatory 3-Tier Concept Mapping (Java Code -> Database Query -> Physical Table)
- **Directive**: For **EVERY single concept** discussed, documented, or taught in this repository (e.g., in query manuals, tutorials, architectural syntheses, and problem solutions), the agent **MUST** provide an end-to-end multi-tier demonstration detailing what happens at three distinct layers:
  1. **Coding Level (Strictly Java Only)**: Show the concrete backend application logic in **Java** (e.g., standard JDBC, JPA/Hibernate, or connection pool mechanics such as HikariCP). Demonstrate connection handling, transaction boundaries (`conn.setAutoCommit(false)`, `conn.commit()`, `conn.rollback()`), prepared statements, or entity mappings.
  2. **Database Query Level**: Show the exact raw SQL statement(s) emitted to the database engine (e.g., DDL, DML, DQL, or TCL statements like `BEGIN`, `UPDATE`, `COMMIT`, `SAVEPOINT`). Explain how the engine parses, validates catalog permissions, optimizes, and coordinates locks/snapshots.
  3. **Physical Table / Storage Level**: Show the concrete data table state before, during, and after execution. Illustrate the exact row/tuple transformations, buffer pool page modifications, dirty flags, undo stack chains, and disk file updates with ASCII tables or structured state representations.
- **Enforcement**: No theoretical concept or operational query manual can be considered complete without this explicit **Java Code $\to$ SQL Query $\to$ Physical Table State** breakdown.

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
├── scripts/
│   └── audit_rendering.py                          # ⚡ Optimized Git-Aware Zero-Failure Rendering Auditor
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

