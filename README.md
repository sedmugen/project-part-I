# DailyKhata

DailyKhata is a planned personal expense management application for Pakistani users, combining receipt digitisation, quick cash expense capture and understandable spending insights.

## Project status

DailyKhata is at the requirements and planning stage. Project Part I includes governance documents and Deliverables 1 to 3. Application implementation has not started in this repository; there is no runnable application, selected technology stack or software release here yet. Existing scripts support document preparation and quality checks.

The capabilities below describe intended scope, not completed features. D3 records proposed acceptance targets; implementation testing and supervisor endorsement remain pending.

## Source of Truth

Markdown is the authoritative source format for all DailyKhata project assets. DOCX and PDF files are exports or historical reference only.

- **Governance source of truth:** `00_Project_Governance/*.md`
- **Deliverable 1 source of truth:** [`01_Deliverable_1/D1.md`](01_Deliverable_1/D1.md)
- **Deliverable 2 source of truth:** [`02_Deliverable_2/D2.md`](02_Deliverable_2/D2.md)
- **Deliverable 3 source of truth:** [`03_Deliverable_3/D3.md`](03_Deliverable_3/D3.md)

Precedence and export rules:
- **Precedence:** Current Markdown takes precedence unless a later Decision Log entry explicitly changes it.
- **Archive Isolation:** Archived files in `archive/` must not override current Markdown.
- **Export Policy:** DOCX and PDF files are exports or historical reference only. Future DOCX files are generated from the authoritative Markdown only when needed for formal submission.

## FYP context and team

This is a BS Computer Science Final Year Project at **Beaconhouse National University**, academic year **2026-2027**.

**Team:** Saad Mughal, Khadijah Zahoor, Zainab Ali Baig and Aleeza Qaiser.

**Supervisor:** Nouman Ali.

## Problem and intended users

Paper receipts, cash purchases without receipts and informal notes make personal and household expense histories difficult to maintain. Manual entry and inconsistent categorisation make it harder to reconstruct totals or compare recorded prices.

DailyKhata aims to reduce this effort through a capture, review, save and query workflow. Primary users are homemakers and household budget managers, university students and salaried professionals. Small shopkeepers are secondary users for petty cash and supplier expenses only.

## Scope and planned capabilities

The baseline is mobile-first, targets ordinary Android-class devices and uses PKR. One account holder manages their own personal or household expense records.

Core **Must Have** capabilities include:

- Registration, authentication, basic profile and settings, and secure user-data storage.
- Receipt photographs or uploads, OCR and structured extraction, with review and correction before saving.
- Manual quick expense entry and text-based cash expense entry.
- Automatic transaction and line-item categorisation, user confirmation or correction, and locally understandable category labels.
- A full internal **Chart of Accounts**, category-to-account mappings and accounting-compatible expense records.
- Transaction history, search, filtering, editing and deletion, category totals, monthly summaries and a dashboard.
- Item-level price history and **semantic product classification**, preserving original receipt text and distinct product, brand and pack-size identities.
- A read-only **AI Financial Assistant** grounded in the current user's authorised records, supporting spending questions, period comparisons, recurring-spending analysis, product-price comparisons and general saving suggestions.

**Should Have** capabilities include voice-based cash entry, English and Urdu localisation, CSV and/or PDF export, custom category labels, simple spending visualisations, month-to-month comparison views and a receipt image archive. **Could Have** capabilities include user-created categories, offline draft entry, expense reminders and exportable household summaries. Optional scope is subject to time and validation.

Current scope excludes bank and wallet integration, payment processing, money transfers, shared household accounts, collaborative budgeting, inventory, point-of-sale functionality and complete business accounting. Automatic recurring expense creation and predictive analytics are future scope. An internal Chart of Accounts does not imply a full accounting suite, and the assistant cannot execute payments or change records.

The [Project Scope](00_Project_Governance/PROJECT_SCOPE.md) and [D3 requirements](03_Deliverable_3/D3.md) contain the full boundaries and priorities.

## Repository structure

The current Git root is the `project-part-I` directory itself. Paths below are relative to that root.

