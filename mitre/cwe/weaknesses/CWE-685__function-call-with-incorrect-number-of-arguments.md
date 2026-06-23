---
cwe_id: CWE-685
name: Function Call With Incorrect Number of Arguments
type: weakness
abstraction: Variant
status: Draft
languages: [C, Perl]
related_capec: []
url: https://cwe.mitre.org/data/definitions/685.html
tags: [mitre-cwe, weakness, CWE-685]
---

# CWE-685 - Function Call With Incorrect Number of Arguments

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-685](https://cwe.mitre.org/data/definitions/685.html)

## Description
The product calls a function, procedure, or routine, but the caller specifies too many arguments, or too few arguments, which may lead to undefined behavior and resultant weaknesses.

## Applicable platforms / languages
C, Perl

## Common consequences
- **Other**: Quality Degradation

## Potential mitigations
- **Testing**: Because this function call often produces incorrect behavior it will usually be detected during testing or normal operation of the product. During testing exercise all possible control paths will typically expose this weakness except in rare cases when the incorrect function call accidentally produces the correct results or if the provided argument type is very similar to the expected argument type.

## Related weaknesses
- CWE-628 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/685.html
