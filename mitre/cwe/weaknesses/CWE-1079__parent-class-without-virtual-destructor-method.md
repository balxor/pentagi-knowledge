---
cwe_id: CWE-1079
name: Parent Class without Virtual Destructor Method
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1079.html
tags: [mitre-cwe, weakness, CWE-1079]
---

# CWE-1079 - Parent Class without Virtual Destructor Method

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1079](https://cwe.mitre.org/data/definitions/1079.html)

## Description
A parent class contains one or more child classes, but the parent class does not have a virtual destructor method.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Reduce Reliability

## Related weaknesses
- CWE-1076 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1079.html
