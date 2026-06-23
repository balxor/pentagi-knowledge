---
cwe_id: CWE-758
name: Reliance on Undefined, Unspecified, or Implementation-Defined Behavior
type: weakness
abstraction: Class
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/758.html
tags: [mitre-cwe, weakness, CWE-758]
---

# CWE-758 - Reliance on Undefined, Unspecified, or Implementation-Defined Behavior

**Abstraction:** Class  -  **Status:** Incomplete  -  **CWE:** [CWE-758](https://cwe.mitre.org/data/definitions/758.html)

## Description
The product uses an API function, data structure, or other entity in a way that relies on properties that are not always guaranteed to hold for that entity.

## Extended description
This can lead to resultant weaknesses when the required properties change, such as when the product is ported to a different platform or if an interaction error (CWE-435) occurs.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Reduce Maintainability, Unexpected State, Quality Degradation

## Related weaknesses
- CWE-710 (ChildOf)

## Observed examples (CVE)
- **CVE-2006-1902**: Change in C compiler behavior causes resultant buffer overflows in programs that depend on behaviors that were undefined in the C standard.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/758.html
