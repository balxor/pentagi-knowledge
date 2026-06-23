---
cwe_id: CWE-462
name: Duplicate Key in Associative List (Alist)
type: weakness
abstraction: Variant
status: Incomplete
languages: [C, C++, Java, C#]
related_capec: []
url: https://cwe.mitre.org/data/definitions/462.html
tags: [mitre-cwe, weakness, CWE-462]
---

# CWE-462 - Duplicate Key in Associative List (Alist)

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-462](https://cwe.mitre.org/data/definitions/462.html)

## Description
Duplicate keys in associative lists can lead to non-unique keys being mistaken for an error.

## Extended description
A duplicate key entry -- if the alist is designed properly -- could be used as a constant time replace function. However, duplicate key entries could be inserted by mistake. Because of this ambiguity, duplicate key entries in an association list are not recommended and should not be allowed.

## Applicable platforms / languages
C, C++, Java, C#

## Common consequences
- **Other**: Quality Degradation, Varies by Context

## Potential mitigations
- **Architecture and Design**: Use a hash table instead of an alist.
- **Architecture and Design**: Use an alist which checks the uniqueness of hash keys with each entry before inserting the entry.

## Related weaknesses
- CWE-694 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/462.html
