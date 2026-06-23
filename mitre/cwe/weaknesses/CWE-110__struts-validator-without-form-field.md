---
cwe_id: CWE-110
name: Struts: Validator Without Form Field
type: weakness
abstraction: Variant
status: Draft
languages: [Java]
related_capec: []
url: https://cwe.mitre.org/data/definitions/110.html
tags: [mitre-cwe, weakness, CWE-110]
---

# CWE-110 - Struts: Validator Without Form Field

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-110](https://cwe.mitre.org/data/definitions/110.html)

## Description
Validation fields that do not appear in forms they are associated with indicate that the validation logic is out of date.

## Extended description
It is easy for developers to forget to update validation logic when they make changes to an ActionForm class. One indication that validation logic is not being properly maintained is inconsistencies between the action form and the validation form. Although J2EE applications are not generally susceptible to memory corruption attacks, if a J2EE application interfaces with native code that does not perform array bounds checking, an attacker may be able to use an input validation mistake in the J2EE application to launch a buffer overflow attack.

## Applicable platforms / languages
Java

## Common consequences
- **Other**: Other

## Related weaknesses
- CWE-1164 (ChildOf)
- CWE-20 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/110.html
