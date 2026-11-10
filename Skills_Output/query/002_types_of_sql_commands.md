# 002: Types of SQL Commands & Engine Operational Families

A comprehensive, internal engine manual based on **Section 01: Introduction to SQL (Lecture 08: Types of SQL Commands)** from the *withBara* SQL course, cross-referenced with companion materials in `Resources/02_docs/01_SQL_Introduction.pdf` and `Resources/03_scripts/SQL_Cheat_Sheet.sql`.

---

## 1. Course Context & Educational Focus
- **Course Module**: `01_Introduction to SQL`
- **Lecture**: `08_Types of SQL Commands.md`
- **Companion Resources**:
  - Slide Deck: `Skills_Input/udemy/withBara/Resources/02_docs/01_SQL_Introduction.pdf`
  - Reference Script: `Skills_Input/udemy/withBara/Resources/03_scripts/SQL_Cheat_Sheet.sql`

---

## 2. Intuition & The Story of a Database

As taught in the course, rather than memorizing dry acronyms, you understand the types of SQL commands by walking through **the lifecycle of an empty database**:

```mermaid
flowchart LR
    subgraph Step1["Step 1: DDL"]
        A["Empty Database"] -->|"CREATE"| B["Empty Table Structure"]
        B -->|"ALTER / DROP"| B
    end

    subgraph Step2["Step 2: DML"]
        C["Application / Web App"] -->|"INSERT / UPDATE / DELETE"| D[("Table with Data")]
    end

    subgraph Step3["Step 3: DQL"]
        D -->|"SELECT / SQL Query"| E["Business Questions and Answers"]
    end

    B --> D
    
    classDef stage fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#f8fafc;
    class A,B,C,D,E stage;
```

1. **Step 1: You have an empty database.** There are no tables, columns, or constraints. You must *define* the structure.
2. **Step 2: You now have empty tables.** You need an application or user to *manipulate* and load data into those structures.
3. **Step 3: You have tables filled with data.** Now business users and analysts can ask analytical questions and *query* the data.

---

## 3. The Three Primary SQL Families

### 1. DDL: Data Definition Language (Building the Skeleton)
- **Purpose**: Defines, modifies, or deletes the metadata and structural objects (tables, schemas, views, indexes) in the database.
- **Engine Impact**: DDL commands write to the database catalog / data dictionary. They alter schema definitions, allocate storage extents, and manage structural constraints.
- **Key Commands**:
  - `CREATE`: Builds brand-new objects (e.g., `CREATE TABLE customers (...)`).
  - `ALTER`: Modifies an already existing structure (e.g., adding a column, modifying data types: `ALTER TABLE customers ADD email VARCHAR(100)`).
  - `DROP`: Permanently removes an object and all its stored data (e.g., `DROP TABLE customers`).
  - `TRUNCATE`: Quickly empties a table by deallocating its storage pages rather than logging row-by-row deletes.

### 2. DML: Data Manipulation Language (Managing the Data Inside)
- **Purpose**: Populates, modifies, and deletes the actual row records stored inside existing tables.
- **Engine Impact**: DML commands interact with the storage engine's buffer cache and Write-Ahead Log (WAL / Transaction Log). They generate transaction records, acquire row/page locks, and maintain index entries.
- **Key Commands**:
  - `INSERT`: Adds brand new rows into a table (e.g., `INSERT INTO customers (id, name) VALUES (1, 'Basel')`).
  - `UPDATE`: Modifies values in existing rows based on conditions (e.g., `UPDATE customers SET score = 100 WHERE id = 1`).
  - `DELETE`: Removes specific rows based on predicates (e.g., `DELETE FROM customers WHERE id = 1`).

### 3. DQL: Data Query Language (Asking Analytical Questions)
- **Purpose**: Retrieves and analyzes data stored in the database without modifying the underlying tables or structures.
- **Engine Impact**: Triggers the Query Optimizer, executes logical query processing (`FROM` → `WHERE` → `GROUP BY` → `HAVING` → `SELECT` → `ORDER BY`), reads data from the buffer cache, and streams results back to the client.
- **Key Command**:
  - `SELECT`: The single, most widely used command in SQL. It forms the backbone of queries, reports, dashboards, and analytical pipelines.

---

## 4. Extended Categories (DCL & TCL)

In enterprise relational databases (and in Sections 03 & 20 of the course), two additional operational families complete the SQL engine suite:

