# Solution Formatting Specification

Every solved problem or design challenge in `Solution Files/` must follow this standardized multi-file structure separated by engine and mathematical derivation.

---

## Directory Organization

```
Solution Files/
└── <Primary Category>/
    └── <Subcategory>/
        ├── <ID>_postgres.sql     # PostgreSQL Production Solution
        ├── <ID>_mysql.sql        # MySQL / Alternate Engine Solution
        └── <ID>_derivation.md    # Formal Derivation, Plan Analysis & Trade-offs
```

---

## `<ID>_derivation.md` Schema

```markdown
# [ID] <Problem Title> - Derivation & Architecture Manual

## 1. Mathematical / Theoretical Formulation
- Formal Relational Algebra query or Functional Dependency derivation.
- Invariants & Normal Form verification (if schema design).

## 2. Collaborative Design Trade-offs
- Option A: (e.g. Normalization vs. Denormalization with materialized views)
- Option B: (e.g. B+ Tree indexing vs. Partitioning)
- Decision Rationale: Why Option A/B was chosen given constraints.

## 3. Execution Plan Dissection (`EXPLAIN ANALYZE`)
- Cost breakdown, scan types, buffer usage, and memory impact.

## 4. Multi-Dialect Implementations
- Key dialect differences (e.g., PostgreSQL `DISTINCT ON`, `FILTER(WHERE...)` vs. MySQL window syntax).
- Cross-database compatibility notes.

## 5. Failure Modes & Edge Case Auditing
- NULL handling, concurrency locks, transaction race conditions, zero-row edge cases.
```

