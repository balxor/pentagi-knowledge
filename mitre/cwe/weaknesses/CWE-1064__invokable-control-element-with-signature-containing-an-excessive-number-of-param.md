---
cwe_id: CWE-1064
name: Invokable Control Element with Signature Containing an Excessive Number of Parameters
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1064.html
tags: [mitre-cwe, weakness, CWE-1064]
---

# CWE-1064 - Invokable Control Element with Signature Containing an Excessive Number of Parameters

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1064](https://cwe.mitre.org/data/definitions/1064.html)

## Description
The product contains a function, subroutine, or method whose signature has an unnecessarily large number of parameters/arguments.

## Extended description
While the interpretation of "large number of parameters" may vary for each product or developer, CISQ recommends a default maximum of 7 parameters/arguments.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Reduce Maintainability, Increase Analytical Complexity

## Related weaknesses
- CWE-1120 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1064.html
