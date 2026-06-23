---
cwe_id: CWE-1087
name: Class with Virtual Method without a Virtual Destructor
type: weakness
abstraction: Base
status: Incomplete
languages: [Object-Oriented]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1087.html
tags: [mitre-cwe, weakness, CWE-1087]
---

# CWE-1087 - Class with Virtual Method without a Virtual Destructor

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1087](https://cwe.mitre.org/data/definitions/1087.html)

## Description
A class contains a virtual method, but the method does not have an associated virtual destructor.

## Applicable platforms / languages
Object-Oriented

## Common consequences
- **Other**: Reduce Reliability

## Related weaknesses
- CWE-1076 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1087.html
