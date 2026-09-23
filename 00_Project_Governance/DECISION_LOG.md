# DailyKhata Decision Log

## Purpose and Status

This log records all authoritative scope, architecture, terminology, and baseline reconciliation decisions for the DailyKhata project.

Decisions DEC-01 through DEC-20 were established on 23 September 2026 as part of the project baseline reconstruction under project owner instructions. They reconcile inconsistencies between earlier draft deliverables (D1 and D2) and the initial governance documents, establishing a unified foundation for Deliverables 1, 2, and 3.

---

## Historical Decision Records

### DEC-01: Canonical Persona Age for Small Shopkeeper

- **Date:** 2026-09-23
- **Status:** Active
- **Previous State:** Deliverable 1 persona table listed Usman Raza at age 41. Deliverable 2 narrative (pp. 3, 7, 8, 10) reported an interview age of 46.
- **Decision:** Retain age 41 as the canonical design persona age across all project documents. Retain the age 46 mention in Deliverable 2 explicitly as an uncorroborated source-reported discrepancy.
- **Reason:** Deliverable 1 established the baseline design persona first. In the absence of original participant recordings or consent forms, the canonical persona model must remain unified rather than maintaining conflicting persona profiles.
- **Impact:** Aligns D1, D2, `CANONICAL_TERMINOLOGY.md`, and consistency audit records.

---

### DEC-02: Primary User Target Group Coverage

- **Date:** 2026-09-23
- **Status:** Active
- **Previous State:** Deliverable 1 summary text narrowed primary users to two groups (homemakers and students), but its body text discussed salaried professionals. Hamza Sheikh (student persona) appeared only in D2.
- **Decision:** Explicitly confirm three primary target groups: (1) Homemakers and household budget managers, (2) University students, and (3) Salaried professionals. Formally carry Hamza Sheikh (age 21) into Deliverable 1.
- **Reason:** Approved project scope and core user problem analysis require all three demographics. Students represent frequent no-receipt cash transactions; salaried professionals represent monthly expense reconciliation; homemakers represent grocery receipts and price tracking.
- **Impact:** Reflected across D1, D2, `PROJECT_SCOPE.md`, and persona registers.

---

### DEC-03: Household Persona Role and Operating Boundary

- **Date:** 2026-09-23
- **Status:** Active
- **Previous State:** Deliverable 1 described Zubair Hassan with inconsistent gendered terms ("wife and family") while calling him a spouse. Both D1 and D2 implied shared budget management.
- **Decision:** Designate Zubair Hassan (P-04) as a secondary beneficiary and family member. He reviews expense summaries shared or exported by the primary account holder. Age remains officially unrecorded.
- **Reason:** DailyKhata is architected as a single-user personal expense application. No multi-user permissions, invitations, or shared-account infrastructure exist in the current scope.
- **Impact:** Governs household feature boundaries in D1, D2, and `PROJECT_SCOPE.md`.

---

### DEC-04: Small Shopkeeper Operating Boundary

- **Date:** 2026-09-23
- **Status:** Active
- **Previous State:** D1 and D2 referred broadly to SMEs, micro-enterprises, daily business transactions, and commercial operations.
- **Decision:** Classify small shopkeepers (Usman Raza, P-05) strictly as secondary direct users who utilise DailyKhata solely for personal shop petty cash, supplier expense receipts, and expense tracking.
- **Reason:** Full commercial accounting, point-of-sale (POS), retail sales management, customer credit ledgers (udhaar khata), and inventory tracking are strictly out of scope.
- **Impact:** Prevents scope creep in D1, D2, and functional requirements.

---

### DEC-05: Boundary Between Expense Capture and Sales Income

- **Date:** 2026-09-23
- **Status:** Active
- **Previous State:** D2 (page 3) quoted Usman stating: "Even if I could just say the amount out loud when a customer pays, that alone would stop me from losing track."
- **Decision:** Preserve the quotation verbatim as historical source-reported evidence, but do not derive sales recording, income ledgers, or customer payment requirements from it.
- **Reason:** The user quote illustrates friction in capturing cash transactions at the moment they occur; however, customer sales fall outside the expense-tracking scope of DailyKhata.
- **Impact:** Clear boundary in D2 requirement elicitation and traceability tables.

