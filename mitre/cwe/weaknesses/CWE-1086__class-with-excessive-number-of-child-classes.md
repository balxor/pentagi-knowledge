---
cwe_id: CWE-1086
name: Class with Excessive Number of Child Classes
type: weakness
abstraction: Base
status: Incomplete
languages: [Object-Oriented]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1086.html
tags: [mitre-cwe, weakness, CWE-1086]
---

# CWE-1086 - Class with Excessive Number of Child Classes

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1086](https://cwe.mitre.org/data/definitions/1086.html)

## Description
A class contains an unnecessarily large number of children.

## Extended description
While the interpretation of "large number of children" may vary for each product or developer, CISQ recommends a default maximum of 10 child classes.

## Applicable platforms / languages
Object-Oriented

## Common consequences
- **Other**: Reduce Maintainability, Increase Analytical Complexity

## Related weaknesses
- CWE-1093 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1086.html
