---
cwe_id: CWE-498
name: Cloneable Class Containing Sensitive Information
type: weakness
abstraction: Variant
status: Draft
languages: [Object-Oriented, C++, Java, C#]
related_capec: []
url: https://cwe.mitre.org/data/definitions/498.html
tags: [mitre-cwe, weakness, CWE-498]
---

# CWE-498 - Cloneable Class Containing Sensitive Information

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-498](https://cwe.mitre.org/data/definitions/498.html)

## Description
The code contains a class with sensitive data, but the class is cloneable. The data can then be accessed by cloning the class.

## Extended description
Cloneable classes are effectively open classes, since data cannot be hidden in them. Classes that do not explicitly deny cloning can be cloned by any other class without running the constructor.

## Applicable platforms / languages
Object-Oriented, C++, Java, C#

## Common consequences
- **Access Control**: Bypass Protection Mechanism

## Potential mitigations
- **Implementation**: If you do make your classes clonable, ensure that your clone method is final and throw super.clone().

## Related weaknesses
- CWE-668 (ChildOf)
- CWE-200 (CanPrecede)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/498.html
