# DailyKhata Canonical Terminology

## Purpose and Use

This register establishes the official vocabulary, persona identities, and identifier rules for the DailyKhata project. All project team members, deliverables, requirements specifications, and codebase artefacts must adhere to these definitions.

Synonyms or informal terms appearing in attributed stakeholder quotes may be retained as historical quotation, but they must not replace or alter canonical system concepts.

---

## 1. Master Glossary

| Preferred Term | Meaning | Avoid / Notes |
| :--- | :--- | :--- |
| **DailyKhata** | Personal expense management application designed for the Pakistani personal and household context. | Avoid "Daily Khata", "Daily-Khata", or referring to it as an enterprise ERP / POS platform. |
| **Receipt digitisation** | Conversion of receipt information into reviewable structured digital records. | Avoid implying a promise of 100% perfect or unreviewed optical character recognition. |
| **OCR** | Optical character recognition; extracting raw textual characters from printed receipt images. | Distinct from structured data extraction, which interprets the recognised characters into semantic fields. |
| **Expense transaction** | A saved digital expense record owned by a single user account. | Avoid confusing with bank transaction imports, payment gateway executions, or credit card sync. |
| **Line item** | An individual entry on a receipt containing raw item text, category, and available quantity and price data. | A single expense transaction may aggregate multiple line items. |
| **Automatic categorisation** | System proposal of expense categories for transactions and line items based on receipt data or entry text. | Suggestions are always subject to mandatory user confirmation or manual correction before saving. |
| **Expense category** | A user-visible classification representing everyday spending buckets (e.g. Ration, Transport, Utilities). | Keep separate from internal accounting accounts. Ordinary users see only category labels. |
| **Chart of Accounts** | Internal structured register of accounting accounts, codes, and classifications operating behind the UI. | Distinct from user-visible categories. Users do not see or configure Chart of Accounts codes. |
| **Accounting mapping** | Predefined link connecting a user-facing expense category to an underlying internal accounting account. | Avoid changing category mappings without recording changes. Renaming a label must not alter the mapping silently. |
| **Item-level price history** | Historical record of prices paid over time for identifiable products, including unit volume and dates. | Requires comparable units and quantities; do not infer equivalent price if pack size is unknown. |
| **Semantic product classification** | Mapping individual commercial products to shared canonical product types (e.g. assigning Laundry Detergent). | Must preserve original receipt text and brand identity; canonical grouping does not merge distinct items. |
| **Original receipt text** | Unmodified text captured from a receipt image, retained separately from normalised fields. | Never overwrite original receipt text during OCR cleanup or user editing. |
| **Individual product** | A distinct commercial product, including its specific brand, variant, and pack size (e.g. Surf Excel 1kg). | Distinct from generic product types. Do not conflate different pack sizes or formulas. |
| **Brand** | Commercial brand identity of a product (e.g. Surf Excel, Ariel, Bonus) where identifiable. | Not interchangeable with product type or expense category. |
| **Canonical product type** | Generic product classification grouping equivalent items across multiple brands (e.g. Laundry Detergent). | Enables cross-brand price trend analysis without discarding brand-level distinction. |
| **AI Financial Assistant** | Core conversational capability grounded strictly in the authenticated user's stored DailyKhata records. | Has no bank execution or payment transfer capability. Grounded strictly in stored ledger facts. |
| **Localisation** | Adaptation of the interface and interaction for English and Urdu, including right-to-left layout and Urdu script. | Classified as Should Have. Do not document Urdu support as fully delivered until verified. |
| **Custom category label** | User renaming of a predefined category label (e.g. renaming Ration to Groceries). | Classified as Should Have. Does not create a new accounting account. |
| **User-created category** | Defining an entirely new category identity and establishing its accounting mapping. | Classified as Could Have. Introduces accounting mapping complexity. |
| **Household expense management** | A single account holder recording and managing household expenses for family review. | Single-user architecture. Avoid describing as multi-user collaborative household accounts. |
| **Recurring-spending analysis** | Conversational assistant discussion and explanation of past repeated expenditures. | Core Must Have capability. Distinct from automated recurring transaction creation (future scope). |
| **Unusually high spending** | Data-grounded identification and conversational explanation of unusually large past spending entries. | Core Must Have capability. Distinct from predictive machine-learning anomaly detection (future scope). |
| **Month-to-month comparison views** | Dedicated graphical screens comparing expenditures between calendar months. | Classified as Should Have. Conversational comparisons via the AI assistant are Must Have. |
| **Receipt image archive** | Long-term storage and retrieval of raw receipt image files after extraction has completed. | Classified as Should Have. Structured transaction storage is permanent; image retention is optional. |
| **Design persona** | A representative user profile synthesised to guide user experience and requirements design. | Avoid presenting persona profiles as independently verified empirical participant data. |
| **Source-reported evidence** | Qualitative observations, statements, and testing narratives preserved from early project fieldwork. | Must be reported with acknowledged limitations; distinct from statistically representative surveys. |
| **Project-team analysis** | Logical synthesis, architectural deductions, and design rationales formulated by the development team. | Clearly label as team reasoning; do not present as external stakeholder statements. |
| **Must Have** | Essential capability required for the minimum successful FYP delivery. | Cannot be dropped or deferred without formal scope renegotiation. |
| **Should Have** | Important capability intended for implementation, deferrable if technical or schedule limits require. | Highly desirable; implemented after core Must Have features are stable. |
| **Could Have** | Useful optional enhancement that may be attempted if time permits. | Lower delivery priority; evaluated during late-stage development. |
| **Future Scope** | Planned or plausible long-term enhancement outside the current FYP implementation commitment. | Excluded from the current project evaluation boundary; documented for future direction. |
| **Out of Scope** | Explicitly excluded functionality that DailyKhata will not deliver. | Strictly forbidden from implementation or requirement commitments. |

