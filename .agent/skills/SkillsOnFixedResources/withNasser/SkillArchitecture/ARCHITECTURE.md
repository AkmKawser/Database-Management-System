# Architecture & Operational Mechanics: `withNasser` Skill

## 1. System Overview & Purpose

The **`withNasser`** skill is a portable, self-contained, agent-agnostic knowledge and retrieval module encapsulating:
* **Resource Type**: Udemy Course (Database Engineering & Internals by Hussein Nasser)
* **Source Path**: `Skills_Input/udemy/withNasser`
* **Architecture Standard**: SkillsOnFixedResources (Type 1)

---

## 2. Directory Layout

```
.agent/skills/SkillsOnFixedResources/withNasser/
├── SkillArchitecture/
│   ├── ARCHITECTURE.md                  <-- Technical specifications (this file)
│   └── withNasser_Architecture_README.md  <-- High-level overview & agent execution rules
├── SKILL.md                             <-- Universal agent entrypoint & query decision rules
├── references/
│   ├── table_of_contents.md             <-- Fast human & agent topic index
│   └── toc.json                         <-- Machine-readable outline tree
└── scripts/
    └── query_withnasser.py        <-- Precision CLI search & extraction
```

---

## 3. High-Level Architecture Diagram

```mermaid
flowchart TD
    User([User Prompt / Topic Request]) --> Agent[Agentic AI Engine]
    
    subgraph KnowledgeSources["Tri-Source Knowledge Ingestion"]
        direction TB
        SourceData["Source Material (Skills_Input/udemy/withNasser)"]
        Router["Zero-Token Fast Router<br/>(table_of_contents.md / toc.json)"]
        CLISearch["Precision CLI Search<br/>(python query_withnasser.py)"]
        
        Router --> CLISearch
        SourceData --> CLISearch
        
        LLM["Pre-trained Reasoning & Memory"]
        Web["Targeted Web Search & Docs"]
    end
    
    Agent --> KnowledgeSources
    
    subgraph SynthesisLayer["Analysis & Synthesis Layer"]
        direction TB
        Step1["Analyze Theoretical Foundations & Invariants"]
        Step2["Dissect Engine Operations / Relational Algebra"]
        Step3["Synthesize Visual Architecture Diagram (Mermaid)"]
        Step1 --> Step2 --> Step3
    end
    
    KnowledgeSources --> SynthesisLayer
    SynthesisLayer --> Output["Standardized Query Output<br/>(Skills_Output/withNasser_output/query/<NNN>_<topic>.md)"]
```
