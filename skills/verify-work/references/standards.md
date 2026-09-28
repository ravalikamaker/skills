# Standards for a relevant verification concern

Use only the standard and sections that change the acceptance decision. Start
with the project's agreed version and requirements; a newer publication does
not silently change that contract.

| Concern | Official reference | Apply narrowly |
| --- | --- | --- |
| HTTP API contracts | [OpenAPI Specification](https://spec.openapis.org/oas/latest.html) | Compare the agreed request, response, and error contract with implementation and consumer behavior. Schema validity alone does not establish correct business behavior. |
| Application security | [OWASP ASVS](https://owasp.org/projects/asvs) | Select requirements relevant to the application's risks and agreed verification scope; connect findings to evidence rather than reciting the whole standard. |
| Accessibility | [WCAG](https://www.w3.org/TR/WCAG22/) | Check applicable criteria for the affected user journey and required conformance target, with direct interaction evidence where needed. Automated checks cover only part of accessibility. |
| Broader secure-development process | [NIST SSDF](https://csrc.nist.gov/projects/ssdf) | Use when assessing secure-development practices or process evidence, not as a substitute for application behavior or security checks. |

Report the standard/version, selected scope, and observed gaps when used. A
bounded check does not establish full conformance, certification, or compliance.
Do not invent a legal obligation, expand into a full audit, or require every
standard for ordinary work.