```text
project-part-I/
|-- 00_Project_Governance/       Authoritative project governance Markdown files
|   |-- README.md                Governance directory overview and authority guide
|   |-- PROJECT_SCOPE.md         Canonical scope baseline and boundaries
|   |-- DOCUMENTATION_STANDARD.md Writing, formatting and requirement rules
|   |-- CANONICAL_TERMINOLOGY.md Approved vocabulary and persona identities
|   |-- DECISION_LOG.md          Chronological project decisions and confirmation items
|   |-- CONSISTENCY_RULES.md     Cross-document consistency and precedence rules
|   `-- reconstruction_work/     Supporting authoring and audit scripts
|-- 01_Deliverable_1/            Deliverable 1 authoritative Markdown (D1.md) and task brief
|-- 02_Deliverable_2/            Deliverable 2 authoritative Markdown (D2.md) and task brief
|-- 03_Deliverable_3/            Deliverable 3 authoritative Markdown (D3.md), task brief and working artefacts
|-- archive/                     Archived exports and historical records
|   |-- historical-submissions/  Original submitted DOCX/PDF files
|   |-- old-docx/                Earlier reconstructed and submission-edition DOCX files
|   `-- superseded-governance/   Superseded governance DOCX files
|-- References/                  Local reference directory
|-- .github/                     Pull request template
|-- README.md
|-- CONTRIBUTING.md
|-- CODE_OF_CONDUCT.md
|-- SECURITY.md
|-- LICENSE
|-- .gitignore
`-- .gitattributes
```

Git does not retain empty directories, so `References/` will appear in clones only when it contains tracked material. Existing `reconstruction_work/` and `requirements_work/` directories contain authoring scripts, audits and rendered review artefacts. They are supporting material, not application source or submission deliverables.

## Project Part I documentation

Start with current governance, then read D1, D2 and D3 in order.

| Document | Purpose |
| --- | --- |
| [Project Scope](00_Project_Governance/PROJECT_SCOPE.md) | Current scope authority and capability priorities |
| [Canonical Terminology](00_Project_Governance/CANONICAL_TERMINOLOGY.md) | Shared concepts and identities |
| [Decision Log](00_Project_Governance/DECISION_LOG.md) | Scope decisions and unresolved confirmations |
| [Documentation Standard](00_Project_Governance/DOCUMENTATION_STANDARD.md) | Language, document control, formatting and review rules |
| [Consistency Rules](00_Project_Governance/CONSISTENCY_RULES.md) | Cross-document consistency and precedence rules |
| [D1: Target Market & Audience Analysis](01_Deliverable_1/D1.md) | Intended users, problems and project foundation |
| [D2: Problem Identification, Stakeholder Identification & Requirement Elicitation](02_Deliverable_2/D2.md) | Evidence, stakeholders and derived requirement candidates |
| [D3: Requirements Specification](03_Deliverable_3/D3.md) | Business, functional and non-functional requirements, traceability and proposed acceptance criteria |

Historical v1.0 governance and original submission files are preserved in `archive/` for provenance. Use the authoritative Markdown documents linked above when interpreting reconciled scope. Archived files must not override current Markdown. A document version or baseline label does not establish supervisor approval.

## Setup and development

For now, clone the repository and read the authoritative Markdown documents. There are no application installation, build or test commands yet.

Before implementation begins, record the selected delivery approach, language, framework, database, OCR and model services, and hosting decisions through the existing decision process. Then add reproducible setup instructions, runtime versions, a sanitised configuration example and build/test commands here. Do not infer application dependencies from the document-production scripts.

## Contribution workflow

Use a short-lived branch for each issue or focused task, then open a pull request to `main`. Obtain approval from at least one other team member before merging, resolve review comments and run applicable checks. Treat `main` as the shared stable baseline: no direct feature commits or force pushes. These are team workflow rules; they do not imply that GitHub branch protection has been configured.

See [CONTRIBUTING.md](CONTRIBUTING.md) for branch names, commits, reviews and testing, [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for team conduct, and [SECURITY.md](SECURITY.md) for sensitive reports.

## Documentation conventions

- Use British English and the canonical DailyKhata terminology. Do not use em dash characters.
- Preserve requirement identifiers and priorities. Reference existing `SC`, `SS`, `BR`, `FR` and `NFR` IDs where relevant; retain D2 `EV` and `DR` provenance links.
- Distinguish planned, implemented and validated behaviour. Proposed targets and source-reported research are not measured results.
- Authoritative documentation is maintained in Markdown. Generate Word exports only when formal submission editions are required.
- Record scope changes in the Decision Log before propagating them to affected documents; do not silently alter the baseline.
- Use synthetic or properly anonymised examples. Keep credentials, private receipts, participant records and personal contact details out of commits and reviews.

## Licence

Original DailyKhata software and project-authored documentation are licensed under the [MIT License](LICENSE). Third-party teaching material, quoted sources and other externally authored content retain their respective rights and notices; their presence here does not relicense them under MIT. Academic attribution and evidence provenance remain part of the contribution process.
