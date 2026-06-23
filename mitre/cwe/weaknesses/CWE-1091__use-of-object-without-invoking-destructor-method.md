---
cwe_id: CWE-1091
name: Use of Object without Invoking Destructor Method
type: weakness
abstraction: Base
status: Incomplete
languages: [Object-Oriented]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1091.html
tags: [mitre-cwe, weakness, CWE-1091]
---

# CWE-1091 - Use of Object without Invoking Destructor Method

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1091](https://cwe.mitre.org/data/definitions/1091.html)

## Description
The product contains a method that accesses an object but does not later invoke the element's associated finalize/destructor method.

## Applicable platforms / languages
Object-Oriented

## Common consequences
- **Other**: Reduce Performance

## Related weaknesses
- CWE-772 (ChildOf)
- CWE-1076 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1091.html
