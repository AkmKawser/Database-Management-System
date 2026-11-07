# Relational Schema Design & Normalization Template

A deterministic, mathematical blueprint for analyzing business specifications, identifying functional dependencies, deriving minimal covers, synthesizing relational schemas, and proving normal form invariants (1NF $\to$ 2NF $\to$ 3NF $\to$ BCNF).

---

## 🧭 Purpose & Agent Guardrail

> **Mandatory Rule for the Agent**: Never generate raw table DDLs directly from a prompt without first extracting explicit functional dependencies, computing candidate keys, and validating normal forms through the formal phases defined below.

---

## 📋 Phase 1: Entity & Functional Dependency Extraction

### 1. Attribute Universe ($\mathcal{U}$)
List every unique attribute identified in the domain requirements:
$$\mathcal{U} = \{A_1, A_2, \dots, A_n\}$$

### 2. Functional Dependency Set ($\mathcal{F}$)
Express all business constraints and business rules as functional dependencies of the form $X \to Y$, where $X, Y \subseteq \mathcal{U}$:
- $FD_1: X_1 \to Y_1$ (Business justification)
- $FD_2: X_2 \to Y_2$ (Business justification)
- ...

---

## 🔑 Phase 2: Candidate Key & Closure Derivation

### 1. Attribute Closure Algorithm ($X^+$)
For each candidate determinant set $X$:
1. Initialize $X^{(0)} = X$.
2. Repeatedly apply $Y \to Z \in \mathcal{F}$: if $Y \subseteq X^{(i)}$, then $X^{(i+1)} = X^{(i)} \cup Z$.
3. Terminate when $X^{(i+1)} = X^{(i)}$. $X^+ = X^{(i)}$.

### 2. Candidate Keys Definition
Identify all minimal superkeys $K \subseteq \mathcal{U}$ such that:
1. $K^+ = \mathcal{U}$ (Superkey property)
2. $\forall A \in K, (K \setminus \{A\})^+ \neq \mathcal{U}$ (Minimality property)

### 3. Prime vs. Non-Prime Attribute Classification
- **Prime Attributes**: Any attribute belonging to at least one candidate key $K$.
- **Non-Prime Attributes**: Attributes that belong to no candidate key.

---

## 📐 Phase 3: Minimal Cover (Canonical Cover $\mathcal{F}_c$) Derivation

1. **Deconstruct RHS**: Ensure every FD in $\mathcal{F}$ has a single attribute on the right-hand side ($X \to A_1 A_2 \implies X \to A_1, X \to A_2$).
2. **Remove Extraneous LHS Attributes**: For $X \to Y$, test if $A \in X$ is extraneous by checking if $(X \setminus \{A\})^+$ under $\mathcal{F}$ contains $Y$.
3. **Eliminate Redundant FDs**: For each $FD_i \in \mathcal{F}$, check if $\mathcal{F} \setminus \{FD_i\} \models FD_i$. If yes, delete $FD_i$.
4. **Merge Identical Determinants**: Recombine dependencies with identical LHS ($X \to Y_1, X \to Y_2 \implies X \to Y_1 Y_2$).

---

## 🔍 Phase 4: Normal Form Invariant Audit

Audit the schema iteratively against the hierarchy of normal forms:

| Normal Form | Formal Condition / Invariant | Common Violations & Solutions |
| :--- | :--- | :--- |
| **1NF** | Every attribute domain contains only atomic (indivisible) values; no repeating groups or nested collections. | Unnest comma-separated strings or JSON arrays into distinct rows or child tables. |
| **2NF** | In 1NF and **no non-prime attribute is partially dependent on any candidate key** (i.e., $X \to A$ where $X \subset K$ is disallowed). | Decompose partial dependencies into a dedicated relation with $X$ as primary key. |
| **3NF** | In 2NF and for every non-trivial $X \to A$, **either $X$ is a superkey OR $A$ is a prime attribute** (eliminates transitive dependencies). | Decompose transitive dependencies $X \to Y \to A$ into separate relations $(X, Y)$ and $(Y, A)$. |
| **BCNF** | For every non-trivial functional dependency $X \to A$, **$X$ MUST be a superkey**. | Decompose relation $R$ into $R_1(X \cup A)$ and $R_2(R \setminus A)$. Check for dependency preservation trade-offs! |

---

## ⚖️ Phase 5: Trade-off Evaluation (3NF vs. BCNF & Lossless Join)

When decomposing relations:
1. **Lossless-Join Guarantee**: A decomposition of $R$ into $(R_1, R_2)$ is guaranteed lossless if and only if:
   $$(R_1 \cap R_2) \to (R_1 \setminus R_2) \in \mathcal{F}^+ \quad \text{or} \quad (R_1 \cap R_2) \to (R_2 \setminus R_1) \in \mathcal{F}^+$$
2. **Dependency Preservation**: Check whether all FDs in $\mathcal{F}_c$ can be enforced without requiring cross-table joins.
   > **Proactive Consultation Rule**: If a decomposition achieves BCNF but sacrifices dependency preservation (e.g., $AB \to C, C \to B$), the agent **must** inform the user and request confirmation on whether to keep 3NF (preserving dependencies) or enforce BCNF (requiring application-layer assertions or triggers).

---

## 🛠️ Phase 6: Production SQL DDL Synthesis

Generate verified, production-ready DDL definitions:
- Explicit `PRIMARY KEY` and `FOREIGN KEY (..) REFERENCES .. ON DELETE CASCADE/SET NULL` constraints.
- Correct nullability (`NOT NULL`), default values, check constraints (`CHECK (...)`).
- Dedicated foreign key indexing to prevent full table scans and deadlocks during cascading updates.
