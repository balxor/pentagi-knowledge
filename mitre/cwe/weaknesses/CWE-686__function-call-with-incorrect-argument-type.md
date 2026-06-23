---
cwe_id: CWE-686
name: Function Call With Incorrect Argument Type
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/686.html
tags: [mitre-cwe, weakness, CWE-686]
---

# CWE-686 - Function Call With Incorrect Argument Type

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-686](https://cwe.mitre.org/data/definitions/686.html)

## Description
The product calls a function, procedure, or routine, but the caller specifies an argument that is the wrong data type, which may lead to resultant weaknesses.

## Extended description
This weakness is most likely to occur in loosely typed languages, or in strongly typed languages in which the types of variable arguments cannot be enforced at compilation time, or where there is implicit casting.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Quality Degradation

## Related weaknesses
- CWE-628 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/686.html
