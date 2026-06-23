---
cwe_id: CWE-1082
name: Class Instance Self Destruction Control Element
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1082.html
tags: [mitre-cwe, weakness, CWE-1082]
---

# CWE-1082 - Class Instance Self Destruction Control Element

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1082](https://cwe.mitre.org/data/definitions/1082.html)

## Description
The code contains a class instance that calls the method or function to delete or destroy itself.

## Extended description
For example, in C++, "delete this" will cause the object to delete itself.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Reduce Reliability

## Related weaknesses
- CWE-1076 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1082.html
