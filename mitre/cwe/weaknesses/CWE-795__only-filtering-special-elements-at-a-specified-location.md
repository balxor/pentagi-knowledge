---
cwe_id: CWE-795
name: Only Filtering Special Elements at a Specified Location
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/795.html
tags: [mitre-cwe, weakness, CWE-795]
---

# CWE-795 - Only Filtering Special Elements at a Specified Location

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-795](https://cwe.mitre.org/data/definitions/795.html)

## Description
The product receives data from an upstream component, but only accounts for special elements at a specified location, thereby missing remaining special elements that may exist before sending it to a downstream component.

## Extended description
A filter might only account for instances of special elements when they occur: relative to a marker (e.g. "at the beginning/end of string; the second argument"), or at an absolute position (e.g. "byte number 10"). This may leave special elements in the data that did not match the filter position, but still may be dangerous.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity**: Unexpected State

## Related weaknesses
- CWE-791 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/795.html
