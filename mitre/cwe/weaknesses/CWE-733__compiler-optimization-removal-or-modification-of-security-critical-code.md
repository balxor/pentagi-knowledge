---
cwe_id: CWE-733
name: Compiler Optimization Removal or Modification of Security-critical Code
type: weakness
abstraction: Base
status: Incomplete
languages: [C, C++, Compiled]
related_capec: [CAPEC-10, CAPEC-24, CAPEC-46, CAPEC-8, CAPEC-9]
url: https://cwe.mitre.org/data/definitions/733.html
tags: [mitre-cwe, weakness, CWE-733]
---

# CWE-733 - Compiler Optimization Removal or Modification of Security-critical Code

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-733](https://cwe.mitre.org/data/definitions/733.html)

## Description
The developer builds a security-critical protection mechanism into the software, but the compiler optimizes the program such that the mechanism is removed or modified.

## Applicable platforms / languages
C, C++, Compiled

## Common consequences
- **Access Control, Other**: Bypass Protection Mechanism, Alter Execution Logic

## Related attack patterns (CAPEC)
- [CAPEC-10](https://capec.mitre.org/data/definitions/10.html)
- [CAPEC-24](https://capec.mitre.org/data/definitions/24.html)
- [CAPEC-46](https://capec.mitre.org/data/definitions/46.html)
- [CAPEC-8](https://capec.mitre.org/data/definitions/8.html)
- [CAPEC-9](https://capec.mitre.org/data/definitions/9.html)

## Related weaknesses
- CWE-1038 (ChildOf)

## Observed examples (CVE)
- **CVE-2008-1685**: C compiler optimization, as allowed by specifications, removes code that is used to perform checks to detect integer overflows.
- **CVE-2019-1010006**: Chain: compiler optimization (CWE-733) removes or modifies code used to detect integer overflow (CWE-190), allowing out-of-bounds write (CWE-787).

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/733.html