---

### DEC-06: Mandatory Confirmation Before Saving Automated Predictions

- **Date:** 2026-09-23
- **Status:** Active
- **Previous State:** Deliverable 1 implied that expense categorization would occur automatically without requiring user intervention. Deliverable 2 emphasised user distrust of automated classification and required user verification.
- **Decision:** The system shall automatically suggest categories, but mandatory user review, confirmation, and correction are required before any transaction or line item is committed to storage.
- **Reason:** Preserves data integrity and user trust. Local Pakistani receipts frequently contain ambiguous items or mixed-category purchases that require human oversight.
- **Impact:** `SC-07` and `SC-12` classified as Must Have in `PROJECT_SCOPE.md`, D1, and D2.

---

### DEC-07: Prioritisation of Expense Capture Modalities

- **Date:** 2026-09-23
- **Status:** Active
- **Previous State:** Early documents alternated between calling voice input "core", "voice-first", or optional, conflating manual cash entry with speech recognition.
- **Decision:** Manual quick expense entry (`SC-08`) and text-based cash entry (`SC-09`) are Must Have. Voice-based cash entry (`SC-10` / `SS-01`) is Should Have.
- **Reason:** Ensures reliable capture for unreceipted cash purchases without making speech-to-text integration or acoustic noise tolerance a baseline blocker for project completion.
- **Impact:** Capability register in `PROJECT_SCOPE.md`, D1, and D2.

---

### DEC-08: Removal of Unsupported Population and Market Claims

- **Date:** 2026-09-23
- **Status:** Active
- **Previous State:** Deliverable 1 contained unverified assertions claiming "several million target users in Pakistan", "typical monthly household spending of Rs. 40,000", and "universal abandonment of budgeting apps within 2 to 3 weeks".
- **Decision:** Remove all sweeping quantitative market claims and unverified population estimates. Present qualitative findings strictly as reported individual participant experiences with transparent attribution.
- **Reason:** No survey data, demographic sampling, or economic citations were present in the project records to support these numerical claims.
- **Impact:** Methodological integrity restored in D1, D2, and consistency audit.

---

### DEC-09: Framing of Competitor Analysis Evidence

- **Date:** 2026-09-23
- **Status:** Active
- **Previous State:** Deliverables asserted definitive product limitations regarding competing apps (Mint, Wallet, Cashew, and local bank apps), claiming universal absence of receipt scanning or price history.
- **Decision:** Frame competitor analysis strictly as historical, team-reported exploratory testing conducted on specific dates on Android devices. Do not assert broad or permanent commercial competitor inferiority.
- **Reason:** App versions, exact test dates, and screenshots were not catalogued. Honest academic reporting demands distinguishing exploratory test notes from comprehensive market audits.
- **Impact:** Competitor review sections in D1 and D2.

---

### DEC-10: System Latency and Performance Expectations

- **Date:** 2026-09-23
- **Status:** Active
- **Previous State:** Deliverable 1 promised "almost instant answers", while Deliverable 2 promised "all capture in under 10 seconds" and "OCR in a few seconds".
- **Decision:** Treat speed as a general usability expectation during early design. Formal performance benchmarks (timing simple cash entry, OCR processing, and network roundtrips separately) must be measured during later empirical validation.
- **Reason:** Network conditions, image resolution, receipt length, and third-party model latencies vary substantially; a universal 10-second commitment is technically unrealistic prior to prototyping.
- **Impact:** Performance requirements framing in D1, D2, and D3.

---

### DEC-11: Offline Connectivity and Device Boundary

- **Date:** 2026-09-23
- **Status:** Active
- **Previous State:** Deliverable 2 mentioned operation under intermittent Pakistani connectivity without specifying whether OCR and AI services would operate offline.
- **Decision:** Core Must Have workflows require transparent loading states, error handling, and retry mechanisms when connectivity fails. Local offline draft entry (`SS-09`) is classified as Could Have. Full offline OCR and offline LLM execution are not required.
- **Reason:** Mobile-class devices cannot reliably execute large vision-language models or OCR pipelines on-device without severe hardware constraints.
- **Impact:** Defined in `PROJECT_SCOPE.md` and NFR candidates.

