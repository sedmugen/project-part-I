# DailyKhata Cross-Document Consistency Rules

## Purpose and Scope

This rulebook establishes mandatory consistency and backward-compatibility rules across all DailyKhata project deliverables, system specifications, and implementation documents.

Its purpose is to prevent scope drift, persona contradictions, unrecorded priority inflation, and terminology divergence across the project lifecycle.

---

## 1. Core Consistency Principles

### 1.1 Backward Compatibility
Every subsequent project deliverable must remain fully compatible with previously approved deliverables:
- Deliverable 2 inherits the target market, user problems, personas, and scope baseline established in Deliverable 1.
- Deliverable 3 decomposes the elicitation findings and candidate requirements from Deliverables 1 and 2 into formal functional specifications.
- Later deliverables may elaborate, refine, or decompose approved concepts, but they must never silently contradict, rename, or invalidate earlier baselines.

### 1.2 No Silent Scope Changes
- Features and capabilities may not be introduced, removed, or shifted between priority tiers (Must Have, Should Have, Could Have, Future Scope, Out of Scope) without a formal decision in [`DECISION_LOG.md`](DECISION_LOG.md).
- Optional features (Should Have or Could Have) must never silently become mandatory commitments in later documents.
- Future Scope or Out of Scope items must not be partially implemented or promised as current commitments without team consensus and recorded approval.

### 1.3 Stable Persona Model
The project relies on five canonical personas defined in [`CANONICAL_TERMINOLOGY.md`](CANONICAL_TERMINOLOGY.md):
- **P-01 (Ayesha Tariq, 34):** Homemaker and household budget manager (Primary).
- **P-02 (Bilal Ahmed, 27):** Salaried professional (Primary).
- **P-03 (Hamza Sheikh, 21):** University student (Primary).
- **P-04 (Zubair Hassan, age unrecorded):** Family member and spouse (Secondary beneficiary; reviews shared summaries; no multi-user household login).
- **P-05 (Usman Raza, 41):** Small shopkeeper (Secondary direct user; expense tracking and petty cash only; sales and inventory excluded).

No deliverable may alter persona names, canonical ages, or primary/secondary classifications.

### 1.4 Persistent Identifiers
- Scope identifiers (`SC-01` to `SC-30`, `SS-03` to `SS-11`) must remain stable across all matrices.
- Formal requirement identifiers (`BR-###`, `FR-[SUBSYSTEM]-###`, `NFR-[QUALITY]-###`) must remain permanent once established in Deliverable 3.
- If a requirement is deprecated or modified, its identifier must be retired or marked superseded. Never reuse a retired identifier for a different capability.

### 1.5 Terminology Discipline
- Always use canonical terms defined in [`CANONICAL_TERMINOLOGY.md`](CANONICAL_TERMINOLOGY.md).
- Do not introduce arbitrary synonyms that obscure system concepts (e.g. do not alternate between "expense category" and "budget bucket" or "accounting account" and "ledger tab").

### 1.6 External Deliverable Self-Containment
Submission deliverables (`01_Deliverable_1`, `02_Deliverable_2`, `03_Deliverable_3`) are evaluated by academic examiners. They must be completely readable and self-contained without requiring the reader to have access to this internal `00_Project_Governance` directory.

---

## 2. Invariant Architecture Boundaries

When drafting or evaluating deliverables, the following architectural invariants must be preserved:

