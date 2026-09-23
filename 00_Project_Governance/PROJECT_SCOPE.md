# DailyKhata Project Scope Baseline

## 1. Project Definition

DailyKhata is a personal expense management application primarily designed for Pakistani users who frequently deal with paper receipts, cash transactions, and informal expense tracking.

The system reduces the effort required to maintain personal or household expense records through:
- Receipt digitisation and optical character recognition (OCR)
- Quick cash expense capture and manual entry
- Automatic transaction and line-item categorisation with mandatory user confirmation and correction
- A structured internal Chart of Accounts operating behind an intuitive user interface
- Transaction history, search, filtering, and monthly spending summaries
- Item-level price history and semantic product classification
- An AI Financial Assistant grounded in authorised stored records

## 2. Primary Project Objective

The primary objective is to enable everyday users in Pakistan to record, organise, and understand personal and household expenditures with substantially less manual friction than paper notebooks, generic phone notes, spreadsheets, or complex budgeting software.

Core delivery priorities for the four-student FYP team:
- Prioritise a robust, end-to-end capture, review, save, and query workflow over optional extensions.
- Support both receipt-based and no-receipt cash expenditures.
- Keep users in control by requiring confirmation and permitting correction of all automated predictions.
- Maintain accurate accounting structures without burdening the end user with accounting complexity.
- Ground AI responses strictly in the user's authorised stored data.

## 3. Users and Operating Boundaries

### 3.1 Primary Users
The project focuses on three primary user groups:
1. **Homemakers and Household Budget Managers (P-01):** Manage weekly household and grocery spending; handle cash and paper receipts; need low-effort capture, familiar category labels, and grocery price history.
2. **Salaried Professionals (P-02):** Reconcile and track monthly personal spending; seek consolidated monthly summaries and natural-language querying with minimal ongoing maintenance.
3. **University Students (P-03):** Manage personal allowances and frequent small cash purchases; require rapid text entry without paper receipts and clear category totals.

### 3.2 Secondary Users and Beneficiaries
1. **Small Shopkeepers (P-05 - Secondary Direct User):** May use DailyKhata strictly for personal shop petty cash, supplier expense receipts, and expense tracking.
2. **Family Members and Spouses (P-04 - Secondary Beneficiary):** Review expense summaries shared or exported by the primary account holder. No separate multi-user login or permissions are implied.
3. **Accountants and Financial Advisers (Secondary External Stakeholders):** Optional recipients of exported reports or summaries.

### 3.3 Operating Boundaries
- **Household Boundary:** DailyKhata operates as a single-account system. An account holder records personal or household expenditures. Multi-user accounts, shared ledgers, role hierarchies, and collaborative budgeting are strictly future scope.
- **Shopkeeper Boundary:** Limited strictly to expense tracking (petty cash and supplier expenses). Point-of-sale (POS), sales recording, inventory tracking, customer khata (credit ledgers), and payroll are strictly excluded.

## 4. Feature Scope Register

The project classifies features using MoSCoW priorities:
- **Must Have:** Essential for the minimum successful FYP delivery.
- **Should Have:** Important capabilities intended for implementation, deferrable if technical or schedule constraints require.
- **Could Have:** Useful optional enhancements if time permits.
- **Future Scope:** Planned extensions outside the current FYP implementation commitment.
- **Out of Scope:** Explicitly excluded capabilities.

### 4.1 In-Scope Features (Must Have)

