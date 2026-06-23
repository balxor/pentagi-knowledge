---
cwe_id: CWE-608
name: Struts: Non-private Field in ActionForm Class
type: weakness
abstraction: Variant
status: Draft
languages: [Java]
related_capec: []
url: https://cwe.mitre.org/data/definitions/608.html
tags: [mitre-cwe, weakness, CWE-608]
---

# CWE-608 - Struts: Non-private Field in ActionForm Class

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-608](https://cwe.mitre.org/data/definitions/608.html)

## Description
An ActionForm class contains a field that has not been declared private, which can be accessed without using a setter or getter.

## Applicable platforms / languages
Java

## Common consequences
- **Integrity, Confidentiality**: Modify Application Data, Read Application Data

## Potential mitigations
- **Implementation**: Make all fields private. Use getter to get the value of the field. Setter should be used only by the framework; setting an action form field from other actions is bad practice and should be avoided.

## Related weaknesses
- CWE-668 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/608.html
