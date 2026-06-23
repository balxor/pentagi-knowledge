---
cwe_id: CWE-1126
name: Declaration of Variable with Unnecessarily Wide Scope
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1126.html
tags: [mitre-cwe, weakness, CWE-1126]
---

# CWE-1126 - Declaration of Variable with Unnecessarily Wide Scope

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1126](https://cwe.mitre.org/data/definitions/1126.html)

## Description
The source code declares a variable in one scope, but the variable is only used within a narrower scope.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Reduce Maintainability, Increase Analytical Complexity

## Related weaknesses
- CWE-710 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1126.html
