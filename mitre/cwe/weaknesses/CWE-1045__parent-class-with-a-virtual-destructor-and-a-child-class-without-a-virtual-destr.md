---
cwe_id: CWE-1045
name: Parent Class with a Virtual Destructor and a Child Class without a Virtual Destructor
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1045.html
tags: [mitre-cwe, weakness, CWE-1045]
---

# CWE-1045 - Parent Class with a Virtual Destructor and a Child Class without a Virtual Destructor

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1045](https://cwe.mitre.org/data/definitions/1045.html)

## Description
A parent class has a virtual destructor method, but the parent has a child class that does not have a virtual destructor.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Reduce Reliability

## Related weaknesses
- CWE-1076 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1045.html