---

## 2. Canonical Identities and Stakeholders

### 2.1 Canonical Personas

| ID | Name | Age | Role | Classification | Core Focus |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **P-01** | Ayesha Tariq | 34 | Homemaker and household budget manager | Primary User | Weekly household and grocery tracking; handles cash and receipts; needs familiar categories and price trends. |
| **P-02** | Bilal Ahmed | 27 | Salaried professional | Primary User | Monthly personal expense reconciliation; requires minimal manual upkeep and natural-language query answers. |
| **P-03** | Hamza Sheikh | 21 | University student | Primary User | Personal allowance and frequent small cash expenditures; needs rapid no-receipt entry and clear category totals. |
| **P-04** | Zubair Hassan | Not recorded | Family member and spouse of account holder | Secondary Beneficiary | Reviews household spending summaries shared or exported by the primary user. No separate login required. |
| **P-05** | Usman Raza | 41 (canonical design age) | Small shopkeeper | Secondary Direct User | Tracks personal shop petty cash and supplier receipts. Point-of-sale, sales records, and inventory are excluded. |

*Note on P-05 Age:* The canonical design persona age is established as 41 (from D1 baseline). A historical interview note in D2 mentions age 46, which is recorded as an uncorroborated source discrepancy under DEC-01.

### 2.2 Stakeholder Classification
- **Primary Stakeholders:** Primary users (P-01, P-02, P-03) who interact directly with the personal ledger.
- **Secondary Stakeholders:** Secondary direct users (P-05 shopkeeper for expense tracking), secondary beneficiaries (P-04 family reviewers), and external report recipients (financial advisers).
- **Internal Stakeholders:** Four-student development team (implementation, testing, documentation) and project supervisor Nouman Ali (supervision and academic evaluation).
- **External Technical Providers (Conditional):** Managed third-party OCR, language-model, or cloud-hosting providers (if selected during architectural implementation).
- **Excluded / Future Stakeholders:** Commercial banking partners, payment gateway providers, and tax authorities (strictly future or out of scope).
- **Regulatory Domain:** Privacy, consumer protection, and security context represent system constraint domains, not named human stakeholders.

---

## 3. Priority and Identifier Conventions

### 3.1 Capability Identifier Rules
- `SC-01` through `SC-30`: In-scope system capabilities. Identifiers and baseline descriptions remain stable.
- `SS-03` through `SS-06`, and `SS-08` through `SS-11`: Secondary system capabilities (Should Have and Could Have).
- **Legacy Aliases:**
  - `SS-01` is an alias for `SC-10` (Voice-based cash expense entry, Should Have).
  - `SS-02` is an alias for `SC-29` (CSV and/or PDF export, Should Have).
  - `SS-07` is an alias for `SC-28` (English and Urdu localisation, Should Have).
  Aliases do not create duplicate features and must never alter capability priorities.

### 3.2 Formal Requirement Identifiers (for D3 and Implementation)
- `BR-###`: Business Requirements (e.g. `BR-001`)
- `FR-[SUBSYSTEM]-###`: Functional Requirements (e.g. `FR-OCR-001`, `FR-LEDGER-002`)
- `NFR-[QUALITY]-###`: Non-Functional Requirements (e.g. `NFR-SEC-001`, `NFR-PERF-001`)

Identifiers must never be renumbered, reassigned, or reused once established in an approved baseline.