| Category | Full Name | Core Commands | Engine Role |
| :--- | :--- | :--- | :--- |
| **DCL** | Data Control Language | `GRANT`, `REVOKE` | Controls security, user permissions, and access privileges to database objects. |
| **TCL** | Transaction Control Language | `COMMIT`, `ROLLBACK`, `SAVEPOINT` | Manages atomicity and durability of DML operations within transactions. Ensures ACID compliance. |

---

## 5. Universal Rule 9: 3-Tier Concept Mapping (Java -> SQL Wire -> Physical Table)

To see how DDL, DML, and DQL execute in production systems, we trace the complete lifecycle across Java application code, database SQL execution, and physical table storage pages:

### Tier 1: DDL (Data Definition Language) - Schema Creation

#### Layer 1: Coding Level (Strictly Java Only)
```java
package com.dbms.lifecycle;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class SchemaInitializationService {
    private static final String URL = "jdbc:postgresql://localhost:5432/salesdb";
    private static final String USER = "db_admin";
    private static final String PASS = "AdminSecretPass!";

    public void initializeCustomerSchema() {
        String createTableSql = """
            CREATE TABLE IF NOT EXISTS customers (
                customer_id SERIAL PRIMARY KEY,
                first_name  VARCHAR(50) NOT NULL,
                country     VARCHAR(50) NOT NULL,
                score       INT DEFAULT 0 CHECK (score >= 0)
            );
            """;

        try (Connection conn = DriverManager.getConnection(URL, USER, PASS);
             Statement stmt = conn.createStatement()) {

            // DDL statement execution
            stmt.execute(createTableSql);
            System.out.println("[DDL SUCCESS] Table 'customers' created with integrity constraints.");

        } catch (SQLException e) {
            System.err.println("[DDL ERROR] " + e.getErrorCode() + " : " + e.getMessage());
        }
    }
}
```

#### Layer 2: Database Query & Internal Engine Lifecycle
```sql
CREATE TABLE IF NOT EXISTS customers (
    customer_id SERIAL PRIMARY KEY,
    first_name  VARCHAR(50) NOT NULL,
    country     VARCHAR(50) NOT NULL,
    score       INT DEFAULT 0 CHECK (score >= 0)
);
```
1. **Catalog Allocation**: Engine checks `pg_class` / `sys.tables`. If absent, allocates a new Relation OID (`relfilenode`).
2. **Constraint Indexing**: B-tree index created automatically for `PRIMARY KEY (customer_id)`.
3. **Storage Extent**: Allocates first disk block/extent (typically 8KB page) in the database tablespace.

#### Layer 3: Physical Table / Disk State
- **System Catalog**: Registered in `information_schema.tables` and `pg_attribute`.
- **Physical Data Page #1**: Empty page allocated with Page Header (LSN, lower pointer, upper pointer), 0 tuple slots.

---

### Tier 2: DML (Data Manipulation Language) - Populating & Modifying Records

#### Layer 1: Coding Level (Strictly Java Only)
```java
package com.dbms.lifecycle;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class CustomerDataService {
    private static final String URL = "jdbc:postgresql://localhost:5432/salesdb";
    private static final String USER = "app_user";
    private static final String PASS = "AppSecretPass!";

    public void registerCustomer(String name, String country, int score) {
        String insertSql = "INSERT INTO customers (first_name, country, score) VALUES (?, ?, ?)";

        try (Connection conn = DriverManager.getConnection(URL, USER, PASS);
             PreparedStatement pstmt = conn.prepareStatement(insertSql)) {

            pstmt.setString(1, name);
            pstmt.setString(2, country);
            pstmt.setInt(3, score);

            int rowsInserted = pstmt.executeUpdate();
            System.out.println("[DML SUCCESS] Inserted " + rowsInserted + " customer row.");

        } catch (SQLException e) {
            System.err.println("[DML ERROR] " + e.getErrorCode() + " : " + e.getMessage());
        }
    }

    public void updateScore(int customerId, int addedScore) {
        String updateSql = "UPDATE customers SET score = score + ? WHERE customer_id = ?";

        try (Connection conn = DriverManager.getConnection(URL, USER, PASS);
             PreparedStatement pstmt = conn.prepareStatement(updateSql)) {

            pstmt.setInt(1, addedScore);
            pstmt.setInt(2, customerId);

            int rowsUpdated = pstmt.executeUpdate();
            System.out.println("[DML SUCCESS] Updated " + rowsUpdated + " row(s).");

        } catch (SQLException e) {
            System.err.println("[DML ERROR] " + e.getErrorCode() + " : " + e.getMessage());
        }
    }
}
```

