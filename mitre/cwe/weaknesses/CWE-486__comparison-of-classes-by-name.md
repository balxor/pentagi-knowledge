---
cwe_id: CWE-486
name: Comparison of Classes by Name
type: weakness
abstraction: Variant
status: Draft
languages: [Java]
related_capec: []
url: https://cwe.mitre.org/data/definitions/486.html
tags: [mitre-cwe, weakness, CWE-486]
---

# CWE-486 - Comparison of Classes by Name

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-486](https://cwe.mitre.org/data/definitions/486.html)

## Description
The product compares classes by name, which can cause it to use the wrong class when multiple classes can have the same name.

## Extended description
If the decision to trust the methods and data of an object is based on the name of a class, it is possible for malicious users to send objects of the same name as trusted classes and thereby gain the trust afforded to known classes and types.

## Applicable platforms / languages
Java

## Common consequences
- **Integrity, Confidentiality, Availability**: Execute Unauthorized Code or Commands

## Potential mitigations
- **Implementation**: Use class equivalency to determine type. Rather than use the class name to determine if an object is of a given type, use the getClass() method, and == operator.

## Related weaknesses
- CWE-1025 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/486.html
