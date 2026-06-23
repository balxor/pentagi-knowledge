---
cwe_id: CWE-183
name: Permissive List of Allowed Inputs
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not Technology-Specific]
related_capec: [CAPEC-120, CAPEC-3, CAPEC-43, CAPEC-71]
url: https://cwe.mitre.org/data/definitions/183.html
tags: [mitre-cwe, weakness, CWE-183]
---

# CWE-183 - Permissive List of Allowed Inputs

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-183](https://cwe.mitre.org/data/definitions/183.html)

## Description
The product implements a protection mechanism that relies on a list of inputs (or properties of inputs) that are explicitly allowed by policy because the inputs are assumed to be safe, but the list is too permissive - that is, it allows an input that is unsafe, leading to resultant weaknesses.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific

## Common consequences
- **Access Control**: Bypass Protection Mechanism

## Related attack patterns (CAPEC)
- [CAPEC-120](https://capec.mitre.org/data/definitions/120.html)
- [CAPEC-3](https://capec.mitre.org/data/definitions/3.html)
- [CAPEC-43](https://capec.mitre.org/data/definitions/43.html)
- [CAPEC-71](https://capec.mitre.org/data/definitions/71.html)

## Related weaknesses
- CWE-697 (ChildOf)
- CWE-434 (CanPrecede)

## Observed examples (CVE)
- **CVE-2019-12799**: chain: bypass of untrusted deserialization issue (CWE-502) by using an assumed-trusted class (CWE-183)
- **CVE-2019-10458**: sandbox bypass using a method that is on an allowlist
- **CVE-2017-1000095**: sandbox bypass using unsafe methods that are on an allowlist
- **CVE-2019-10458**: CI/CD pipeline feature has unsafe elements in allowlist, allowing bypass of script restrictions
- **CVE-2017-1000095**: Default allowlist includes unsafe methods, allowing bypass of sandbox

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/183.html
