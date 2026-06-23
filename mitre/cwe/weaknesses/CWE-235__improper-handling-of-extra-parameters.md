---
cwe_id: CWE-235
name: Improper Handling of Extra Parameters
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-460]
url: https://cwe.mitre.org/data/definitions/235.html
tags: [mitre-cwe, weakness, CWE-235]
---

# CWE-235 - Improper Handling of Extra Parameters

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-235](https://cwe.mitre.org/data/definitions/235.html)

## Description
The product does not handle or incorrectly handles when the number of parameters, fields, or arguments with the same name exceeds the expected amount.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity**: Unexpected State

## Related attack patterns (CAPEC)
- [CAPEC-460](https://capec.mitre.org/data/definitions/460.html)

## Related weaknesses
- CWE-233 (ChildOf)

## Observed examples (CVE)
- **CVE-2003-1014**: MIE. multiple gateway/security products allow restriction bypass using multiple MIME fields with the same name, which are interpreted differently by clients.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/235.html
