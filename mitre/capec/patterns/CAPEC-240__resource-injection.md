---
capec_id: CAPEC-240
name: Resource Injection
type: attack-pattern
abstraction: Meta
likelihood: High
severity: High
related_cwe: [CWE-99]
related_attack: []
url: https://capec.mitre.org/data/definitions/240.html
tags: [mitre-capec, attack-pattern, CAPEC-240]
---

# CAPEC-240 - Resource Injection

**Abstraction:** Meta  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-240](https://capec.mitre.org/data/definitions/240.html)

## Description
An adversary exploits weaknesses in input validation by manipulating resource identifiers enabling the unintended modification or specification of a resource.

## Prerequisites
- The target application allows the user to both specify the identifier used to access a system resource. Through this permission, the user gains the capability to perform actions on that resource (e.g., overwrite the file)

## Consequences
- **Confidentiality**: Read Data
- **Integrity**: Modify Data

## Mitigations
- Ensure all input content that is delivered to client is sanitized against an acceptable content specification.
- Perform input validation for all content.
- Enforce regular patching of software.

## Related weaknesses (CWE)
- [CWE-99](https://cwe.mitre.org/data/definitions/99.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/240.html
