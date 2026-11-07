# Query Optimization & Indexing Engineering Template

A systematic template for inspecting query execution plans, evaluating predicate selectivity, choosing optimal index types, preventing anti-patterns, and proving performance gains with measurable metrics.

---

## 🧭 Purpose & Agent Guardrail

> **Mandatory Rule for the Agent**: Do not suggest an index or rewrite a slow query based purely on heuristics. You must dissect the execution plan (`EXPLAIN ANALYZE`), identify the exact bottleneck (sequential scan, nested loop explosion, hash spill, sort memory spill), and verify the trade-off with the user before finalizing optimizations.

---

## 📊 Phase 1: Query Profiling & Execution Plan Baseline

1. **Target Query & Schema Baseline**:
   - Provide the complete SQL query.
   - List target table row count, table disk size, and existing index definitions.
2. **Execution Plan Dissection (`EXPLAIN (ANALYZE, BUFFERS)` in PostgreSQL / `EXPLAIN FORMAT=JSON` in MySQL)**:
   - **Cost Estimate vs. Actual Time**: Startup cost, total cost, actual execution time.
   - **Buffer Activity**: Shared hit blocks, shared read blocks (disk I/O vs. RAM cache).
   - **Scan Types Detected**: `Seq Scan`, `Index Scan`, `Index Only Scan`, `Bitmap Index Scan`.
   - **Join Types Detected**: `Nested Loop`, `Hash Join`, `Merge Join`.
   - **Spill Warnings**: External sort / hash batch disk spilling (`WorkMem` overflow).

---

## 🎯 Phase 2: Predicate Selectivity & Index Strategy

### 1. Selectivity Calculation
Calculate or estimate filter selectivity:
$$\text{Selectivity} = \frac{|\sigma_{\text{predicate}}(R)|}{|R|}$$
- **High Selectivity ($\ll 5\%$)**: Ideal candidate for B+ Tree or index lookup.
- **Low Selectivity ($> 20\%$)**: Optimizer will likely prefer a Sequential/Full Table Scan; indexing may add write overhead with zero read benefit.

### 2. Index Structure Selection
Select the appropriate index mechanics based on data types and access patterns:

| Index Type | Optimal Workload / Operators | Trade-offs & Limitations |
| :--- | :--- | :--- |
| **B+ Tree (Default)** | Equality (`=`), Range (`<`, `<=`, `>`, `>=`, `BETWEEN`), Prefix Match (`LIKE 'abc%'`), Sort ordering (`ORDER BY`) | High maintenance cost on volatile tables; large storage footprint. |
| **Hash Index** | Strict equality lookups (`=`) | Cannot serve range queries, sorting, or multi-column partial matches. |
| **GIN (Generalized Inverted)** | Arrays, JSONB documents, full-text search, multi-value attributes | Heavier write amplification; expensive index maintenance. |
| **BRIN (Block Range Index)** | Naturally sorted time-series or sequential data across huge tables (millions of rows) | Tiny storage footprint, but useless on random or scattered data. |

---

## 🧩 Phase 3: Composite Index Column Ordering Rule

When designing composite indexes on columns $(C_1, C_2, \dots, C_k)$:
1. **Rule 1 (Equality First)**: Place all columns filtered with strict equality (`WHERE C_1 = constant`) first.
2. **Rule 2 (Range Last)**: Place the column filtered with a range predicate (`WHERE C_2 BETWEEN x AND y`) after equality columns. Any column placed after a range column cannot be used for index traversal.
3. **Rule 3 (Covering Index)**: Include projection columns (`INCLUDE (C_3, C_4)`) to achieve an **Index Only Scan** and eliminate heap lookups.

---

## ⚡ Phase 4: Anti-Pattern Audit & Query Refactoring

Audit the query against common relational optimization traps:

- [ ] **SARGability (Search Argument Quality)**: Are functions applied to indexed columns? (e.g., `WHERE DATE(created_at) = '2026-01-01'` $\to$ rewrite to `WHERE created_at >= '2026-01-01' AND created_at < '2026-01-02'`).
- [ ] **Implicit Type Coercion**: Ensure parameter types match column types exactly to prevent disabling index scans.
- [ ] **Correlated Subqueries vs. CTE / Window Functions**: Replace expensive $O(N \times M)$ correlated subqueries with joins or window partitions (`ROW_NUMBER() OVER (...)`).
- [ ] **`SELECT *` Waste**: Eliminate redundant column fetches that defeat index-only scans and congest memory bandwidth.
- [ ] **Offset Pagination Bottlenecks**: Replace `OFFSET 1000000 LIMIT 20` with keyset/cursor pagination (`WHERE id > :last_seen_id ORDER BY id ASC LIMIT 20`).

---

## 📈 Phase 5: Verification & Post-Optimization Plan

Compare baseline vs. optimized plan metrics side-by-side:

| Metric | Before Optimization | After Optimization | Delta / Improvement |
| :--- | :--- | :--- | :--- |
| **Execution Time** | e.g. 1,420 ms | e.g. 3.2 ms | **443x speedup** |
| **Shared Hit/Read Blocks**| e.g. 45,000 blocks | e.g. 12 blocks | **99.9% I/O reduction** |
| **Scan Strategy** | `Seq Scan on large_table` | `Index Only Scan using idx_cover` | Zero heap access |
| **Memory / Disk Spill** | `External merge Disk: 18MB`| `Quicksort Memory: 120kB` | Eliminated disk spill |
