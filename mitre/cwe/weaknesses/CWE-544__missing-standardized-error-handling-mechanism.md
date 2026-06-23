---
cwe_id: CWE-544
name: Missing Standardized Error Handling Mechanism
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/544.html
tags: [mitre-cwe, weakness, CWE-544]
---

# CWE-544 - Missing Standardized Error Handling Mechanism

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-544](https://cwe.mitre.org/data/definitions/544.html)

## Description
The product does not use a standardized method for handling errors throughout the code, which might introduce inconsistent error handling and resultant weaknesses.

## Extended description
If the product handles error messages individually, on a one-by-one basis, this is likely to result in inconsistent error handling. The causes of errors may be lost. Also, detailed information about the causes of an error may be unintentionally returned to the user.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity, Other**: Quality Degradation, Unexpected State, Varies by Context

## Potential mitigations
- **Architecture and Design**: define a strategy for handling errors of different severities, such as fatal errors versus basic log events. Use or create built-in language features, or an external package, that provides an easy-to-use API and define coding standards for the detection and handling of errors.

## Related weaknesses
- CWE-755 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/544.html
