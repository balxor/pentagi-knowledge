---
cwe_id: CWE-793
name: Only Filtering One Instance of a Special Element
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/793.html
tags: [mitre-cwe, weakness, CWE-793]
---

# CWE-793 - Only Filtering One Instance of a Special Element

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-793](https://cwe.mitre.org/data/definitions/793.html)

## Description
The product receives data from an upstream component, but only filters a single instance of a special element before sending it to a downstream component.

## Extended description
Incomplete filtering of this nature may be location-dependent, as in only the first or last element is filtered.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity**: Unexpected State

## Related weaknesses
- CWE-792 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/793.html