#### Layer 2: Database Query & Internal Engine Lifecycle
```sql
-- Query 1: INSERT
INSERT INTO customers (first_name, country, score) VALUES ('Alice', 'USA', 250);

-- Query 2: UPDATE
UPDATE customers SET score = score + 50 WHERE customer_id = 1;
```
1. **Buffer Page Write**: Engine finds free space in Page #1 via Free Space Map (FSM).
2. **WAL Append**: Writes Redo record (`LSN 101: INSERT customers tuple 1`) to sequential log buffer.
3. **Dirty Buffer**: Page #1 marked `DIRTY=1` in memory.
4. **Row Lock & MVCC**: When `UPDATE` executes, acquires Row-Exclusive lock (`X-Lock`), marks old tuple as deleted (`xmax = XID`), and inserts new tuple version with score `300`.

#### Layer 3: Physical Table Transformation

**Table Data Page #1 (Post-INSERT):**

| Line Pointer | customer_id | first_name | country | score | Tuple Flag |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `Item 1` | `1` | Alice | `USA` | `250` | `Live / Clean` |

**Table Data Page #1 (Post-UPDATE):**

| Line Pointer | customer_id | first_name | country | score | Tuple State |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `Item 1` | `1` | Alice | `USA` | `250` | `Dead Tuple (xmax=XID)` |
| `Item 2` | `1` | Alice | `USA` | `300` | `Live Tuple (xmin=XID, xmax=0)` |

---

### Tier 3: DQL (Data Query Language) - Analytical Read Retrieval

#### Layer 1: Coding Level (Strictly Java Only)
```java
package com.dbms.lifecycle;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class CustomerReportingService {
    private static final String URL = "jdbc:postgresql://localhost:5432/salesdb";
    private static final String USER = "reporting_user";
    private static final String PASS = "ReadOnlyPass!";

    public void printCustomerScoreboard() {
        String dqlQuery = """
            SELECT customer_id, first_name, country, score
            FROM customers
            WHERE score >= 200
            ORDER BY score DESC
            """;

        try (Connection conn = DriverManager.getConnection(URL, USER, PASS);
             PreparedStatement pstmt = conn.prepareStatement(dqlQuery);
             ResultSet rs = pstmt.executeQuery()) {

            System.out.println("--- HIGH SCORING CUSTOMERS ---");
            while (rs.next()) {
                System.out.printf("ID: %d | Name: %s | Country: %s | Score: %d%n",
                    rs.getInt("customer_id"),
                    rs.getString("first_name"),
                    rs.getString("country"),
                    rs.getInt("score")
                );
            }

        } catch (SQLException e) {
            System.err.println("[DQL ERROR] " + e.getErrorCode() + " : " + e.getMessage());
        }
    }
}
```

#### Layer 2: Database Query & Internal Engine Lifecycle
```sql
SELECT customer_id, first_name, country, score
FROM customers
WHERE score >= 200
ORDER BY score DESC;
```
1. **Query Optimizer**: Determines plan (Index Scan on primary key vs Sequential Scan on Page #1).
2. **Snapshot Visibility**: Evaluates MVCC visibility. Reads only `Item 2` (score: 300) and ignores `Item 1` (dead tuple).
3. **Zero Transaction Log Overhead**: Allocates no transaction slot (read-only virtual transaction), produces zero WAL log records, acquires shared locks (`S-Lock`) or snapshot timestamps.

#### Layer 3: Physical Output Stream Received by Java Client

| customer_id | first_name | country | score |
| :--- | :--- | :--- | :--- |
| `1` | Alice | `USA` | `300` |

---

## 6. Comprehensive Summary Comparison Table

| Category | What It Operates On | Primary Keywords | Transaction Log Impact | Real-World Metaphor |
| :--- | :--- | :--- | :--- | :--- |
| **DDL** | **Structure** (Tables, Schemas, Indexes) | `CREATE`, `ALTER`, `DROP`, `TRUNCATE` | Minimal / Metadata updates | Constructing the rooms of a warehouse |
| **DML** | **Data Rows** (Contents inside tables) | `INSERT`, `UPDATE`, `DELETE`, `MERGE` | Heavy (row-level logging & locking) | Stocking and moving boxes inside the warehouse |
| **DQL** | **Retrieval** (Read-only analytical output) | `SELECT` | Zero (Read-only; shared locks/snapshots) | Inspecting and counting the inventory |
| **TCL** | **Transactions** (Unit of work) | `COMMIT`, `ROLLBACK`, `SAVEPOINT` | Flushes transaction logs to disk | Signing off on shipment confirmations |
| **DCL** | **Permissions** (Security) | `GRANT`, `REVOKE` | Security catalog updates | Issuing security badges to warehouse workers |

