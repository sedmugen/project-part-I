# Contributing to DailyKhata

This repository supports a four-person university FYP team. Keep changes focused, reviewable and consistent with the [README](README.md), current governance and D3 requirements.

## Plan and coordinate

Create or use a GitHub issue for a substantive task. State the expected result, an owner, relevant requirement IDs and a short acceptance checklist. Agree ownership in the team before overlapping work. Small spelling or link fixes can be explained directly in a pull request.

Use the existing priorities to plan work. A Must Have capability must not depend on an optional feature. Discuss architecture or scope changes before implementation; follow the Decision Log process for changes to the baseline and involve the supervisor where academic review is required.

## Branches and commits

Start from an up-to-date `main` and use one short-lived branch per task. Use lowercase words separated by hyphens:

- `feat/<short-description>` for implementation, for example `feat/receipt-review`.
- `fix/<short-description>` for corrections.
- `docs/<short-description>` for documentation.
- `chore/<short-description>` for repository maintenance.

Include an issue number if useful, such as `docs/12-requirements-links`. Avoid personal information in branch names. Do not commit feature work directly to `main`, force push shared branches or rewrite another contributor's history. If a branch falls behind, merge the latest `main` into it and resolve conflicts with the affected author.

Make small, logically grouped commits. Use concise, imperative messages such as `docs: clarify receipt review scope` or `feat: add expense draft review`. Explain the reason and relevant IDs in the commit body when useful. Do not bundle formatting, generated artefacts and unrelated behaviour changes together.

Inspect `git status` and the diff before staging. Stage named files or selected changes, then review `git diff --cached` before committing. Never include another team member's unrelated local work, credentials or private data.

## Pull requests and review

1. Push your task branch and open a pull request targeting `main`. Use a draft pull request for early feedback.
2. Describe the problem, change, related issue and requirement IDs, validation performed, and known limitations. Use the repository's pull request template.
3. Request review from at least one other team member. Rotate reviewers so knowledge is shared across the four-person team; authors must not approve their own work.
4. Reviewers check scope, correctness, privacy, documentation consistency and testing evidence. For changes to account isolation, financial totals or assistant access, request a second teammate's review when available.
5. Resolve comments and conflicts, and pass all applicable checks. If no automated checks exist, record manual checks explicitly. Ask the reviewer to recheck substantive changes made after approval.
6. Merge only after another team member approves the final changes. Use a normal merge commit to preserve the reviewed history, then remove the completed task branch when it is no longer needed.

Treat `main` as protected by team agreement. This document does not configure or claim GitHub branch protection. Keep discussion constructive and follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## Requirements and documentation

Use the current documents linked from the README. D3 defines formal `BR-###`, `FR-GROUP-###` and `NFR-GROUP-###` IDs. For example, receipt correction work can reference `SC-07` and `FR-REVIEW-002`; account isolation work can reference `FR-AUTH-004` and `NFR-SEC-003`. Use only IDs that exist and apply to the change. Preserve D2 `EV` and `DR` source links where relevant. Mark a repository-only change as not applicable rather than inventing a requirement.

Never reuse retired IDs or silently change priorities. A baseline change must record the old and new decision, reason, authority and affected IDs in the Decision Log, then update affected documents and repeat consistency checks. Keep historical versions intact.

Write in British English, use canonical terms such as Chart of Accounts and AI Financial Assistant, and avoid em dash characters. Separate reported evidence, team analysis, proposed behaviour and validated results. Do not invent interview findings, performance results, submission dates or supervisor approval.

For Word deliverables, agree one editor per file at a time because binary changes cannot be merged reliably. Follow the existing Documentation Standard, maintain version and revision information, refresh document fields, and inspect rendered pages. Include a concise change summary and, when useful, a sanitised PDF preview in the pull request. Check links, tables, requirement references and cross-document consistency before requesting review.

## Validation and testing

At the current documentation stage, check spelling, links, scope, requirement IDs and the absence of em dash characters. Confirm that unrelated deliverables and historical sources remain unchanged. No application test suite exists yet.

Once implementation begins:

- Document repeatable build, lint and test commands in the README and run checks relevant to each change.
- Link behavioural tests to D3 requirements and acceptance scenarios. Add regression coverage for bug fixes and describe any checks that could not run.
- Verify receipt review and manual fallback, account isolation, consistent totals after edits or deletion, comparable product prices and assistant access boundaries as those workflows are implemented.
- Use synthetic or anonymised fixtures. Keep live credentials, real financial records and participant data out of fixtures, logs and screenshots.
- Report the device, data and conditions for performance or usability checks. Proposed D3 targets are not validated results until measured; disclose mocked services and other limits.

## Sensitive information and licensing

Report vulnerabilities through [SECURITY.md](SECURITY.md), not public issue details. Use local configuration for secrets and commit only sanitised examples. Ignore rules help prevent mistakes but do not replace a diff review.

Contribute only material you have permission to share. Original contributions are made under the repository's [MIT License](LICENSE). Preserve third-party notices, cite external sources and do not treat teaching materials as project-authored work. Disclose AI assistance where required by university policy and verify its output before submission.
