---
cwe_id: CWE-683
name: Function Call With Incorrect Order of Arguments
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/683.html
tags: [mitre-cwe, weakness, CWE-683]
---

# CWE-683 - Function Call With Incorrect Order of Arguments

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-683](https://cwe.mitre.org/data/definitions/683.html)

## Description
The product calls a function, procedure, or routine, but the caller specifies the arguments in an incorrect order, leading to resultant weaknesses.

## Extended description
While this weakness might be caught by the compiler in some languages, it can occur more frequently in cases in which the called function accepts variable numbers or types of arguments, such as format strings in C. It also can occur in languages or environments that do not enforce strong typing.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Quality Degradation

## Potential mitigations
- **Implementation**: Use the function, procedure, or routine as specified.

## Related weaknesses
- CWE-628 (ChildOf)

## Observed examples (CVE)
- **CVE-2006-7049**: Application calls functions with arguments in the wrong order, allowing attacker to bypass intended access restrictions.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/683.html
