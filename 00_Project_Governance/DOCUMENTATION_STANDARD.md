# DailyKhata Documentation Standard

## Purpose and Applicability

This standard establishes the mandatory writing, language, formatting, requirement-specification, and quality-assurance rules for all documentation within the DailyKhata Final Year Project.

It governs:
- Internal project governance and working specifications drafted in Markdown
- Official academic submission documents prepared for Beaconhouse National University (D1, D2, D3, and final thesis reports)

---

## Section A: Content Rules

### A.1 Single Source of Truth
Every project fact, scope boundary, capability priority, and user profile must align with the definitions in `PROJECT_SCOPE.md` and `CANONICAL_TERMINOLOGY.md`. No deliverable may silently redefine or alter an approved baseline.

### A.2 Evidence Provenance and Integrity
Documentation must strictly distinguish between different classes of statements:
- **Source-Reported Evidence:** Data, quotes, and observations documented in historical fieldwork records (e.g. initial interviews in D2). These must be reported with their acknowledged limitations and original context.
- **Attributed Stakeholder Statements:** Direct quotations from participants. These must not be altered, expanded, or invented.
- **Project-Team Analysis:** Interpretations, logical deductions, and architectural reasoning developed by the development team. These must be clearly presented as analysis, not as empirical survey findings.
- **Derived Requirements:** System requirements systematically derived from user problems or documentary mandates.
- **Proposed Design Decisions:** Technical implementation choices subject to ongoing development and evaluation.

### A.3 Prohibition of Fabricated Claims
- Never invent interviews, participant names, surveys, questionnaire metrics, or user quotes.
- Do not cite unsubstantiated market statistics (such as unverified claims of "millions of target users" or "average monthly expenditure of Rs. 40,000").
- Do not assert unverified competitor superiority or claim that all existing financial apps lack specific features unless accompanied by verifiable, dated test records.
- Clearly acknowledge when data or empirical validation has not yet been collected.

### A.4 Backward Compatibility and Traceability
- Later deliverables must build upon and remain compatible with earlier approved submissions.
- High-level problems identified in D1 and elicitation findings in D2 must trace cleanly into functional specifications in D3.
- If an earlier assumption must change, the change must be recorded in [`DECISION_LOG.md`](DECISION_LOG.md) before deliverable text is modified.

---

## Section B: Language Rules

### B.1 British English
All documentation must use British English spelling and grammar consistently (en-GB standard):
- Use `categorisation`, `digitisation`, `organisation`, `prioritise`, `optimisation`.
- Use `behaviour`, `colour`, `honour`.
- Use `programme` (except when referring to computer code `program`).
- Use `adviser` (preferred over advisor).
- Use `licence` for the noun, `license` for the verb.

### B.2 Strict Prohibition of Em Dashes
> [!IMPORTANT]
> The Unicode em dash character (Unicode U+2014) is strictly prohibited across all DailyKhata documentation, code comments, tables, diagrams, headers, footers, and commit messages.

- Use standard punctuation instead: commas, colons, semicolons, parentheses, or ordinary hyphens (`-`).
- Automated pre-release checks must search all files for the em dash character and confirm zero occurrences.

### B.3 Canonical Naming and Capitalisation
Use official names and casing consistently:
- `DailyKhata` (CamelCase, single word; never Daily Khata or Daily-Khata)
- `Chart of Accounts` (capitalised as an architectural entity)
- `AI Financial Assistant` (capitalised as a core system capability)
- `Must Have`, `Should Have`, `Could Have`, `Future Scope`, `Out of Scope` (standardised MoSCoW casing)

---

## Section C: Submission Formatting Rules (Word Submissions)

While working drafts are maintained in Markdown, official submissions to the university must be rendered to Microsoft Word (.docx) or PDF and conform to the following layout specifications:

### C.1 Page Configuration
- **Paper Size:** A4 portrait (210 mm x 297 mm).
- **Margins:** Top 1.0 inch (25.4 mm), Bottom 1.0 inch (25.4 mm), Left 1.25 inches (31.75 mm), Right 1.0 inch (25.4 mm).
- **Orientation:** Portrait throughout. Landscape is permitted only for wide architectural diagrams or wide tabular matrices.

### C.2 Typography and Hierarchy
- **Font Family:** Times New Roman throughout the document.
- **Body Text:** 12 pt, justified alignment, 1.15 line spacing, 0 pt before, 6 pt after.
- **Document Title:** 20 pt, bold, centred.
- **Deliverable Subtitle:** 16 pt, bold, centred.
- **Heading 1:** 16 pt, bold, left-aligned, 12 pt before, 6 pt after.
- **Heading 2:** 14 pt, bold, left-aligned, 12 pt before, 6 pt after.
- **Heading 3:** 12 pt, bold, left-aligned, 12 pt before, 6 pt after.
- **Heading 4:** 12 pt, bold italic, left-aligned, 12 pt before, 6 pt after.
- **Automatic Numbering:** Headings 1 through 4 must use Word multilevel list numbering linked to styles (e.g. 1., 1.1, 1.1.1). Never type heading numbers manually.

