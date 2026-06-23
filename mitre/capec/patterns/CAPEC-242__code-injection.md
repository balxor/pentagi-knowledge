---
capec_id: CAPEC-242
name: Code Injection
type: attack-pattern
abstraction: Meta
likelihood: High
severity: High
related_cwe: [CWE-94]
related_attack: []
url: https://capec.mitre.org/data/definitions/242.html
tags: [mitre-capec, attack-pattern, CAPEC-242]
---

# CAPEC-242 - Code Injection

**Abstraction:** Meta  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-242](https://capec.mitre.org/data/definitions/242.html)

## Description
An adversary exploits a weakness in input validation on the target to inject new code into that which is currently executing. This differs from code inclusion in that code inclusion involves the addition or replacement of a reference to a code file, which is subsequently loaded by the target and used as part of the code of some application.

## Prerequisites
- The target software does not validate user-controlled input such that the execution of a process may be altered by sending code in through legitimate data channels, using no other mechanism.

## Consequences
- **Availability**: Other (Code Injection attack patterns can result in a wide variety of consequences and negatively affect all three elements of the security triad.)
- **Confidentiality**: Other (Code Injection attack patterns can result in a wide variety of consequences and negatively affect all three elements of the security triad.)
- **Integrity**: Other (Code Injection attack patterns can result in a wide variety of consequences and negatively affect all three elements of the security triad.)

## Mitigations
- Utilize strict type, character, and encoding enforcement
- Ensure all input content that is delivered to client is sanitized against an acceptable content specification.
- Perform input validation for all content.
- Enforce regular patching of software.

## Related weaknesses (CWE)
- [CWE-94](https://cwe.mitre.org/data/definitions/94.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/242.html
