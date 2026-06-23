---
cwe_id: CWE-1084
name: Invokable Control Element with Excessive File or Data Access Operations
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1084.html
tags: [mitre-cwe, weakness, CWE-1084]
---

# CWE-1084 - Invokable Control Element with Excessive File or Data Access Operations

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1084](https://cwe.mitre.org/data/definitions/1084.html)

## Description
A function or method contains too many operations that utilize a data manager or file resource.

## Extended description
While the interpretation of "too many operations" may vary for each product or developer, CISQ recommends a default maximum of 7 operations for the same data manager or file.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Reduce Maintainability

## Related weaknesses
- CWE-405 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1084.html
