---
cwe_id: CWE-797
name: Only Filtering Special Elements at an Absolute Position
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/797.html
tags: [mitre-cwe, weakness, CWE-797]
---

# CWE-797 - Only Filtering Special Elements at an Absolute Position

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-797](https://cwe.mitre.org/data/definitions/797.html)

## Description
The product receives data from an upstream component, but only accounts for special elements at an absolute position (e.g. "byte number 10"), thereby missing remaining special elements that may exist before sending it to a downstream component.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity**: Unexpected State

## Related weaknesses
- CWE-795 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/797.html