| Boundary | Invariant Rule | Forbidden Drift |
| :--- | :--- | :--- |
| **Household Boundary** | Single-account system. Primary user manages records; family members review shared/exported summaries. | Describing multi-user logins, household member invitations, or collaborative editing as current scope. |
| **Shopkeeper Boundary** | Petty cash, supplier expense receipts, and expense summaries only. | Introducing POS features, retail customer sales ledgers (udhaar), inventory, or payroll. |
| **Accounting Boundary** | Full internal Chart of Accounts operating behind user-friendly categories. Double-entry journals must balance wherever implemented. | Forcing users to enter debit/credit journals or claiming audited statutory IFRS / tax compliance. |
| **AI Assistant Boundary** | Conversational responses grounded strictly in the user's authorised stored financial records. Read-only access. | Allowing the assistant to execute bank payments, transfer funds, or claiming predictive anomaly detection. |
| **Localisation Boundary** | English and Urdu localisation is Should Have (`SC-28`). Predefined local English labels (e.g. Ration) are Must Have (`SC-13`). | Claiming full Urdu translation is complete before it has been implemented and validated. |
| **Data Integrity Boundary** | Mandatory user review and confirmation before committing OCR extraction or category proposals (`SC-07`, `SC-12`). | Overwriting raw receipt text with normalised classifications or silently saving unreviewed predictions. |

---

## 3. Conflict Resolution Protocol

When a conflict, ambiguity, or discrepancy arises between documents or during implementation:

```
[Discrepancy Identified]
        │
        ▼
[Check Authoritative Source]
  - Scope / Priorities  ──► PROJECT_SCOPE.md
  - Terminology / Roles ──► CANONICAL_TERMINOLOGY.md
  - Style / Writing     ──► DOCUMENTATION_STANDARD.md
        │
        ▼
[Does Existing Baseline Resolve It?]
  ├─► YES: Correct the drifting document to match governance.
  └─► NO:  Team discussion + Supervisor consultation.
        │
        ▼
[Formulate Resolution]
  - Create new entry in DECISION_LOG.md (e.g. DEC-21).
  - Update relevant governance file(s).
  - Propagate change across all affected deliverables.
  - Re-run consistency verification checklist.
```

---

## 4. Cross-Document Consistency Checklist

Use this checklist prior to finalising any deliverable or major pull request:

### Scope and Priorities
- [ ] Every feature mentioned in the document exists in `PROJECT_SCOPE.md`.
- [ ] No Must Have feature is downgraded to Should Have without an active decision log entry.
- [ ] No Should Have or Could Have feature is framed as a mandatory requirement.
- [ ] No Out of Scope item (`OS-01` to `OS-20`) is described as being developed or supported.
- [ ] Future Scope features are explicitly described as long-term possibilities, not current deliverables.

### Personas and Stakeholders
- [ ] All five personas (P-01 to P-05) use canonical names, roles, and ages.
- [ ] Usman Raza is described with canonical design age 41 (noting 46 as a source discrepancy if discussing fieldwork).
- [ ] Zubair Hassan is identified as a secondary beneficiary without separate account credentials.
- [ ] Primary users are clearly stated as homemakers, students, and salaried professionals.

### System Architecture
- [ ] User-facing categories (e.g. Ration) are distinguished from internal accounting accounts (e.g. Groceries Expense).
- [ ] Double-entry bookkeeping is described as balanced (total debits equal total credits).
- [ ] AI Financial Assistant is bounded by read-only access to user data with zero money-transfer powers.
- [ ] Raw receipt text is documented as being preserved separately from normalised product types.

### Traceability and Identifiers
- [ ] Scope IDs (`SC-01` to `SC-30`, `SS-03` to `SS-11`) match `PROJECT_SCOPE.md`.
- [ ] Legacy aliases (`SS-01`, `SS-02`, `SS-07`) are mapped to `SC-10`, `SC-29`, `SC-28` and do not duplicate scope.
- [ ] Formal requirement identifiers (`BR-###`, `FR-[SUBSYSTEM]-###`, `NFR-[QUALITY]-###`) are unique and persistent.

### Style and Integrity
- [ ] Zero em dashes (Unicode U+2014) present in the document.
- [ ] British English spelling used throughout.
- [ ] Fieldwork evidence is clearly distinguished from project-team analysis.
- [ ] No unsubstantiated market statistics or unverified competitor superiority claims.
