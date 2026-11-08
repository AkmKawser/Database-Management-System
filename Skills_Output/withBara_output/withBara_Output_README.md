# `withBara_output` Query Hub & Manual Archive

This directory stores in-depth, lecture-grounded manuals explaining how SQL works internally, based on the **withBara** 30-Hour SQL Bootcamp and its companion slides, schemas, and SQL scripts.

---

## 📑 Generated Query Manuals Index

| Query ID | Topic / Manual Title | Source Section | Companion Slides / Script | Status |
| :---: | :--- | :--- | :--- | :---: |
| `001` | [SQL Logical Execution Order & Internal Engine Processing](query/001_sql_logical_execution_order_internals.md) | `02_SELECT Query` | `02_Query_Data_SELECT.pdf` / `01_Query_Data_SELECT.sql` | ✅ Published |

---

## 🧭 Generation Guidelines

Every manual in `query/` is generated using the [`withBara` Agent Skill](../../.agent/skills/SkillsOnFixedResources/withBara/SKILL.md) and incorporates:
- **Course Transcript Intuition**: Plain-English teaching style matching the course author.
- **Engine Execution Pipeline**: Step-by-step memory/filter passes (Mermaid diagram).
- **Execution vs. Coding Order**: Why specific clauses fail or succeed based on engine timing.
- **Companion Resources**: Cross-referencing `Resources/02_docs/` and `Resources/03_scripts/`.

