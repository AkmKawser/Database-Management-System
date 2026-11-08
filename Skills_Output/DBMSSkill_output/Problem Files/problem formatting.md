# Problem Formatting Schema

All database challenges, schema design tasks, and query optimization problems ingested into `question bank.md` must adhere to this standardized Markdown schema.

---

## Specification Template

### `[ID]` `<Problem Title>`

- **Category**: `<Primary Category>` / `<Subcategory>`
- **Target Engine(s)**: `PostgreSQL` | `MySQL` | `Distributed SQL (Cockroach/Spanner)`
- **Difficulty**: `Easy` | `Medium` | `Hard`
- **Source**: `[Platform / Book / Custom Specification](URL or Reference)`

#### 1. Problem Description & Business Context
<Concise explanation of the domain, business entity relationships, and operational context.>

#### 2. Schema Definition (DDL) & Volume Estimates
```sql
-- Paste reference DDL or table outlines here
```
- **Estimated Table Size**: `N rows`
- **Read/Write Ratio**: `95% Read / 5% Write` (or OLTP vs. OLAP)

#### 3. Constraints & Expected Invariants
- Functional Dependencies: `X → Y`
- Integrity Constraints: Foreign Keys, Unique Keys, Check Constraints
- Latency / SLA Target: `< 10ms at p99`

#### 4. Sample Input Data & Expected Output
**Sample Input:**
| id | name | department_id | salary |
| :--- | :--- | :--- | :--- |
| 1 | Alice | 10 | 95000 |
| 2 | Bob | 10 | 80000 |

**Expected Output:**
| department_id | top_earner | salary |
| :--- | :--- | :--- |
| 10 | Alice | 95000 |

---

