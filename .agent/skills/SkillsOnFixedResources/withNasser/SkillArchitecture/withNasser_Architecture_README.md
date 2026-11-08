# Skill Architecture & Usage Instructions: `withNasser`

This document defines the technical architecture, execution pipeline, and usage guidelines for the **`withNasser`** skill.

---

## 🏛️ System Architecture

The `withNasser` skill connects any agentic AI system to domain knowledge without suffering from context exhaustion, token window degradation, or hallucinations.

## 📖 Operational Instructions for Agents

1. **Surgical Search First**: Never answer from memory alone. Run `scripts/query_withnasser.py "<topic>"` to retrieve verified citations.
2. **Deep Outline Verification**: Check `Skills_Output/withNasser_output/outline/` for exact section and topic matches.
3. **Standardized Manual Output**: Output all requested topics into `Skills_Output/withNasser_output/query/<NNN>_<topic>.md`.