| ID | Capability | Description | Priority |
| :--- | :--- | :--- | :--- |
| SC-01 | User registration and authentication | Secure registration, credential management, and session control. | Must Have |
| SC-02 | Basic user profile and settings | User profile management, basic preferences, and configuration. | Must Have |
| SC-03 | Personal digital expense ledger | Core ledger storing individual expense transactions. | Must Have |
| SC-04 | Photograph or upload receipts | Image capture or upload of printed paper receipts. | Must Have |
| SC-05 | OCR receipt processing | Optical character recognition on clear printed receipts. | Must Have |
| SC-06 | Structured data extraction | Extraction of merchant, date, line items, quantities, prices, and total. | Must Have |
| SC-07 | Review and edit OCR results | Mandatory user review and manual correction screen before saving. | Must Have |
| SC-08 | Manual quick expense entry | Rapid form-based entry for expenditures without receipts. | Must Have |
| SC-09 | Text-based cash expense entry | Quick natural-language text entry for cash purchases. | Must Have |
| SC-11 | Automatic categorisation | Category suggestions for transactions and individual line items. | Must Have |
| SC-12 | User confirmation and correction | User approval or correction of predicted expense categories. | Must Have |
| SC-13 | Local expense category labels | Predefined, culturally familiar category labels (e.g. Ration, Utilities). | Must Have |
| SC-14 | Full internal Chart of Accounts | Structured internal chart of accounts behind the user interface. | Must Have |
| SC-15 | Category-to-account mapping | Fixed mapping linking user-facing categories to internal accounts. | Must Have |
| SC-16 | Accounting-compatible storage | Transaction storage compatible with balanced financial ledgers. | Must Have |
| SC-17 | Transaction history | Chronological log of recorded transactions with detailed breakdown. | Must Have |
| SC-18 | Search and filtering | Search by merchant, category, date range, or price. | Must Have |
| SC-19 | Category-level spending totals | Aggregated spending totals grouped by expense category. | Must Have |
| SC-20 | Basic monthly spending summaries | Monthly expenditure overviews and periodic totals. | Must Have |
| SC-21 | Item-level price history | Tracking price trends over time for identifiable products. | Must Have |
| SC-22 | Semantic product classification | Mapping items to canonical product types (e.g. Laundry Detergent). | Must Have |
| SC-23 | Natural-language financial querying | Answering questions about historical expenditures conversationally. | Must Have |
| SC-24 | AI Financial Assistant | Core conversational assistant grounded in authorised stored data. | Must Have |
| SC-25 | Dashboard | Visual summary of current spending, recent entries, and category totals. | Must Have |
| SC-26 | Editing and deleting saved expenses | Full maintenance of saved expenses with consistent dependent totals. | Must Have |
| SC-27 | Secure user-data storage | Authenticated storage, password hashing, and user-isolated data access. | Must Have |
| SC-30 | Ordinary Android-class device support | Usability and performance on standard low-to-mid-range Android devices. | Must Have |

### 4.2 Secondary Scope (Should Have and Could Have)

| ID | Legacy Alias | Capability | Description | Priority |
| :--- | :--- | :--- | :--- | :--- |
| SC-10 | SS-01 | Voice-based cash expense entry | Short spoken expense input (e.g. "Rickshaw 350 rupees"). | Should Have |
| SC-28 | SS-07 | English and Urdu localisation | Bilingual interface, Urdu RTL rendering, and Urdu text support. | Should Have |
| SC-29 | SS-02 | CSV and/or PDF export | Basic export of expense tables and transaction lists. | Should Have |
| SS-03 | - | Custom category labels | Renaming user-facing labels of existing categories. | Should Have |
| SS-04 | - | Simple spending visualisations | Charts and visual graphs of spending distributions. | Should Have |
| SS-05 | - | Month-to-month comparison views | Dedicated comparison screens across consecutive billing months. | Should Have |
| SS-06 | - | Receipt image archive | Retaining and viewing uploaded receipt images after processing. | Should Have |
| SS-08 | - | User-created categories | Defining entirely new categories and accounting account mappings. | Could Have |
| SS-09 | - | Offline draft expense entry | Local queuing of cash expense drafts when offline. | Could Have |
| SS-10 | - | Expense reminders | Local notifications prompting regular expense logging. | Could Have |
| SS-11 | - | Exportable household summaries | Dedicated pre-formatted summary for household review. | Could Have |

