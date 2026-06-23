---
cwe_id: CWE-586
name: Explicit Call to Finalize()
type: weakness
abstraction: Base
status: Draft
languages: [Java]
related_capec: []
url: https://cwe.mitre.org/data/definitions/586.html
tags: [mitre-cwe, weakness, CWE-586]
---

# CWE-586 - Explicit Call to Finalize()

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-586](https://cwe.mitre.org/data/definitions/586.html)

## Description
The product makes an explicit call to the finalize() method from outside the finalizer.

## Extended description
While the Java Language Specification allows an object's finalize() method to be called from outside the finalizer, doing so is usually a bad idea. For example, calling finalize() explicitly means that finalize() will be called more than once: the first time will be the explicit call and the last time will be the call that is made after the object is garbage collected.

## Applicable platforms / languages
Java

## Common consequences
- **Integrity, Other**: Unexpected State, Quality Degradation

## Potential mitigations
- **Implementation**: Do not make explicit calls to finalize().

## Related weaknesses
- CWE-1076 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/586.html
