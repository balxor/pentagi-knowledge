---
cwe_id: CWE-688
name: Function Call With Incorrect Variable or Reference as Argument
type: weakness
abstraction: Variant
status: Draft
languages: [C, Perl]
related_capec: []
url: https://cwe.mitre.org/data/definitions/688.html
tags: [mitre-cwe, weakness, CWE-688]
---

# CWE-688 - Function Call With Incorrect Variable or Reference as Argument

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-688](https://cwe.mitre.org/data/definitions/688.html)

## Description
The product calls a function, procedure, or routine, but the caller specifies the wrong variable or reference as one of the arguments, which may lead to undefined behavior and resultant weaknesses.

## Applicable platforms / languages
C, Perl

## Common consequences
- **Other**: Quality Degradation

## Potential mitigations
- **Testing**: Because this function call often produces incorrect behavior it will usually be detected during testing or normal operation of the product. During testing exercise all possible control paths will typically expose this weakness except in rare cases when the incorrect function call accidentally produces the correct results or if the provided argument type is very similar to the expected argument type.

## Related weaknesses
- CWE-628 (ChildOf)

## Observed examples (CVE)
- **CVE-2005-2548**: Kernel code specifies the wrong variable in first argument, leading to resultant NULL pointer dereference.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/688.html
