---
cwe_id: CWE-794
name: Incomplete Filtering of Multiple Instances of Special Elements
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/794.html
tags: [mitre-cwe, weakness, CWE-794]
---

# CWE-794 - Incomplete Filtering of Multiple Instances of Special Elements

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-794](https://cwe.mitre.org/data/definitions/794.html)

## Description
The product receives data from an upstream component, but does not filter all instances of a special element before sending it to a downstream component.

## Extended description
Incomplete filtering of this nature may be applied to: sequential elements (special elements that appear next to each other) or non-sequential elements (special elements that appear multiple times in different locations).

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity**: Unexpected State

## Related weaknesses
- CWE-792 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/794.html
