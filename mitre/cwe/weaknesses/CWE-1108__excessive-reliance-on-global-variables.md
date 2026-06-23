---
cwe_id: CWE-1108
name: Excessive Reliance on Global Variables
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1108.html
tags: [mitre-cwe, weakness, CWE-1108]
---

# CWE-1108 - Excessive Reliance on Global Variables

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1108](https://cwe.mitre.org/data/definitions/1108.html)

## Description
The code is structured in a way that relies too much on using or setting global variables throughout various points in the code, instead of preserving the associated information in a narrower, more local context.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Reduce Maintainability, Increase Analytical Complexity

## Related weaknesses
- CWE-1076 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1108.html