### C.3 Tables and Figures
- **Table Text:** 10 pt or 11 pt, single or 1.05 line spacing, 3 pt after.
- **Table Headers:** Bold, light grey fill (`#E7E7E7` or `#F0F0F0`), repeating header row enabled for page splits.
- **Table Borders:** Clean, light grey borders (`#D9D9D9`).
- **Table Captions:** Placed immediately above the table using Word SEQ fields (e.g. `Table 1: Description`).
- **Figure Captions:** Placed immediately below the figure using Word SEQ fields (e.g. `Figure 1: Description`).
- **In-Text Citations:** Every table and figure must be referenced in the body text prior to its appearance.

### C.4 Front Matter and Headers/Footers
- **Cover Page:** Clean, unnumbered cover displaying university name, department, project title (DAILYKHATA), deliverable number and title, all four team members with student IDs, supervisor name (Nouman Ali), and academic year (2026-2027).
- **Document Control & Revision History:** Compact tabular records on the page following the cover.
- **Table of Contents:** Generated automatically from Heading 1 to Heading 3 styles.
- **List of Tables / List of Figures:** Generated automatically when tables or figures are present.
- **Header:** `DailyKhata | Final Year Project` (9 pt, right-aligned, suppressed on cover).
- **Footer:** `Beaconhouse National University | BS Computer Science` (centred) with continuous Arabic page numbering `Page X of Y` (9 pt, suppressed on cover).

---

## Section D: Requirement-Writing Rules

### D.1 Requirement Syntax and Style
- Formal requirements must be clear, concise, singular, unambiguous, and verifiable.
- Avoid vague language such as "should ideally", "where practical", "user-friendly", or "system could maybe".
- Use the word **shall** strictly for mandatory system behaviour within the stated scope and deliverable phase:
  - Functional / Non-Functional: "The system shall [action/capability]..."
  - Business: "DailyKhata shall enable [stakeholder] to [objective]..."

### D.2 Identifier Conventions
Requirements must use structured, persistent identifiers that are never renumbered or reassigned:

| Level | Syntax | Description | Example |
| :--- | :--- | :--- | :--- |
| Business Requirement | `BR-###` | High-level commercial or operational objective | `BR-001`, `BR-002` |
| Functional Requirement | `FR-[SUBSYSTEM]-###` | Verifiable functional capability grouped by component | `FR-OCR-001`, `FR-LEDGER-002`, `FR-AI-001` |
| Non-Functional Requirement | `NFR-[QUALITY]-###` | System quality attribute, constraint, or performance bound | `NFR-SEC-001`, `NFR-PERF-002`, `NFR-USAB-001` |

Subsystem codes for Functional Requirements:
- `AUTH`: Authentication and user profile management
- `LEDGER`: Expense entry, transactions, and editing
- `OCR`: Receipt image upload, processing, and extraction
- `CAT`: Automatic categorisation, confirmation, and category mappings
- `COA`: Chart of Accounts and accounting storage
- `PRICE`: Item-level price tracking and semantic product grouping
- `AI`: AI Financial Assistant conversation and analysis
- `LOC`: Localisation and language switching
- `EXP`: Exporting and reporting

Quality codes for Non-Functional Requirements:
- `SEC`: Security, authentication, and data privacy
- `PERF`: Latency, processing time, and responsiveness
- `USAB`: Usability, workflow friction, and error recovery
- `COMP`: Compatibility with devices and operating environments
- `REL`: Data integrity, balanced journals, and system reliability

---

## Section E: Final QA Rules and Workflow

### E.1 Drafting Workflow
1. **Markdown First:** Author and review all requirement text, architectural notes, and narrative content in Git-tracked Markdown files first.
2. **Internal Peer Review:** Team members review changes via Git diff to verify alignment with governance rules.
3. **Word Document Compilation:** Only after Markdown content is approved is the content compiled or updated in Word format for formal university submission.
4. **Final Export:** Update all Word TOC fields, verify pagination, inspect table borders, and export to PDF.

### E.2 Pre-Submission Quality Assurance Checklist
Before any deliverable is submitted for academic grading:
- [ ] **Em Dash Check:** Automated text search confirms zero occurrences of the em dash character (Unicode U+2014).
- [ ] **Spelling & Grammar:** British English proofing applied; technical terminology verified.
- [ ] **Canonical Terminology:** All terms align with `CANONICAL_TERMINOLOGY.md`.
- [ ] **Persona Consistency:** Persona names, ages, and profiles match canonical definitions.
- [ ] **Scope Alignment:** Feature priorities strictly reflect `PROJECT_SCOPE.md`. No out-of-scope capabilities presented as in-scope.
- [ ] **Requirement IDs:** Identifiers follow standard syntax (`BR-###`, `FR-[SUBSYSTEM]-###`, `NFR-[QUALITY]-###`); no duplicate IDs.
- [ ] **Evidence Provenance:** Fieldwork evidence and team analysis are clearly distinguished.
- [ ] **Word Formatting (Submission Files):** Margins, fonts, headings, headers/footers, and `Page X of Y` numbering checked.
- [ ] **TOC & Captions:** Table of Contents refreshed; all tables and figures have captions and in-text references.
- [ ] **Visual Layout:** No clipped text, orphan headings, or broken table rows across page boundaries.
