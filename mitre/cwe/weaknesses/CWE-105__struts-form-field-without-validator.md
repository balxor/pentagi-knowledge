---
cwe_id: CWE-105
name: Struts: Form Field Without Validator
type: weakness
abstraction: Variant
status: Draft
languages: [Java]
related_capec: []
url: https://cwe.mitre.org/data/definitions/105.html
tags: [mitre-cwe, weakness, CWE-105]
---

# CWE-105 - Struts: Form Field Without Validator

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-105](https://cwe.mitre.org/data/definitions/105.html)

## Description
The product has a form field that is not validated by a corresponding validation form, which can introduce other weaknesses related to insufficient input validation.

## Extended description
Omitting validation for even a single input field may give attackers the leeway they need to compromise the product. Although J2EE applications are not generally susceptible to memory corruption attacks, if a J2EE application interfaces with native code that does not perform array bounds checking, an attacker may be able to use an input validation mistake in the J2EE application to launch a buffer overflow attack.

## Applicable platforms / languages
Java

## Common consequences
- **Integrity**: Unexpected State
- **Integrity**: Bypass Protection Mechanism

## Potential mitigations
- **Implementation**: Validate all form fields. If a field is unused, it is still important to constrain it so that it is empty or undefined.

## Related weaknesses
- CWE-1173 (ChildOf)
- CWE-20 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/105.html
