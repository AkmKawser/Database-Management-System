# Skill Architecture & Usage Instructions: `withBara`

This document defines the technical architecture, execution pipeline, and usage guidelines for the **`withBara`** database & SQL internals skill.

---

## 🏛️ System Architecture

The `withBara` skill connects any agentic AI system to deep SQL internals knowledge without suffering from context exhaustion, token window degradation, or hallucinations.

```mermaid
flowchart TD
    User(["User Prompt / SQL Topic Request"]) --> Agent["Agentic AI System"]
    
    subgraph KnowledgeSources["Tri-Source Knowledge Ingestion"]
        direction TB
        Transcripts["28 Course Modules Transcripts - Skills_Input/udemy/withBara/"]
        CompanionResources["Companion Resources - 16 PDF Slides (02_docs/) and 31 SQL Scripts (03_scripts/)"]
        Router["Zero-Token Fast Router - table_of_contents.md / toc.json"]
        CLISearch["Precision Search CLI - python query_withbara.py"]
        
        Router --> CLISearch
        Transcripts --> CLISearch
        CompanionResources --> CLISearch
        
        LLM["Pre-trained Engine Reasoning and Memory"]
        Web["Targeted Web Search and Docs"]
    end
    
    Agent --> KnowledgeSources
    
    subgraph ExecutionAnalysis["Execution and Internal Mechanics Layer"]
        direction TB
        Step1["Analyze Logical Execution Order vs Coding Order"]
        Step2["Dissect Storage Engine Operations (Buffer, WAL, Locking)"]
        Step3["Synthesize Visual Pipeline Diagram (Mermaid)"]
        Step4["Cross-reference 10_SQL_30_Performance_Tips.pdf"]
        Step1 --> Step2 --> Step3 --> Step4
    end
    
    KnowledgeSources --> ExecutionAnalysis
    
    ExecutionAnalysis --> Output["Standardized Query Output - Skills_Output/query/"]
```

---

## 📖 Operational Instructions for Agents

### 1. Dual Ingestion Rule (Transcripts + Resources)
- **Rule**: Never answer from general knowledge alone. The agent **MUST** inspect the spoken `.md` lecture transcript files for the instructor's pedagogical explanation and analogies, while cross-referencing `02_docs/` for slide models and `03_scripts/` for working SQL code.

### 2. Surgical Retrieval via CLI
Instead of dumping full lecture chapters into context, use the precision CLI:
```bash
python .agent/skills/SkillsOnFixedResources/withBara/scripts/query_withbara.py "<topic>"
```

### 3. Output Standardization Protocol
Every manual generated must follow the 6-phase blueprint in [`SKILL.md`](../SKILL.md) and be saved to:
`Skills_Output/withBara_output/query/<NNN>_<topic_name>.md`
And indexed in `Skills_Output/withBara_output/withBara_Output_README.md`.

