# DailyKhata Project Governance

## Purpose and Overview

This folder contains the internal governance baseline and project-control rules for the DailyKhata Final Year Project (Beaconhouse National University, BS Computer Science, 2026-2027).

It exists to provide a single, version-controlled source of truth across all deliverables, preventing scope drift, terminology inconsistencies, and unrecorded architectural changes among team collaborators.

## Internal vs Submission Deliverables

- **Internal Governance Files (this folder):** Working standards, boundary definitions, decision registers, and consistency rules for internal team alignment. These documents contain internal IDs and operational guidelines.
- **External Submission Documents (`01_Deliverable_1`, `02_Deliverable_2`, etc.):** Academic deliverables prepared for university evaluation. Submission deliverables must be self-contained and fully understandable without requiring the reader or evaluator to consult this governance directory.

## File Authority Guide

Each file in this directory governs a specific domain of the project:

| Document | Primary Authority | Key Contents |
| :--- | :--- | :--- |
| [`PROJECT_SCOPE.md`](PROJECT_SCOPE.md) | Scope Baseline & Boundaries | In-scope capabilities (SC-01 to SC-30, SS-03 to SS-11), out-of-scope register (OS-01 to OS-20), user boundaries, and architectural constraints. |
| [`DOCUMENTATION_STANDARD.md`](DOCUMENTATION_STANDARD.md) | Style & Drafting Standards | Language rules (British English, strict no-em-dash rule), submission Word specifications, requirement syntax, and QA checklists. |
| [`CANONICAL_TERMINOLOGY.md`](CANONICAL_TERMINOLOGY.md) | Vocabulary & Identity Register | Approved concept definitions, canonical persona profiles (P-01 to P-05), stakeholder classifications, and identifier rules. |
| [`DECISION_LOG.md`](DECISION_LOG.md) | Historical & Active Decisions | Chronological record of architectural, scope, and editorial decisions (DEC-01 to DEC-20) and items pending field confirmation. |
| [`CONSISTENCY_RULES.md`](CONSISTENCY_RULES.md) | Alignment & Compatibility Rules | Backward-compatibility requirements, cross-document invariants, change protocols, and pre-submission audit checklists. |

## How Contributors Should Use This Folder

1. **Before Authoring or Editing Deliverables:** Consult `PROJECT_SCOPE.md` and `CANONICAL_TERMINOLOGY.md` to confirm feature priorities, allowed boundaries, and standard terminology.
2. **When Writing Content:** Follow `DOCUMENTATION_STANDARD.md` strictly (notably British English, requirement syntax, and the zero-em-dash rule).
3. **When Addressing Conflicts or Gaps:** Do not silently modify scope or definitions. Review `DECISION_LOG.md` to understand why a baseline was established.
4. **Before Submitting Deliverables:** Run through the verification checklist in `CONSISTENCY_RULES.md`.

## Managing Changes

To propose or record changes to project baseline facts:

1. Discuss the change within the four-student project team and align with supervisor advice.
2. Record the change as a new sequential entry in [`DECISION_LOG.md`](DECISION_LOG.md) (`DEC-21`, `DEC-22`, etc.), documenting previous state, new decision, rationale, and impacted documents.
3. Update `PROJECT_SCOPE.md` or `CANONICAL_TERMINOLOGY.md` if capabilities, terms, or boundaries were modified.
4. Propagate the change across all affected deliverable drafts consistently.
5. Verify backward compatibility using the checklist in [`CONSISTENCY_RULES.md`](CONSISTENCY_RULES.md).
