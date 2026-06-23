---
cwe_id: CWE-573
name: Improper Following of Specification by Caller
type: weakness
abstraction: Class
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/573.html
tags: [mitre-cwe, weakness, CWE-573]
---

# CWE-573 - Improper Following of Specification by Caller

**Abstraction:** Class  -  **Status:** Draft  -  **CWE:** [CWE-573](https://cwe.mitre.org/data/definitions/573.html)

## Description
The product does not follow or incorrectly follows the specifications as required by the implementation language, environment, framework, protocol, or platform.

## Extended description
When leveraging external functionality, such as an API, it is important that the caller does so in accordance with the requirements of the external functionality or else unintended behaviors may result, possibly leaving the system vulnerable to any number of exploits.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Quality Degradation, Varies by Context

## Related weaknesses
- CWE-710 (ChildOf)

## Observed examples (CVE)
- **CVE-2006-7140**: Crypto implementation removes padding when it shouldn't, allowing forged signatures
- **CVE-2006-4339**: Crypto implementation removes padding when it shouldn't, allowing forged signatures

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/573.html