---

### DEC-12: Incorporation of Authoritative Baseline Capabilities

- **Date:** 2026-09-23
- **Status:** Active
- **Previous State:** Original student draft deliverables omitted or under-specified user authentication, ledger data maintenance, the internal Chart of Accounts, semantic product models, and conversational assistant capabilities.
- **Decision:** Formally incorporate all 38 baseline capabilities from the user-authorised scope into D1, D2, and the governance repository. Explain these additions as project architecture requirements rather than retroactively attributing them to interview quotes.
- **Reason:** Essential system structures (such as user isolation, data security, and structured double-entry accounts) are foundational engineering requirements.
- **Impact:** Authoritative scope alignment across all deliverables.

---

### DEC-13: AI Assistant Scope vs Dedicated Views and Predictive Systems

- **Date:** 2026-09-23
- **Status:** Active
- **Previous State:** Overlap between conversational assistant queries, dedicated comparison screens, and automated anomaly-detection alerts.
- **Decision:** Conversational queries regarding past spending, periodic comparisons, recurring spending patterns, and unusually high recorded expenses are core Must Have capabilities of the AI Financial Assistant (`SC-23`, `SC-24`). Dedicated graphical comparison screens (`SS-05`) are Should Have. Predictive machine-learning anomaly detection is strictly Future Scope.
- **Reason:** Cleanly separates data-grounded conversational analytics from complex standalone visualization screens and predictive machine-learning pipelines.
- **Impact:** `PROJECT_SCOPE.md`, `CANONICAL_TERMINOLOGY.md`, and feature register.

---

### DEC-14: Category Nomenclature, Hierarchy, and Aliases

- **Date:** 2026-09-23
- **Status:** Active
- **Previous State:** Predefined categories, custom category labels, and user-created categories were conflated. Secondary scope entries duplicate primary entries under different IDs.
- **Decision:** (1) Culturally familiar local category labels (e.g. Ration) are Must Have (`SC-13`). (2) User renaming of existing labels is Should Have (`SS-03`). (3) Defining brand new categories is Could Have (`SS-08`). (4) Reconcile legacy aliases: `SS-01` -> `SC-10`, `SS-02` -> `SC-29`, `SS-07` -> `SC-28`.
- **Reason:** Preserves traceability while preventing duplicate counting or priority drift.
- **Impact:** Scope register and terminology mapping.

---

### DEC-15: Standardised Document Hierarchy and Official Titles

- **Date:** 2026-09-23
- **Status:** Active
- **Previous State:** Deliverable 2 cover repeated the Deliverable 1 title. Heading formats and page styles varied widely across drafts. The D3 university brief contained conflicting rubric markings (10 marks heading vs 20 marks breakdown).
- **Decision:** Standardise on one unified documentation layout. Use official assignment titles: D1 is "Target Market & Audience Analysis"; D2 is "Problem Identification, Stakeholder Identification & Requirement Elicitation". For D3, adopt its requirements engineering workflow while leaving grading rubric reconciliation to the supervisor.
- **Reason:** Ensures academic professionalism and cross-deliverable consistency.
- **Impact:** Document formatting rules and assignment title baselines.

---

### DEC-16: Authority, Baseline Dating, and Supervisor Endorsement

- **Date:** 2026-09-23
- **Status:** Active
- **Previous State:** Governance documents were marked "Approved Baseline" without recorded dates or supervisor sign-off records.
- **Decision:** Preserve v1.0 governance files as historical records. Set the authoritative reconstruction baseline date to 23 September 2026 under user authorization. Explicitly state that supervisor endorsement is to be recorded after formal academic review.
- **Reason:** Academic honesty; an assignment submission deadline or internal revision does not constitute verified faculty endorsement.
- **Impact:** Document Control blocks and audit records.

---

### DEC-17: Internal Accounting Structure and Double-Entry Invariance

