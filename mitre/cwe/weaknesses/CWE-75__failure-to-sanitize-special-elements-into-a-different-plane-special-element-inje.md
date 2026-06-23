---
cwe_id: CWE-75
name: Failure to Sanitize Special Elements into a Different Plane (Special Element Injection)
type: weakness
abstraction: Class
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-81, CAPEC-93]
url: https://cwe.mitre.org/data/definitions/75.html
tags: [mitre-cwe, weakness, CWE-75]
---

# CWE-75 - Failure to Sanitize Special Elements into a Different Plane (Special Element Injection)

**Abstraction:** Class  -  **Status:** Draft  -  **CWE:** [CWE-75](https://cwe.mitre.org/data/definitions/75.html)

## Description
The product does not adequately filter user-controlled input for special elements with control implications.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity, Confidentiality, Availability**: Modify Application Data, Execute Unauthorized Code or Commands

## Potential mitigations
- **Requirements**: Programming languages and supporting technologies might be chosen which are not subject to these issues.
- **Implementation**: Utilize an appropriate mix of allowlist and denylist parsing to filter special element syntax from all input.

## Related attack patterns (CAPEC)
- [CAPEC-81](https://capec.mitre.org/data/definitions/81.html)
- [CAPEC-93](https://capec.mitre.org/data/definitions/93.html)

## Related weaknesses
- CWE-74 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/75.html
