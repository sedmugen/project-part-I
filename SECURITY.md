# Security policy

DailyKhata is a student FYP at the requirements stage. There is no released application or supported release series yet. Security and privacy controls in the requirements are planned obligations, not claims of implemented protection. The student maintainers handle reports as availability permits; there is no dedicated security team, guaranteed response time or bug bounty programme.

## Reporting a concern privately

Do not post vulnerability details, credentials, receipt images or personal financial information in public issues or pull requests.

1. If GitHub shows **Report a vulnerability** in this repository's Security tab, use that private reporting route. Its availability is not assumed by this policy.
2. Team members can otherwise contact a maintainer privately through an existing university or team channel. External reporters can use a private contact route voluntarily published on a maintainer's GitHub profile.
3. If no private route is available, open an issue containing only a request for a private security contact. Wait for a private channel before sharing details.

Include the affected file, branch or commit, expected and observed behaviour, potential impact and minimal reproduction steps using synthetic data. Share sanitised logs only when necessary. Report suspected exposure without copying the exposed secret or downloading other people's records. Test only with accounts and data you are authorised to use.

## Handling reports

A maintainer should acknowledge the report when available, assess its impact and coordinate a fix with another team member. The team should validate the correction, agree disclosure with the reporter and document the resolution without exposing private information. Reporters may follow up through the same private channel if they have not heard back.

For exposed credentials, revoke or rotate them promptly with the service owner. Removing a file in a later commit does not invalidate a secret or remove it from history. Coordinate any necessary history remediation separately; do not rewrite shared history without agreement.

## Development expectations

Keep secrets in local configuration or an appropriate secret store, never in source, documents, examples or logs. Use synthetic or anonymised test data and minimise receipt or expense data shared with external services. Review account isolation, safe uploads, data retention and the AI Financial Assistant's read-only access against the existing D3 security and privacy requirements as implementation proceeds.

When software releases begin, update this policy with actual supported versions and a confirmed private reporting route.
