---
cwe_id: CWE-478
name: Missing Default Case in Multiple Condition Expression
type: weakness
abstraction: Base
status: Draft
languages: [C, C++, Java, C#, Python, JavaScript]
related_capec: []
url: https://cwe.mitre.org/data/definitions/478.html
tags: [mitre-cwe, weakness, CWE-478]
---

# CWE-478 - Missing Default Case in Multiple Condition Expression

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-478](https://cwe.mitre.org/data/definitions/478.html)

## Description
The code does not have a default case in an expression with multiple conditions, such as a switch statement.

## Extended description
If a multiple-condition expression (such as a switch in C) omits the default case but does not consider or handle all possible values that could occur, then this might lead to complex logical errors and resultant weaknesses. Because of this, further decisions are made based on poor information, and cascading failure results. This cascading failure may result in any number of security issues, and constitutes a significant failure in the system.

## Applicable platforms / languages
C, C++, Java, C#, Python, JavaScript

## Common consequences
- **Integrity**: Varies by Context, Alter Execution Logic

## Potential mitigations
- **Implementation**: Ensure that there are no cases unaccounted for when adjusting program flow or values based on the value of a given variable. In the case of switch style statements, the very simple act of creating a default case can, if done correctly, mitigate this situation. Often however, the default case is used simply to represent an assumed option, as opposed to working as a check for invalid input. This is poor practice and in some cases is as bad as omitting a default case entirely.

## Related weaknesses
- CWE-1023 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/478.html