- **Date:** 2026-09-23
- **Status:** Active
- **Previous State:** Earlier texts mentioned "standards-aligned accounting", which could be misinterpreted as statutory IFRS corporate compliance or audited business accounting.
- **Decision:** Maintain a structured internal Chart of Accounts (COA) with stable accounts, account types, and category mappings. Where double-entry bookkeeping is used, every journal entry must balance (debits equal credits). Users never input raw accounting codes.
- **Reason:** Provides clean, structured data for financial queries without claiming statutory tax or accounting certification.
- **Impact:** `PROJECT_SCOPE.md` and accounting data model.

---

### DEC-18: Evidence Provenance and Interview Schedule Framing

- **Date:** 2026-09-23
- **Status:** Active
- **Previous State:** Elicitation interviews were ambiguously described both as an immediate sequence and as a later revisit.
- **Decision:** Present the question sequence logically without asserting an unverified multi-day visit schedule. Label all qualitative interview and observation data as source-reported evidence; label personas as design profiles.
- **Reason:** Accurately reflects available project documentation without asserting unsupported fieldwork logistics.
- **Impact:** D2 research methods and evidence register.

---

### DEC-19: Pagination and Numbering Convention

- **Date:** 2026-09-23
- **Status:** Active
- **Previous State:** Documentation standard v1.0 permitted either Roman numerals for front matter or continuous Arabic numerals, causing formatting variance.
- **Decision:** Adopt continuous Arabic page numbering (`Page X of Y`) across all submission documents, counting the cover page in the total page count but hiding the number on the cover itself.
- **Reason:** Minimises Word field errors and ensures clean, uniform cross-document pagination.
- **Impact:** `DOCUMENTATION_STANDARD.md` and submission document templates.

---

### DEC-20: Separation of Receipt Text, Products, and Image Storage

- **Date:** 2026-09-23
- **Status:** Active
- **Previous State:** Early drafts described receipt retention as permanent and implied normalising product names would replace raw receipt text.
- **Decision:** (1) Core structured transaction storage is permanent; raw receipt image archiving is Should Have (`SS-06`). (2) Raw extracted receipt text must be stored separately and never overwritten by normalised product names, brands, or canonical types.
- **Reason:** Protects against data loss, avoids inflating cloud storage costs for receipt images, and ensures semantic classification does not discard original evidence.
- **Impact:** Data model and semantic product architecture in `PROJECT_SCOPE.md`.

---

## 3. Human Confirmation Register

The following items represent historical fieldwork and project records that require ongoing verification by the student team and supervisor:

| Item | Action Required | Baseline Treatment Pending Verification |
| :--- | :--- | :--- |
| **Usman participant age** | Project team to inspect raw interview notes for participant age. | Canonical persona age remains 41; D2 source discrepancy (46) is preserved as reported evidence. |
| **Fieldwork provenance** | Project team to compile available interview dates, audio, notes, or consent forms. | Original D2 narrative is treated as qualitative source-reported evidence only; no empirical claims. |
| **Competitor comparison details** | Team to record tested app versions, test dates, and the identity of the tested bank app. | Preserved as a historical team exploratory test narrative; no verified permanent claims. |
| **Supervisor review and sign-off** | Present reconstructed baseline to supervisor Nouman Ali for formal endorsement. | Replacement documents dated 23 September 2026; supervisor endorsement marked pending review. |
| **Measurable performance targets** | Conduct pilot tests on Android devices to measure cash entry, OCR, and query latencies. | Performance treated as usability expectations; quantitative targets deferred to validation phase. |

---

## 4. Future Change Procedure

When proposing a new project decision or altering an established baseline:

1. **Assign Sequential ID:** Use the next unused decision identifier (e.g. `DEC-21`).
2. **Document Required Fields:**
   - **Date:** Date of decision adoption (YYYY-MM-DD).
   - **Status:** `Active`, `Superseded`, or `Replaced`.
   - **Previous State:** Concrete description of the earlier assumption or text.
   - **Decision:** Clear, definitive statement of the new agreement.
   - **Reason:** Engineering, academic, or logistical rationale.
   - **Impact:** List of all affected deliverables, scope identifiers, and codebase components.
3. **Update Governance:** Propagate changes to `PROJECT_SCOPE.md`, `CANONICAL_TERMINOLOGY.md`, or `DOCUMENTATION_STANDARD.md`.
4. **Propagate to Deliverables:** Update draft submission files and verify consistency using `CONSISTENCY_RULES.md`.
