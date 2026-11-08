# Skill Architecture & Usage Instructions: `SkillGenerator`

This document defines the technical execution steps for generating new agent skills using **`SkillGenerator`**.

---

## 🏛️ Operational Steps

1. **Activate Generator**:
   ```bash
   python .agent/skills/SkillGenerator/scripts/generate_skill.py --type <fixed|dynamic> --name <Name> --source-path <SourcePath>
   ```
2. **Review Output**:
   Verify that all required files (`SKILL.md`, `SkillArchitecture/`, `references/`, `scripts/`, `Skills_Output/`) were correctly formed.
3. **Link to Repository Navigation**:
   Update `README.md` and log the conversation session in `chat.md`.
