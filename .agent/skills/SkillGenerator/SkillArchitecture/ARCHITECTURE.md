# Architecture & Operational Mechanics: `SkillGenerator`

## 1. System Overview

The **`SkillGenerator`** is a meta-skill designed to eliminate manual boilerplate creation and guarantee that every newly added skill adheres to the architecture of `Science_Of_Coding` and `Database Management System`.

---

## 2. Supported Skill Paradigms

```mermaid
flowchart TD
    UserPrompt["User: 'Make a skill for this new book / course / problem set'"] --> HITL{"Human-in-the-Loop Dialog:<br/>Which Type of Skill?"}
    
    HITL -->|Type 1: Fixed Resource| FixedBranch["Fixed Resource Skill (SkillsOnFixedResources)<br/>- Textbooks, Udemy courses, PDF manuals<br/>- Outputs: outline/ + query/"]
    HITL -->|Type 2: Dynamic Resource| DynamicBranch["Dynamic Resource Skill (SkillsOnDynamicResources)<br/>- Problem sets, practice challenges<br/>- Outputs: Problem Files/ + Solution Files/"]

    FixedBranch --> GenCLI["Run scripts/generate_skill.py"]
    DynamicBranch --> GenCLI

    GenCLI --> Scaffold["1. Create .agent/skills/<Type>/<Name>/<br/>2. Create SkillArchitecture/ (ARCHITECTURE.md + README.md)<br/>3. Create scripts/ & references/<br/>4. Create Skills_Output/<Name>_output/"]
    
    Scaffold --> Sync["5. Update README.md navigation badges<br/>6. Record session in chat.md<br/>7. Git commit & push"]

    classDef stage fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#f8fafc;
    class UserPrompt,HITL,FixedBranch,DynamicBranch,GenCLI,Scaffold,Sync stage;
```

---

## 3. Structural Matrix Comparison

| Output Folder | Type 1 (`SkillsOnFixedResources`) | Type 2 (`SkillsOnDynamicResources`) |
| :--- | :--- | :--- |
| **`.agent/skills/.../`** | `SkillsOnFixedResources/<Name>/` | `SkillsOnDynamicResources/<Name>/` |
| **`SkillArchitecture/`** | `ARCHITECTURE.md` + `<Name>_Architecture_README.md` | `ARCHITECTURE.md` + `<Name>_Architecture_README.md` |
| **References / Setup** | `table_of_contents.md` + `toc.json` | `dbms categories.docx` + `problem formatting.md` |
| **Scripts** | `query_<name>.py` (keyword / page extractor) | `ingest_manager.py` (queue reader & HITL parser) |
| **`Skills_Output/`** | `<Name>_output/outline/` & `<Name>_output/query/` | `<Name>_output/Problem Files/` & `Solution Files/` |
| **Master Index** | `<Name>_Output_README.md` | `question bank.md` & `<Name>_Output_README.md` |
