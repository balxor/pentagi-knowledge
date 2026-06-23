---
cwe_id: CWE-1047
name: Modules with Circular Dependencies
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1047.html
tags: [mitre-cwe, weakness, CWE-1047]
---

# CWE-1047 - Modules with Circular Dependencies

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1047](https://cwe.mitre.org/data/definitions/1047.html)

## Description
The product contains modules in which one module has references that cycle back to itself, i.e., there are circular dependencies.

## Extended description
As an example, with Java, this weakness might indicate cycles between packages.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Reduce Maintainability

## Related weaknesses
- CWE-1120 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1047.html
