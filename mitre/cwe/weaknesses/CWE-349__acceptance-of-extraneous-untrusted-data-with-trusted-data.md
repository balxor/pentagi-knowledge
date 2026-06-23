---
cwe_id: CWE-349
name: Acceptance of Extraneous Untrusted Data With Trusted Data
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-141, CAPEC-142, CAPEC-75]
url: https://cwe.mitre.org/data/definitions/349.html
tags: [mitre-cwe, weakness, CWE-349]
---

# CWE-349 - Acceptance of Extraneous Untrusted Data With Trusted Data

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-349](https://cwe.mitre.org/data/definitions/349.html)

## Description
The product, when processing trusted data, accepts any untrusted data that is also included with the trusted data, treating the untrusted data as if it were trusted.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control, Integrity**: Bypass Protection Mechanism, Modify Application Data

## Related attack patterns (CAPEC)
- [CAPEC-141](https://capec.mitre.org/data/definitions/141.html)
- [CAPEC-142](https://capec.mitre.org/data/definitions/142.html)
- [CAPEC-75](https://capec.mitre.org/data/definitions/75.html)

## Related weaknesses
- CWE-345 (ChildOf)

## Observed examples (CVE)
- **CVE-2002-0018**: Does not verify that trusted entity is authoritative for all entities in its response.
- **CVE-2006-5462**: use of extra data in a signature allows certificate signature forging

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/349.html