*Note on legacy aliases:* `SS-01`, `SS-02`, and `SS-07` are retained solely for backward compatibility with earlier project drafts. They map directly to `SC-10`, `SC-29`, and `SC-28` respectively, and do not introduce new requirements.

## 5. Architectural Boundaries

### 5.1 Accounting and Category Boundary
- DailyKhata maintains an internal Chart of Accounts (COA) with distinct account codes, account types, and parent-child relationships.
- Ordinary users interact only with familiar, user-facing category labels (such as Ration, Transport, Utilities, Healthcare). They do not see, select, or configure account codes or journal entries.
- Category mappings link each user-facing category to an underlying expense account (e.g., Ration maps to Groceries Expense).
- **Double-Entry Constraint:** Where double-entry ledger recording is implemented, all journal entries must balance (total debits equal total credits). For example, a cash grocery purchase of Rs. 2,500 debits Groceries Expense by Rs. 2,500 and credits Cash by Rs. 2,500.
- Regulatory certification, statutory tax reporting, IFRS compliance claims, and complete SME business accounting are outside scope.

### 5.2 Semantic Product Intelligence
DailyKhata maintains a clear separation between receipt text and semantic product models:
1. **Original Receipt Text:** Unmodified text extracted from the receipt (e.g. "Surf Excel 1kg").
2. **Individual Product:** Specific commercial item with brand, packaging, and unit volume.
3. **Brand:** Distinct brand identifier (e.g. "Surf Excel" vs "Bonus").
4. **Canonical Product Type:** Shared generic concept (e.g. "Laundry Detergent").
5. **Expense Category:** User-facing budget bucket (e.g. "Household Supplies").
6. **Accounting Account:** Internal ledger account (e.g. "Household Supplies Expense").

Illustrative mapping:
- Item A: Original text `Surf Excel 1kg` -> Brand `Surf Excel` -> Canonical Type `Laundry Detergent` -> Category `Household Supplies` -> Account `Household Supplies Expense`.
- Item B: Original text `Bonus 1kg` -> Brand `Bonus` -> Canonical Type `Laundry Detergent` -> Category `Household Supplies` -> Account `Household Supplies Expense`.

This distinction ensures that brand identities and exact pack sizes are never erased during normalisation, while enabling broad category analysis and item-level price comparisons over time.

### 5.3 AI Financial Assistant Boundary
- **Core Functionality:** The AI Financial Assistant is a conversational capability grounded strictly in the authenticated user's stored DailyKhata data.
- **Permitted Behaviors:** Answering queries regarding past expenses, calculating category totals, comparing spending between periods, discussing recurring past spending patterns, explaining changes in spending, highlighting unusually high spending, and providing general data-grounded budgeting suggestions.
- **Strict Limits:** The assistant has read-only access to the user's financial records. It cannot initiate money transfers, execute payments, modify bank accounts, or connect directly to payment gateways.
- **Distinction from Future Scope:** Conversational review of past spending is core (Must Have); automated creation of recurring transaction schedules and predictive machine-learning anomaly detection are future scope.

### 5.4 Localisation Boundary
- English and Urdu localisation is classified as **Should Have**.
- Localisation includes Urdu translations of UI labels, right-to-left (RTL) layout adjustments, and potential Urdu-language querying with the assistant.
- Predefined local category labels in English (e.g. Ration) are **Must Have** independently of full bilingual Urdu translation.
- Urdu support must not be documented as guaranteed until fully implemented and validated.

### 5.5 Platform and Implementation Constraints
- Target platform: Mobile-first application supporting standard Android-class devices.
- Technical implementation decisions (frontend framework, backend language, database, cloud hosting, and specific OCR or LLM service providers) are implementation choices, subject to privacy, cost, and test feasibility.
- The project team is not required to train custom foundation models or OCR engines from scratch; existing pre-trained models and managed APIs may be integrated.
- Offline support is restricted to Could Have draft entry (`SS-09`). Full offline OCR and offline LLM execution are not required.

