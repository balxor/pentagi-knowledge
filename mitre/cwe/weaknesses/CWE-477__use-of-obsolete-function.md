---
cwe_id: CWE-477
name: Use of Obsolete Function
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/477.html
tags: [mitre-cwe, weakness, CWE-477]
---

# CWE-477 - Use of Obsolete Function

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-477](https://cwe.mitre.org/data/definitions/477.html)

## Description
The code uses deprecated or obsolete functions, which suggests that the code has not been actively reviewed or maintained.

## Extended description
As programming languages evolve, functions occasionally become obsolete due to: Advances in the language Improved understanding of how operations should be performed effectively and securely Changes in the conventions that govern certain operations Functions that are removed are usually replaced by newer counterparts that perform the same task in some different and hopefully improved way.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Quality Degradation

## Potential mitigations
- **Implementation**: Refer to the documentation for the obsolete function in order to determine why it is deprecated or obsolete and to learn about alternative ways to achieve the same functionality.
- **Requirements**: Consider seriously the security implications of using an obsolete function. Consider using alternate functions.

## Related weaknesses
- CWE-710 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/477.html
