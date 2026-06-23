---
cwe_id: CWE-1173
name: Improper Use of Validation Framework
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1173.html
tags: [mitre-cwe, weakness, CWE-1173]
---

# CWE-1173 - Improper Use of Validation Framework

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-1173](https://cwe.mitre.org/data/definitions/1173.html)

## Description
The product does not use, or incorrectly uses, an input validation framework that is provided by the source language or an independent library.

## Extended description
Many modern coding languages provide developers with input validation frameworks to make the task of input validation easier and less error-prone. These frameworks will automatically check all input against specified criteria and direct execution to error handlers when invalid input is received. The improper use (i.e., an incorrect implementation or missing altogether) of these frameworks is not directly exploitable, but can lead to an exploitable condition if proper input validation is not performed later in the product. Not using provided input validation frameworks can also hurt the maintainability of code as future developers may not recognize the downstream input validation being used in the place of the validation framework.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity**: Unexpected State

## Potential mitigations
- **Implementation**: Properly use provided input validation frameworks.

## Related weaknesses
- CWE-20 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1173.html