### 5.6 Security and Privacy Boundary
The security baseline covers realistic student prototype protections:
- User authentication and session management
- Secure password hashing using industry-standard algorithms
- Protected client-server communication
- Strict user data isolation (preventing cross-user record exposure)
- Input validation and sanitisation
- Safe receipt image upload handling and storage

The project explicitly excludes commercial certifications such as PCI DSS, SOC 2, ISO 27001, dedicated 24/7 SIEM monitoring, or external regulatory audits.

## 6. Explicitly Out of Scope

The following capabilities are excluded from the DailyKhata FYP scope:

| ID | Excluded Capability | Rationale |
| :--- | :--- | :--- |
| OS-01 | Direct bank account integration | Requires commercial open-banking APIs and banking agreements outside FYP scope. |
| OS-02 | Automatic card transaction synchronisation | High security overhead, regulatory barriers, and partner dependencies. |
| OS-03 | Easypaisa or JazzCash auto-synchronisation | Proprietary closed APIs and financial regulatory constraints in Pakistan. |
| OS-04 | Open banking API integration | Pakistan open-banking framework is not universally accessible for student projects. |
| OS-05 | Payment processing | DailyKhata is an expense-tracking ledger, not a payment gateway. |
| OS-06 | Sending or receiving money | Money transfer introduces remittance licensing and compliance mandates. |
| OS-07 | Enterprise ERP functionality | Incompatible with personal and household expense focus. |
| OS-08 | Inventory management | Retail stock tracking falls outside personal expense management. |
| OS-09 | Point-of-sale (POS) systems | Retail cash register operations are outside personal ledger boundaries. |
| OS-10 | Payroll systems | Employee wage tracking is a business enterprise capability. |
| OS-11 | Tax preparation and statutory filing | Complex legal liability and changing national tax regulations. |
| OS-12 | Investment portfolio management | Stock, mutual fund, and asset tracking outside expense focus. |
| OS-13 | Credit scoring and credit risk evaluation | Credit agency data and lending risk models are excluded. |
| OS-14 | Fraud-detection infrastructure | Banking-grade fraud infrastructure is unnecessary for a personal ledger. |
| OS-15 | Commercial banking functionality | Cheque clearing, deposit holding, and merchant acquiring are excluded. |
| OS-16 | Enterprise multi-tenant organisation management | DailyKhata is designed for individual users, not corporate hierarchies. |
| OS-17 | Production infrastructure for millions of concurrent users | Academic prototype scope; evaluated on realistic student test cohorts. |
| OS-18 | Banking-grade regulatory certification | No formal compliance audits or certifications are sought. |
| OS-19 | Full multi-country financial infrastructure | Strictly tailored to the Pakistani expense and currency context. |
| OS-20 | Arbitrary third-party financial integrations | Third-party fintech integrations outside core defined scope. |

## 7. Future Scope

The following features represent plausible long-term product enhancements that are not committed for the current FYP:
- Automatic bank and mobile wallet transaction ingestion
- Shared household accounts with multi-user permissions and collaborative budgeting
- Expanded business accounting, inventory, and POS functionality
- Automated recurring expense creation and scheduled transaction posting
- Budgeting goals and predictive overspending alerts
- Machine-learning anomaly detection for unusual spending patterns
- Advanced financial advisory engines and investment planning
- Deeper Urdu natural-language interaction and additional regional languages
- Multi-currency transaction support
- Direct retailer integrations and automatic digital e-receipt ingestion

## 8. Scope Governance and Change Control

1. **Baseline Invariance:** This scope baseline governs all DailyKhata deliverables, requirements specifications, and implementation decisions. Capabilities may not silently move across priority categories.
2. **Controlled Change Rule:** Any proposed modification to scope, priorities, or operating boundaries must be formally evaluated and recorded in [`DECISION_LOG.md`](DECISION_LOG.md) before altering code or deliverable text.
3. **Traceability:** Requirements developed in later deliverables (such as D3) must trace back to the capability identifiers (`SC-01` to `SC-30`, `SS-03` to `SS-11`) defined in this register.
