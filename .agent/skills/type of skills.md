# Paradigms of Agent Skills in Database Management System (DBMS)

In the **Database Management System** architecture, agent skills are modular, deterministic capabilities that connect agentic AI models directly to authoritative database theory, storage engine internals, formal relational algebra, query optimization templates, and standardized problem/solution pipelines.

Following the engineering standard established in `Science_Of_Coding`, skills are categorized into two primary paradigms:
1. **Type 1: Database Reference Skills (`SkillsOnFixedResources`)**
2. **Type 2: Dynamic Modeling & Query Skills (`SkillsOnDynamicResources`)**

---

## 📚 Type 1: Database Reference Skills (`SkillsOnFixedResources`)

### 1. Concept & Purpose
A **Database Reference Skill** encapsulates an entire textbook, academic monograph, or educational course (e.g. Udemy course transcripts) into a structured, agent-executable knowledge base. Rather than loading massive PDF text dumps into LLM context (which induces high latency, hallucinations, and context dilution), the skill organizes the literature into:
1. **Mandatory Deep Outlines (`Skills_Output/<skill>_output/outline/`)**: An exhaustive, hierarchical map listing every section, lecture/chapter, subtopic, and sub-subtopic. This provides an instant search index for the user to discover covered concepts.
2. **Machine-Readable Routing Maps**: Structural indices (`table_of_contents.md`, `toc.json`) enabling zero-token navigation down to chapter, section, and page ranges.
3. **Surgical Page Extraction CLI**: Dedicated Python scripts (`query_dbms_book.py` / `query_withbara.py`) that extract exact page windows or lecture transcript passages.
4. **Collaborative Trade-off Protocols**: When designing a database schema, storage tier, or query plan with multiple valid trade-offs (e.g., B+ Tree vs. LSM-Tree; 3NF vs. Denormalized Star Schema; Optimistic vs. Pessimistic Concurrency), the agent **must** present trade-offs to the developer and confirm the path before implementation.

### 2. Standardized Output Structure for `SkillsOnFixedResources`
Every fixed resource skill adheres to the following output folder architecture:
```
Skills_Output/<skill_name>_output/
├── outline/                 # Exhaustive curriculum/book breakdown with all subtopics
│   └── <skill>_Complete_Course_Outline.md
├── query/                   # Generated topic manuals & execution deep-dives
│   └── <NNN>_<topic_name>.md
└── <skill>_Output_README.md # Master output index and navigation badges
```

### 2. Concrete Examples for DBMS
- **`silberschatz_dbms`**: Covers core relational theory, relational algebra, SQL DDL/DML semantics, functional dependencies, 3NF/BCNF normalization algorithms, and ACID crash recovery.
- **`ddia_internals`**: Covers storage engines (SSTables, LSM, B-Trees), replication models (single-leader, multi-leader, leaderless), partitioning/sharding, consensus protocols (Raft/Paxos), and isolation levels (Read Committed, Repeatable Read, SSI).

---

## 🛠️ Type 2: Dynamic Modeling & Query Skills (`SkillsOnDynamicResources`)

### 1. Concept & Purpose
A **Dynamic DBMS Skill** manages the ingestion, classification, schema modeling, query synthesis, and index tuning of real-world database problems and challenges gathered from production setups, interview banks, online judges (LeetCode SQL, HackerRank, StrataScratch), and system design prompts.

The skill enforces:
1. **Multi-Source Ingestion**:
   - **Local Workbooks**: Staging documents for raw problem statements, entity lists, or business requirements.
   - **Document Drops**: Ingestion directory (`put the file here/`) for offline ER diagrams, problem PDFs, schema dumps (`schema.sql`), and sample CSV datasets.
   - **Platform Challenges**: Problem sets from SQL challenge platforms, query tuning benchmarks, and enterprise schema specs.
2. **Dynamic 2-Tier Hierarchical Classification (HITL)**:
   - Reads categories from dynamic taxonomies (`dbms categories.docx` or Markdown definitions).
   - Prompts the user interactively (Human-in-the-Loop) to verify the **Primary Category** (e.g., *Relational Modeling*, *Query Optimization*, *Transactions & Concurrency*, *Distributed Storage*) and **Subcategory** (e.g., *3NF Decomposition*, *Index Selectivity*, *Deadlock Prevention*, *Sharding Keys*) before committing records.
3. **Non-Destructive Archival Protocol**:
   - Preserves clean problem specifications with formal functional dependencies, volume constraints, read/write ratios, and sample datasets in `question bank.md`.
   - Raw source files and notes are **never deleted** without explicit confirmation.
4. **Mandatory Template Synthesis & Dialect-Separated Outputs**:
   - Every solution is synthesized using an authoritative template under `Skills_Input/Templates/`.
   - Produces separated dialects (e.g., `<ID>_postgres.sql`, `<ID>_mysql.sql`) and a comprehensive mathematical derivation (`<ID>_derivation.md`) containing relational algebra, ER diagrams, query cost explanations (`EXPLAIN ANALYZE`), and index recommendations.

### 2. Concrete Implementation: `DBMSSkill`
- **Location**: `.agent/skills/SkillsOnDynamicResources/DBMSSkill/`
- **Controls**: Problem staging, queue ingestion, interactive HITL category validation, question bank updates, and dialect-separated solution generation.

---

## ⚖️ Summary Comparison

| Dimension | Type 1: Fixed Resource Skills (`SkillsOnFixedResources`) | Type 2: Dynamic Resource Skills (`SkillsOnDynamicResources`) |
| :--- | :--- | :--- |
| **Primary Focus** | Authoritative theory, formal proofs, engine mechanics, algorithmic invariants | Problem ingestion, schema modeling, query authoring, benchmark verification |
| **Target Data Source** | Curated textbooks, academic papers, official engine internal manuals | Dynamic user input, problem sets, business specs, SQL queries, raw CSVs/DDLs |
| **Extraction Method** | CLI page-range extractor via Table-of-Contents routing | Phased ingestion pipelines and staging doc readers |
| **Human-in-the-Loop** | Proactive architectural trade-off alignment before coding | Interactive Primary/Subcategory classification confirmation |
| **Output Destination** | `Skills_Output/<SkillName>_output/query/` (Theory manuals & roadmaps) | `Skills_Output/DBMSSkill_output/Solution Files/<Category>/<Subcategory>/` |

