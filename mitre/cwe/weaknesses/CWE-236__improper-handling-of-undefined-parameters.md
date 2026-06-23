---
cwe_id: CWE-236
name: Improper Handling of Undefined Parameters
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/236.html
tags: [mitre-cwe, weakness, CWE-236]
---

# CWE-236 - Improper Handling of Undefined Parameters

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-236](https://cwe.mitre.org/data/definitions/236.html)

## Description
The product does not handle or incorrectly handles when a particular parameter, field, or argument name is not defined or supported by the product.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity**: Unexpected State

## Related weaknesses
- CWE-233 (ChildOf)

## Observed examples (CVE)
- **CVE-2002-1488**: Crash in IRC client via PART message from a channel the user is not in.
- **CVE-2001-0650**: Router crash or bad route modification using BGP updates with invalid transitive attribute.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/236.html
