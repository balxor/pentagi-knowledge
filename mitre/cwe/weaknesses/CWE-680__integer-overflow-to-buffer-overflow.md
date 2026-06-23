---
cwe_id: CWE-680
name: Integer Overflow to Buffer Overflow
type: weakness
abstraction: Compound
status: Draft
languages: [Memory-Unsafe, C, C++]
related_capec: [CAPEC-10, CAPEC-100, CAPEC-14, CAPEC-24, CAPEC-45, CAPEC-46, CAPEC-47, CAPEC-67, CAPEC-8, CAPEC-9, CAPEC-92]
url: https://cwe.mitre.org/data/definitions/680.html
tags: [mitre-cwe, weakness, CWE-680]
---

# CWE-680 - Integer Overflow to Buffer Overflow

**Abstraction:** Compound  -  **Status:** Draft  -  **CWE:** [CWE-680](https://cwe.mitre.org/data/definitions/680.html)

## Description
The product performs a calculation to determine how much memory to allocate, but an integer overflow can occur that causes less memory to be allocated than expected, leading to a buffer overflow.

## Applicable platforms / languages
Memory-Unsafe, C, C++

## Common consequences
- **Integrity, Availability, Confidentiality**: Modify Memory, DoS: Crash, Exit, or Restart, Execute Unauthorized Code or Commands

## Related attack patterns (CAPEC)
- [CAPEC-10](https://capec.mitre.org/data/definitions/10.html)
- [CAPEC-100](https://capec.mitre.org/data/definitions/100.html)
- [CAPEC-14](https://capec.mitre.org/data/definitions/14.html)
- [CAPEC-24](https://capec.mitre.org/data/definitions/24.html)
- [CAPEC-45](https://capec.mitre.org/data/definitions/45.html)
- [CAPEC-46](https://capec.mitre.org/data/definitions/46.html)
- [CAPEC-47](https://capec.mitre.org/data/definitions/47.html)
- [CAPEC-67](https://capec.mitre.org/data/definitions/67.html)
- [CAPEC-8](https://capec.mitre.org/data/definitions/8.html)
- [CAPEC-9](https://capec.mitre.org/data/definitions/9.html)
- [CAPEC-92](https://capec.mitre.org/data/definitions/92.html)

## Related weaknesses
- CWE-190 (StartsWith)
- CWE-190 (ChildOf)

## Observed examples (CVE)
- **CVE-2021-43537**: Chain: in a web browser, an unsigned 64-bit integer is forcibly cast to a 32-bit integer (CWE-681) and potentially leading to an integer overflow (CWE-190). If an integer overflow occurs, this can cause heap memory corruption (CWE-122)
- **CVE-2017-1000121**: chain: unchecked message size metadata allows integer overflow (CWE-190) leading to buffer overflow (CWE-119).

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/680.html
