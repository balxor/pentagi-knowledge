---
cwe_id: CWE-796
name: Only Filtering Special Elements Relative to a Marker
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/796.html
tags: [mitre-cwe, weakness, CWE-796]
---

# CWE-796 - Only Filtering Special Elements Relative to a Marker

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-796](https://cwe.mitre.org/data/definitions/796.html)

## Description
The product receives data from an upstream component, but only accounts for special elements positioned relative to a marker (e.g. "at the beginning/end of a string; the second argument"), thereby missing remaining special elements that may exist before sending it to a downstream component.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity**: Unexpected State

## Related weaknesses
- CWE-795 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/796.html
