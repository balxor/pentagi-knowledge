---
cwe_id: CWE-181
name: Incorrect Behavior Order: Validate Before Filter
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-120, CAPEC-267, CAPEC-3, CAPEC-43, CAPEC-78, CAPEC-79, CAPEC-80]
url: https://cwe.mitre.org/data/definitions/181.html
tags: [mitre-cwe, weakness, CWE-181]
---

# CWE-181 - Incorrect Behavior Order: Validate Before Filter

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-181](https://cwe.mitre.org/data/definitions/181.html)

## Description
The product validates data before it has been filtered, which prevents the product from detecting data that becomes invalid after the filtering step.

## Extended description
This can be used by an attacker to bypass the validation and launch attacks that expose weaknesses that would otherwise be prevented, such as injection.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Bypass Protection Mechanism

## Potential mitigations
- **Implementation, Architecture and Design**: Inputs should be decoded and canonicalized to the application's current internal representation before being filtered.

## Related attack patterns (CAPEC)
- [CAPEC-120](https://capec.mitre.org/data/definitions/120.html)
- [CAPEC-267](https://capec.mitre.org/data/definitions/267.html)
- [CAPEC-3](https://capec.mitre.org/data/definitions/3.html)
- [CAPEC-43](https://capec.mitre.org/data/definitions/43.html)
- [CAPEC-78](https://capec.mitre.org/data/definitions/78.html)
- [CAPEC-79](https://capec.mitre.org/data/definitions/79.html)
- [CAPEC-80](https://capec.mitre.org/data/definitions/80.html)

## Related weaknesses
- CWE-179 (ChildOf)

## Observed examples (CVE)
- **CVE-2002-0934**: Directory traversal vulnerability allows remote attackers to read or modify arbitrary files via invalid characters between two . (dot) characters, which are filtered and result in a ".." sequence.
- **CVE-2003-0282**: Directory traversal vulnerability allows attackers to overwrite arbitrary files via invalid characters between two . (dot) characters, which are filtered and result in a ".." sequence.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/181.html
