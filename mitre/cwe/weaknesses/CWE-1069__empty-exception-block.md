---
cwe_id: CWE-1069
name: Empty Exception Block
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1069.html
tags: [mitre-cwe, weakness, CWE-1069]
---

# CWE-1069 - Empty Exception Block

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-1069](https://cwe.mitre.org/data/definitions/1069.html)

## Description
An invokable code block contains an exception handling block that does not contain any code, i.e. is empty.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Reduce Reliability

## Potential mitigations
- **Implementation**: For every exception block add code that handles the specific exception in the way intended by the application.

## Related weaknesses
- CWE-1071 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1069.html
