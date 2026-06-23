---
cwe_id: CWE-481
name: Assigning instead of Comparing
type: weakness
abstraction: Variant
status: Draft
languages: [C, C++, Java, C#]
related_capec: []
url: https://cwe.mitre.org/data/definitions/481.html
tags: [mitre-cwe, weakness, CWE-481]
---

# CWE-481 - Assigning instead of Comparing

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-481](https://cwe.mitre.org/data/definitions/481.html)

## Description
The code uses an operator for assignment when the intention was to perform a comparison.

## Extended description
In many languages the compare statement is very close in appearance to the assignment statement and are often confused. This bug is generally the result of a typo and usually causes obvious problems with program execution. If the comparison is in an if statement, the if statement will usually evaluate the value of the right-hand side of the predicate.

## Applicable platforms / languages
C, C++, Java, C#

## Common consequences
- **Other**: Alter Execution Logic

## Potential mitigations
- **Implementation**: Place constants on the left. If one attempts to assign a constant with a variable, the compiler will produce an error.

## Related weaknesses
- CWE-480 (ChildOf)
- CWE-697 (CanPrecede)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/481.html
