# withNasser: Complete Course Curriculum & Deep Topic Outline
> **Course**: Fundamentals of Database Engineering
> **Instructor**: Hussein Nasser
> **Coverage**: Exhaustive index of all 18 sections, lectures, database internals topics, PDF/PPTX slides, and SQL scripts for surgical searching and query retrieval.

---

## ⚡ Fast Jump Table of Contents

1. [01_Course Updates](#01course-updates)
2. [02_ACID](#02acid)
3. [03_Understanding Database Internals](#03understanding-database-internals)
4. [04_Database Indexing](#04database-indexing)
5. [05_B-Tree vs B+Tree in Production Database Systems](#05b-tree-vs-btree-in-production-database-systems)
6. [06_Database Partitioning](#06database-partitioning)
7. [07_Database Sharding](#07database-sharding)
8. [08_Concurrency Control](#08concurrency-control)
9. [09_Database Replication](#09database-replication)
10. [10_Database System Design](#10database-system-design)
11. [11_Database Engines](#11database-engines)
12. [12_Database Cursors](#12database-cursors)
13. [13_NoSQL Architecture](#13nosql-architecture)
14. [14_Database Security](#14database-security)
15. [15_Homomorphic Encryption - Performing Database Queries on Encrypted Data](#15homomorphic-encryption---performing-database-queries-on-encrypted-data)
16. [16_Answering your Questions](#16answering-your-questions)
17. [17_Database Discussions](#17database-discussions)
18. [18_Archived Lectures](#18archived-lectures)

---

## 01_Course Updates

### 📄 01_Welcome to the Course
- **Transcript File**: `Skills_Input/udemy/withNasser/01_Course Updates/01_Welcome to the Course.md`
- *Key Engine Mechanisms*: `ACID, ATOMICITY, BLOOM FILTER, CONSISTENCY, DURABILITY, ISOLATION, MYSQL, PARTITIONING, POSTGRES, SHARDING`

### 📄 02_Course Note 1
- **Transcript File**: `Skills_Input/udemy/withNasser/01_Course Updates/02_Course Note 1.md`
- *Key Engine Mechanisms*: `POSTGRES, REPLICATION`

### 📄 03_Course Note 2
- **Transcript File**: `Skills_Input/udemy/withNasser/01_Course Updates/03_Course Note 2.md`
- *Key Engine Mechanisms*: `ACID, ATOMICITY, CONSISTENCY, CURSOR, DURABILITY, ISOLATION, MYSQL, PARTITIONING, POSTGRES, REPLICATION, SHARDING`

### 📄 04_Course Note 3
- **Transcript File**: `Skills_Input/udemy/withNasser/01_Course Updates/04_Course Note 3.md`
- *Key Engine Mechanisms*: `ACID, ATOMICITY, CONSISTENCY, DURABILITY, ISOLATION, PAGE, PARTITIONING, SHARDING`

### 📄 05_Note about Docker
- **Transcript File**: `Skills_Input/udemy/withNasser/01_Course Updates/05_Note about Docker.md`

### 📄 06_Slides
- **Transcript File**: `Skills_Input/udemy/withNasser/01_Course Updates/06_Slides.md`

---

## 02_ACID

- 📑 **Companion Slide Deck / Book**: `01_ACID-Updated.odp` (`Skills_Input/udemy/withNasser/02_ACID/01_ACID-Updated.odp`)

- 📑 **Companion Slide Deck / Book**: `01_ACID-Updated.pdf` (`Skills_Input/udemy/withNasser/02_ACID/01_ACID-Updated.pdf`)

- 📑 **Companion Slide Deck / Book**: `01_ACID-Updated.pptx` (`Skills_Input/udemy/withNasser/02_ACID/01_ACID-Updated.pptx`)

### 📄 01_Introduction to ACID
- **Transcript File**: `Skills_Input/udemy/withNasser/02_ACID/01_Introduction to ACID.md`
- **Subtopics & Key Concepts**:
      - **Attached Resources**
- *Key Engine Mechanisms*: `ACID, ATOMICITY, CONSISTENCY, DURABILITY, ISOLATION, MYSQL, POSTGRES`

### 📄 02_What is a Transaction
- **Transcript File**: `Skills_Input/udemy/withNasser/02_ACID/02_What is a Transaction.md`
- *Key Engine Mechanisms*: `CONSISTENCY, ISOLATION, MYSQL, POSTGRES, REDO, UNDO`

### 📄 03_Atomicity
- **Transcript File**: `Skills_Input/udemy/withNasser/02_ACID/03_Atomicity.md`
- *Key Engine Mechanisms*: `ACID, ATOMICITY, OPTIMISTIC`

### 📄 04_Isolation
- **Transcript File**: `Skills_Input/udemy/withNasser/02_ACID/04_Isolation.md`
- *Key Engine Mechanisms*: `ACID, DIRTY READ, ISOLATION, MVCC, MYSQL, OPTIMISTIC, PAGE, PESSIMISTIC, PHANTOM, POSTGRES, READ COMMITTED, READ UNCOMMITTED`

### 📄 05_Consistency
- **Transcript File**: `Skills_Input/udemy/withNasser/02_ACID/05_Consistency.md`
- *Key Engine Mechanisms*: `ACID, ATOMICITY, CONSISTENCY, DURABILITY, ISOLATION, REPLICATION`

### 📄 06_Durability
- **Transcript File**: `Skills_Input/udemy/withNasser/02_ACID/06_Durability.md`
- *Key Engine Mechanisms*: `ACID, CONSISTENCY, DURABILITY, WAL`

### 📄 07_ACID by Practical Examples
- **Transcript File**: `Skills_Input/udemy/withNasser/02_ACID/07_ACID by Practical Examples.md`
- *Key Engine Mechanisms*: `ACID, ATOMICITY, CONSISTENCY, DURABILITY, ISOLATION, MYSQL, POSTGRES, READ COMMITTED, REPEATABLE READ, SERIALIZABLE`

- 💻 **Companion Script / Command File**: `08_mysql-commands.txt` (`Skills_Input/udemy/withNasser/02_ACID/08_mysql-commands.txt`)

### 📄 08_Phantom Reads
- **Transcript File**: `Skills_Input/udemy/withNasser/02_ACID/08_Phantom Reads.md`
- **Subtopics & Key Concepts**:
      - **Attached Resources**
- *Key Engine Mechanisms*: `DIRTY READ, ISOLATION, MVCC, MYSQL, PESSIMISTIC, PHANTOM, POSTGRES, REPEATABLE READ, SERIALIZABLE`

- 📑 **Companion Slide Deck / Book**: `09_read.pdf` (`Skills_Input/udemy/withNasser/02_ACID/09_read.pdf`)

### 📄 09_Serializable vs Repeatable Read
- **Transcript File**: `Skills_Input/udemy/withNasser/02_ACID/09_Serializable vs Repeatable Read.md`
- **Subtopics & Key Concepts**:
      - **Attached Resources**
- *Key Engine Mechanisms*: `ISOLATION, POSTGRES, READ COMMITTED, REPEATABLE READ, SERIALIZABLE`

### 📄 10_Eventual Consistency
- **Transcript File**: `Skills_Input/udemy/withNasser/02_ACID/10_Eventual Consistency.md`
- **Subtopics & Key Concepts**:
      - **Attached Resources**
- *Key Engine Mechanisms*: `ACID, ATOMICITY, CONSISTENCY, DURABILITY, ISOLATION, POSTGRES, REPEATABLE READ, SHARDING`

- 📑 **Companion Slide Deck / Book**: `10_Eventual Consistency.odp` (`Skills_Input/udemy/withNasser/02_ACID/10_Eventual Consistency.odp`)

- 📑 **Companion Slide Deck / Book**: `10_Eventual Consistency.pdf` (`Skills_Input/udemy/withNasser/02_ACID/10_Eventual Consistency.pdf`)

- 📑 **Companion Slide Deck / Book**: `10_Eventual Consistency.pptx` (`Skills_Input/udemy/withNasser/02_ACID/10_Eventual Consistency.pptx`)

---

## 03_Understanding Database Internals

### 📄 01_How tables and indexes are stored on disk (MUST WATCH before continue)
- **Transcript File**: `Skills_Input/udemy/withNasser/03_Understanding Database Internals/01_How tables and indexes are stored on disk (MUST WATCH before continue).md`
- **Subtopics & Key Concepts**:
      - **Attached Resources**
- *Key Engine Mechanisms*: `B-TREE, MYSQL, PAGE, POSTGRES`

- 📑 **Companion Slide Deck / Book**: `01_How tables and indexes are stored on disk.odp` (`Skills_Input/udemy/withNasser/03_Understanding Database Internals/01_How tables and indexes are stored on disk.odp`)

- 📑 **Companion Slide Deck / Book**: `01_How tables and indexes are stored on disk.pdf` (`Skills_Input/udemy/withNasser/03_Understanding Database Internals/01_How tables and indexes are stored on disk.pdf`)

- 📑 **Companion Slide Deck / Book**: `01_How tables and indexes are stored on disk.pptx` (`Skills_Input/udemy/withNasser/03_Understanding Database Internals/01_How tables and indexes are stored on disk.pptx`)

### 📄 02_Row-Based vs Column-Based Databases
- **Transcript File**: `Skills_Input/udemy/withNasser/03_Understanding Database Internals/02_Row-Based vs Column-Based Databases.md`
- **Subtopics & Key Concepts**:
      - **Attached Resources**
- *Key Engine Mechanisms*: `MYSQL, PARTITIONING, POSTGRES`

- 📑 **Companion Slide Deck / Book**: `02_Row-Based vs Column-Based Databases.odp` (`Skills_Input/udemy/withNasser/03_Understanding Database Internals/02_Row-Based vs Column-Based Databases.odp`)

- 📑 **Companion Slide Deck / Book**: `02_Row-Based vs Column-Based Databases.pdf` (`Skills_Input/udemy/withNasser/03_Understanding Database Internals/02_Row-Based vs Column-Based Databases.pdf`)

- 📑 **Companion Slide Deck / Book**: `02_Row-Based vs Column-Based Databases.pptx` (`Skills_Input/udemy/withNasser/03_Understanding Database Internals/02_Row-Based vs Column-Based Databases.pptx`)

### 📄 03_Primary Key vs Secondary Key - What you probably didn't know
- **Transcript File**: `Skills_Input/udemy/withNasser/03_Understanding Database Internals/03_Primary Key vs Secondary Key - What you probably didn't know.md`
- *Key Engine Mechanisms*: `B-TREE, MYSQL, PAGE, POSTGRES`

### 📄 04_Databases Pages (Article)
- **Transcript File**: `Skills_Input/udemy/withNasser/03_Understanding Database Internals/04_Databases Pages (Article).md`
- **Subtopics & Key Concepts**:
      - ****Database Pages — A deep dive****
      - **A Pool of Pages**
      - ****Page Content****
      - **Small vs Large Pages**
      - **How page are stored on Disk**
      - **Postgres Page Layout**
      - **Page header — 24 bytes**
      - **ItemIds — 4 byte each**
      - **Items — variable length**
      - **Special — variable length**
      - **Summary**
- *Key Engine Mechanisms*: `B+TREE, INNODB, MVCC, MYSQL, PAGE, POSTGRES, WAL`

---

## 04_Database Indexing

### 📄 01_Create Postgres Table with a million Rows (from scratch)
- **Transcript File**: `Skills_Input/udemy/withNasser/04_Database Indexing/01_Create Postgres Table with a million Rows (from scratch).md`
- **Subtopics & Key Concepts**:
      - **Attached Resources**
- *Key Engine Mechanisms*: `PARTITIONING, POSTGRES`

- 💻 **Companion Script / Command File**: `01_one-million-pg.txt` (`Skills_Input/udemy/withNasser/04_Database Indexing/01_one-million-pg.txt`)

- 💻 **Companion Script / Command File**: `02_employees.sql` (`Skills_Input/udemy/withNasser/04_Database Indexing/02_employees.sql`)

### 📄 02_Getting Started with Indexing
- **Transcript File**: `Skills_Input/udemy/withNasser/04_Database Indexing/02_Getting Started with Indexing.md`
- **Subtopics & Key Concepts**:
      - **Attached Resources**
- *Key Engine Mechanisms*: `B-TREE, BITMAP INDEX SCAN, MYSQL, PAGE, POSTGRES, TABLE SCAN`

- 💻 **Companion Script / Command File**: `03_grades.sql` (`Skills_Input/udemy/withNasser/04_Database Indexing/03_grades.sql`)

### 📄 03_Understanding The SQL Query Planner and Optimizer with Explain
- **Transcript File**: `Skills_Input/udemy/withNasser/04_Database Indexing/03_Understanding The SQL Query Planner and Optimizer with Explain.md`
- **Subtopics & Key Concepts**:
      - **Attached Resources**
- *Key Engine Mechanisms*: `INDEX SCAN, PAGE, POSTGRES, TABLE SCAN`

### 📄 04_Bitmap Index Scan vs Index Scan vs Table Scan
- **Transcript File**: `Skills_Input/udemy/withNasser/04_Database Indexing/04_Bitmap Index Scan vs Index Scan vs Table Scan.md`
- **Subtopics & Key Concepts**:
      - **Attached Resources**
- *Key Engine Mechanisms*: `B-TREE, BITMAP INDEX SCAN, INDEX SCAN, PAGE, POSTGRES, TABLE SCAN`

### 📄 05_Key vs Non-Key Column Database Indexing
- **Transcript File**: `Skills_Input/udemy/withNasser/04_Database Indexing/05_Key vs Non-Key Column Database Indexing.md`
- **Subtopics & Key Concepts**:
      - **Attached Resources**
- *Key Engine Mechanisms*: `B-TREE, INDEX SCAN, POSTGRES`

- 💻 **Companion Script / Command File**: `05_students.sql` (`Skills_Input/udemy/withNasser/04_Database Indexing/05_students.sql`)

### 📄 06_Index Scan vs Index Only Scan
- **Transcript File**: `Skills_Input/udemy/withNasser/04_Database Indexing/06_Index Scan vs Index Only Scan.md`
- *Key Engine Mechanisms*: `B-TREE, INDEX SCAN, POSTGRES, TABLE SCAN`

### 📄 07_Combining Database Indexes for Better Performance
- **Transcript File**: `Skills_Input/udemy/withNasser/04_Database Indexing/07_Combining Database Indexes for Better Performance.md`
- *Key Engine Mechanisms*: `BITMAP INDEX SCAN, INDEX SCAN, POSTGRES, TABLE SCAN`

### 📄 08_How Database Optimizers Decide to Use Indexes
- **Transcript File**: `Skills_Input/udemy/withNasser/04_Database Indexing/08_How Database Optimizers Decide to Use Indexes.md`
- **Subtopics & Key Concepts**:
      - **Attached Resources**
- *Key Engine Mechanisms*: `INDEX SCAN, POSTGRES, TABLE SCAN`

- 📑 **Companion Slide Deck / Book**: `08_multiple-indexes.pdf` (`Skills_Input/udemy/withNasser/04_Database Indexing/08_multiple-indexes.pdf`)

### 📄 09_Create Index Concurrently - Avoid Blocking Production Database Writes
- **Transcript File**: `Skills_Input/udemy/withNasser/04_Database Indexing/09_Create Index Concurrently - Avoid Blocking Production Database Writes.md`
- *Key Engine Mechanisms*: `POSTGRES`

### 📄 10_Bloom Filters
- **Transcript File**: `Skills_Input/udemy/withNasser/04_Database Indexing/10_Bloom Filters.md`
- **Subtopics & Key Concepts**:
      - **Attached Resources**
- *Key Engine Mechanisms*: `BLOOM FILTER, CONSISTENT HASHING, PAGE`

- 📑 **Companion Slide Deck / Book**: `10_bloom-filter.odp` (`Skills_Input/udemy/withNasser/04_Database Indexing/10_bloom-filter.odp`)

- 📑 **Companion Slide Deck / Book**: `10_bloom-filter.pdf` (`Skills_Input/udemy/withNasser/04_Database Indexing/10_bloom-filter.pdf`)

- 📑 **Companion Slide Deck / Book**: `10_bloom-filter.pptx` (`Skills_Input/udemy/withNasser/04_Database Indexing/10_bloom-filter.pptx`)

### 📄 11_Working with Billion-Row Table
- **Transcript File**: `Skills_Input/udemy/withNasser/04_Database Indexing/11_Working with Billion-Row Table.md`
- *Key Engine Mechanisms*: `PARTITIONING, SHARDING`

### 📄 12_How UUIDs in B+Tree Indexes can affect performance
- **Transcript File**: `Skills_Input/udemy/withNasser/04_Database Indexing/12_How UUIDs in B+Tree Indexes can affect performance.md`
- *Key Engine Mechanisms*: `B-TREE, MYSQL, PAGE, POSTGRES`

### 📄 13_Article - The Cost of Long running Transactions
- **Transcript File**: `Skills_Input/udemy/withNasser/04_Database Indexing/13_Article - The Cost of Long running Transactions.md`
- *Key Engine Mechanisms*: `PAGE, POSTGRES, UNDO`

### 📄 14_Article - Microsoft SQL Server Clustered Index Design
- **Transcript File**: `Skills_Input/udemy/withNasser/04_Database Indexing/14_Article - Microsoft SQL Server Clustered Index Design.md`
- **Subtopics & Key Concepts**:
      - **Attached Resources**
- *Key Engine Mechanisms*: `B-TREE, PAGE`

- 📑 **Companion Slide Deck / Book**: `14_SQL Server Index Architecture and Design Guide - SQL Server _ Microsoft Docs.pdf` (`Skills_Input/udemy/withNasser/04_Database Indexing/14_SQL Server Index Architecture and Design Guide - SQL Server _ Microsoft Docs.pdf`)

---

## 05_B-Tree vs B+Tree in Production Database Systems

### 📄 01_B-Tree Section's Introduction & Agenda
- **Transcript File**: `Skills_Input/udemy/withNasser/05_B-Tree vs B+Tree in Production Database Systems/01_B-Tree Section's Introduction & Agenda.md`
- **Subtopics & Key Concepts**:
      - **Attached Resources**
- *Key Engine Mechanisms*: `B-TREE, INNODB, MYSQL, POSTGRES`

- 📑 **Companion Slide Deck / Book**: `01_b-tree-original-paper.pdf` (`Skills_Input/udemy/withNasser/05_B-Tree vs B+Tree in Production Database Systems/01_b-tree-original-paper.pdf`)

- 📑 **Companion Slide Deck / Book**: `01_B-trees vs B+trees.odp` (`Skills_Input/udemy/withNasser/05_B-Tree vs B+Tree in Production Database Systems/01_B-trees vs B+trees.odp`)

- 📑 **Companion Slide Deck / Book**: `01_B-trees vs B+trees.pdf` (`Skills_Input/udemy/withNasser/05_B-Tree vs B+Tree in Production Database Systems/01_B-trees vs B+trees.pdf`)

- 📑 **Companion Slide Deck / Book**: `01_B-trees vs B+trees.pptx` (`Skills_Input/udemy/withNasser/05_B-Tree vs B+Tree in Production Database Systems/01_B-trees vs B+trees.pptx`)

### 📄 02_Full Table Scans
- **Transcript File**: `Skills_Input/udemy/withNasser/05_B-Tree vs B+Tree in Production Database Systems/02_Full Table Scans.md`
- *Key Engine Mechanisms*: `MYSQL, PAGE, TABLE SCAN`

### 📄 03_Original B-Tree
- **Transcript File**: `Skills_Input/udemy/withNasser/05_B-Tree vs B+Tree in Production Database Systems/03_Original B-Tree.md`
- *Key Engine Mechanisms*: `B-TREE, MYSQL, PAGE, POSTGRES`

### 📄 04_How the Original B-Tree Helps Performance
- **Transcript File**: `Skills_Input/udemy/withNasser/05_B-Tree vs B+Tree in Production Database Systems/04_How the Original B-Tree Helps Performance.md`
- *Key Engine Mechanisms*: `B-TREE, PAGE, POSTGRES, TABLE SCAN`

### 📄 05_Original B-Tree Limitations
- **Transcript File**: `Skills_Input/udemy/withNasser/05_B-Tree vs B+Tree in Production Database Systems/05_Original B-Tree Limitations.md`
- *Key Engine Mechanisms*: `B-TREE, PAGE`

### 📄 06_B+Tree
- **Transcript File**: `Skills_Input/udemy/withNasser/05_B-Tree vs B+Tree in Production Database Systems/06_B+Tree.md`
- *Key Engine Mechanisms*: `B-TREE, PAGE`

### 📄 07_B+Tree DBMS Considerations
- **Transcript File**: `Skills_Input/udemy/withNasser/05_B-Tree vs B+Tree in Production Database Systems/07_B+Tree DBMS Considerations.md`
- *Key Engine Mechanisms*: `MYSQL, PAGE, POSTGRES`

### 📄 08_B+Tree Storage Cost in MySQL vs Postgres
- **Transcript File**: `Skills_Input/udemy/withNasser/05_B-Tree vs B+Tree in Production Database Systems/08_B+Tree Storage Cost in MySQL vs Postgres.md`
- *Key Engine Mechanisms*: `MYSQL, POSTGRES`

### 📄 09_B-Tree Section's Summary
- **Transcript File**: `Skills_Input/udemy/withNasser/05_B-Tree vs B+Tree in Production Database Systems/09_B-Tree Section's Summary.md`
- *Key Engine Mechanisms*: `MYSQL, POSTGRES`

---

## 06_Database Partitioning

### 📄 01_Introduction to Database Partitioning
- **Transcript File**: `Skills_Input/udemy/withNasser/06_Database Partitioning/01_Introduction to Database Partitioning.md`
- **Subtopics & Key Concepts**:
      - **Attached Resources**
- *Key Engine Mechanisms*: `PARTITIONING, POSTGRES, SHARDING`

- 📑 **Companion Slide Deck / Book**: `01_Partitioning.odp` (`Skills_Input/udemy/withNasser/06_Database Partitioning/01_Partitioning.odp`)

- 📑 **Companion Slide Deck / Book**: `01_Partitioning.pdf` (`Skills_Input/udemy/withNasser/06_Database Partitioning/01_Partitioning.pdf`)

- 📑 **Companion Slide Deck / Book**: `01_Partitioning.pptx` (`Skills_Input/udemy/withNasser/06_Database Partitioning/01_Partitioning.pptx`)

- 💻 **Companion Script / Command File**: `01_Partitioning.txt` (`Skills_Input/udemy/withNasser/06_Database Partitioning/01_Partitioning.txt`)

### 📄 02_What is Partitioning
- **Transcript File**: `Skills_Input/udemy/withNasser/06_Database Partitioning/02_What is Partitioning.md`
- *Key Engine Mechanisms*: `PARTITIONING`

### 📄 03_Vertical vs Horizontal Partitioning
- **Transcript File**: `Skills_Input/udemy/withNasser/06_Database Partitioning/03_Vertical vs Horizontal Partitioning.md`
- *Key Engine Mechanisms*: `PARTITIONING`

### 📄 04_Partitioning Types
- **Transcript File**: `Skills_Input/udemy/withNasser/06_Database Partitioning/04_Partitioning Types.md`
- *Key Engine Mechanisms*: `PARTITIONING`

### 📄 05_The Difference Between Partitioning and Sharding
- **Transcript File**: `Skills_Input/udemy/withNasser/06_Database Partitioning/05_The Difference Between Partitioning and Sharding.md`
- *Key Engine Mechanisms*: `PARTITIONING, SHARDING`

### 📄 06_Preparing Postgres, Database, Table, Indexes
- **Transcript File**: `Skills_Input/udemy/withNasser/06_Database Partitioning/06_Preparing Postgres, Database, Table, Indexes.md`
- *Key Engine Mechanisms*: `PARTITIONING, POSTGRES`

### 📄 07_Execute Multiple Queries on the Table
- **Transcript File**: `Skills_Input/udemy/withNasser/06_Database Partitioning/07_Execute Multiple Queries on the Table.md`
- *Key Engine Mechanisms*: `BITMAP INDEX SCAN, INDEX SCAN`

### 📄 08_Create and Attach Partitioned Tables
- **Transcript File**: `Skills_Input/udemy/withNasser/06_Database Partitioning/08_Create and Attach Partitioned Tables.md`
- *Key Engine Mechanisms*: `PARTITIONING`

### 📄 09_Populate the Partitions and Create Indexes
- **Transcript File**: `Skills_Input/udemy/withNasser/06_Database Partitioning/09_Populate the Partitions and Create Indexes.md`
- *Key Engine Mechanisms*: `POSTGRES`

### 📄 10_Class Project - Querying and Checking the Size of Partitions
- **Transcript File**: `Skills_Input/udemy/withNasser/06_Database Partitioning/10_Class Project - Querying and Checking the Size of Partitions.md`
- *Key Engine Mechanisms*: `EXPLAIN ANALYZE, INDEX SCAN, POSTGRES`

### 📄 11_The Advantages of Partitioning
- **Transcript File**: `Skills_Input/udemy/withNasser/06_Database Partitioning/11_The Advantages of Partitioning.md`
- *Key Engine Mechanisms*: `INDEX SCAN, MYSQL, PARTITIONING, POSTGRES`

### 📄 12_The Disadvantages of Partitioning
- **Transcript File**: `Skills_Input/udemy/withNasser/06_Database Partitioning/12_The Disadvantages of Partitioning.md`
- *Key Engine Mechanisms*: `PARTITIONING`

### 📄 13_Section Summary - Partitioning
- **Transcript File**: `Skills_Input/udemy/withNasser/06_Database Partitioning/13_Section Summary - Partitioning.md`
- *Key Engine Mechanisms*: `PARTITIONING, SHARDING`

### 📄 14_How to Automate Partitioning in Postgres
- **Transcript File**: `Skills_Input/udemy/withNasser/06_Database Partitioning/14_How to Automate Partitioning in Postgres.md`
- **Subtopics & Key Concepts**:
      - **Attached Resources**
- *Key Engine Mechanisms*: `PARTITIONING, POSTGRES`

---

## 07_Database Sharding

- 💻 **Companion Script / Command File**: `01_commands.txt` (`Skills_Input/udemy/withNasser/07_Database Sharding/01_commands.txt`)

### 📄 01_Introduction to Database Sharding
- **Transcript File**: `Skills_Input/udemy/withNasser/07_Database Sharding/01_Introduction to Database Sharding.md`
- **Subtopics & Key Concepts**:
      - **Attached Resources**
- *Key Engine Mechanisms*: `CONSISTENT HASHING, PARTITIONING, POSTGRES, SHARDING`

- 💻 **Companion Script / Command File**: `01_links-code-commands.txt` (`Skills_Input/udemy/withNasser/07_Database Sharding/01_links-code-commands.txt`)

- 📑 **Companion Slide Deck / Book**: `01_Sharding.odp` (`Skills_Input/udemy/withNasser/07_Database Sharding/01_Sharding.odp`)

- 📑 **Companion Slide Deck / Book**: `01_Sharding.pdf` (`Skills_Input/udemy/withNasser/07_Database Sharding/01_Sharding.pdf`)

- 📑 **Companion Slide Deck / Book**: `01_Sharding.pptx` (`Skills_Input/udemy/withNasser/07_Database Sharding/01_Sharding.pptx`)

- 💻 **Companion Script / Command File**: `01_Sharding.txt` (`Skills_Input/udemy/withNasser/07_Database Sharding/01_Sharding.txt`)

### 📄 02_What is Database Sharding
- **Transcript File**: `Skills_Input/udemy/withNasser/07_Database Sharding/02_What is Database Sharding.md`
- *Key Engine Mechanisms*: `CONSISTENT HASHING, PAGE, SHARDING`

### 📄 03_Consistent Hashing
- **Transcript File**: `Skills_Input/udemy/withNasser/07_Database Sharding/03_Consistent Hashing.md`
- *Key Engine Mechanisms*: `CONSISTENT HASHING`

### 📄 04_Horizontal partitioning vs Sharding
- **Transcript File**: `Skills_Input/udemy/withNasser/07_Database Sharding/04_Horizontal partitioning vs Sharding.md`
- *Key Engine Mechanisms*: `PARTITIONING, SHARDING`

### 📄 05_Sharding with Postgres
- **Transcript File**: `Skills_Input/udemy/withNasser/07_Database Sharding/05_Sharding with Postgres.md`
- *Key Engine Mechanisms*: `POSTGRES`

### 📄 06_Spin up Docker Postgres Shards
- **Transcript File**: `Skills_Input/udemy/withNasser/07_Database Sharding/06_Spin up Docker Postgres Shards.md`
- *Key Engine Mechanisms*: `POSTGRES, SHARDING`

### 📄 07_Writing to a Shard
- **Transcript File**: `Skills_Input/udemy/withNasser/07_Database Sharding/07_Writing to a Shard.md`
- *Key Engine Mechanisms*: `CONSISTENCY, CONSISTENT HASHING, PAGE, POSTGRES, SHARDING`

### 📄 08_Reading from a Shard
- **Transcript File**: `Skills_Input/udemy/withNasser/07_Database Sharding/08_Reading from a Shard.md`
- *Key Engine Mechanisms*: `CONSISTENT HASHING, SHARDING`

### 📄 09_Advantages of Database Sharding
- **Transcript File**: `Skills_Input/udemy/withNasser/07_Database Sharding/09_Advantages of Database Sharding.md`
- *Key Engine Mechanisms*: `CONSISTENT HASHING, SHARDING`

### 📄 10_Disadvantages of Database Sharding
- **Transcript File**: `Skills_Input/udemy/withNasser/07_Database Sharding/10_Disadvantages of Database Sharding.md`
- *Key Engine Mechanisms*: `CONSISTENT HASHING, PARTITIONING, SHARDING`

### 📄 11_Database Sharding Section Summary
- **Transcript File**: `Skills_Input/udemy/withNasser/07_Database Sharding/11_Database Sharding Section Summary.md`
- *Key Engine Mechanisms*: `CONSISTENT HASHING, PARTITIONING, SHARDING`

### 📄 12_When Should you consider Sharding your Database
- **Transcript File**: `Skills_Input/udemy/withNasser/07_Database Sharding/12_When Should you consider Sharding your Database.md`
- *Key Engine Mechanisms*: `ACID, ATOMICITY, B-TREE, CONSISTENCY, INDEX SCAN, MYSQL, PARTITIONING, POSTGRES, REPLICATION, SHARDING`

---

## 08_Concurrency Control

### 📄 01_Shared vs Exclusive Locks
- **Transcript File**: `Skills_Input/udemy/withNasser/08_Concurrency Control/01_Shared vs Exclusive Locks.md`
- *Key Engine Mechanisms*: `CONSISTENCY`

### 📄 02_Dead Locks
- **Transcript File**: `Skills_Input/udemy/withNasser/08_Concurrency Control/02_Dead Locks.md`
- *Key Engine Mechanisms*: `OPTIMISTIC, POSTGRES`

### 📄 03_Two-phase Locking
- **Transcript File**: `Skills_Input/udemy/withNasser/08_Concurrency Control/03_Two-phase Locking.md`
- *Key Engine Mechanisms*: `POSTGRES`

### 📄 04_Solving the Double Booking Problem (Code Example)
- **Transcript File**: `Skills_Input/udemy/withNasser/08_Concurrency Control/04_Solving the Double Booking Problem (Code Example).md`
- **Subtopics & Key Concepts**:
      - **Attached Resources**
- *Key Engine Mechanisms*: `MYSQL, POSTGRES`

### 📄 05_Double Booking Problem Part 2 ( Alternative Solution and explination)
- **Transcript File**: `Skills_Input/udemy/withNasser/08_Concurrency Control/05_Double Booking Problem Part 2 ( Alternative Solution and explination).md`
- *Key Engine Mechanisms*: `ACID, B-TREE, ISOLATION, MYSQL, OPTIMISTIC, PESSIMISTIC, POSTGRES, READ COMMITTED, READ UNCOMMITTED`

- 📑 **Companion Slide Deck / Book**: `06_offset.pdf` (`Skills_Input/udemy/withNasser/08_Concurrency Control/06_offset.pdf`)

### 📄 06_SQL Pagination With Offset is Very Slow
- **Transcript File**: `Skills_Input/udemy/withNasser/08_Concurrency Control/06_SQL Pagination With Offset is Very Slow.md`
- **Subtopics & Key Concepts**:
      - **Attached Resources**
- *Key Engine Mechanisms*: `EXPLAIN ANALYZE, INDEX SCAN, PAGE, POSTGRES`

### 📄 07_Database Connection Pooling
- **Transcript File**: `Skills_Input/udemy/withNasser/08_Concurrency Control/07_Database Connection Pooling.md`
- **Subtopics & Key Concepts**:
      - **Attached Resources**
- *Key Engine Mechanisms*: `ACID, POSTGRES`

---

## 09_Database Replication

### 📄 01_Introduction to Database Replication
- **Transcript File**: `Skills_Input/udemy/withNasser/09_Database Replication/01_Introduction to Database Replication.md`
- **Subtopics & Key Concepts**:
      - **Attached Resources**
- *Key Engine Mechanisms*: `CONSISTENCY, POSTGRES, REPLICATION`

- 📑 **Companion Slide Deck / Book**: `01_Replication.odp` (`Skills_Input/udemy/withNasser/09_Database Replication/01_Replication.odp`)

- 📑 **Companion Slide Deck / Book**: `01_Replication.pdf` (`Skills_Input/udemy/withNasser/09_Database Replication/01_Replication.pdf`)

- 📑 **Companion Slide Deck / Book**: `01_Replication.pptx` (`Skills_Input/udemy/withNasser/09_Database Replication/01_Replication.pptx`)

### 📄 02_MasterStandby Replication
- **Transcript File**: `Skills_Input/udemy/withNasser/09_Database Replication/02_MasterStandby Replication.md`
- *Key Engine Mechanisms*: `CONSISTENCY, POSTGRES, REPLICATION`

### 📄 03_Multi-master Replication
- **Transcript File**: `Skills_Input/udemy/withNasser/09_Database Replication/03_Multi-master Replication.md`
- *Key Engine Mechanisms*: `REPLICATION`

### 📄 04_Synchronous vs Asynchronous Replication
- **Transcript File**: `Skills_Input/udemy/withNasser/09_Database Replication/04_Synchronous vs Asynchronous Replication.md`
- *Key Engine Mechanisms*: `CONSISTENCY, POSTGRES, REPLICATION`

### 📄 05_Replication Demo with Postgres
- **Transcript File**: `Skills_Input/udemy/withNasser/09_Database Replication/05_Replication Demo with Postgres.md`
- **Subtopics & Key Concepts**:
      - **Attached Resources**
- *Key Engine Mechanisms*: `POSTGRES, REPLICATION`

### 📄 06_Pros and Cons of Replication
- **Transcript File**: `Skills_Input/udemy/withNasser/09_Database Replication/06_Pros and Cons of Replication.md`
- *Key Engine Mechanisms*: `CONSISTENCY, POSTGRES, REPLICATION`

---

## 10_Database System Design

### 📄 01_Twitter System Design Database Design
- **Transcript File**: `Skills_Input/udemy/withNasser/10_Database System Design/01_Twitter System Design Database Design.md`
- *Key Engine Mechanisms*: `ACID, CURSOR, MYSQL, PAGE, POSTGRES, SHARDING, SQLITE`

### 📄 02_Building a Short URL System Database Backend
- **Transcript File**: `Skills_Input/udemy/withNasser/10_Database System Design/02_Building a Short URL System Database Backend.md`
- *Key Engine Mechanisms*: `B-TREE, CONSISTENCY, MYSQL, POSTGRES, REPLICATION, SHARDING`

---

## 11_Database Engines

### 📄 01_Database Engines Introduction
- **Transcript File**: `Skills_Input/udemy/withNasser/11_Database Engines/01_Database Engines Introduction.md`
- *Key Engine Mechanisms*: `ACID, MYSQL`

- 📑 **Companion Slide Deck / Book**: `02_Database Engines.odp` (`Skills_Input/udemy/withNasser/11_Database Engines/02_Database Engines.odp`)

- 📑 **Companion Slide Deck / Book**: `02_Database Engines.pdf` (`Skills_Input/udemy/withNasser/11_Database Engines/02_Database Engines.pdf`)

- 📑 **Companion Slide Deck / Book**: `02_Database Engines.pptx` (`Skills_Input/udemy/withNasser/11_Database Engines/02_Database Engines.pptx`)

### 📄 02_What is a Database Engine
- **Transcript File**: `Skills_Input/udemy/withNasser/11_Database Engines/02_What is a Database Engine.md`
- **Subtopics & Key Concepts**:
      - **Attached Resources**
- *Key Engine Mechanisms*: `ACID, ATOMICITY, CONSISTENCY, DURABILITY, ISOLATION, MYSQL, POSTGRES`

### 📄 03_XtraDB
- **Transcript File**: `Skills_Input/udemy/withNasser/11_Database Engines/03_XtraDB.md`
- *Key Engine Mechanisms*: `ACID, MYSQL`

### 📄 04_SQLite
- **Transcript File**: `Skills_Input/udemy/withNasser/11_Database Engines/04_SQLite.md`
- *Key Engine Mechanisms*: `ACID, MYSQL, POSTGRES, SQLITE`

### 📄 05_Aria
- **Transcript File**: `Skills_Input/udemy/withNasser/11_Database Engines/05_Aria.md`
- *Key Engine Mechanisms*: `MYSQL`

### 📄 06_BerkeleyDB
- **Transcript File**: `Skills_Input/udemy/withNasser/11_Database Engines/06_BerkeleyDB.md`

### 📄 07_LevelDB
- **Transcript File**: `Skills_Input/udemy/withNasser/11_Database Engines/07_LevelDB.md`
- *Key Engine Mechanisms*: `B-TREE`

### 📄 08_RocksDB
- **Transcript File**: `Skills_Input/udemy/withNasser/11_Database Engines/08_RocksDB.md`
- *Key Engine Mechanisms*: `ACID, B-TREE, MYSQL`

### 📄 09_Popular Database Engines
- **Transcript File**: `Skills_Input/udemy/withNasser/11_Database Engines/09_Popular Database Engines.md`
- *Key Engine Mechanisms*: `MYSQL, POSTGRES`

### 📄 10_MyISAM
- **Transcript File**: `Skills_Input/udemy/withNasser/11_Database Engines/10_MyISAM.md`
- *Key Engine Mechanisms*: `ACID, ATOMICITY, B-TREE, MYSQL`

### 📄 11_InnoDB
- **Transcript File**: `Skills_Input/udemy/withNasser/11_Database Engines/11_InnoDB.md`
- *Key Engine Mechanisms*: `ACID, ATOMICITY, CONSISTENCY, DURABILITY, INNODB, ISOLATION, MYSQL, POSTGRES`

### 📄 12_Switching Database Engines with mySQL
- **Transcript File**: `Skills_Input/udemy/withNasser/11_Database Engines/12_Switching Database Engines with mySQL.md`
- **Subtopics & Key Concepts**:
      - **Attached Resources**
- *Key Engine Mechanisms*: `ACID, INNODB, ISOLATION, MYSQL, POSTGRES`

---

## 12_Database Cursors

### 📄 01_What are Database Cursors
- **Transcript File**: `Skills_Input/udemy/withNasser/12_Database Cursors/01_What are Database Cursors.md`
- **Subtopics & Key Concepts**:
      - **Attached Resources**
- *Key Engine Mechanisms*: `BITMAP INDEX SCAN, CURSOR, INDEX SCAN, PAGE, POSTGRES, TABLE SCAN`

### 📄 02_Server Side vs Client Side Database Cursors
- **Transcript File**: `Skills_Input/udemy/withNasser/12_Database Cursors/02_Server Side vs Client Side Database Cursors.md`
- **Subtopics & Key Concepts**:
      - **Attached Resources**
- *Key Engine Mechanisms*: `CURSOR, POSTGRES`

### 📄 03_Inserting Million Rows with Python in Postgres using Client Side Cursor
- **Transcript File**: `Skills_Input/udemy/withNasser/12_Database Cursors/03_Inserting Million Rows with Python in Postgres using Client Side Cursor.md`
- *Key Engine Mechanisms*: `CURSOR, POSTGRES`

### 📄 04_Querying with Server Side Cursor
- **Transcript File**: `Skills_Input/udemy/withNasser/12_Database Cursors/04_Querying with Server Side Cursor.md`

### 📄 05_Pros and Cons of Server vs Client Side Cursors
- **Transcript File**: `Skills_Input/udemy/withNasser/12_Database Cursors/05_Pros and Cons of Server vs Client Side Cursors.md`
- *Key Engine Mechanisms*: `CURSOR`

### 📄 06_Article - Server Side Cursor Types in SQL Server
- **Transcript File**: `Skills_Input/udemy/withNasser/12_Database Cursors/06_Article - Server Side Cursor Types in SQL Server.md`
- **Subtopics & Key Concepts**:
      - ****DECLARE CURSOR (Transact-SQL)****
      - **Syntax**
      - **Arguments**
      - **Attached Resources**
- *Key Engine Mechanisms*: `CURSOR, ISOLATION, OPTIMISTIC`

- 📑 **Companion Slide Deck / Book**: `06_SQLServer-ServerSide-Cursor-Types.pdf` (`Skills_Input/udemy/withNasser/12_Database Cursors/06_SQLServer-ServerSide-Cursor-Types.pdf`)

---

## 13_NoSQL Architecture

### 📄 01_SQL vs NoSQL and how MongoDB Revolutionized NoSQL
- **Transcript File**: `Skills_Input/udemy/withNasser/13_NoSQL Architecture/01_SQL vs NoSQL and how MongoDB Revolutionized NoSQL.md`
- *Key Engine Mechanisms*: `B-TREE, CHECKPOINT, DURABILITY, MYSQL, PAGE, POSTGRES, REDO`

### 📄 02_MongoDB Internals
- **Transcript File**: `Skills_Input/udemy/withNasser/13_NoSQL Architecture/02_MongoDB Internals.md`
- **Subtopics & Key Concepts**:
      - **MongoDB internal Architecture**
      - **Components of MongoDB**
      - **Documents & Collections**
      - **_id index**
      - **Secondary indexes**
      - **Original MongoDB Architecture**
      - **MongoDB WiredTiger Architecture**
      - **Clustered Collections Architecture**
      - **Summary**
      - **References**
- *Key Engine Mechanisms*: `B+TREE, INNODB, MYSQL, PAGE, WAL`

### 📄 03_MongoDB Clustered Collections
- **Transcript File**: `Skills_Input/udemy/withNasser/13_NoSQL Architecture/03_MongoDB Clustered Collections.md`
- *Key Engine Mechanisms*: `ACID, B-TREE, INNODB, MYSQL, PAGE, POSTGRES`

### 📄 04_Querying with Client Side Cursor
- **Transcript File**: `Skills_Input/udemy/withNasser/13_NoSQL Architecture/04_Querying with Client Side Cursor.md`
- *Key Engine Mechanisms*: `CURSOR`

### 📄 05_MemCached In-Memory database Architecture
- **Transcript File**: `Skills_Input/udemy/withNasser/13_NoSQL Architecture/05_MemCached In-Memory database Architecture.md`
- **Subtopics & Key Concepts**:
      - **Memcached Architecture**
      - **To Cache is a cop-out**
      - **Memcached Architecture**
      - **What is Memcached?**
      - **Memory Management**
      - **Threading**
      - **LRU (Least Recently Used)**
      - **LRU Locking**
      - **Reads and Writes**
      - **Reads**
      - **Writes**
      - **Collisions**
      - **Distributed Cache**
      - **Telnet Demo**
      - **Distributed Memcached with NodeJS**
      - **Summary**
- *Key Engine Mechanisms*: `PAGE`

### 📄 06_Memcached NoSQL Architecture
- **Transcript File**: `Skills_Input/udemy/withNasser/13_NoSQL Architecture/06_Memcached NoSQL Architecture.md`
- **Subtopics & Key Concepts**:
      - **Attached Resources**
- *Key Engine Mechanisms*: `ACID, CONSISTENT HASHING, ISOLATION, PAGE, PARTITIONING, SHARDING`

- 📑 **Companion Slide Deck / Book**: `06_memcached.odp` (`Skills_Input/udemy/withNasser/13_NoSQL Architecture/06_memcached.odp`)

- 📑 **Companion Slide Deck / Book**: `06_memcached.pdf` (`Skills_Input/udemy/withNasser/13_NoSQL Architecture/06_memcached.pdf`)

- 📑 **Companion Slide Deck / Book**: `06_memcached.pptx` (`Skills_Input/udemy/withNasser/13_NoSQL Architecture/06_memcached.pptx`)

### 📄 07_NOSQL Redis Internals
- **Transcript File**: `Skills_Input/udemy/withNasser/13_NoSQL Architecture/07_NOSQL Redis Internals.md`
- **Subtopics & Key Concepts**:
      - **Attached Resources**
- *Key Engine Mechanisms*: `ACID, ATOMICITY, CONSISTENCY, CONSISTENT HASHING, DURABILITY, ISOLATION, MYSQL, PARTITIONING, POSTGRES, REPLICATION`

- 📑 **Companion Slide Deck / Book**: `07_Redis.odp` (`Skills_Input/udemy/withNasser/13_NoSQL Architecture/07_Redis.odp`)

- 📑 **Companion Slide Deck / Book**: `07_Redis.pdf` (`Skills_Input/udemy/withNasser/13_NoSQL Architecture/07_Redis.pdf`)

- 📑 **Companion Slide Deck / Book**: `07_Redis.pptx` (`Skills_Input/udemy/withNasser/13_NoSQL Architecture/07_Redis.pptx`)

### 📄 08_CAP Theorem Explained
- **Transcript File**: `Skills_Input/udemy/withNasser/13_NoSQL Architecture/08_CAP Theorem Explained.md`
- *Key Engine Mechanisms*: `ACID, ATOMICITY, CONSISTENCY, DURABILITY, ISOLATION, MYSQL, PARTITIONING, REDO, REPLICATION`

---

## 14_Database Security

### 📄 01_How to Secure Your Postgres Database by Enabling TLSSSL
- **Transcript File**: `Skills_Input/udemy/withNasser/14_Database Security/01_How to Secure Your Postgres Database by Enabling TLSSSL.md`
- *Key Engine Mechanisms*: `PAGE, POSTGRES`

### 📄 02_Deep Look into Postgres Wire Protocol with Wireshark
- **Transcript File**: `Skills_Input/udemy/withNasser/14_Database Security/02_Deep Look into Postgres Wire Protocol with Wireshark.md`
- *Key Engine Mechanisms*: `POSTGRES`

### 📄 03_Deep Look Into MongoDB Wire Protocol with Wireshark
- **Transcript File**: `Skills_Input/udemy/withNasser/14_Database Security/03_Deep Look Into MongoDB Wire Protocol with Wireshark.md`
- *Key Engine Mechanisms*: `CURSOR, SHARDING`

### 📄 04_What is the Largest SQL Statement that You can Send to Your Database
- **Transcript File**: `Skills_Input/udemy/withNasser/14_Database Security/04_What is the Largest SQL Statement that You can Send to Your Database.md`
- *Key Engine Mechanisms*: `POSTGRES`

### 📄 05_Best Practices Working with REST & Databases
- **Transcript File**: `Skills_Input/udemy/withNasser/14_Database Security/05_Best Practices Working with REST & Databases.md`
- *Key Engine Mechanisms*: `POSTGRES`

### 📄 06_Database Permissions and Best Practices for Building REST API
- **Transcript File**: `Skills_Input/udemy/withNasser/14_Database Security/06_Database Permissions and Best Practices for Building REST API.md`
- *Key Engine Mechanisms*: `PAGE, POSTGRES`

---

## 15_Homomorphic Encryption - Performing Database Queries on Encrypted Data

- 💻 **Companion Script / Command File**: `01_commands.txt` (`Skills_Input/udemy/withNasser/15_Homomorphic Encryption - Performing Database Queries on Encrypted Data/01_commands.txt`)

- 📑 **Companion Slide Deck / Book**: `01_Homomorphic Encryption.odp` (`Skills_Input/udemy/withNasser/15_Homomorphic Encryption - Performing Database Queries on Encrypted Data/01_Homomorphic Encryption.odp`)

- 📑 **Companion Slide Deck / Book**: `01_Homomorphic Encryption.pdf` (`Skills_Input/udemy/withNasser/15_Homomorphic Encryption - Performing Database Queries on Encrypted Data/01_Homomorphic Encryption.pdf`)

- 📑 **Companion Slide Deck / Book**: `01_Homomorphic Encryption.pptx` (`Skills_Input/udemy/withNasser/15_Homomorphic Encryption - Performing Database Queries on Encrypted Data/01_Homomorphic Encryption.pptx`)

- 💻 **Companion Script / Command File**: `01_Homomorphic Encryption.txt` (`Skills_Input/udemy/withNasser/15_Homomorphic Encryption - Performing Database Queries on Encrypted Data/01_Homomorphic Encryption.txt`)

### 📄 01_Introduction to Homomorphic Encryption
- **Transcript File**: `Skills_Input/udemy/withNasser/15_Homomorphic Encryption - Performing Database Queries on Encrypted Data/01_Introduction to Homomorphic Encryption.md`
- **Subtopics & Key Concepts**:
      - **Attached Resources**

### 📄 02_What is Encryption
- **Transcript File**: `Skills_Input/udemy/withNasser/15_Homomorphic Encryption - Performing Database Queries on Encrypted Data/02_What is Encryption.md`

### 📄 03_Why Can't we always Encrypt
- **Transcript File**: `Skills_Input/udemy/withNasser/15_Homomorphic Encryption - Performing Database Queries on Encrypted Data/03_Why Can't we always Encrypt.md`

### 📄 04_What is Homomorphic Encryption
- **Transcript File**: `Skills_Input/udemy/withNasser/15_Homomorphic Encryption - Performing Database Queries on Encrypted Data/04_What is Homomorphic Encryption.md`

### 📄 05_Homomorphic Encryption Demo
- **Transcript File**: `Skills_Input/udemy/withNasser/15_Homomorphic Encryption - Performing Database Queries on Encrypted Data/05_Homomorphic Encryption Demo.md`

### 📄 06_Clone and Build the Code
- **Transcript File**: `Skills_Input/udemy/withNasser/15_Homomorphic Encryption - Performing Database Queries on Encrypted Data/06_Clone and Build the Code.md`
- *Key Engine Mechanisms*: `PAGE`

### 📄 07_Going Through the Code and the Database
- **Transcript File**: `Skills_Input/udemy/withNasser/15_Homomorphic Encryption - Performing Database Queries on Encrypted Data/07_Going Through the Code and the Database.md`

### 📄 08_Searching The Encrypted Database
- **Transcript File**: `Skills_Input/udemy/withNasser/15_Homomorphic Encryption - Performing Database Queries on Encrypted Data/08_Searching The Encrypted Database.md`

### 📄 09_Is Homomorphic Encryption Ready
- **Transcript File**: `Skills_Input/udemy/withNasser/15_Homomorphic Encryption - Performing Database Queries on Encrypted Data/09_Is Homomorphic Encryption Ready.md`

---

## 16_Answering your Questions

### 📄 01_Heap Index scan instead of Index only scan why
- **Transcript File**: `Skills_Input/udemy/withNasser/16_Answering your Questions/01_Heap Index scan instead of Index only scan why.md`
- *Key Engine Mechanisms*: `B-TREE, BITMAP INDEX SCAN, EXPLAIN ANALYZE, ISOLATION, MVCC, PAGE, POSTGRES, READ COMMITTED`

### 📄 02_What is the unit of the Cost in Postgres Planner
- **Transcript File**: `Skills_Input/udemy/withNasser/16_Answering your Questions/02_What is the unit of the Cost in Postgres Planner.md`
- *Key Engine Mechanisms*: `PAGE, POSTGRES`

### 📄 03_All Isolation Levels - Explained Details
- **Transcript File**: `Skills_Input/udemy/withNasser/16_Answering your Questions/03_All Isolation Levels - Explained Details.md`
- *Key Engine Mechanisms*: `ISOLATION, MYSQL, OPTIMISTIC, PESSIMISTIC, PHANTOM, POSTGRES, READ COMMITTED, READ UNCOMMITTED, REPEATABLE READ, SERIALIZABLE`

### 📄 04_Snapshot and Repeatable Read Isolation difference
- **Transcript File**: `Skills_Input/udemy/withNasser/16_Answering your Questions/04_Snapshot and Repeatable Read Isolation difference.md`
- *Key Engine Mechanisms*: `INDEX SCAN, ISOLATION, PAGE, PHANTOM, POSTGRES, READ COMMITTED, REPEATABLE READ`

### 📄 05_I have an Index why is the database doing a full table scan
- **Transcript File**: `Skills_Input/udemy/withNasser/16_Answering your Questions/05_I have an Index why is the database doing a full table scan.md`
- *Key Engine Mechanisms*: `PAGE, POSTGRES`

### 📄 06_Why Databases Read Pages instead of Rows
- **Transcript File**: `Skills_Input/udemy/withNasser/16_Answering your Questions/06_Why Databases Read Pages instead of Rows.md`
- *Key Engine Mechanisms*: `PAGE`

### 📄 07_How does Indexing a column with duplicate values work
- **Transcript File**: `Skills_Input/udemy/withNasser/16_Answering your Questions/07_How does Indexing a column with duplicate values work.md`
- *Key Engine Mechanisms*: `PAGE`

### 📄 08_Should I drop unused indexes
- **Transcript File**: `Skills_Input/udemy/withNasser/16_Answering your Questions/08_Should I drop unused indexes.md`
- *Key Engine Mechanisms*: `PAGE, POSTGRES`

### 📄 09_Why use serializable Isolation Level when we have SELECT FOR UPDATE
- **Transcript File**: `Skills_Input/udemy/withNasser/16_Answering your Questions/09_Why use serializable Isolation Level when we have SELECT FOR UPDATE.md`
- *Key Engine Mechanisms*: `ISOLATION, OPTIMISTIC, PESSIMISTIC`

### 📄 10_Can I use the same database connection for multiple clients
- **Transcript File**: `Skills_Input/udemy/withNasser/16_Answering your Questions/10_Can I use the same database connection for multiple clients.md`

### 📄 11_Do I need a transaction if I'm only reading
- **Transcript File**: `Skills_Input/udemy/withNasser/16_Answering your Questions/11_Do I need a transaction if I'm only reading.md`
- *Key Engine Mechanisms*: `PAGE, POSTGRES`

### 📄 12_Why does an update in Postgres touches all indexes
- **Transcript File**: `Skills_Input/udemy/withNasser/16_Answering your Questions/12_Why does an update in Postgres touches all indexes.md`
- *Key Engine Mechanisms*: `B-TREE, DURABILITY, MYSQL, PAGE, POSTGRES, REPLICATION`

### 📄 13_What is the value of bitmap index scan
- **Transcript File**: `Skills_Input/udemy/withNasser/16_Answering your Questions/13_What is the value of bitmap index scan.md`
- *Key Engine Mechanisms*: `BITMAP INDEX SCAN, INDEX SCAN, MYSQL, PAGE, POSTGRES, REPLICATION, TABLE SCAN`

### 📄 14_What does Explain Analyze actually do
- **Transcript File**: `Skills_Input/udemy/withNasser/16_Answering your Questions/14_What does Explain Analyze actually do.md`
- *Key Engine Mechanisms*: `ACID, B-TREE, DURABILITY, EXPLAIN ANALYZE, INDEX SCAN, MVCC, MYSQL, PAGE, POSTGRES, REDO`

### 📄 15_Postgres vs MySQL (The fundamental differences)
- **Transcript File**: `Skills_Input/udemy/withNasser/16_Answering your Questions/15_Postgres vs MySQL (The fundamental differences).md`
- **Subtopics & Key Concepts**:
      - **Postgres vs MySQL**
      - **The main differences with examples**
      - **But First.. Fundamentals**
      - **MySQL**
      - **Postgres**
      - **Queries Cost**
      - **Data types Matter**
      - **Undo logs**
      - **Processes vs Threads**
      - **Summary**
- *Key Engine Mechanisms*: `B+TREE, INDEX SCAN, INDEX SEEK, INNODB, ISOLATION, MVCC, MYSQL, PAGE, POSTGRES, READ COMMITTED, UNDO`

### 📄 16_Does Create Index block writes and Why
- **Transcript File**: `Skills_Input/udemy/withNasser/16_Answering your Questions/16_Does Create Index block writes and Why.md`
- *Key Engine Mechanisms*: `POSTGRES`

### 📄 17_Postgres Process Architecture
- **Transcript File**: `Skills_Input/udemy/withNasser/16_Answering your Questions/17_Postgres Process Architecture.md`
- **Subtopics & Key Concepts**:
      - **PostgreSQL Process Architecture**
      - **Postmaster Process**
      - **Backend Process**
      - **Background Workers**
      - **Parallel Queries**
      - **Pros and Cons of Parallel Queries**
      - **Notes on Background workers**
      - **Auxiliary Processes**
      - **Background Writer (bw)**
      - **Checkpointer (cp)**
      - **Startup Process (st)**
      - **Logger (lg)**
      - **Autovacuum Launcher (avl)**
      - **WAL writer (ww)**
      - **WAL archiver (wa)**
      - **WAL receiver (wr)**
      - **Other Processes**
      - **Autovaccume workers**
      - **WAL senders**
      - **Process vs Thread**
      - **Summary**
- *Key Engine Mechanisms*: `CHECKPOINT, DURABILITY, PAGE, POSTGRES, REDO, REPLICATION, UNDO, WAL`

### 📄 18_Index Scan vs Index Seek
- **Transcript File**: `Skills_Input/udemy/withNasser/16_Answering your Questions/18_Index Scan vs Index Seek.md`
- **Subtopics & Key Concepts**:
      - **B+Tree Index Seek vs Index Scan**
      - **To Seek or To Scan**
      - **Index Seek Example**
      - **Index Scan Example**
      - **We do we need a seek and a scan?**
      - **Where it breaks down**
      - **Summary**
- *Key Engine Mechanisms*: `B+TREE, INDEX SCAN, INDEX SEEK, PAGE, TABLE SCAN`

---

## 17_Database Discussions

### 📄 01_SELECT COUNT () can impact your Backend Application performance, here is why
- **Transcript File**: `Skills_Input/udemy/withNasser/17_Database Discussions/01_SELECT COUNT () can impact your Backend Application performance, here is why.md`
- *Key Engine Mechanisms*: `INDEX SCAN, POSTGRES`

### 📄 02_How Shopify Switched from UUID as Primary Key
- **Transcript File**: `Skills_Input/udemy/withNasser/17_Database Discussions/02_How Shopify Switched from UUID as Primary Key.md`
- *Key Engine Mechanisms*: `MYSQL, PAGE`

### 📄 03_How does the Database Store Data On Disk
- **Transcript File**: `Skills_Input/udemy/withNasser/17_Database Discussions/03_How does the Database Store Data On Disk.md`
- *Key Engine Mechanisms*: `B-TREE, PAGE`

### 📄 04_Postgres Architecture
- **Transcript File**: `Skills_Input/udemy/withNasser/17_Database Discussions/04_Postgres Architecture.md`
- *Key Engine Mechanisms*: `CHECKPOINT, DURABILITY, INNODB, MVCC, MYSQL, PAGE, POSTGRES, REDO, REPLICATION, UNDO`

### 📄 05_Is QUIC a Good Protocol for Databases
- **Transcript File**: `Skills_Input/udemy/withNasser/17_Database Discussions/05_Is QUIC a Good Protocol for Databases.md`
- *Key Engine Mechanisms*: `POSTGRES`

### 📄 06_What is a Distributed Transaction
- **Transcript File**: `Skills_Input/udemy/withNasser/17_Database Discussions/06_What is a Distributed Transaction.md`
- *Key Engine Mechanisms*: `ACID, ATOMICITY, CONSISTENCY, DURABILITY, ISOLATION, POSTGRES`

### 📄 07_Hash Tables and Consistent Hashing
- **Transcript File**: `Skills_Input/udemy/withNasser/17_Database Discussions/07_Hash Tables and Consistent Hashing.md`
- *Key Engine Mechanisms*: `CONSISTENCY, CONSISTENT HASHING, PARTITIONING, REPLICATION, SHARDING`

### 📄 08_Indexing in PostgreSQL vs MySQL
- **Transcript File**: `Skills_Input/udemy/withNasser/17_Database Discussions/08_Indexing in PostgreSQL vs MySQL.md`
- *Key Engine Mechanisms*: `INDEX SCAN, MYSQL, POSTGRES`

### 📄 09_Why Uber Moved from Postgres to MySQL (Discussion)
- **Transcript File**: `Skills_Input/udemy/withNasser/17_Database Discussions/09_Why Uber Moved from Postgres to MySQL (Discussion).md`
- *Key Engine Mechanisms*: `ACID, ATOMICITY, B-TREE, CONSISTENCY, ISOLATION, MVCC, MYSQL, PAGE, POSTGRES, REPLICATION, SHARDING, UNDO`

### 📄 10_Can NULLs Improve your Database Queries Performance
- **Transcript File**: `Skills_Input/udemy/withNasser/17_Database Discussions/10_Can NULLs Improve your Database Queries Performance.md`
- **Subtopics & Key Concepts**:
      - **Attached Resources**
- *Key Engine Mechanisms*: `PAGE, POSTGRES`

- 📑 **Companion Slide Deck / Book**: `10_NULL.pdf` (`Skills_Input/udemy/withNasser/17_Database Discussions/10_NULL.pdf`)

### 📄 11_Write Amplification Explained in Backend Apps, Database Systems and SSDs
- **Transcript File**: `Skills_Input/udemy/withNasser/17_Database Discussions/11_Write Amplification Explained in Backend Apps, Database Systems and SSDs.md`
- *Key Engine Mechanisms*: `B-TREE, MYSQL, PAGE, POSTGRES`

### 📄 12_WAL, Redo and Undo logs
- **Transcript File**: `Skills_Input/udemy/withNasser/17_Database Discussions/12_WAL, Redo and Undo logs.md`
- *Key Engine Mechanisms*: `CHECKPOINT, DURABILITY, ISOLATION, PAGE, POSTGRES, REDO, UNDO`

### 📄 13_Optimistic vs Pessmistic Concurrency Control
- **Transcript File**: `Skills_Input/udemy/withNasser/17_Database Discussions/13_Optimistic vs Pessmistic Concurrency Control.md`
- *Key Engine Mechanisms*: `ISOLATION, MYSQL, OPTIMISTIC, PAGE, PESSIMISTIC, POSTGRES`

### 📄 14_Avoid SELECT , even on a single-column tables
- **Transcript File**: `Skills_Input/udemy/withNasser/17_Database Discussions/14_Avoid SELECT , even on a single-column tables.md`
- **Subtopics & Key Concepts**:
      - **A story from 2012**
      - **How database reads work**
      - **Kiss Index-Only Scans Goodbye**
      - **Deserialization Cost**
      - **Not All Columns Are Inline**
      - **Network Cost**
      - **Client Deserialization**
      - **Unpredictability**
      - **Code Grep**
      - **Summary**
- *Key Engine Mechanisms*: `PAGE, POSTGRES`

### 📄 15_Postgres Locks - A Deep Dive
- **Transcript File**: `Skills_Input/udemy/withNasser/17_Database Discussions/15_Postgres Locks - A Deep Dive.md`
- **Subtopics & Key Concepts**:
      - **Postgres Locks — A Deep Dive**
      - **Attached Resources**
- *Key Engine Mechanisms*: `POSTGRES`

- 📑 **Companion Slide Deck / Book**: `15_Postgres Locks — A Deep Dive-New.pdf` (`Skills_Input/udemy/withNasser/17_Database Discussions/15_Postgres Locks — A Deep Dive-New.pdf`)

### 📄 16_How Slow is select in row store
- **Transcript File**: `Skills_Input/udemy/withNasser/17_Database Discussions/16_How Slow is select in row store.md`
- **Subtopics & Key Concepts**:
      - **How Slow is Select * in row stores?**
      - ****Kiss Index-Only Scans Goodbye****
      - ****Deserialization Cost****
      - ****Not All Columns Are Inline****
      - ****Network Cost****
      - ****Client Deserialization****
      - ****Unpredictability****
      - ****Summary****
      - **Attached Resources**
- *Key Engine Mechanisms*: `PAGE, POSTGRES`

- 📑 **Companion Slide Deck / Book**: `16_howslowisselect.epub` (`Skills_Input/udemy/withNasser/17_Database Discussions/16_howslowisselect.epub`)

- 📑 **Companion Slide Deck / Book**: `16_howslowisselect.pdf` (`Skills_Input/udemy/withNasser/17_Database Discussions/16_howslowisselect.pdf`)

### 📄 17_MySQL InnoDB Advanced Locking Techniques
- **Transcript File**: `Skills_Input/udemy/withNasser/17_Database Discussions/17_MySQL InnoDB Advanced Locking Techniques.md`
- *Key Engine Mechanisms*: `ATOMICITY, B-TREE, INNODB, MYSQL, PAGE`

---

## 18_Archived Lectures

- 📑 **Companion Slide Deck / Book**: `01_ACID.odp` (`Skills_Input/udemy/withNasser/18_Archived Lectures/01_ACID.odp`)

- 📑 **Companion Slide Deck / Book**: `01_ACID.pdf` (`Skills_Input/udemy/withNasser/18_Archived Lectures/01_ACID.pdf`)

- 📑 **Companion Slide Deck / Book**: `01_ACID.pptx` (`Skills_Input/udemy/withNasser/18_Archived Lectures/01_ACID.pptx`)

### 📄 01_Introduction to ACID (Archived)
- **Transcript File**: `Skills_Input/udemy/withNasser/18_Archived Lectures/01_Introduction to ACID (Archived).md`
- **Subtopics & Key Concepts**:
      - **Attached Resources**
- *Key Engine Mechanisms*: `ACID, ATOMICITY, CONSISTENCY, DURABILITY, ISOLATION, MYSQL, POSTGRES`

### 📄 02_What is a Transaction (Archived)
- **Transcript File**: `Skills_Input/udemy/withNasser/18_Archived Lectures/02_What is a Transaction (Archived).md`

### 📄 03_Atomicity (Archived 2022)
- **Transcript File**: `Skills_Input/udemy/withNasser/18_Archived Lectures/03_Atomicity (Archived 2022).md`
- *Key Engine Mechanisms*: `ATOMICITY, POSTGRES`

### 📄 04_Isolation (Archived 2022)
- **Transcript File**: `Skills_Input/udemy/withNasser/18_Archived Lectures/04_Isolation (Archived 2022).md`
- *Key Engine Mechanisms*: `CONSISTENCY, DIRTY READ, ISOLATION, PHANTOM, READ COMMITTED, READ UNCOMMITTED, REPEATABLE READ, SERIALIZABLE`

### 📄 05_Consistency (Archived 2022)
- **Transcript File**: `Skills_Input/udemy/withNasser/18_Archived Lectures/05_Consistency (Archived 2022).md`
- *Key Engine Mechanisms*: `ACID, ATOMICITY, CONSISTENCY, ISOLATION, MYSQL, POSTGRES, SHARDING`

### 📄 06_Durability (Archived 2022)
- **Transcript File**: `Skills_Input/udemy/withNasser/18_Archived Lectures/06_Durability (Archived 2022).md`
- *Key Engine Mechanisms*: `CONSISTENCY, DURABILITY`

### 📄 07_Atomicity (Archived 2024)
- **Transcript File**: `Skills_Input/udemy/withNasser/18_Archived Lectures/07_Atomicity (Archived 2024).md`
- *Key Engine Mechanisms*: `ACID, ATOMICITY, OPTIMISTIC`

---

