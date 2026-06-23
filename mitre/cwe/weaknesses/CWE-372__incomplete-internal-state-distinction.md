---
cwe_id: CWE-372
name: Incomplete Internal State Distinction
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-140, CAPEC-74]
url: https://cwe.mitre.org/data/definitions/372.html
tags: [mitre-cwe, weakness, CWE-372]
---

# CWE-372 - Incomplete Internal State Distinction

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-372](https://cwe.mitre.org/data/definitions/372.html)

## Description
The product does not properly determine which state it is in, causing it to assume it is in state X when in fact it is in state Y, causing it to perform incorrect operations in a security-relevant manner.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity, Other**: Varies by Context, Unexpected State

## Related attack patterns (CAPEC)
- [CAPEC-140](https://capec.mitre.org/data/definitions/140.html)
- [CAPEC-74](https://capec.mitre.org/data/definitions/74.html)

## Related weaknesses
- CWE-664 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/372.html
