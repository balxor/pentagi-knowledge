---
cwe_id: CWE-303
name: Incorrect Implementation of Authentication Algorithm
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-90]
url: https://cwe.mitre.org/data/definitions/303.html
tags: [mitre-cwe, weakness, CWE-303]
---

# CWE-303 - Incorrect Implementation of Authentication Algorithm

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-303](https://cwe.mitre.org/data/definitions/303.html)

## Description
The requirements for the product dictate the use of an established authentication algorithm, but the implementation of the algorithm is incorrect.

## Extended description
This incorrect implementation may allow authentication to be bypassed.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Bypass Protection Mechanism

## Related attack patterns (CAPEC)
- [CAPEC-90](https://capec.mitre.org/data/definitions/90.html)

## Related weaknesses
- CWE-1390 (ChildOf)

## Observed examples (CVE)
- **CVE-2003-0750**: Conditional should have been an 'or' not an 'and'.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/303.html
