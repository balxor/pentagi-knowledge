---
cwe_id: CWE-1074
name: Class with Excessively Deep Inheritance
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1074.html
tags: [mitre-cwe, weakness, CWE-1074]
---

# CWE-1074 - Class with Excessively Deep Inheritance

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1074](https://cwe.mitre.org/data/definitions/1074.html)

## Description
A class has an inheritance level that is too high, i.e., it has a large number of parent classes.

## Extended description
While the interpretation of "large number of parent classes" may vary for each product or developer, CISQ recommends a default maximum of 7 parent classes.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Reduce Maintainability, Increase Analytical Complexity

## Related weaknesses
- CWE-1093 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1074.html
