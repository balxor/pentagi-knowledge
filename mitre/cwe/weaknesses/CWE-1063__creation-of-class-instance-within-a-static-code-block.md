---
cwe_id: CWE-1063
name: Creation of Class Instance within a Static Code Block
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1063.html
tags: [mitre-cwe, weakness, CWE-1063]
---

# CWE-1063 - Creation of Class Instance within a Static Code Block

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1063](https://cwe.mitre.org/data/definitions/1063.html)

## Description
A static code block creates an instance of a class.

## Extended description
This pattern identifies situations where a storable data element or member data element is initialized with a value in a block of code which is declared as static.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Reduce Performance

## Related weaknesses
- CWE-1176 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1063.html
