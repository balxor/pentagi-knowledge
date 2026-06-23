---
cwe_id: CWE-492
name: Use of Inner Class Containing Sensitive Data
type: weakness
abstraction: Variant
status: Draft
languages: [Java]
related_capec: []
url: https://cwe.mitre.org/data/definitions/492.html
tags: [mitre-cwe, weakness, CWE-492]
---

# CWE-492 - Use of Inner Class Containing Sensitive Data

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-492](https://cwe.mitre.org/data/definitions/492.html)

## Description
Inner classes are translated into classes that are accessible at package scope and may expose code that the programmer intended to keep private to attackers.

## Extended description
Inner classes quietly introduce several security concerns because of the way they are translated into Java bytecode. In Java source code, it appears that an inner class can be declared to be accessible only by the enclosing class, but Java bytecode has no concept of an inner class, so the compiler must transform an inner class declaration into a peer class with package level access to the original outer class. More insidiously, since an inner class can access private fields in its enclosing class, once an inner class becomes a peer class in bytecode, the compiler converts private fields accessed by the inner class into protected fields.

## Applicable platforms / languages
Java

## Common consequences
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Implementation**: Using sealed classes protects object-oriented encapsulation paradigms and therefore protects code from being extended in unforeseen ways.
- **Implementation**: Inner Classes do not provide security. Warning: Never reduce the security of the object from an outer class, going to an inner class. If an outer class is final or private, ensure that its inner class is private as well.

## Related weaknesses
- CWE-668 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/492.html
