---
cwe_id: CWE-1096
name: Singleton Class Instance Creation without Proper Locking or Synchronization
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1096.html
tags: [mitre-cwe, weakness, CWE-1096]
---

# CWE-1096 - Singleton Class Instance Creation without Proper Locking or Synchronization

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-1096](https://cwe.mitre.org/data/definitions/1096.html)

## Description
The product implements a Singleton design pattern but does not use appropriate locking or other synchronization mechanism to ensure that the singleton class is only instantiated once.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Reduce Reliability

## Related weaknesses
- CWE-820 (ChildOf)
- CWE-662 (ChildOf)
- CWE-662 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1096.html
