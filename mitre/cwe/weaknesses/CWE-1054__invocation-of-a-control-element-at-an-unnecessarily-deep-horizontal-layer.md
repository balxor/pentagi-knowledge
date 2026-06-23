---
cwe_id: CWE-1054
name: Invocation of a Control Element at an Unnecessarily Deep Horizontal Layer
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1054.html
tags: [mitre-cwe, weakness, CWE-1054]
---

# CWE-1054 - Invocation of a Control Element at an Unnecessarily Deep Horizontal Layer

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1054](https://cwe.mitre.org/data/definitions/1054.html)

## Description
The code at one architectural layer invokes code that resides at a deeper layer than the adjacent layer, i.e., the invocation skips at least one layer, and the invoked code is not part of a vertical utility layer that can be referenced from any horizontal layer.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Reduce Maintainability

## Related weaknesses
- CWE-1061 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1054.html
