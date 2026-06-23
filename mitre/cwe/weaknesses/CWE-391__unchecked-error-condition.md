---
cwe_id: CWE-391
name: Unchecked Error Condition
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/391.html
tags: [mitre-cwe, weakness, CWE-391]
---

# CWE-391 - Unchecked Error Condition

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-391](https://cwe.mitre.org/data/definitions/391.html)

## Description
[PLANNED FOR DEPRECATION. SEE MAINTENANCE NOTES AND CONSIDER CWE-252, CWE-248, OR CWE-1069.] Ignoring exceptions and other error conditions may allow an attacker to induce unexpected behavior unnoticed.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity, Other**: Varies by Context, Unexpected State, Alter Execution Logic

## Potential mitigations
- **Requirements**: The choice between a language which has named or unnamed exceptions needs to be done. While unnamed exceptions exacerbate the chance of not properly dealing with an exception, named exceptions suffer from the up call version of the weak base class problem.
- **Requirements**: A language can be used which requires, at compile time, to catch all serious exceptions. However, one must make sure to use the most current version of the API as new exceptions could be added.
- **Implementation**: Catch all relevant exceptions. This is the recommended solution. Ensure that all exceptions are handled in such a way that you can be sure of the state of your system at any given moment.

## Related weaknesses
- CWE-754 (ChildOf)
- CWE-703 (ChildOf)
- CWE-703 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/391.html
