---
cwe_id: CWE-198
name: Use of Incorrect Byte Ordering
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/198.html
tags: [mitre-cwe, weakness, CWE-198]
---

# CWE-198 - Use of Incorrect Byte Ordering

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-198](https://cwe.mitre.org/data/definitions/198.html)

## Description
The product receives input from an upstream component, but it does not account for byte ordering (e.g. big-endian and little-endian) when processing the input, causing an incorrect number or value to be used.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity**: Unexpected State

## Related weaknesses
- CWE-188 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/198.html
