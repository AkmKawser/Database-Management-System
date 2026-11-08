---
name: SkillGenerator
description: Interactive Human-in-the-Loop (HITL) skill generator. Generates production-ready agent skills for both Type 1 (Fixed Resources such as Textbooks, Udemy courses, PDF manuals) and Type 2 (Dynamic Resources such as Problem ingestion, question banks, and multi-dialect solutions), adhering to the exact folder structure and architectural standard established in Science_Of_Coding and Database Management System.
---

# Universal Skill Generator (`SkillGenerator`)

The **`SkillGenerator`** is an autonomous capability that interviews the user via Human-in-the-Loop (HITL) dialogues, collects configuration parameters, and scaffolds complete, production-ready agent skills adhering strictly to the repository architecture.

---

## 🎯 When to Activate

Trigger this skill when:
1. The user asks to "make a skill", "generate a skill", or mentions `@SkillGenerator`.
2. A new book, Udemy course, or problem set is added to `Skills_Input/` and requires a dedicated skill module.

---

## 🤝 Phased Human-in-the-Loop (HITL) Workflow

Whenever generating a skill, the agent **MUST** execute the following phased consultation:

### Phase 1: Determine Skill Paradigm (HITL Selection)
Ask the user which paradigm they want to build using the `ask_question` tool or structured prompt:
1. **Type 1: Fixed Resource Skill (`SkillsOnFixedResources`)**
   - For static literature: Curated Textbooks, Udemy Courses, Documentation Drops, or PDF Manuals.
   - Generates: `SKILL.md`, `SkillArchitecture/` (`ARCHITECTURE.md` + `<skill>_Architecture_README.md`), `references/` (`table_of_contents.md` + `toc.json`), `scripts/` (`query_<skill>.py`), and `Skills_Output/<skill>_output/outline/` + `query/`.
2. **Type 2: Dynamic Resource Skill (`SkillsOnDynamicResources`)**
   - For real-time intake: Problem sets, interview challenges, staging workbooks, and solution generators.
   - Generates: `SKILL.md`, `SkillArchitecture/`, `scripts/` (`ingest_manager.py`), and `Skills_Output/<skill>_output/Problem Files/` + `Solution Files/`.

### Phase 2: Collect Domain Specifics
- Skill Identifier Name (e.g., `ddia_internals`, `Silberschatz_DBMS`, `LeetCodeSQL`).
- Source Location in `Skills_Input/` (e.g., `Skills_Input/books/Internals/`).
- Primary target engine / languages (e.g., PostgreSQL, MySQL, SQL Server, Python, Java).

### Phase 3: Automated Scaffolding & Verification
Execute the generator CLI:
```bash
python .agent/skills/SkillGenerator/scripts/generate_skill.py --type <fixed|dynamic> --name <SkillName> --source-path <Path>
```

### Phase 4: Hub & Navigation Synchronization
1. Add new skill navigation badges to root [`README.md`](../../../../README.md).
2. Append task milestones to [`Upcoming Updates/Upcoming Updates.md`](../../../../Upcoming%20Updates/Upcoming%20Updates.md).
3. Record the session in [`chat.md`](../../../../chat.md).
4. Commit and push changes to GitHub.

