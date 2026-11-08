# Relational Database: Complete Outline

A full topic-by-topic outline covering relational database concepts, from fundamentals to advanced topics.

## 1. Introduction to Databases

- Data, information, and databases
- File system vs. DBMS
- Advantages of a DBMS
- DBMS architecture (1-tier, 2-tier, 3-tier)
- Three-schema architecture and data independence
- Database users and roles (DBA, developers, end users)
- Data models (hierarchical, network, relational, object-oriented, NoSQL)

## 2. Entity-Relationship (ER) Modeling

- Entities, attributes, and relationships
- Attribute types (simple, composite, multivalued, derived)
- Keys (super, candidate, primary, alternate, composite)
- Cardinality (1:1, 1:N, M:N) and participation constraints
- Weak entities
- Enhanced ER: generalization, specialization, aggregation
- ER diagram notation

## 3. The Relational Model

- Core terms: relation, tuple, attribute, domain, degree, cardinality
- Properties of relations
- Keys: primary, candidate, foreign, composite
- Integrity constraints (domain, entity, referential, key)
- Converting ER diagrams to relational schemas

## 4. Relational Algebra and Calculus

- Basic operators: selection (σ), projection (π), union, difference, Cartesian product, rename
- Derived operators: intersection, joins (inner, outer, natural, theta), division
- Tuple relational calculus
- Domain relational calculus
- Query equivalence and expressive power

## 5. SQL

- **DDL:** CREATE, ALTER, DROP, TRUNCATE
- **DML:** SELECT, INSERT, UPDATE, DELETE
- **DCL:** GRANT, REVOKE
- **TCL:** COMMIT, ROLLBACK, SAVEPOINT
- Constraints: NOT NULL, UNIQUE, PRIMARY KEY, FOREIGN KEY, CHECK, DEFAULT
- Filtering and sorting: WHERE, ORDER BY, LIKE, IN, BETWEEN
- Aggregate functions: COUNT, SUM, AVG, MIN, MAX
- GROUP BY and HAVING
- Joins (INNER, LEFT, RIGHT, FULL, CROSS, SELF)
- Subqueries (nested, correlated)
- Set operations: UNION, INTERSECT, EXCEPT
- Views, indexes, and sequences
- Stored procedures, functions, triggers, and cursors
- Window functions and common table expressions (CTEs)

## 6. Database Design and Normalization

- Design guidelines and anomalies (insertion, update, deletion)
- Functional dependencies and Armstrong's axioms
- Closure of attributes and canonical cover
- Normal forms: 1NF, 2NF, 3NF, BCNF
- Multivalued dependencies and 4NF
- Join dependencies and 5NF
- Lossless-join and dependency-preserving decomposition
- Denormalization and when to use it

## 7. Storage and File Organization

- Storage hierarchy (primary, secondary, tertiary)
- Disk structure and RAID levels
- File organization: heap, sequential, hashed, clustered
- Records, blocks, and buffer management

## 8. Indexing and Hashing

- Single-level and multilevel indexes
- Primary, secondary, and clustering indexes
- B-tree and B+ tree
- Static and dynamic hashing (extendible, linear)
- Bitmap indexes

## 9. Query Processing and Optimization

- Query parsing, translation, and execution plans
- Cost estimation
- Heuristic optimization and equivalence rules
- Join algorithms (nested loop, sort-merge, hash join)
- Using EXPLAIN and query tuning

## 10. Transaction Management

- Transaction concepts and states
- **ACID properties**
- Schedules: serial, serializable, recoverable, cascadeless
- Conflict and view serializability
- Precedence graphs

## 11. Concurrency Control

- Problems: lost update, dirty read, non-repeatable read, phantom read
- Isolation levels
- Lock-based protocols (shared/exclusive, two-phase locking)
- Deadlock: prevention, detection, recovery
- Timestamp-based protocols
- Optimistic and multiversion concurrency control (MVCC)

## 12. Database Recovery

- Failure types (transaction, system, media)
- Log-based recovery (deferred and immediate update)
- Write-ahead logging
- Checkpoints
- ARIES algorithm
- Shadow paging
- Backup and restore strategies

## 13. Database Security and Administration

- Authentication and authorization
- Access control (discretionary, role-based)
- SQL injection and prevention
- Encryption and auditing
- Backup, monitoring, and performance tuning

## 14. Advanced and Emerging Topics

- Distributed databases: fragmentation, replication, two-phase commit
- CAP theorem and BASE vs. ACID
- Parallel databases
- Data warehousing, OLAP vs. OLTP, star and snowflake schemas
- NoSQL (document, key-value, column-family, graph)
- Object-relational databases
- NewSQL and cloud databases

## 15. Practical Component

- Installing and using a DBMS (MySQL, PostgreSQL, Oracle, SQL Server)
- Designing a schema from requirements
- Writing and optimizing queries
- Mini-project: end-to-end database application
