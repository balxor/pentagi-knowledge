---
cwe_id: CWE-499
name: Serializable Class Containing Sensitive Data
type: weakness
abstraction: Variant
status: Draft
languages: [Java]
related_capec: []
url: https://cwe.mitre.org/data/definitions/499.html
tags: [mitre-cwe, weakness, CWE-499]
---

# CWE-499 - Serializable Class Containing Sensitive Data

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-499](https://cwe.mitre.org/data/definitions/499.html)

## Description
The code contains a class with sensitive data, but the class does not explicitly deny serialization. The data can be accessed by serializing the class through another class.

## Extended description
Serializable classes are effectively open classes since data cannot be hidden in them. Classes that do not explicitly deny serialization can be serialized by any other class, which can then in turn use the data stored inside it.

## Applicable platforms / languages
Java

## Common consequences
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Implementation**: In Java, explicitly define final writeObject() to prevent serialization. This is the recommended solution. Define the writeObject() function to throw an exception explicitly denying serialization.
- **Implementation**: Make sure to prevent serialization of your objects.

## Related weaknesses
- CWE-668 (ChildOf)
- CWE-200 (CanPrecede)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/499.html
