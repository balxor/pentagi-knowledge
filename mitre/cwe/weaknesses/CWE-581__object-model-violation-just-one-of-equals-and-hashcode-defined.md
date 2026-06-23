---
cwe_id: CWE-581
name: Object Model Violation: Just One of Equals and Hashcode Defined
type: weakness
abstraction: Variant
status: Draft
languages: [Java]
related_capec: []
url: https://cwe.mitre.org/data/definitions/581.html
tags: [mitre-cwe, weakness, CWE-581]
---

# CWE-581 - Object Model Violation: Just One of Equals and Hashcode Defined

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-581](https://cwe.mitre.org/data/definitions/581.html)

## Description
The product does not maintain equal hashcodes for equal objects.

## Extended description
Java objects are expected to obey a number of invariants related to equality. One of these invariants is that equal objects must have equal hashcodes. In other words, if a.equals(b) == true then a.hashCode() == b.hashCode().

## Applicable platforms / languages
Java

## Common consequences
- **Integrity, Other**: Other

## Potential mitigations
- **Implementation**: Both Equals() and Hashcode() should be defined.

## Related weaknesses
- CWE-573 (ChildOf)
- CWE-697 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/581.html
